#!/usr/bin/env python3
import argparse
import datetime as dt
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urljoin
from urllib.request import Request, urlopen

import yaml

RECORDING_SITE_URL = "https://leccap.engin.umich.edu/leccap/site/0t929w2oc176a98jk69"


class RecordingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.recordings: List[dict] = []
        self._class_stack: List[set] = []
        self._current: Optional[dict] = None

    def _in_class(self, class_name: str) -> bool:
        return any(class_name in classes for classes in self._class_stack)

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        class_attr = attrs_dict.get("class", "")
        classes = {c.strip() for c in class_attr.split() if c.strip()}

        if tag == "div" and "recording" in classes:
            self._current = {
                "date_text": "",
                "href": None,
                "data_date": attrs_dict.get("data-date"),
            }

        if tag == "div":
            self._class_stack.append(classes)

        if self._current is None or not self._in_class("recording"):
            return

        if tag == "a" and "href" in attrs_dict and self._current.get("href") is None:
            self._current["href"] = attrs_dict["href"]

    def handle_endtag(self, tag):
        if tag != "div" or not self._class_stack:
            return

        ended_classes = self._class_stack.pop()
        if "recording" in ended_classes and self._current is not None:
            self.recordings.append(self._current)
            self._current = None

    def handle_data(self, data):
        if self._current is None or not self._in_class("recording"):
            return
        if not (self._in_class("rec-date") or self._in_class("date")):
            return
        chunk = data.strip()
        if not chunk:
            return
        if self._current["date_text"]:
            self._current["date_text"] += " " + chunk
        else:
            self._current["date_text"] = chunk


def parse_date_text(text: str) -> Optional[dt.date]:
    if not text:
        return None

    cleaned = " ".join(text.split())
    for pattern, parser in (
        (r"(\d{4}-\d{2}-\d{2})", lambda s: dt.datetime.strptime(s, "%Y-%m-%d").date()),
        (
            r"(\d{1,2})/(\d{1,2})/(\d{2,4})",
            lambda s: _parse_mdy_date(s),
        ),
        (
            r"([A-Za-z]+)\s+(\d{1,2})(?:,)?\s+(\d{4})",
            lambda s: _parse_long_date(s),
        ),
        (
            r"([A-Za-z]+)\s+(\d{1,2})",
            lambda s: _parse_month_day_without_year(s),
        ),
    ):
        match = re.search(pattern, cleaned)
        if match:
            return parser(match.group(0))
    return None


def _parse_mdy_date(text: str) -> dt.date:
    month, day, year = text.split("/")
    year_num = int(year)
    if year_num < 100:
        year_num += 2000
    return dt.date(year_num, int(month), int(day))


