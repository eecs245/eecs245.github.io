"""Release the prepared Fall 2026 HW6 solutions once, never before their due time."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import io
import os
import re
import subprocess
import sys
import tarfile

START = datetime(2026, 11, 4, 5, 1, tzinfo=timezone.utc)
END = datetime(2026, 11, 7, tzinfo=timezone.utc)
STUDENT_SHA = 'bdd5f9be6ae3b094f77fd773c0479cc2be423c5bdb53e77780097947d09ff138'

def release(root, now, validate_only=False):
    if not validate_only and not START <= now < END:
        return False, False
    marker = root / '.github/releases/hw06-solutions-2026.complete'
    if marker.exists():
        return True, False
    resource = root / 'resources/homeworks/hw06'
    if hashlib.sha256((resource / 'hw06.pdf').read_bytes()).hexdigest() != STUDENT_SHA:
        raise RuntimeError('Published student HW6 changed; refusing release.')
    module = root / '_modules/week-09.md'
    text = module.read_text()
    pattern = r'(?m)^      - name: HW 6\n(?:^        .*\n)*'
    matches = list(re.finditer(pattern, text))
    if len(matches) != 1 or '        type: hw\n' not in matches[0].group():
        raise RuntimeError('Expected one HW6 homepage event.')
    payload = subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-pbkdf2',
        '-iter', '200000', '-pass', 'env:HW06_RELEASE_PASSWORD', '-in',
        str(root / '_incoming/hw06-solutions-2026.tar.gz.enc')],
        check=True, capture_output=True).stdout
    with tarfile.open(fileobj=io.BytesIO(payload), mode='r:gz') as archive:
        members = archive.getmembers()
        for member in members:
            path = Path(member.name)
            if (not member.isfile() or path.is_absolute() or '..' in path.parts
                or path.parts[:3] != ('resources', 'homeworks', 'hw06')
                or member.name == 'resources/homeworks/hw06/hw06.pdf'):
                raise RuntimeError('Unexpected release payload file.')
        for member in members:
            destination = root / member.name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(archive.extractfile(member).read())
    sys.path.insert(0, str(root / 'scripts'))
    from check_assignment_html import check_source_markdown
    failures = check_source_markdown(resource / 'index.md', allow_solutions=True)
    if failures:
        raise RuntimeError('\n'.join(failures))
    if validate_only:
        print('Encrypted release package decrypted and validated successfully; publication skipped.')
        return False, False
    match = matches[0]
    event = re.sub(r'(?m)^        solutions:.*\n', '', match.group())
    event += '        solutions: true\n'
    module.write_text(text[:match.start()] + event + text[match.end():])
    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text('Released Fall 2026 HW6 solutions.\n')
    return True, True

if __name__ == '__main__':
    due, changed = release(Path.cwd(), datetime.now(timezone.utc),
        validate_only=os.environ.get('VALIDATE_ONLY') == 'true')
    print(f'Release due: {due}; changed: {changed}')
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
            output.write(f'due={str(due).lower()}\nchanged={str(changed).lower()}\n')
