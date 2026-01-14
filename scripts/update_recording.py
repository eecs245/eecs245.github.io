#!/usr/bin/env python3
import argparse
import datetime as dt
import os
import re
import subprocess
import sys
import time
from urllib.parse import urljoin


LECCAP_SITE_URL = "https://leccap.engin.umich.edu/leccap/site/0t929w2oc176a98jk69"
LECCAP_BASE_URL = "https://leccap.engin.umich.edu"
MODULES_DIR = "_modules"
LECCAP_TIMEOUT_MS = int(os.getenv("LECCAP_TIMEOUT_MS", "5000"))
LECCAP_DEBUG_DIR = os.getenv("LECCAP_DEBUG_DIR")
LECCAP_COOKIE = os.getenv("LECCAP_COOKIE")
LECCAP_COOKIE_DOMAIN = os.getenv("LECCAP_COOKIE_DOMAIN", "leccap.engin.umich.edu")
LECCAP_COOKIE_PATH = os.getenv("LECCAP_COOKIE_PATH", "/")
LECCAP_COOKIE_FILE = os.getenv("LECCAP_COOKIE_FILE", ".leccap_cookie")
LECCAP_HEADLESS = os.getenv("LECCAP_HEADLESS", "false").lower() in ("1", "true", "yes", "on")


def _maybe_dump_debug(page, label):
    if not LECCAP_DEBUG_DIR:
        return
    os.makedirs(LECCAP_DEBUG_DIR, exist_ok=True)
    html_path = os.path.join(LECCAP_DEBUG_DIR, f"{label}.html")
    try:
        with open(html_path, "w", encoding="utf-8") as handle:
            handle.write(page.content())
    except Exception:
        pass
    try:
        page.screenshot(path=os.path.join(LECCAP_DEBUG_DIR, f"{label}.png"), full_page=True)
    except Exception:
        pass


def _cookies_from_header(header_value, domain, path):
    cookies = []
    if not header_value:
        return cookies
    for part in header_value.split(";"):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            continue
        name, value = part.split("=", 1)
        name = name.strip()
        value = value.strip()
        if not name:
            continue
        cookies.append(
            {
                "name": name,
                "value": value,
                "domain": domain,
                "path": path,
            }
        )
    return cookies


def _load_cookie_header():
    if LECCAP_COOKIE:
        return LECCAP_COOKIE
    if not LECCAP_COOKIE_FILE:
        return None
    try:
        with open(LECCAP_COOKIE_FILE, "r", encoding="utf-8") as handle:
            value = handle.read().strip()
            return value or None
    except FileNotFoundError:
        return None


def fetch_leccap_recordings(url):
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    except ImportError as exc:
        raise RuntimeError("playwright is required; install with `pip install playwright`") from exc

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=LECCAP_HEADLESS)
        context = browser.new_context()
        cookie_header = _load_cookie_header()
        if cookie_header:
            cookies = _cookies_from_header(
                cookie_header, LECCAP_COOKIE_DOMAIN, LECCAP_COOKIE_PATH
            )
            if cookies:
                context.add_cookies(cookies)
        page = context.new_page()
        try:
            page.goto(url, wait_until="domcontentloaded")
            deadline = time.monotonic() + (LECCAP_TIMEOUT_MS / 1000.0)
            found = False
            last_error = None
            while time.monotonic() < deadline:
                try:
                    page.wait_for_selector("div.recording", timeout=500)
                    found = True
                    break
                except PlaywrightTimeout as exc:
                    last_error = exc
                for frame in page.frames:
                    try:
                        if frame.query_selector("div.recording"):
                            found = True
                            break
                    except Exception:
                        continue
                if found:
                    break
            if not found:
                _maybe_dump_debug(page, "timeout")
                frame_urls = []
                for frame in page.frames:
                    try:
                        frame_urls.append(frame.url)
                    except Exception:
                        continue
                debug_note = ""
                if LECCAP_DEBUG_DIR:
                    debug_note = f" (debug dumped to {LECCAP_DEBUG_DIR})"
                raise RuntimeError(
                    "timed out waiting for recordings; set LECCAP_TIMEOUT_MS to increase"
                    + debug_note
                    + f"; frames: {frame_urls}"
                ) from last_error

            recordings = []
            recording_nodes = page.query_selector_all("div.recording")
            if not recording_nodes:
                for frame in page.frames:
                    try:
                        recording_nodes = frame.query_selector_all("div.recording")
                    except Exception:
                        continue
                    if recording_nodes:
                        break
            for recording in recording_nodes:
                link_href = None
                link = recording.query_selector("a")
                if link:
                    link_href = link.get_attribute("href")
                date_text = ""
                date_node = recording.query_selector("div.rec-date")
                if date_node:
                    date_text = date_node.inner_text() or ""
                recordings.append({"href": link_href, "date_text": date_text})
            return recordings
        finally:
            browser.close()


