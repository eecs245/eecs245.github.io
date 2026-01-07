#!/usr/bin/env python3
import argparse
import datetime as dt
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import List, Optional, Tuple
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

import yaml

# Parameters to tune without touching logic.
RECORDING_SITE_URL = "https://leccap.engin.umich.edu/leccap/site/0t929w2oc176a98jk69"
LOCAL_TIMEZONE = "America/Detroit"
REVIEW_TIME_LOCAL = "14:10"  # 2:10 PM local time.


class RecordingParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.recordings = []
        self._div_stack = []
        self._current = None

    def _in_class(self, class_name: str) -> bool:
        return any(class_name in classes for classes in self._div_stack)

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        class_attr = attrs_dict.get("class", "")
        classes = {c.strip() for c in class_attr.split() if c.strip()}

        if tag == "div" and "recording" in classes:
            self._current = {"date_text": "", "href": None}
        if tag == "div":
            self._div_stack.append(classes)

        if not self._in_class("recording"):
            return

        if tag == "div" and "play-link" in classes and "href" in attrs_dict and self._current:
            self._current["href"] = attrs_dict["href"]
        if self._in_class("play-link") and tag == "a" and "href" in attrs_dict and self._current:
            self._current["href"] = attrs_dict["href"]

    def handle_endtag(self, tag):
        if tag == "div":
            if not self._div_stack:
                return
            ended_classes = self._div_stack.pop()
            if "recording" in ended_classes:
                if self._current:
                    self.recordings.append(self._current)
                self._current = None

    def handle_data(self, data):
        if self._in_class("recording") and self._in_class("date") and self._current is not None:
            chunk = data.strip()
            if not chunk:
                return
            if self._current["date_text"]:
                self._current["date_text"] += " " + chunk
            else:
                self._current["date_text"] = chunk


def parse_date_text(date_text: str, target_year: int) -> Optional[dt.date]:
    cleaned = re.sub(r"\s+", " ", date_text.strip())
    if not cleaned:
        return None

    formats = [
        "%B %d, %Y",
        "%b %d, %Y",
        "%B %d %Y",
        "%b %d %Y",
        "%m/%d/%Y",
        "%m/%d/%y",
        "%Y-%m-%d",
    ]
    for fmt in formats:
        try:
            return dt.datetime.strptime(cleaned, fmt).date()
        except ValueError:
            continue

    # Handle missing year like "Jan 12" by injecting target year.
    month_day_match = re.match(r"^([A-Za-z]+)\s+(\d{1,2})$", cleaned)
    if month_day_match:
        month_name, day = month_day_match.groups()
        for fmt in ("%B %d %Y", "%b %d %Y"):
            try:
                return dt.datetime.strptime(f"{month_name} {day} {target_year}", fmt).date()
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


def find_module_for_date(modules_dir: Path, target_date: dt.date) -> Optional[Tuple[Path, str]]:
    for path in sorted(modules_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        try:
            _, yaml_text, _ = extract_front_matter(text)
        except ValueError:
            continue
        data = yaml.safe_load(yaml_text) or {}
        days = data.get("days", [])
        for day in days:
            if str(day.get("date")) != target_date.isoformat():
                continue
            for event in day.get("events", []):
                if event.get("type") == "lecture" and event.get("name"):
                    return path, event["name"]
    return None


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
        for j in range(idx + 1, end_idx):
            if re.match(r"^\s*recording:\s*", lines[j]):
                if lines[j].strip() == recording_line.strip():
                    return False
                lines[j] = recording_line
                break
        else:
            insert_at = None
            for j in range(idx + 1, end_idx):
                if re.match(r"^\s*title:\s*", lines[j]):
                    insert_at = j + 1
                    break
            if insert_at is None:
                for j in range(idx + 1, end_idx):
                    if re.match(r"^\s*type:\s*", lines[j]):
                        insert_at = j + 1
                        break
            if insert_at is None:
                insert_at = idx + 1
            lines.insert(insert_at, recording_line)

        if dry_run:
            return True

        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return True

    raise ValueError(f"Lecture name not found in {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Update lecture recording link in module YAML.")
    parser.add_argument("--recording-site-url", default=os.getenv("RECORDING_SITE_URL", RECORDING_SITE_URL))
    parser.add_argument(
        "--recording-site-html",
        type=Path,
        default=os.getenv("RECORDING_SITE_HTML"),
        help="Path to a saved recording site HTML file (useful for 403s).",
    )
    parser.add_argument("--timezone", default=os.getenv("LOCAL_TIMEZONE", LOCAL_TIMEZONE))
    parser.add_argument("--date", default=os.getenv("TARGET_DATE"), help="YYYY-MM-DD override")
    parser.add_argument("--modules-dir", default="_modules")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    tz = ZoneInfo(args.timezone)
    now = dt.datetime.now(tz)
    if args.date:
        target_date = dt.date.fromisoformat(args.date)
    else:
        target_date = now.date()

    recordings = fetch_recordings(args.recording_site_url, args.recording_site_html)
    parsed = []
    for rec in recordings:
        rec_date = parse_date_text(rec.get("date_text", ""), target_date.year)
        if rec_date is None:
            continue
        parsed.append((rec_date, rec.get("href")))

    newest_link = None
    for rec_date, href in parsed:
        if rec_date == target_date and href:
            newest_link = urljoin(args.recording_site_url, href)
            break

    if not newest_link:
        print(f"No recording found for {target_date.isoformat()} at {args.recording_site_url}")
        return 1

    modules_dir = Path(args.modules_dir)
    match = find_module_for_date(modules_dir, target_date)
    if not match:
        print(f"No lecture found for {target_date.isoformat()} in {modules_dir}")
        return 1

    module_path, lecture_name = match
    changed = update_recording_in_file(module_path, lecture_name, newest_link, args.dry_run)
    if changed:
        print(f"Updated {module_path} for {lecture_name} with {newest_link}")
    else:
        print(f"No change needed for {module_path} ({lecture_name})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
