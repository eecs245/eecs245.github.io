#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


BAD_TEXT_PATTERNS = (
    "Giveyour",
    "andw_",
    "andslopeof",
    "wasfitonthe",
    "happenstopass",
    "Whatis",
    "minipage",
    "<em>{",
    r"!\cdot!",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check generated assignment pages for common EECS 245 HTML rendering failures."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Assignment resource directories or generated index.html files to check.",
    )
    parser.add_argument(
        "--allow-solutions",
        action="store_true",
        help="Allow solutions links/artifacts for an explicit solutions release.",
    )
    parser.add_argument(
        "--source-only",
        action="store_true",
        help="Run checks that do not require built _site HTML.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    website_root = repo_root / "website"
    failures: list[str] = []

    for raw_path in args.paths:
        path = resolve_repo_path(repo_root, Path(raw_path))
        source_md, built_html = resolve_assignment_paths(path, website_root)

        if source_md.exists():
            failures.extend(check_source_markdown(source_md, allow_solutions=args.allow_solutions))
        else:
            failures.append(f"{source_md}: missing source markdown")

        if args.source_only:
            continue
        if built_html.exists():
            failures.extend(check_built_html(built_html, website_root))
        else:
            failures.append(f"{built_html}: missing built HTML; run the Jekyll build first")

    if failures:
        for failure in failures:
            print(failure)
        return 1

    print("Assignment HTML checks passed.")
    return 0


def resolve_repo_path(repo_root: Path, path: Path) -> Path:
    return path if path.is_absolute() else repo_root / path


def resolve_assignment_paths(path: Path, website_root: Path) -> tuple[Path, Path]:
    if path.name == "index.html":
        built_html = path
        resource_dir = website_root / "resources" / path.parent.relative_to(
            website_root / "_site" / "resources"
        )
        return resource_dir / "index.md", built_html

    resource_dir = path if path.is_dir() else path.parent
    if resource_dir.name == "_site":
        raise ValueError(f"Expected an assignment resource path, not {resource_dir}.")
    relative = resource_dir.relative_to(website_root)
    return resource_dir / "index.md", website_root / "_site" / relative / "index.html"


def check_source_markdown(source_md: Path, allow_solutions: bool) -> list[str]:
    text = source_md.read_text()
    failures: list[str] = []

    if re.search(r"(?m)^ {4}<div class=\"math-display\">", text):
        failures.append(f"{source_md}: indented math-display block will render as code")
    if re.search(r"(?m)^- \[[^\n\]]*<span class=\"math-inline\"", text):
        failures.append(f"{source_md}: raw inline-math HTML leaked into the table of contents")
    if re.search(r'<span class="math-inline">[^<]*(?:&#42;|&#39;)[^<]*</span>', text):
        failures.append(f"{source_md}: escaped punctuation leaked into inline math")
    if re.search(r'<span class="math-inline">[^<]*_[^<]*</span>', text):
        failures.append(f"{source_md}: raw underscore in inline math may render as emphasis")
    if re.search(r"\\(?:textcolor|color)(?:\[[^\]]+\])?\{", text):
        failures.append(f"{source_md}: LaTeX color command leaked into generated Markdown")
    if re.search(r'\[[^\]]+\]\{style="color:', text):
        failures.append(f"{source_md}: Pandoc attribute span leaked into Markdown")
    if re.search(r'(?m)^\d+\.[ \t]*$\n\n<div class="math-display">', text):
        failures.append(f"{source_md}: ordered-list display math will break numbering")
    if re.search(r"(?m)^ {4,}[-*]\s+.*<span class=\"math-inline\"", text):
        failures.append(f"{source_md}: indented math list item will render as code")
    if re.search(r"(?m)^:::\s*minipage\s*$", text):
        failures.append(f"{source_md}: LaTeX minipage fence leaked into markdown")
    if re.search(r"(?m)(?:^---$[ \t]*\n\s*){2,}", text):
        failures.append(f"{source_md}: repeated horizontal rule separators")
    if re.search(r"(?m)(?:^|\s)\*Hint:", text):
        failures.append(f"{source_md}: hint emphasis starts with a raw markdown asterisk")
    if re.search(r"(?m)^<em>Hint:[^\n]*\*</em>$", text):
        failures.append(f"{source_md}: hint emphasis ends with a stray markdown asterisk")
    if re.search(r"(?m)^\*\s*$", text):
        failures.append(f"{source_md}: standalone markdown emphasis marker")
    for line_number, line in enumerate(text.splitlines(), start=1):
        if "Hint:" in line and ("</em>*" in line or line.rstrip().endswith("*")):
            failures.append(f"{source_md}:{line_number}: malformed hint emphasis")
    if not allow_solutions:
        if "Solutions PDF" in text or "-solutions.pdf" in text:
            failures.append(f"{source_md}: solutions link present in non-solutions release")
        for path in source_md.parent.glob("*-solutions.pdf"):
            failures.append(f"{source_md.parent}: solutions PDF present in non-solutions release: {path.name}")

    if "/labs/" in source_md.as_posix():
        for heading in re.findall(r"(?m)^## (.+)$", text):
            if heading in {"Activities"} or heading.startswith("Recap:"):
                continue
            if not heading.startswith("Activity "):
                failures.append(f"{source_md}: unnumbered lab activity heading `{heading}`")

    mc_bubble = '<span class="mc-bubble" aria-hidden="true"></span>'
    for line_number, line in enumerate(text.splitlines(), start=1):
        if line.count(mc_bubble) < 2:
            continue
        if line.startswith('<div class="mc-options">') or line.lstrip().startswith("|"):
            continue
        failures.append(f"{source_md}:{line_number}: multiple choice bubbles are not grouped as options")

    failures.extend(check_markdown_images(source_md, text))
    return failures


def check_markdown_images(source_md: Path, text: str) -> list[str]:
    failures: list[str] = []
    image_paths = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
    image_paths.extend(re.findall(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", text))

    for image_path in image_paths:
        if re.match(r"^(?:https?:)?//", image_path) or image_path.startswith("/"):
            continue
        target = (source_md.parent / image_path).resolve()
        if not target.exists():
            failures.append(f"{source_md}: missing image target `{image_path}`")
    return failures


def check_built_html(built_html: Path, website_root: Path) -> list[str]:
    text = built_html.read_text()
    failures: list[str] = []

    for code_block in re.findall(r"(?s)<pre\b.*?</pre>", text):
        decoded = html.unescape(strip_tags(code_block))
        if '<div class="math-display">' in decoded or "$$" in decoded:
            failures.append(f"{built_html}: math display rendered as a code block")
            break
        if '<span class="math-inline">' in decoded:
            failures.append(f"{built_html}: inline math rendered as a code block")
            break

    for pattern in BAD_TEXT_PATTERNS:
        if pattern in text:
            failures.append(f"{built_html}: possible mangled math text `{pattern}`")

    if re.search(r"(?s)<hr\s*/?>\s*<hr\s*/?>", text):
        failures.append(f"{built_html}: repeated horizontal rules")

    failures.extend(check_html_images(built_html, website_root, text))
    return failures


def check_html_images(built_html: Path, website_root: Path, text: str) -> list[str]:
    failures: list[str] = []
    for src in re.findall(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", text):
        if re.match(r"^(?:https?:)?//", src):
            continue
        if src.startswith("/"):
            target = website_root / "_site" / src.lstrip("/")
        else:
            target = (built_html.parent / src).resolve()
        if not target.exists():
            failures.append(f"{built_html}: missing built image `{src}`")
    return failures


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


if __name__ == "__main__":
    sys.exit(main())