def parse_date_text(text):
    if not text:
        return None
    cleaned = " ".join(text.split())
    iso_match = re.search(r"(\d{4}-\d{2}-\d{2})", cleaned)
    if iso_match:
        return dt.datetime.strptime(iso_match.group(1), "%Y-%m-%d").date()

    mdy_match = re.search(r"(\d{1,2})/(\d{1,2})/(\d{2,4})", cleaned)
    if mdy_match:
        month = int(mdy_match.group(1))
        day = int(mdy_match.group(2))
        year = int(mdy_match.group(3))
        if year < 100:
            year += 2000
        return dt.date(year, month, day)

    month_match = re.search(r"([A-Za-z]+)\s+(\d{1,2})(?:,)?\s+(\d{4})", cleaned)
    if month_match:
        month_name = month_match.group(1).lower()
        day = int(month_match.group(2))
        year = int(month_match.group(3))
        month_map = {
            "jan": 1,
            "january": 1,
            "feb": 2,
            "february": 2,
            "mar": 3,
            "march": 3,
            "apr": 4,
            "april": 4,
            "may": 5,
            "jun": 6,
            "june": 6,
            "jul": 7,
            "july": 7,
            "aug": 8,
            "august": 8,
            "sep": 9,
            "sept": 9,
            "september": 9,
            "oct": 10,
            "october": 10,
            "nov": 11,
            "november": 11,
            "dec": 12,
            "december": 12,
        }
        month = month_map.get(month_name)
        if month:
            return dt.date(year, month, day)
    return None


def select_latest_recording(recordings):
    parsed = []
    for recording in recordings:
        date_obj = parse_date_text(recording.get("date_text", ""))
        parsed.append((date_obj, recording))
    dated = [item for item in parsed if item[0] is not None]
    if dated:
        return max(dated, key=lambda item: item[0])[1]
    return recordings[-1]


def find_module_by_date(date_str):
    date_pattern = re.compile(rf"^\s*-\s*date:\s*['\"]?{re.escape(date_str)}['\"]?\s*$")
    module_files = sorted(
        path
        for path in os.listdir(MODULES_DIR)
        if path.startswith("week-") and path.endswith(".md")
    )
    for filename in module_files:
        path = os.path.join(MODULES_DIR, filename)
        with open(path, "r", encoding="utf-8") as handle:
            for line in handle:
                if date_pattern.match(line):
                    return path
    return None


