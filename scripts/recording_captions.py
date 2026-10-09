"""Refresh search captions using the recording poster's authenticated session."""
import datetime as dt
import hashlib
import html
import json
from pathlib import Path
import re


def parse_captions(raw):
    text = raw.decode('utf-8-sig').replace('\r\n', '\n').strip()
    if not text.startswith('WEBVTT') or re.search(r'<(?:html|!doctype)', text, re.I):
        raise ValueError('Expected WebVTT captions; received an empty, login, or unexpected response')
    cues, seen = [], set()
    def seconds(value):
        if not re.fullmatch(r'(?:\d{2,}:)?\d{2}:\d{2}\.\d{3}', value):
            raise ValueError('Invalid caption timestamp')
        parts = value.split(':')
        if float(parts[-1]) >= 60 or (len(parts) == 3 and int(parts[-2]) >= 60):
            raise ValueError('Invalid caption timestamp')
        return sum(float(p) * 60 ** i for i, p in enumerate(reversed(parts)))
    for block in re.split(r'\n\s*\n', text):
        lines = block.splitlines()
        if not lines or re.match(r'^(WEBVTT|NOTE(?:\s|$)|STYLE$|REGION$)', lines[0]):
            continue
        timing = next((i for i, line in enumerate(lines) if '-->' in line), None)
        if timing is None:
            raise ValueError('Malformed caption block')
        match = re.fullmatch(r'(\S+)\s+-->\s+(\S+)(?:\s+.*)?', lines[timing])
        if not match:
            raise ValueError('Malformed caption timing')
        start, end = seconds(match[1]), seconds(match[2])
        body = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]*>', '', ' '.join(lines[timing+1:])))).strip()
        if end < start:
            raise ValueError('Reversed caption timestamps')
        key = (start, end, body)
        if end > start and body and key not in seen:
            cues.append(dict(start=start, end=end, text=body))
            seen.add(key)
    if not cues:
        raise ValueError('Captions are not available yet; rerun the recording poster when ready')
    return sorted(cues, key=lambda c: (c['start'], c['end']))


def _write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists() or path.read_bytes() != data:
        temporary = path.with_suffix(path.suffix + '.tmp')
        temporary.write_bytes(data)
        temporary.replace(path)


def refresh_captions(context, target, repo, course):
    """Always fetch current captions, even when the link/title already matches."""
    repo = Path(repo)
    recording_url = target['recording_url']
    match = re.fullmatch(r'https://leccap.engin.umich.edu/leccap/player/r/([A-Za-z0-9]+)/?', recording_url)
    if not match:
        raise ValueError('Unexpected recording URL')
    key = match[1]
    source = 'https://leccap.engin.umich.edu/leccap/player/api/webvtt/?rk=' + key
    response = context.request.get(source, timeout=30000)
    if not response.ok:
        raise RuntimeError(f'Caption download failed (HTTP {response.status}); recording has not been published')
    raw = response.body()
    cues = parse_captions(raw)  # Validate before touching a previous cache.
    digest = hashlib.sha256(raw).hexdigest()
    metadata = dict(status='available', recordingUrl=recording_url, sourceUrl=source,
                    method='Authenticated recording poster caption-track export',
                    importedAt=dt.datetime.now(dt.timezone.utc).isoformat(), sha256=digest)
    if course == '245':
        cache = repo / 'tools/course-search/scripts/caption-cache'
        vtt, meta = cache / (key + '.vtt'), cache / (key + '.json')
        if meta.exists() and vtt.exists() and vtt.read_bytes() == raw:
            old = json.loads(meta.read_text())
            if old.get('sha256') == digest and old.get('recordingUrl') == recording_url and old.get('sourceUrl') and old.get('method'):
                metadata = old
        _write(vtt, raw)
        _write(meta, (json.dumps(metadata, indent=2) + '\n').encode())
        paths = [vtt, meta]
    else:
        path = repo / '_data/lecture-transcripts' / f"lec{int(target['lecture_number']):02d}.json"
        old = json.loads(path.read_text()) if path.exists() else {}
        bounds = old.get('lectureRange', {'start': 0, 'end': None}) if old.get('recording') == recording_url else {'start': 0, 'end': None}
        cues = [c for c in cues if c['start'] >= bounds['start'] and (bounds['end'] is None or c['end'] <= bounds['end'])]
        if not cues:
            raise ValueError('No captions within the saved lecture bounds')
        segments, i = [], 0
        while i < len(cues):
            j = i + 1
            while j < len(cues) and cues[j]['start'] < cues[i]['start'] + 45:
                j += 1
            segments.append(dict(start=cues[i]['start'], end=max(c['end'] for c in cues[i:j]),
                                 text=' '.join(c['text'] for c in cues[i:j])))
            next_i = i + 1
            while next_i < j and cues[next_i]['start'] < cues[i]['start'] + 35:
                next_i += 1
            i = next_i
        if old.get('provenance', {}).get('sha256') == digest and old.get('recording') == recording_url:
            metadata = old['provenance']
        data = dict(recording=recording_url, source='CAEN authenticated WebVTT captions',
                    lectureRange=bounds, segments=segments, provenance=metadata)
        _write(path, (json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n').encode())
        paths = [path]
    print(f"Refreshed Lecture {target['lecture_number']} captions ({len(cues)} cues)")
    return [str(p) for p in paths]
