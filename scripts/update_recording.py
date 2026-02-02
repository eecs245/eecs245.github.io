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
LECCAP_MANAGE_URL = "https://leccap.engin.umich.edu/leccap/manage/site/recordings/0t929w2oc176a98jk69/?q=&f=any"
MODULES_DIR = "_modules"
LECCAP_TIMEOUT_MS = int(os.getenv("LECCAP_TIMEOUT_MS", "5000"))
LECCAP_DEBUG_DIR = os.getenv("LECCAP_DEBUG_DIR")
LECCAP_COOKIE = os.getenv("LECCAP_COOKIE")
LECCAP_COOKIE_DOMAIN = os.getenv("LECCAP_COOKIE_DOMAIN", "leccap.engin.umich.edu")
LECCAP_COOKIE_PATH = os.getenv("LECCAP_COOKIE_PATH", "/")
LECCAP_COOKIE_FILE = os.getenv("LECCAP_COOKIE_FILE", ".leccap_cookie")
LECCAP_STORAGE_STATE = os.getenv("LECCAP_STORAGE_STATE", ".leccap_storage_state.json")
LECCAP_LOGIN_URL = os.getenv("LECCAP_LOGIN_URL", "https://weblogin.umich.edu/")
UMICH_USER = os.getenv("UMICH_USER")
UMICH_PASS = os.getenv("UMICH_PASS")
LECCAP_HEADLESS = os.getenv("LECCAP_HEADLESS", "false").lower() in ("1", "true", "yes", "on")
LECCAP_INTERACTIVE_LOGIN = os.getenv("LECCAP_INTERACTIVE_LOGIN", "false").lower() in (
    "1",
    "true",
    "yes",
    "on",
)


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


def _create_context(browser):
    storage_state = None
    if LECCAP_STORAGE_STATE and os.path.exists(LECCAP_STORAGE_STATE):
        storage_state = LECCAP_STORAGE_STATE
    if storage_state:
        context = browser.new_context(storage_state=storage_state)
    else:
        context = browser.new_context()
    cookie_header = _load_cookie_header()
    if cookie_header:
        cookies = _cookies_from_header(
            cookie_header, LECCAP_COOKIE_DOMAIN, LECCAP_COOKIE_PATH
        )
        if cookies:
            context.add_cookies(cookies)
    return context


def _is_login_url(url):
    if not url:
        return False
    lowered = url.lower()
    return (
        "weblogin" in lowered
        or "shibboleth" in lowered
        or "/idp/" in lowered
        or "login" in lowered
    )


def _ensure_logged_in(page, manage_url, interactive_login):
    if not _is_login_url(page.url):
        return
    if not interactive_login:
        raise RuntimeError(
            "login required; provide LECCAP_STORAGE_STATE or LECCAP_COOKIE "
            "or use --interactive-login"
        )
    try:
        if UMICH_USER:
            page.fill("input[name='j_username']", UMICH_USER)
        if UMICH_PASS:
            page.fill("input[name='j_password']", UMICH_PASS)
    except Exception:
        pass
    try:
        page.wait_for_url(
            re.compile(r"leccap\.engin\.umich\.edu"),
            timeout=max(LECCAP_TIMEOUT_MS * 12, 60000),
        )
    except Exception:
        pass
    if not _is_login_url(page.url):
        return
    page.goto(manage_url, wait_until="domcontentloaded")
    try:
        page.wait_for_url(
            re.compile(r"leccap\.engin\.umich\.edu"),
            timeout=max(LECCAP_TIMEOUT_MS * 12, 60000),
        )
    except Exception:
        pass
    if _is_login_url(page.url):
        raise RuntimeError("still on UMich login page; complete login/DUO, then retry")


def _fetch_leccap_recordings_with_context(context, url):
    from playwright.sync_api import TimeoutError as PlaywrightTimeout

    page = context.new_page()
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


