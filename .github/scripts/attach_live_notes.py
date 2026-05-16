import json
import os
import re
import shutil
import subprocess
from glob import glob
from io import StringIO

from ruamel.yaml import YAML
from ruamel.yaml.constructor import DuplicateKeyError

MODULES_DIR = "_modules"
INCOMING_DIRS = ("_incoming/live-notes", "_incoming/live_notes")
LECTURE_PDF_DIR = "resources/lecture-pdfs"


def parse_lecture_number(value: str):
    if not value:
        return None
    match = re.search(r"lec\s*0*(\d+)|\b0*(\d+)\b", value, re.IGNORECASE)
    if not match:
        return None
    number = match.group(1) or match.group(2)
    return int(number) if number is not None else None


def parse_lecture_from_path(path: str):
    match = re.search(r"lec0*(\d+)", os.path.basename(path), re.IGNORECASE)
    if not match:
        return None
    return int(match.group(1))


def incoming_paths(pattern: str):
    seen = set()
    for incoming_dir in INCOMING_DIRS:
        for path in glob(f"{incoming_dir}/{pattern}"):
            if path not in seen:
                seen.add(path)
                yield path


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

    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            yaml_text = "".join(lines[1:i])
            rest_text = "".join(lines[i + 1 :])
            return yaml_text, rest_text, True

    raise RuntimeError("Front matter starts with '---' but no closing '---' found.")


def build_front_matter(yaml_obj) -> str:
    ryaml = YAML()
    ryaml.preserve_quotes = True
    ryaml.width = 10_000
    ryaml.indent(mapping=2, sequence=4, offset=2)

    buf = StringIO()
    ryaml.dump(yaml_obj, buf)
    dumped = buf.getvalue()
    return f"---\n{dumped}---\n"


def collect_requests():
    requests = {}

    lecture_input = os.getenv("LECTURE_INPUT") or ""
    lec = parse_lecture_number(lecture_input)
    if lec is not None:
        requests[lec] = {
            "lecture": lec,
            "pdf_path": f"{LECTURE_PDF_DIR}/lec{lec:02d}-filled.pdf",
        }

    for json_path in incoming_paths("lec*.json"):
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        lec = data.get("lecture")
        if lec is None:
            lec = parse_lecture_from_path(json_path)
        if lec is None:
            raise RuntimeError(f"Could not determine lecture number from {json_path}.")

        lec = int(lec)
        req = requests.setdefault(
            lec,
            {
                "lecture": lec,
                "pdf_path": f"{LECTURE_PDF_DIR}/lec{lec:02d}-filled.pdf",
            },
        )

        req["incoming_json"] = json_path

    for pdf_path in incoming_paths("lec*.pdf"):
        lec = parse_lecture_from_path(pdf_path)
        if lec is None:
            raise RuntimeError(f"Could not determine lecture number from {pdf_path}.")
        req = requests.setdefault(
            lec,
            {
                "lecture": lec,
                "pdf_path": f"{LECTURE_PDF_DIR}/lec{lec:02d}-filled.pdf",
            },
        )
        req["incoming_pdf"] = pdf_path

    return [requests[key] for key in sorted(requests)]


def update_modules(lecture: int, pdf_path: str):
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
        except DuplicateKeyError:
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
                if re.fullmatch(rf"LEC\s*0*{lecture}\b", name, re.IGNORECASE):
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
        raise RuntimeError(f"Lecture {lecture} not found in modules (searched name: 'LEC {lecture}').")

    return changed_files


def require_pdf_ready(lecture: int, pdf_path: str):
    if os.path.isfile(pdf_path):
        return

    incoming_dirs = ", ".join(INCOMING_DIRS)
    raise RuntimeError(
        f"Refusing to attach live notes for Lecture {lecture}: {pdf_path} does not exist. "
        "Upload the PDF first through the GitHub Contents API, or provide it as an incoming "
        f"lec*.pdf file under one of: {incoming_dirs}."
    )


def main():
    requests = collect_requests()
    if not requests:
        lec = infer_lecture_from_recent_pdf()
        if lec is None:
            raise RuntimeError(
                "Could not determine lecture number from LECTURE_INPUT, incoming files, or recent PDF history."
            )
        requests = [
            {
                "lecture": lec,
                "pdf_path": f"{LECTURE_PDF_DIR}/lec{lec:02d}-filled.pdf",
            }
        ]

    changed_files = []
    consumed_paths = []

    for request in requests:
        lecture = request["lecture"]
        pdf_path = request["pdf_path"]
        source_pdf = request.get("incoming_pdf")
        if source_pdf:
            os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
            shutil.copyfile(source_pdf, pdf_path)
            consumed_paths.append(source_pdf)
        if request.get("incoming_json"):
            consumed_paths.append(request["incoming_json"])

        require_pdf_ready(lecture, pdf_path)
        changed_files.extend(update_modules(lecture, pdf_path))

    for path in consumed_paths:
        if os.path.exists(path):
            os.remove(path)

    unique_changed = list(dict.fromkeys(changed_files))
    print("Updated:", ", ".join(unique_changed) if unique_changed else "(none; already up to date)")


if __name__ == "__main__":
    main()
