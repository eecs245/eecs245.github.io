import os
from glob import glob
from io import StringIO

from ruamel.yaml import YAML

MODULES_DIR = "_modules"

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
    # --- replacement for load_requests(): single lecture per run via workflow_dispatch ---
    lecture_input = os.getenv("LECTURE_INPUT") or ""
    if not lecture_input.strip():
        raise RuntimeError("LECTURE_INPUT is required (set by workflow_dispatch input 'lecture').")

    lec = int(lecture_input)
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
        doc = ryaml.load(yaml_text) or {}
        modified = False

        for day in doc.get("days", []) or []:
            for event in day.get("events", []) or []:
                if event.get("type") != "lecture":
                    continue

                name = (event.get("name") or "").strip()
                if name in {f"LEC {lec}", f"LEC {lec:02d}"}:
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