def fetch_leccap_recordings(url):
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    except ImportError as exc:
        raise RuntimeError("playwright is required; install with `pip install playwright`") from exc

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=LECCAP_HEADLESS)
        context = _create_context(browser)
        try:
            return _fetch_leccap_recordings_with_context(context, url)
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
        if re.match(r"^\s*-\s*name:\s*", lines[idx]) or re.match(
            r"^\s*events:\s*$", lines[idx]
        ):
            event_starts.append(idx)
    if not event_starts:
        raise RuntimeError(f"no events found for {date_str} in {path}")

    event_starts.append(day_end)
    target_start = None
    target_end = None
    lecture_name = None
    lecture_title = None
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
            for line in block:
                match = re.match(r"^\s*title:\s*(.+)\s*$", line)
                if match:
                    lecture_title = match.group(1).strip()
                    break
            break

    if target_start is None:
        events_start = None
        for idx in range(day_start, day_end):
            if re.match(r"^\s*events:\s*$", lines[idx]):
                events_start = idx
                break
        if events_start is not None:
            block = lines[events_start:day_end]
            if any(re.match(r"^\s*type:\s*lecture\s*$", line) for line in block):
                target_start = events_start
                target_end = day_end
                for line in block:
                    match = re.match(r"^\s*-\s*name:\s*(.+)\s*$", line)
                    if match:
                        lecture_name = match.group(1).strip()
                        break
                for line in block:
                    match = re.match(r"^\s*title:\s*(.+)\s*$", line)
                    if match:
                        lecture_title = match.group(1).strip()
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

    return updated, lecture_name, lecture_title


def lecture_number_from_name(name):
    if not name:
        return None
    match = re.search(r"\bLEC\s*(\d+)\b", name)
    if match:
        return match.group(1)
    return None


