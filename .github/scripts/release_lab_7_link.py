#!/usr/bin/env python3
"""Release Lab 7 no earlier than 5:30 PM Eastern on October 21, 2026."""
from datetime import datetime, timezone
from pathlib import Path
import os
import sys

RELEASE_AT = datetime(2026, 10, 21, 21, 30, tzinfo=timezone.utc)


def release(path: Path, now: datetime) -> bool:
    if now < RELEASE_AT:
        print("Lab 7 is not due for release yet.")
        return False
    text = path.read_text()
    entry = """      - name: LAB 7
        type: lab
        title: Null Space and the Rank-Nullity Theorem
"""
    linked = entry + "        problems: ../resources/labs/lab07/\n"
    if linked in text:
        print("Lab 7 is already linked.")
        return False
    if text.count(entry) != 1:
        raise RuntimeError("Expected one unlinked Lab 7 entry.")
    path.write_text(text.replace(entry, linked, 1))
    print("Released Lab 7 homepage link.")
    return True


if __name__ == "__main__":
    changed = release(Path(sys.argv[1] if len(sys.argv) > 1 else "_modules/week-08.md"), datetime.now(timezone.utc))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write(f"changed={str(changed).lower()}\n")
