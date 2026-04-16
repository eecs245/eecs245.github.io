#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


MATHJAX_SNIPPET = (
    '<script type="text/javascript" async '
    'src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">'
    " </script>"
)

HOMEWORK_STYLE_SNIPPET = """<style>
.main-content p {
  margin-bottom: 1.15em;
}
</style>"""


@dataclass
class Metadata:
    assignment: str
    due_date: str
    submission_instructions_latex: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Convert an EECS 245 homework LaTeX file into a website markdown page, "
            "copy referenced local assets, and optionally update a week module link."
        )
    )
    parser.add_argument("source_tex", help="Path to the homework .tex file.")
    parser.add_argument("output_md", help="Path to the generated markdown file.")
    parser.add_argument(
        "--week-file",
        help="Optional week module to update, e.g. website/_modules/week-16.md.",
    )
    parser.add_argument(
        "--event-title",
        help='Homework event title to update in the week file, e.g. "Homework 11".',
    )
    parser.add_argument(
        "--problems-link",
        help=(
            "Problems link to write into the week file. "
            "Defaults to the generated homework directory, relative to the week file."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    source_tex = resolve_source_tex(repo_root, Path(args.source_tex))
    output_md = resolve_repo_path(repo_root, Path(args.output_md))

    if (args.week_file is None) ^ (args.event_title is None):
        raise SystemExit("--week-file and --event-title must be provided together.")

    metadata = extract_metadata(source_tex.read_text())
    expanded_tex = expand_inputs(source_tex)
    transformed_tex = transform_homework_tex(expanded_tex)

    output_md.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        body_tex = tmp_dir / "body.tex"
        body_md = tmp_dir / "body.md"
        body_tex.write_text(transformed_tex)

        run_pandoc(body_tex, body_md)

        body_markdown = body_md.read_text().strip()
        submission_instructions = latex_fragment_to_markdown(
            metadata.submission_instructions_latex
        ).strip()
        final_markdown = build_homework_page(
            metadata=metadata,
            submission_instructions=submission_instructions,
            body_markdown=body_markdown,
        )

        output_md.write_text(final_markdown)

    copy_referenced_assets(output_md, source_tex.parent)

    if args.week_file:
        week_file = resolve_repo_path(repo_root, Path(args.week_file))
        problems_link = args.problems_link or compute_default_problems_link(
            week_file=week_file,
            output_md=output_md,
        )
        update_week_file(
            week_file=week_file,
            event_title=args.event_title,
            problems_link=problems_link,
        )

    return 0


def resolve_repo_path(repo_root: Path, path: Path) -> Path:
    return path if path.is_absolute() else repo_root / path


def resolve_source_tex(repo_root: Path, requested_path: Path) -> Path:
    candidate = resolve_repo_path(repo_root, requested_path)
    if candidate.exists():
        return candidate

    pdf_fallback = candidate.parent / "pdf" / candidate.name
    if pdf_fallback.exists():
        return pdf_fallback

    raise FileNotFoundError(
        f"Could not find source TeX file at {candidate} or fallback {pdf_fallback}."
    )


def extract_metadata(text: str) -> Metadata:
    assignment = extract_newcommand(text, "assignment")
    due_date = extract_newcommand(text, "duedate")
    submission_instructions = extract_newcommand(text, "submissioninstructions")
    return Metadata(
        assignment=assignment,
        due_date=collapse_whitespace(due_date),
        submission_instructions_latex=submission_instructions.strip(),
    )


def extract_newcommand(text: str, name: str) -> str:
    marker = f"\\newcommand{{\\{name}}}"
    start = text.find(marker)
    if start == -1:
        raise ValueError(f"Could not find {marker}.")

    brace_start = start + len(marker)
    if brace_start >= len(text) or text[brace_start] != "{":
        raise ValueError(f"Malformed {marker}.")

    body, _ = extract_braced(text, brace_start)
    return body


def extract_braced(text: str, brace_start: int) -> tuple[str, int]:
    depth = 0
    chars: list[str] = []
    i = brace_start
    while i < len(text):
        ch = text[i]
        if ch == "{":
            depth += 1
            if depth > 1:
                chars.append(ch)
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return "".join(chars), i + 1
            chars.append(ch)
        else:
            chars.append(ch)
        i += 1

    raise ValueError("Unbalanced braces while parsing metadata.")


def expand_inputs(path: Path) -> str:
    return expand_inputs_from_text(path.read_text(), path.parent)


def expand_inputs_from_text(text: str, base_dir: Path) -> str:
    pattern = re.compile(r"\\input\{([^}]+)\}")

    def replace(match: re.Match[str]) -> str:
        relative_path = match.group(1)
        if not relative_path.endswith(".tex"):
            relative_path += ".tex"
        included_path = (base_dir / relative_path).resolve()
        if not included_path.exists():
            raise FileNotFoundError(f"Could not resolve input file {included_path}.")
        return expand_inputs(included_path)

    return pattern.sub(replace, text)


def transform_homework_tex(text: str) -> str:
    text = strip_document_wrapper(text)
    text = replace_prob_markers(text)
    text = replace_subprob_markers(text)
    text = replace_solution_markers(text)
    text = text.replace("\\newpage", "")
    text = text.replace("\\makemytitle", "% stripped makemytitle")
    return text


def strip_document_wrapper(text: str) -> str:
    text = re.sub(r"(?s)^.*?\\begin\{document\}", "", text)
    text = re.sub(r"\\end\{document\}\s*$", "", text)
    text = re.sub(r"\\makemytitle\s*\{.*?\}\s*\{.*?\}\s*\{.*?\}\s*\{.*?\}\s*\{.*?\}", "", text, count=1, flags=re.S)
    return text


def replace_prob_markers(text: str) -> str:
    problem_number = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal problem_number
        problem_number += 1
        optional_title = match.group(1)

        header = f"\\section*{{Problem {problem_number}"
        points_badge = ""
        if optional_title:
            title = optional_title.strip()
            points_match = re.search(r"\((\d+)\s*pts?\)\s*$", title)
            if points_match:
                points = points_match.group(1)
                title = title[: points_match.start()].rstrip()
                points_badge = f"<!-- POINTS_BADGE:{points} -->"
            if title:
                header += f": {title}"
        header += "}\n"
        return "\n% PROBLEM_BOUNDARY\n" + header + points_badge + "\n"

    text = re.sub(r"\\begin\{prob\}(?:\[(.*?)\])?", replace, text)
    return text.replace("\\end{prob}", "")


def replace_subprob_markers(text: str) -> str:
    chunks = text.split("% PROBLEM_BOUNDARY")
    processed_chunks = [chunks[0]]

    for chunk in chunks[1:]:
        part_index = 0

        def replace(match: re.Match[str]) -> str:
            nonlocal part_index
            part_index += 1
            letter = chr(ord("a") + part_index - 1)
            points = match.group(1)
            points_badge = f"<!-- POINTS_BADGE:{points} -->" if points else ""
            return f"\n\\subsection*{{Part {letter})}}\n{points_badge}\n"

        processed_chunk = re.sub(
            r"\\begin\{subprob\}(?:\(\s*(\d+)\s*pts?\s*\))?", replace, chunk
        )
        processed_chunks.append(processed_chunk)

    text = "".join(processed_chunks)
    return text.replace("\\end{subprob}", "")


def replace_solution_markers(text: str) -> str:
    text = re.sub(r"\\begin\{solution\}.*?\\end\{solution\}", "", text, flags=re.S)
    return text


def run_pandoc(input_path: Path, output_path: Path) -> None:
    command = [
        "pandoc",
        str(input_path),
        "--from=latex",
        "--to=markdown+raw_html",
        "--shift-heading-level-by=1",
        "--wrap=none",
        "-o",
        str(output_path),
    ]
    subprocess.run(command, check=True)


def latex_fragment_to_markdown(fragment: str) -> str:
    with tempfile.TemporaryDirectory() as tmp_dir_str:
        tmp_dir = Path(tmp_dir_str)
        input_path = tmp_dir / "fragment.tex"
        output_path = tmp_dir / "fragment.md"
        input_path.write_text(fragment)
        run_pandoc(input_path, output_path)
        return cleanup_markdown(output_path.read_text())


def build_homework_page(
    metadata: Metadata,
    submission_instructions: str,
    body_markdown: str,
) -> str:
    cleaned_body = cleanup_markdown(body_markdown)
    toc = generate_toc(cleaned_body)

    parts = [
        "---",
        "layout: page",
        f'title: "{escape_frontmatter(metadata.assignment)}"',
        f'description: "{escape_frontmatter(metadata.assignment)} problems."',
        "nav_exclude: true",
        "---",
        "",
        MATHJAX_SNIPPET,
        "",
        HOMEWORK_STYLE_SNIPPET,
        "",
        f"# {metadata.assignment}",
        "",
        f"**Due:** {metadata.due_date}",
        "",
        submission_instructions,
        "",
        toc,
        "",
        cleaned_body,
        "",
    ]
    return "\n".join(parts)


def generate_toc(body_markdown: str) -> str:
    toc_lines = ["## Problems", ""]
    problem_pattern = re.compile(
        r"^## (Problem \d+(?::\s*(.+?))?)\s*(?:<span.*?</span>)?$", re.M
    )

    for match in problem_pattern.finditer(body_markdown):
        full_title = match.group(1)
        full_heading = re.sub(r"^##\s+", "", match.group(0))
        anchor_text = re.sub(r"<[^>]+>", "", full_heading)
        anchor = re.sub(r"[^\w\s-]", "", anchor_text.lower())
        anchor = re.sub(r"\s+", "-", anchor.strip())

        toc_lines.append(f"- [{full_title}](#{anchor})")

    if len(toc_lines) <= 2:
        return ""

    return "\n".join(toc_lines)


def cleanup_markdown(text: str) -> str:
    text = text.replace("\\\u2019", "'")
    text = text.replace("\\&", "&")
    text = text.replace('\\"', '"')
    text = text.replace("\\<", "<")
    text = text.replace("\\>", ">")
    text = re.sub(
        r"^(#{2,6}\s+.+?)\s+\{#.*?\.unnumbered\}$",
        r"\1",
        text,
        flags=re.M,
    )
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = fix_latex_for_mathjax(text)
    text = fix_image_syntax(text)
    text = add_problem_separators(text)
    text = convert_points_badges(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"^---\n+---", "---", text, flags=re.M)
    return text.strip()


def add_problem_separators(text: str) -> str:
    text = re.sub(r"^(## Problem)", r"---\n\n\1", text, flags=re.M)
    return text


def convert_points_badges(text: str) -> str:
    def replace_badge(match: re.Match[str]) -> str:
        points = match.group(1)
        return f'<span class="badge" style="background-color: #00274C; color: #FFCB05; padding: 4px 10px; border-radius: 4px; font-size: 14px; font-weight: 500; margin-left: 8px;">{points} pts</span>'

    text = re.sub(r"<!-- POINTS_BADGE:(\d+) -->", replace_badge, text)

    def add_badge_standalone(match: re.Match[str]) -> str:
        heading = match.group(1)
        badge = match.group(2)
        return f"{heading} {badge}\n\n"

    text = re.sub(
        r"^(##+ [^\n]+)\n\n(<span class=\"badge\"[^<]*</span>)[ \t]*\n+",
        add_badge_standalone,
        text,
        flags=re.M,
    )

    def add_badge_inline(match: re.Match[str]) -> str:
        heading = match.group(1)
        badge = match.group(2)
        rest = match.group(3)
        return f"{heading} {badge}\n\n{rest}"

    text = re.sub(
        r"^(##+ [^\n]+)\n\n(<span class=\"badge\"[^<]*</span>) +([^\n])",
        add_badge_inline,
        text,
        flags=re.M,
    )

    return text


def fix_latex_for_mathjax(text: str) -> str:
    def fix_backslashes_in_math(content: str) -> str:
        return content.replace("\\\\", "\\\\\\\\")

    def process_display_math(match: re.Match[str]) -> str:
        content = match.group(1)
        return "$$" + fix_backslashes_in_math(content) + "$$"

    text = re.sub(r"\$\$(.*?)\$\$", process_display_math, text, flags=re.S)

    def convert_inline_math(match: re.Match[str]) -> str:
        content = match.group(1)
        if "\n\n" in content or content.startswith("$"):
            return match.group(0)
        content = fix_backslashes_in_math(content)
        return f"\\\\({content}\\\\)"

    text = re.sub(r"(?<!\$)\$([^\$\n]+?)\$(?!\$)", convert_inline_math, text)

    text = re.sub(r"\\\\(\s*)$", r"<br>\1", text, flags=re.M)

    return text


def fix_image_syntax(text: str) -> str:
    text = re.sub(r"^:::\s*center\s*$", "", text, flags=re.M)
    text = re.sub(r"^:::\s*$", "", text, flags=re.M)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)\{[^}]*\}", r"![\1](\2)", text)
    return text