def lecture_title_from_name(name):
    if not name:
        return None
    match = re.match(r"\s*LEC\s*\d+\s*[:\-]\s*(.+)\s*$", name, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    if re.match(r"\s*LEC\s*\d+\s*$", name, re.IGNORECASE):
        return None
    return name.strip()


def build_recording_title(lecture_number, lecture_title, date_obj):
    if not (lecture_number and lecture_title and date_obj):
        return None
    date_fragment = f"{date_obj.month}/{date_obj.day}"
    return f"Lecture {lecture_number}: {lecture_title} (from {date_fragment})"


def _date_variants(date_obj):
    if not date_obj:
        return []
    month_name = date_obj.strftime("%B")
    return [
        date_obj.strftime("%Y-%m-%d"),
        f"{date_obj.month}/{date_obj.day}",
        f"{date_obj.month}/{date_obj.day}/{date_obj.strftime('%y')}",
        f"{date_obj.month}/{date_obj.day}/{date_obj.year}",
        f"{month_name} {date_obj.day}, {date_obj.year}",
        f"{month_name} {date_obj.day}",
    ]


def _recording_id_from_url(recording_url):
    if not recording_url:
        return None
    parts = recording_url.rstrip("/").split("/")
    return parts[-1] if parts else None


def update_recording_title(
    manage_url,
    title,
    date_obj=None,
    recording_url=None,
    interactive_login=False,
    save_storage_state=False,
    context=None,
):
    if not title:
        raise RuntimeError("recording title is empty")
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
    except ImportError as exc:
        raise RuntimeError("playwright is required; install with `pip install playwright`") from exc

    def _run(page):
        page.goto(manage_url, wait_until="domcontentloaded")
        _ensure_logged_in(page, manage_url, interactive_login)
        _maybe_dump_debug(page, "manage-loaded")
        try:
            page.wait_for_selector("text=Edit", timeout=max(LECCAP_TIMEOUT_MS, 20000))
        except PlaywrightTimeout as exc:
            _maybe_dump_debug(page, "manage-timeout")
            raise RuntimeError("timed out waiting for manage recordings page") from exc

        def _find_locator(selector):
            if page.locator(selector).count() > 0:
                return page, page.locator(selector)
            for frame in page.frames:
                try:
                    locator = frame.locator(selector)
                    if locator.count() > 0:
                        return frame, locator
                except Exception:
                    continue
            return None, None

        def _find_row(selector):
            owner, locator = _find_locator(selector)
            if locator and locator.count() > 0:
                return owner, locator.first
            return None, None

        frame, edit_locator = _find_locator("text=Edit")
        if not edit_locator:
            page.goto(LECCAP_SITE_URL, wait_until="domcontentloaded")
            frame, manage_locator = _find_locator("text=Manage Recordings")
            if manage_locator:
                manage_locator.first.click()
            frame, edit_locator = _find_locator("text=Edit")
        if not edit_locator:
            _maybe_dump_debug(page, "edit-missing")
            raise RuntimeError("could not find Edit button on manage recordings page")

        target_edit = None
        if date_obj:
            _, row = _find_row(f"div.recording[data-date='{date_obj.strftime('%Y-%m-%d')}']")
            if row and row.locator("a.edit-link").count() > 0:
                target_edit = row.locator("a.edit-link").first

        recording_id = _recording_id_from_url(recording_url)
        if recording_id and not target_edit:
            _, row = _find_row(f"div.recording:has(a.view-link[href*='{recording_id}'])")
            if row and row.locator("a.edit-link").count() > 0:
                target_edit = row.locator("a.edit-link").first

        if not target_edit:
            _, rows = _find_locator("div.recording")
            if rows and rows.count() > 0:
                row = rows.last
                if row.locator("a.edit-link").count() > 0:
                    target_edit = row.locator("a.edit-link").first

        if not target_edit:
            target_edit = edit_locator.last

        target_edit.click()
        _maybe_dump_debug(page, "edit-clicked")
        try:
            page.wait_for_selector("input[name='title'], input[aria-label='Title']", timeout=LECCAP_TIMEOUT_MS)
        except PlaywrightTimeout as exc:
            _maybe_dump_debug(page, "edit-timeout")
            raise RuntimeError("timed out waiting for recording edit form") from exc

        _, title_locator = _find_locator("input[name='title'], input[aria-label='Title']")
        if not title_locator:
            _maybe_dump_debug(page, "title-missing")
            raise RuntimeError("could not find Title input on recording edit form")
        title_input = title_locator.first
        title_input.fill(title)
        title_input.evaluate(
            "(el, value) => { el.value = value; el.dispatchEvent(new Event('input', {bubbles:true})); }",
            title,
        )
        _maybe_dump_debug(page, "title-filled")

        selectors = (
            "button:has-text('Save')",
            "button:has-text('Update')",
            "button:has-text('Submit')",
            "button[type='submit']",
            "input[type='submit']",
            "input[value*='Save']",
            "input[value*='Update']",
        )
        for selector in selectors:
            _, locator = _find_locator(selector)
            if locator and locator.count() > 0:
                locator.first.click()
                break
        else:
            form = title_input.locator("xpath=ancestor::form[1]")
            if form.count() > 0:
                form.evaluate("form => form.submit()")
            else:
                _maybe_dump_debug(page, "save-button-missing")
                raise RuntimeError("could not find save/update button on recording edit form")
        _maybe_dump_debug(page, "save-clicked")
        try:
            page.wait_for_load_state("networkidle", timeout=max(LECCAP_TIMEOUT_MS, 20000))
        except Exception:
            pass
        if page.locator(f"input[name='title'][value=\"{title}\"]").count() == 0:
            _maybe_dump_debug(page, "title-not-confirmed")
        if save_storage_state and LECCAP_STORAGE_STATE:
            page.context.storage_state(path=LECCAP_STORAGE_STATE)

    if context is not None:
        page = context.new_page()
        _run(page)
        return

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False if interactive_login else LECCAP_HEADLESS)
        context = _create_context(browser)
        try:
            _run(context.new_page())
        finally:
            browser.close()