def _parse_long_date(text: str) -> dt.date:
    cleaned = text.replace(",", "")
    for fmt in ("%B %d %Y", "%b %d %Y"):
        try:
            return dt.datetime.strptime(cleaned, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Could not parse date: {text}")


def _parse_month_day_without_year(text: str) -> Optional[dt.date]:
    this_year = dt.date.today().year
    for year in (this_year - 1, this_year, this_year + 1):
        for fmt in ("%B %d %Y", "%b %d %Y"):
            try:
                return dt.datetime.strptime(f"{text} {year}", fmt).date()
            except ValueError:
                continue
    return None


def fetch_recordings(site_url: str, html_path: Optional[Path]) -> List[dict]:
    if html_path is not None:
        html = html_path.read_text(encoding="utf-8", errors="replace")
    else:
        req = Request(site_url, headers={"User-Agent": "recording-bot/1.0"})
        with urlopen(req) as response:
            html = response.read().decode("utf-8", errors="replace")

    parser = RecordingParser()
    parser.feed(html)
    return parser.recordings


def extract_front_matter(text: str) -> Tuple[str, str, str]:
    if not text.startswith("---"):
        raise ValueError("Missing front matter header")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("Incomplete front matter")
    _, yaml_text, rest = parts
    return "---", yaml_text.strip("\n"), rest


def find_lecture_entries(modules_dir: Path) -> Dict[dt.date, Tuple[Path, str]]:
    entries: Dict[dt.date, Tuple[Path, str]] = {}
    for path in sorted(modules_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        try:
            _, yaml_text, _ = extract_front_matter(text)
        except ValueError:
            continue
        data = yaml.safe_load(yaml_text) or {}
        for day in data.get("days", []) or []:
            date_text = str(day.get("date") or "").strip()
            if not date_text:
                continue
            try:
                day_date = dt.date.fromisoformat(date_text)
            except ValueError:
                continue
            for event in day.get("events", []) or []:
                if event.get("type") == "lecture" and event.get("name"):
                    entries[day_date] = (path, str(event["name"]))
                    break
    return entries


def choose_recording(recordings: List[dict], lecture_entries: Dict[dt.date, Tuple[Path, str]]) -> Tuple[dt.date, str]:
    candidates = []
    for rec in recordings:
        href = rec.get("href")
        if not href:
            continue
        date_obj = None
        if rec.get("data_date"):
            try:
                date_obj = dt.date.fromisoformat(rec["data_date"])
            except ValueError:
                date_obj = None
        if date_obj is None:
            date_obj = parse_date_text(rec.get("date_text", ""))
        if date_obj is None or date_obj not in lecture_entries:
            continue
        candidates.append((date_obj, href))

    if not candidates:
        raise RuntimeError("No recording matched a lecture date in _modules.")

    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0]


def update_recording_in_file(path: Path, lecture_name: str, recording_url: str, dry_run: bool) -> bool:
    lines = path.read_text(encoding="utf-8").splitlines()
    name_pattern = re.compile(rf"^(\s*)-\s+name:\s*{re.escape(lecture_name)}\s*$")

    for idx, line in enumerate(lines):
        match = name_pattern.match(line)
        if not match:
            continue

        base_indent = len(match.group(1))
        key_indent = base_indent + 2
        end_idx = len(lines)
        for j in range(idx + 1, len(lines)):
            next_line = lines[j]
            stripped = next_line.lstrip()
            indent = len(next_line) - len(stripped)
            if stripped.startswith("- ") and indent <= base_indent:
                end_idx = j
                break

        recording_line = " " * key_indent + f"recording: {recording_url}"
        recording_indexes = []
        insert_at = None
        for j in range(idx + 1, end_idx):
            if re.match(r"^\s*recording:\s*", lines[j]):
                recording_indexes.append(j)
            elif insert_at is None and re.match(r"^\s*title:\s*", lines[j]):
                insert_at = j + 1
            elif insert_at is None and re.match(r"^\s*type:\s*", lines[j]):
                insert_at = j + 1

        if recording_indexes:
            if len(recording_indexes) > 1:
                for duplicate_idx in reversed(recording_indexes[1:]):
                    del lines[duplicate_idx]
            first_idx = recording_indexes[0]
            if lines[first_idx].strip() == recording_line.strip():
                return False
            lines[first_idx] = recording_line
        else:
            if insert_at is None:
                insert_at = idx + 1
            lines.insert(insert_at, recording_line)

        if dry_run:
            return True

        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return True

    raise RuntimeError(f"Lecture name {lecture_name!r} not found in {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Update the latest lecture recording link in module YAML.")
    parser.add_argument("--recording-site-url", default=os.getenv("RECORDING_SITE_URL", RECORDING_SITE_URL))
    parser.add_argument(
        "--recording-site-html",
        type=Path,
        default=Path(os.getenv("RECORDING_SITE_HTML")) if os.getenv("RECORDING_SITE_HTML") else None,
        help="Path to saved recording site HTML for local testing.",
    )
    parser.add_argument("--modules-dir", type=Path, default=Path("_modules"))
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    lecture_entries = find_lecture_entries(args.modules_dir)
    if not lecture_entries:
        raise RuntimeError(f"No lecture entries found in {args.modules_dir}")

    recordings = fetch_recordings(args.recording_site_url, args.recording_site_html)
    target_date, href = choose_recording(recordings, lecture_entries)
    recording_url = urljoin(args.recording_site_url, href)

    module_path, lecture_name = lecture_entries[target_date]
    changed = update_recording_in_file(module_path, lecture_name, recording_url, args.dry_run)
    if changed:
        print(f"Updated {module_path} for {lecture_name} ({target_date.isoformat()}) with {recording_url}")
    else:
        print(f"No change needed for {module_path} ({lecture_name})")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