def collapse_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def escape_frontmatter(text: str) -> str:
    return text.replace('"', '\\"')


def compute_default_problems_link(week_file: Path, output_md: Path) -> str:
    relative_target = output_md.parent.relative_to(week_file.parent.parent)
    return f"../{relative_target.as_posix()}/"


def update_week_file(week_file: Path, event_title: str, problems_link: str) -> None:
    lines = week_file.read_text().splitlines()
    updated = False

    for index, line in enumerate(lines):
        if line.strip() == f"title: {event_title}":
            event_indent = len(line) - len(line.lstrip())
            j = index + 1
            while j < len(lines):
                stripped = lines[j].strip()
                current_indent = len(lines[j]) - len(lines[j].lstrip())

                if stripped.startswith("- name:") and current_indent <= event_indent:
                    break
                if stripped.startswith("title:") and current_indent <= event_indent and j != index:
                    break
                if stripped.startswith("problems:") and current_indent > event_indent:
                    lines[j] = " " * current_indent + f"problems: {problems_link}"
                    updated = True
                    break
                j += 1

            if not updated:
                insert_at = index + 1
                while insert_at < len(lines):
                    stripped = lines[insert_at].strip()
                    current_indent = len(lines[insert_at]) - len(lines[insert_at].lstrip())
                    if stripped.startswith("- name:") and current_indent <= event_indent:
                        break
                    if current_indent <= event_indent and stripped:
                        break
                    insert_at += 1

                lines.insert(index + 1, " " * event_indent + f"problems: {problems_link}")
                updated = True
            break

    if not updated:
        raise ValueError(
            f'Could not find event with title "{event_title}" in {week_file}.'
        )

    week_file.write_text("\n".join(lines) + "\n")


