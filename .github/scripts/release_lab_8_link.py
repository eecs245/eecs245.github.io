#!/usr/bin/env python3
"""Release Lab 8 at 5:30 PM Eastern on October 28, 2026."""
from datetime import datetime, timezone
from pathlib import Path
import os
import re
import sys

RELEASE_AT = datetime(2026, 10, 28, 21, 30, tzinfo=timezone.utc)
RELEASE_END = datetime(2026, 10, 30, tzinfo=timezone.utc)


def release(path: Path, now: datetime) -> tuple[bool, bool]:
    if not RELEASE_AT <= now < RELEASE_END:
        print("Outside the one-time Lab 8 release window.")
        return False, False
    text = path.read_text()
    pattern = r"(?m)^      - name: LAB 8\n(?:^        .*\n)*"
    matches = list(re.finditer(pattern, text))
    if len(matches) != 1:
        raise RuntimeError("Expected exactly one Lab 8 event.")
    match = matches[0]
    entry = match.group()
    if "        type: lab\n" not in entry:
        raise RuntimeError("Lab 8 has an unexpected event type.")
    updated = re.sub(r"(?m)^        (?:pl_direct|pl|pl_text|problems):.*\n", "", entry)
    updated += "        problems: ../resources/labs/lab08/\n"
    changed = entry != updated
    if changed:
        path.write_text(text[:match.start()] + updated + text[match.end():])
    print("Lab 8 linked; PrairieLearn button removed." if changed else "Lab 8 is already released.")
    return True, changed


if __name__ == "__main__":
    due, changed = release(Path(sys.argv[1] if len(sys.argv) > 1 else "_modules/week-09.md"), datetime.now(timezone.utc))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as output:
            output.write(f"due={str(due).lower()}\nchanged={str(changed).lower()}\n")
