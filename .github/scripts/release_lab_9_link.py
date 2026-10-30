#!/usr/bin/env python3
"""Release Lab 9 at 5:30 PM Eastern on November 4, 2026."""
from datetime import datetime, timezone
from pathlib import Path
import os
import re
import sys

RELEASE_AT = datetime(2026, 11, 4, 22, 30, tzinfo=timezone.utc)
RELEASE_END = datetime(2026, 11, 7, tzinfo=timezone.utc)


def release(path: Path, now: datetime) -> tuple[bool, bool]:
    if not RELEASE_AT <= now < RELEASE_END:
        print("Outside the one-time Lab 9 release window.")
        return False, False
    text = path.read_text()
    pattern = r"(?m)^      - name: LAB 9\n(?:^        .*\n)*"
    matches = list(re.finditer(pattern, text))
    if len(matches) != 1:
        raise RuntimeError("Expected exactly one Lab 9 event.")
    match = matches[0]
    entry = match.group()
    if "        type: lab\n" not in entry:
        raise RuntimeError("Lab 9 has an unexpected event type.")
    updated = re.sub(r"(?m)^        (?:scheduled_problems|problems_release_at|problems):.*\n", "", entry)
    updated += "        problems: ../resources/labs/lab09/\n"
    changed = entry != updated
    if changed:
        path.write_text(text[:match.start()] + updated + text[match.end():])
    print("Lab 9 linked." if changed else "Lab 9 is already released.")
    return True, changed


if __name__ == "__main__":
    due, changed = release(Path(sys.argv[1] if len(sys.argv) > 1 else "_modules/week-10.md"), datetime.now(timezone.utc))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write(f"due={str(due).lower()}\nchanged={str(changed).lower()}\n")