def copy_referenced_assets(output_md: Path, source_base_dir: Path) -> None:
    markdown = output_md.read_text()
    relative_paths = find_relative_paths(markdown)
    path_updates: dict[str, str] = {}

    for relative_path in relative_paths:
        source_path = (source_base_dir / relative_path).resolve()
        if not source_path.exists() or not source_path.is_file():
            continue

        dest_filename = source_path.name
        dest_relative = Path("imgs") / dest_filename
        destination_path = output_md.parent / dest_relative

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, destination_path)

        if str(relative_path) != str(dest_relative):
            path_updates[str(relative_path)] = str(dest_relative)

    if path_updates:
        updated_markdown = markdown
        for old_path, new_path in path_updates.items():
            updated_markdown = updated_markdown.replace(f"]({old_path})", f"]({new_path})")
        output_md.write_text(updated_markdown)


def find_relative_paths(markdown: str) -> set[Path]:
    matches = set()
    pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)|\[[^\]]+\]\(([^)]+)\)")
    for match in pattern.finditer(markdown):
        candidate = match.group(1) or match.group(2)
        if not candidate:
            continue
        candidate = candidate.strip()
        if candidate.startswith(("http://", "https://", "#", "mailto:")):
            continue
        if candidate.startswith("<") and candidate.endswith(">"):
            candidate = candidate[1:-1]
        if " " in candidate and not candidate.startswith("imgs/"):
            continue
        matches.add(Path(candidate))
    return matches


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}", file=sys.stderr)
        raise
