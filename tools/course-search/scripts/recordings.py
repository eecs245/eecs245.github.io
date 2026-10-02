"""Offline, publication-gated Leccap caption ingestion. No network requests."""
import datetime as dt
import hashlib
import html
import json
import re
import subprocess
from pathlib import Path
from zoneinfo import ZoneInfo
import yaml

APP = Path(__file__).resolve().parents[1]
CACHE_PREFIX = 'tools/course-search/scripts/caption-cache/'
PLAYER = 'https://leccap.engin.umich.edu/leccap/player/r/'


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def discover(repo, now):
    """Read HEAD only; a date alone never makes a recording public."""
    found = {}
    paths = git(repo, 'ls-tree', '-r', '--name-only', 'HEAD').decode().splitlines()
    for path in sorted(paths):
        if not re.fullmatch(r'_modules/week-\d+\.md', path):
            continue
        raw = git(repo, 'show', 'HEAD:' + path)
        schedule = yaml.safe_load(raw.decode().split('---', 2)[1])
        for day in schedule.get('days', []):
            date = str(day['date'])
            if dt.date.fromisoformat(date) > now.astimezone(ZoneInfo('America/Detroit')).date():
                continue
            for event in day.get('events', []):
                url = event.get('recording', '')
                match = re.fullmatch(re.escape(PLAYER) + r'([A-Za-z0-9]+)/*', str(url))
                if event.get('type') != 'lecture' or not match:
                    continue
                key = match[1]
                # The link's first addition, not the schedule file's first addition.
                dates = git(repo, 'log', '--reverse', '--format=%cI', '-S' + url, 'HEAD', '--', path).decode().splitlines()
                if not dates:
                    raise ValueError('No publication evidence for ' + url)
                released = dates[0]
                if dt.datetime.fromisoformat(released) > now:
                    continue
                number = re.fullmatch(r'LEC (\d+)', str(event.get('name', '')))
                if not number:
                    continue
                found[key] = dict(recordingId=key, recordingUrl=PLAYER + key,
                    title=f"Lecture {number[1]} · {event.get('title', '')}", lectureDate=date,
                    releaseAt=released, schedulePath=path,
                    scheduleSha256=hashlib.sha256(raw).hexdigest())
    return sorted(found.values(), key=lambda r: (r['lectureDate'], r['title']))


def seconds(value):
    parts = value.replace(',', '.').split(':')
    if len(parts) not in (2, 3) or not re.fullmatch(r'\d{2,}:\d{2}(?::\d{2})?\.\d{3}', value.replace(',', '.')):
        raise ValueError('Invalid caption timestamp: ' + value)
    if float(parts[-1]) >= 60 or (len(parts) == 3 and int(parts[-2]) >= 60):
        raise ValueError('Invalid caption timestamp: ' + value)
    return sum(float(p) * 60 ** i for i, p in enumerate(reversed(parts)))


def parse_captions(raw):
    text = raw.decode('utf-8-sig').replace('\r\n', '\n').replace('\r', '\n').strip()
    if re.search(r'<(?:html|!doctype)', text, re.I):
        raise ValueError('HTML/verification page is not a caption export')
    cues = []
    seen = set()
    for block in re.split(r'\n\s*\n', text):
        lines = block.splitlines()
        if not lines or re.match(r'^(WEBVTT|NOTE(?:\s|$)|STYLE$|REGION$)', lines[0]):
            continue
        timing = next((i for i, line in enumerate(lines) if '-->' in line), None)
        if timing is None:
            raise ValueError('Unrecognized caption block')
        match = re.fullmatch(r'(\S+)\s+-->\s+(\S+)(?:\s+.*)?', lines[timing])
        if not match:
            raise ValueError('Malformed cue timing')
        start, end = seconds(match[1]), seconds(match[2])
        body = html.unescape(re.sub(r'<[^>]*>', '', ' '.join(lines[timing + 1:])))
        body = re.sub(r'\s+', ' ', body).strip()
        if end <= start:
            raise ValueError('Caption end must follow start')
        identity = (start, end, body)
        if body and identity not in seen:
            cues.append(dict(start=start, end=end, text=body))
            seen.add(identity)
    if not cues:
        raise ValueError('No timestamped captions')
    return sorted(cues, key=lambda c: (c['start'], c['end']))


