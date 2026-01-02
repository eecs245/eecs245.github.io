import os
import json
import yaml
from glob import glob

INCOMING_DIR = "_incoming/live_notes"
MODULES_DIR = "_modules"

def load_requests():
    lecture_input = os.getenv("LECTURE_INPUT")
    requests = []

    if lecture_input:
        requests.append({
            "lecture": int(lecture_input),
            "pdf_path": f"resources/lecture_pdfs/lec{int(lecture_input):02d}-filled.pdf"
        })
        return requests

    for path in glob(f"{INCOMING_DIR}/lec*.json"):
        with open(path) as f:
            data = json.load(f)
            requests.append(data)
    return requests

def main():
    requests = load_requests()
    if not requests:
        print("No lecture requests found")
        return

    module_files = glob(f"{MODULES_DIR}/week-*.md")
    found = set()

    for module_path in module_files:
        with open(module_path) as f:
            doc = yaml.safe_load(f)

        modified = False
        for day in doc.get("days", []):
            for event in day.get("events", []):
                if event.get("type") == "lecture":
                    for req in requests:
                        if event.get("name") == f"LEC {req['lecture']}":
                            event["live_notes"] = req["pdf_path"]
                            found.add(req["lecture"])
                            modified = True

        if modified:
            with open(module_path, "w") as f:
                yaml.safe_dump(doc, f, sort_keys=False)

    missing = {req["lecture"] for req in requests} - found
    if missing:
        raise RuntimeError(f"Lecture(s) not found in modules: {sorted(missing)}")

    # clean up incoming files
    for req in requests:
        path = f"{INCOMING_DIR}/lec{req['lecture']}.json"
        if os.path.exists(path):
            os.remove(path)

if __name__ == "__main__":
    main()