def save_storage_state(login_url, manage_url, output_path):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("playwright is required; install with `pip install playwright`") from exc

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(manage_url, wait_until="domcontentloaded")
        _ensure_logged_in(page, manage_url, True)
        try:
            page.wait_for_selector("text=Edit", timeout=max(LECCAP_TIMEOUT_MS, 20000))
        except Exception:
            pass
        context.storage_state(path=output_path)
        browser.close()


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
    parser.add_argument("--update-title", action="store_true", help="Update Leccap recording title.")
    parser.add_argument(
        "--interactive-login",
        action="store_true",
        help="Open browser for UMich login if needed.",
    )
    parser.add_argument(
        "--save-storage-state",
        action="store_true",
        help="Launch browser to login and save storage state for Leccap.",
    )
    args = parser.parse_args()

    if args.save_storage_state:
        save_storage_state(LECCAP_LOGIN_URL, LECCAP_MANAGE_URL, LECCAP_STORAGE_STATE)
        print(f"Saved storage state to {LECCAP_STORAGE_STATE}")
        return

    if args.update_title:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:
            raise RuntimeError("playwright is required; install with `pip install playwright`") from exc

        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=False if (args.interactive_login or LECCAP_INTERACTIVE_LOGIN) else LECCAP_HEADLESS
            )
            context = _create_context(browser)
            try:
                recordings = _fetch_leccap_recordings_with_context(context, LECCAP_SITE_URL)
                if not recordings:
                    raise RuntimeError("no recordings found on Leccap page")

                latest = select_latest_recording(recordings)
                if not latest.get("href"):
                    raise RuntimeError("latest recording missing href")

                recording_url = urljoin(LECCAP_BASE_URL, latest["href"])
                date_obj = parse_date_text(latest.get("date_text", ""))
                if not date_obj:
                    raise RuntimeError(
                        f"unable to parse date: {latest.get('date_text', '').strip()}"
                    )
                date_str = date_obj.strftime("%Y-%m-%d")

                module_path = find_module_by_date(date_str)
                if not module_path:
                    raise RuntimeError(f"no module found for date {date_str}")

                updated, lecture_name, lecture_title = update_recording(
                    module_path, date_str, recording_url
                )
                lecture_number = lecture_number_from_name(lecture_name)
                lecture_title = lecture_title or lecture_title_from_name(lecture_name)
                if not lecture_title:
                    raise RuntimeError(
                        f"unable to find lecture title for {date_str} in {module_path}"
                    )
                recording_title = build_recording_title(
                    lecture_number, lecture_title, date_obj
                )
                if lecture_number:
                    print(f"Lecture {lecture_number}: {recording_url}")
                elif lecture_name:
                    print(f"{lecture_name}: {recording_url}")
                else:
                    print(f"Lecture: {recording_url}")
                print(f"Lecture title: {lecture_title}")
                print(f"Leccap title: {recording_title}")

                update_recording_title(
                    LECCAP_MANAGE_URL,
                    recording_title,
                    date_obj=date_obj,
                    recording_url=recording_url,
                    interactive_login=args.interactive_login or LECCAP_INTERACTIVE_LOGIN,
                    context=context,
                )

                if updated:
                    run_git_commands(
                        module_path, lecture_name or "lecture", recording_url, args.push
                    )
                else:
                    print("Recording link already up to date; no changes made.")
                return
            finally:
                browser.close()

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

    updated, lecture_name, lecture_title = update_recording(
        module_path, date_str, recording_url
    )
    lecture_number = lecture_number_from_name(lecture_name)
    lecture_title = lecture_title or lecture_title_from_name(lecture_name)
    if not lecture_title:
        raise RuntimeError(
            f"unable to find lecture title for {date_str} in {module_path}"
        )
    recording_title = build_recording_title(lecture_number, lecture_title, date_obj)
    if lecture_number:
        print(f"Lecture {lecture_number}: {recording_url}")
    elif lecture_name:
        print(f"{lecture_name}: {recording_url}")
    else:
        print(f"Lecture: {recording_url}")
    print(f"Lecture title: {lecture_title}")
    print(f"Leccap title: {recording_title}")

    if args.update_title:
        update_recording_title(
            LECCAP_MANAGE_URL,
            recording_title,
            date_obj=date_obj,
            recording_url=recording_url,
            interactive_login=args.interactive_login or LECCAP_INTERACTIVE_LOGIN,
        )

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