def token_counts(texts):
    result = subprocess.run(['node', str(APP / 'scripts/caption_tokens.mjs')],
        input=json.dumps(texts), text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def passages(cues, counts):
    """Prefer sentence boundaries at 30–60s; cap 90s/220 wordpieces.

    Overlap ~15 seconds of complete cues. Sparse/fast speech can yield shorter
    passages. Never invent times inside a cue; reject unusably long cues.
    """
    if len(counts) != len(cues) or any(n > 220 for n in counts):
        raise ValueError('Caption cue exceeds model budget; export shorter timed cues')
    result = []
    i = 0
    while i < len(cues):
        j, budget = i, 0
        while j < len(cues):
            cue = cues[j]
            if cue['end'] - cue['start'] > 90:
                raise ValueError('Caption cue exceeds 90 seconds')
            if j > i and (cue['end'] - cues[i]['start'] > 90 or budget + counts[j] > 220 or cue['start'] - cues[j-1]['end'] > 15):
                break
            budget += counts[j]
            j += 1
            duration = cue['end'] - cues[i]['start']
            if duration >= 60 or (duration >= 30 and re.search(r'[.!?][\"\u201d]?$', cue['text'])):
                break
        group = cues[i:j]
        result.append(dict(start=group[0]['start'], end=max(c['end'] for c in group),
                           text=' '.join(c['text'] for c in group)))
        if j == len(cues):
            break
        next_i = next((k for k in range(i + 1, j) if cues[k]['start'] >= group[-1]['end'] - 15), j)
        i = next_i
    return result


def timestamp(t):
    t = int(t)
    return f'{t // 3600}:{t // 60 % 60:02}:{t % 60:02}' if t >= 3600 else f'{t // 60}:{t % 60:02}'


def collect(repo, now):
    rows, coverage, provenance = [], [], []
    paths = set(git(repo, 'ls-tree', '-r', '--name-only', 'HEAD').decode().splitlines())
    for lecture in discover(repo, now):
        entry = dict(lecture, status='missing', reason='Caption export not cached')
        key = lecture['recordingId']
        meta_path = CACHE_PREFIX + key + '.json'
        if meta_path in paths:
            try:
                meta = json.loads(git(repo, 'show', 'HEAD:' + meta_path))
                if meta.get('status') == 'pending':
                    entry.update(status='pending', reason=meta.get('reason', 'Captions pending'))
                else:
                    data_path = CACHE_PREFIX + key + '.vtt'
                    raw = git(repo, 'show', 'HEAD:' + data_path)
                    digest = hashlib.sha256(raw).hexdigest()
                    if (meta['recordingUrl'] != lecture['recordingUrl'] or meta['sha256'] != digest
                            or not meta.get('sourceUrl') or not meta.get('method')
                            or dt.datetime.fromisoformat(meta['importedAt']) > now):
                        raise ValueError('Caption provenance does not match export')
                    cues = parse_captions(raw)
                    chunks = passages(cues, token_counts([c['text'] for c in cues]))
                    # Same exact input as embed.mjs; fail visibly, never truncate.
                    inputs = [f"{timestamp(c['start'])}–{timestamp(c['end'])}. . {c['text']}" for c in chunks]
                    if any(n > 254 for n in token_counts(inputs)):
                        raise ValueError('Passage exceeds model input limit')
                    for c in chunks:
                        rows.append(dict(category='Lecture recordings', title=lecture['title'],
                            section=f"{timestamp(c['start'])}–{timestamp(c['end'])}", text=c['text'],
                            url=lecture['recordingUrl'] + '?start=' + str(max(0, int(c['start']) - 5)),
                            recordingId=key, recordingUrl=lecture['recordingUrl'], start=c['start'], end=c['end'],
                            lectureDate=lecture['lectureDate'], releaseAt=lecture['releaseAt'], semester='Fall 2026',
                            detail='Leccap captions · check recording', concepts=[]))
                    entry.update(status='available', reason='', cues=len(cues), passages=len(chunks),
                                 firstCaptionAt=cues[0]['start'], lastCaptionAt=max(c['end'] for c in cues))
                    provenance.append(dict(meta, path=data_path, schedulePath=lecture['schedulePath'],
                                           scheduleSha256=lecture['scheduleSha256'], releaseAt=lecture['releaseAt']))
            except (ValueError, KeyError, TypeError, subprocess.CalledProcessError) as exc:
                entry.update(status='invalid', reason=str(exc))
        coverage.append(entry)
    return rows, dict(published=len(coverage), available=sum(r['status']=='available' for r in coverage), recordings=coverage), provenance
