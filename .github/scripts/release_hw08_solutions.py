"""Publish the prepared Fall 2026 HW 8 solutions after their release time."""

import hashlib
import io
import os
from pathlib import Path
import re
import subprocess
import sys
import tarfile
import tempfile
import time
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen

START = datetime(2026, 11, 16, 5, 1, tzinfo=timezone.utc)
END = datetime(2026, 11, 17, 5, tzinfo=timezone.utc)
SITE = "https://eecs245.org"
RESOURCE = Path("resources/homeworks/hw08")
PACKAGE = Path("_incoming/hw08-solutions-2026.tar.gz.enc")
MODULE = Path("_modules/week-11.md")
MARKER = Path(".github/releases/hw08-solutions-2026.complete")
STUDENT_PDF_SHA = "88877bbdb48815d102cfda2ec5c139ad88d6dbc1663c43d95607ca3951f4c832"
STUDENT_PAGE_SHA = "e6ef75c169ac00730079bdf52658d06881aaea072e50b05895f98c5d459469a9"
PACKAGE_SHA = "6a8a910fc62413c1001c79de0141dc1eebeb18cecb125005015a0a73d74c5b31"
SOLUTION_PDF_SHA = "e268f76e2e8c8ba7ee3481e0695b037668fc67e5b67ba5d04d9b549453d98830"
PAYLOAD_FILES = {"index.md", "hw08-solutions.pdf", "imgs/p6c-counterexample.png"}
HOMEWORK_LINK = "../resources/homeworks/hw08/"


def wait_for_release():
    now = datetime.now(timezone.utc)
    if not START - timedelta(minutes=15) <= now < END:
        return False
    while (remaining := (START - datetime.now(timezone.utc)).total_seconds()) > 0:
        time.sleep(min(remaining, 30))
    return datetime.now(timezone.utc) < END


def prepare_release(validate_only):
    module = MODULE.read_text()
    events = list(re.finditer(r"(?m)^      - name: HW 8\n(?:^        .+\n)*", module))
    if len(events) != 1:
        raise RuntimeError("Expected exactly one HW 8 homepage event.")
    event = events[0]
    if (
        "        type: hw\n" not in event[0]
        or f"        problems: {HOMEWORK_LINK}\n" not in event[0]
    ):
        raise RuntimeError("The HW 8 homepage link changed.")

    if MARKER.exists():
        if hashlib.sha256((RESOURCE / "hw08-solutions.pdf").read_bytes()).hexdigest() != SOLUTION_PDF_SHA:
            raise RuntimeError("The released solutions PDF changed.")
        print("HW 8 solutions are already committed.")
        return False

    published = {"hw08.pdf": STUDENT_PDF_SHA, "index.md": STUDENT_PAGE_SHA}
    for name, expected in published.items():
        if hashlib.sha256((RESOURCE / name).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"The posted HW 8 {name} changed. Review the package before releasing.")

    payload = subprocess.run(
        [
            "openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-iter", "200000",
            "-pass", "env:HW08_RELEASE_PASSWORD", "-in", str(PACKAGE),
        ],
        check=True, capture_output=True,
    ).stdout
    if hashlib.sha256(payload).hexdigest() != PACKAGE_SHA:
        raise RuntimeError("The decrypted package did not match the reviewed release.")

    sys.path.insert(0, str(Path("scripts").resolve()))
    from check_assignment_html import check_source_markdown

    with tempfile.TemporaryDirectory() as directory:
        staging = Path(directory) / "hw08"
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:gz") as archive:
            members = archive.getmembers()
            if len(members) != len(PAYLOAD_FILES) or {m.name for m in members} != PAYLOAD_FILES:
                raise RuntimeError("Unexpected files in the HW 8 release package.")
            for member in members:
                if not member.isfile():
                    raise RuntimeError("Expected a regular file in the HW 8 release package.")
                destination = staging / member.name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(archive.extractfile(member).read())
        page = staging / "index.md"
        failures = check_source_markdown(page, allow_solutions=True)
        if failures:
            raise RuntimeError("\n".join(failures))
        if "<summary>Solution</summary>" not in page.read_text() or "hw08-solutions.pdf" not in page.read_text():
            raise RuntimeError("The HW 8 page must include the solutions and their PDF link.")
        if validate_only:
            print("The encrypted HW 8 package matches the posted assignment and passes validation.")
            return False
        for name in sorted(PAYLOAD_FILES):
            destination = RESOURCE / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes((staging / name).read_bytes())

    updated_event = re.sub(r"(?m)^        solutions:.*\n", "", event[0])
    updated_event += "        solutions: true\n"
    MODULE.write_text(module[:event.start()] + updated_event + module[event.end():])
    MARKER.parent.mkdir(parents=True, exist_ok=True)
    MARKER.write_text("Released Fall 2026 HW 8 solutions.\n")
    return True


def fetch(path):
    request = Request(f"{SITE}/{path}?hw08-release={time.time_ns()}", headers={"Cache-Control": "no-cache"})
    with urlopen(request, timeout=20) as response:
        return response.read()


def live():
    try:
        homepage = fetch("").decode()
        page = fetch(f"{RESOURCE}/").decode()
        pdf = fetch(f"{RESOURCE}/hw08-solutions.pdf")
    except OSError:
        return False
    homepage_link = r'<a\b[^>]*href=["\'][^"\']*resources/homeworks/hw08/["\'][^>]*>\s*<b>'
    pdf_link = r'href=["\'][^"\']*hw08-solutions\.pdf["\']'
    return (
        re.search(homepage_link, homepage) is not None
        and re.search(pdf_link, page) is not None
        and re.search(r"<summary>\s*Solution\s*</summary>", page) is not None
        and hashlib.sha256(pdf).hexdigest() == SOLUTION_PDF_SHA
    )


def output(name, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as stream:
        stream.write(f"{name}={str(value).lower()}\n")


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "window":
        output("due", wait_for_release())
    elif command == "prepare":
        validate_only = os.environ["VALIDATE_ONLY"] == "true"
        if not validate_only and not START <= datetime.now(timezone.utc) < END:
            raise SystemExit("Publication is outside the scheduled release window.")
        output("changed", prepare_release(validate_only))
    elif command == "live":
        output("live", live())
    elif command == "verify":
        deadline = time.monotonic() + 25 * 60
        while not live():
            if time.monotonic() >= deadline:
                raise SystemExit("The homepage, HW 8 solutions page, and solutions PDF did not all go live.")
            time.sleep(30)
        print(f"Verified the live homepage link and solutions at {SITE}/{RESOURCE}/")
    else:
        raise SystemExit(f"Unknown command {command}")
