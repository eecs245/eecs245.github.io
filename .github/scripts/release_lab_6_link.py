#!/usr/bin/env python3

from pathlib import Path
import sys


module_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_modules/week-07.md")
text = module_path.read_text()

lab_6_entry = """      - name: LAB 6
        type: lab
        title: Rank and Column Space
"""
linked_entry = lab_6_entry + "        problems: ../resources/labs/lab06/\n"

if linked_entry in text:
    print("Lab 6 link is already released.")
    raise SystemExit(0)

if text.count(lab_6_entry) != 1:
    raise SystemExit("Could not find the unique Lab 6 homepage entry.")

module_path.write_text(text.replace(lab_6_entry, linked_entry, 1))
print("Released the Lab 6 homepage link.")
