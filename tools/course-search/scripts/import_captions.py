"""Import an authorized local Leccap WebVTT/SRT export (never fetch live)."""
import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
from recordings import APP, PLAYER, discover, parse_captions, passages, token_counts

p = argparse.ArgumentParser(description=__doc__)
p.add_argument('recording_id')
p.add_argument('caption_file', type=Path)
p.add_argument('--source-url', required=True, help='Actual caption track/export URL')
p.add_argument('--method', required=True, help='How the authorized export was obtained')
a = p.parse_args()
now = dt.datetime.now(dt.timezone.utc)
repo = APP.parents[1]
if a.recording_id not in {r['recordingId'] for r in discover(repo, now)}:
    p.error('Recording is not a released lecture in committed _modules/week-*.md')
raw = a.caption_file.read_bytes()
cues = parse_captions(raw)
chunks = passages(cues, token_counts([c['text'] for c in cues]))
cache = APP / 'scripts/caption-cache'
cache.mkdir(exist_ok=True)
(cache / (a.recording_id + '.vtt')).write_bytes(raw)
(cache / (a.recording_id + '.json')).write_text(json.dumps(dict(
    status='available', recordingUrl=PLAYER + a.recording_id,
    sourceUrl=a.source_url, method=a.method, importedAt=now.isoformat(),
    sha256=hashlib.sha256(raw).hexdigest()), indent=2) + '\n')
print(f'Imported {len(cues)} cues / {len(chunks)} passages. Review and commit both cache files before rebuilding.')
