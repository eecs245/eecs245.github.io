import os
import re
import subprocess
from glob import glob
from io import StringIO

from ruamel.yaml import YAML
from ruamel.yaml.constructor import DuplicateKeyError

MODULES_DIR = "_modules"


def parse_lecture_number(value: str):
    if not value:
        return None
    match = re.search(r"lec\s*0*(\d+)|\b0*(\d+)\b", value, re.IGNORECASE)
    if not match:
        return None
    number = match.group(1) or match.group(2)
    return int(number) if number is not None else None


def infer_lecture_from_recent_pdf():
    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "-1",
                "--name-only",
                "--pretty=format:",
                "--",
                "resources/lecture-pdfs",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None

    for line in result.stdout.splitlines():
        match = re.search(r"lec0*(\d+)-filled\.pdf$", line.strip(), re.IGNORECASE)
        if match:
            return int(match.group(1))
    return None

def split_front_matter(text: str):
    """
    Returns (yaml_text, rest_text, has_front_matter).
    Expects Jekyll-style front matter delimited by lines containing only '---'.
    """
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return "", text, False

    # find closing delimiter
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            yaml_text = "".join(lines[1:i])
            rest_text = "".join(lines[i+1:])
            return yaml_text, rest_text, True

    # started front matter but never closed
    raise RuntimeError("Front matter starts with '---' but no closing '---' found.")

def build_front_matter(yaml_obj) -> str:
    # Round-trip dump: preserve quotes, ordering, and indentation as much as possible
    ryaml = YAML()
    ryaml.preserve_quotes = True
    ryaml.width = 10_000  # avoid line-wrapping
    # Match common front-matter indentation styles
    ryaml.indent(mapping=2, sequence=4, offset=2)

    buf = StringIO()
    ryaml.dump(yaml_obj, buf)
    dumped = buf.getvalue()
    return f"---\n{dumped}---\n"

def main():
    lecture_input = os.getenv("LECTURE_INPUT") or ""
    lec = parse_lecture_number(lecture_input)
    if lec is None:
        lec = infer_lecture_from_recent_pdf()
    if lec is None:
        raise RuntimeError(
            "Could not determine lecture number from LECTURE_INPUT or recent PDF history."
        )

    pdf_path = f"resources/lecture-pdfs/lec{lec:02d}-filled.pdf"

    module_files = sorted(glob(f"{MODULES_DIR}/week-*.md"))
    found = False
    changed_files = []

    for module_path in module_files:
        with open(module_path, "r", encoding="utf-8") as f:
            raw = f.read()

        yaml_text, rest_text, has_fm = split_front_matter(raw)
        if not has_fm:
            raise RuntimeError(f"{module_path} has no YAML front matter starting with '---'.")

        ryaml = YAML()
        ryaml.preserve_quotes = True
        modified = False
        try:
            doc = ryaml.load(yaml_text) or {}
        except DuplicateKeyError as exc:
            tolerant_yaml = YAML()
            tolerant_yaml.preserve_quotes = True
            tolerant_yaml.allow_duplicate_keys = True
            doc = tolerant_yaml.load(yaml_text) or {}
            modified = True

        for day in doc.get("days", []) or []:
            for event in day.get("events", []) or []:
                if event.get("type") != "lecture":
                    continue

                name = (event.get("name") or "").strip()
                if re.fullmatch(rf"LEC\s*0*{lec}\b", name, re.IGNORECASE):
                    if event.get("live_notes") != pdf_path:
                        event["live_notes"] = pdf_path
                        modified = True
                    found = True

        if modified:
            new_raw = build_front_matter(doc) + rest_text
            with open(module_path, "w", encoding="utf-8") as f:
                f.write(new_raw)
            changed_files.append(module_path)

    if not found:
        raise RuntimeError(f"Lecture {lec} not found in modules (searched name: 'LEC {lec}').")

    print("Updated:", ", ".join(changed_files) if changed_files else "(none; already up to date)")

if __name__ == "__main__":
    main()
