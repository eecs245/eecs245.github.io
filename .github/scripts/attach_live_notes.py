import os
import json
import yaml
from glob import glob

INCOMING_DIR = "_incoming/live-notes"
MODULES_DIR = "_modules"

def load_requests():
    lecture_input = os.getenv("LECTURE_INPUT") or ""
    requests = []

    if lecture_input.strip():
        lec = int(lecture_input)
        requests.append({
            "lecture": lec,
            "pdf-path": f"resources/lecture-pdfs/lec{lec:02d}-filled.pdf"
        })
        return requests

    for path in glob(f"{INCOMING_DIR}/lec*.json"):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # normalize
        data["lecture"] = int(data["lecture"])
        requests.append(data)

    return requests

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
    # keep key order, readable formatting
    dumped = yaml.safe_dump(yaml_obj, sort_keys=False, allow_unicode=True)
    return f"---\n{dumped}---\n"

def main():
    requests = load_requests()
    if not requests:
        print("No lecture requests found.")
        return

    module_files = sorted(glob(f"{MODULES_DIR}/week-*.md"))
    found = set()
    changed_files = []

    for module_path in module_files:
        with open(module_path, "r", encoding="utf-8") as f:
            raw = f.read()

        yaml_text, rest_text, has_fm = split_front_matter(raw)
        if not has_fm:
            raise RuntimeError(f"{module_path} has no YAML front matter starting with '---'.")

        doc = yaml.safe_load(yaml_text) or {}
        modified = False

        for day in doc.get("days", []) or []:
            for event in day.get("events", []) or []:
                if event.get("type") != "lecture":
                    continue
                name = event.get("name", "")
                for req in requests:
                    if name == f"LEC {req['lecture']}":
                        event["live_notes"] = req["pdf-path"] # Only underscore, for Jekyll compatibility.
                        found.add(req["lecture"])
                        modified = True

        if modified:
            new_raw = build_front_matter(doc) + rest_text
            with open(module_path, "w", encoding="utf-8") as f:
                f.write(new_raw)
            changed_files.append(module_path)

    missing = {req["lecture"] for req in requests} - found
    if missing:
        raise RuntimeError(f"Lecture(s) not found in modules: {sorted(missing)}")

    # delete incoming json only after successful updates
    for req in requests:
        p = f"{INCOMING_DIR}/lec{req['lecture']}.json"
        if os.path.exists(p):
            os.remove(p)

    print("Updated:", ", ".join(changed_files) if changed_files else "(none)")

if __name__ == "__main__":
    main()