def update_recording(path, date_str, recording_url):
    with open(path, "r", encoding="utf-8") as handle:
        lines = handle.readlines()

    date_pattern = re.compile(rf"^(\s*)-\s*date:\s*['\"]?{re.escape(date_str)}['\"]?\s*$")
    any_date_pattern = re.compile(r"^(\s*)-\s*date:\s*['\"]?\d{4}-\d{2}-\d{2}['\"]?\s*$")
    day_start = None
    day_indent = None
    end_front_matter = None
    for idx, line in enumerate(lines):
        if idx > 0 and line.strip() == "---":
            end_front_matter = idx
            break
    for idx, line in enumerate(lines):
        match = date_pattern.match(line)
        if match:
            day_start = idx
            day_indent = len(match.group(1))
            break

    if day_start is None:
        raise RuntimeError(f"date {date_str} not found in {path}")

    day_end = end_front_matter if end_front_matter is not None else len(lines)
    for idx in range(day_start + 1, day_end):
        line = lines[idx]
        match = any_date_pattern.match(line)
        if match and len(match.group(1)) == day_indent:
            day_end = idx
            break

    event_starts = []
    for idx in range(day_start + 1, day_end):
        if re.match(r"^\s*-\s*name:\s*", lines[idx]):
            event_starts.append(idx)
    if not event_starts:
        raise RuntimeError(f"no events found for {date_str} in {path}")

    event_starts.append(day_end)
    target_start = None
    target_end = None
    lecture_name = None
    for i in range(len(event_starts) - 1):
        start = event_starts[i]
        end = event_starts[i + 1]
        block = lines[start:end]
        if any(re.match(r"^\s*type:\s*lecture\s*$", line) for line in block):
            target_start = start
            target_end = end
            for line in block:
                match = re.match(r"^\s*-\s*name:\s*(.+)\s*$", line)
                if match:
                    lecture_name = match.group(1).strip()
                    break
            break

    if target_start is None:
        raise RuntimeError(f"no lecture event found for {date_str} in {path}")

    target_block = lines[target_start:target_end]
    recording_line_idx = None
    insert_after_idx = None
    name_indent = None
    for idx, line in enumerate(target_block):
        if re.match(r"^\s*-\s*name:\s*", line):
            name_indent = len(line) - len(line.lstrip(" "))
        if re.match(r"^\s*recording:\s*", line):
            recording_line_idx = idx
        if re.match(r"^\s*title:\s*", line):
            insert_after_idx = idx
    if insert_after_idx is None:
        for idx, line in enumerate(target_block):
            if re.match(r"^\s*type:\s*", line):
                insert_after_idx = idx
                break
    if insert_after_idx is None:
        insert_after_idx = 0

    field_indent = name_indent + 2 if name_indent is not None else 8
    recording_line = f"{' ' * field_indent}recording: {recording_url}\n"

    updated = False
    if recording_line_idx is not None:
        existing = target_block[recording_line_idx]
        if existing != recording_line:
            target_block[recording_line_idx] = recording_line
            updated = True
    else:
        target_block.insert(insert_after_idx + 1, recording_line)
        updated = True

    if updated:
        lines[target_start:target_end] = target_block
        with open(path, "w", encoding="utf-8") as handle:
            handle.writelines(lines)

    return updated, lecture_name


def lecture_number_from_name(name):
    if not name:
        return None
    match = re.search(r"\bLEC\s*(\d+)\b", name)
    if match:
        return match.group(1)
    return None


def run_git_commands(path, lecture_name, recording_url, push):
    subprocess.run(["git", "add", path], check=True)
    lecture_fragment = lecture_name or "lecture recording"
    message = f"Add recording link for {lecture_fragment}"
    subprocess.run(["git", "commit", "-m", message], check=True)
    if push:
        subprocess.run(["git", "push"], check=True)
    else:
        subprocess.run(["bundle", "exec", "jekyll", "serve"], check=True)


def main():
    parser = argparse.ArgumentParser(description="Update latest Leccap recording link.")
    parser.add_argument("--push", action="store_true", help="Commit and push changes.")
    args = parser.parse_args()

    recordings = fetch_leccap_recordings(LECCAP_SITE_URL)
    if not recordings:
        raise RuntimeError("no recordings found on Leccap page")

    latest = select_latest_recording(recordings)
    if not latest.get("href"):
        raise RuntimeError("latest recording missing href")

    recording_url = urljoin(LECCAP_BASE_URL, latest["href"])
    date_obj = parse_date_text(latest.get("date_text", ""))
    if not date_obj:
        raise RuntimeError(f"unable to parse date: {latest.get('date_text', '').strip()}")
    date_str = date_obj.strftime("%Y-%m-%d")

    module_path = find_module_by_date(date_str)
    if not module_path:
        raise RuntimeError(f"no module found for date {date_str}")

    updated, lecture_name = update_recording(module_path, date_str, recording_url)
    lecture_number = lecture_number_from_name(lecture_name)
    if lecture_number:
        print(f"Lecture {lecture_number}: {recording_url}")
    elif lecture_name:
        print(f"{lecture_name}: {recording_url}")
    else:
        print(f"Lecture: {recording_url}")

    if updated:
        run_git_commands(module_path, lecture_name or "lecture", recording_url, args.push)
    else:
        print("Recording link already up to date; no changes made.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)
