"""Build one title-only search record per explicitly curated YouTube video."""
import datetime
from urllib.parse import parse_qs, urlparse

CHANNEL = 'UCtt0J63CZ9kZOQ81wFI4oKQ'


def collect(videos, release_at, first_id=0):
    records, seen = [], set()
    for video in videos:
        title = video['title'].strip()
        url = urlparse(video['url'])
        ids = parse_qs(url.query).get('v', [])
        if (not title or url.scheme != 'https' or url.netloc != 'www.youtube.com'
                or url.path != '/watch' or len(ids) != 1 or len(ids[0]) != 11):
            raise ValueError('Invalid curated YouTube title or URL')
        if ids[0] in seen:
            raise ValueError('Duplicate curated YouTube video: ' + ids[0])
        seen.add(ids[0])
        uploaded = datetime.datetime.fromisoformat(video['uploadDate'])
        if uploaded.year == 2024 or video['channelId'] != CHANNEL:
            raise ValueError('Video is outside the approved channel/year scope')
        if not video.get('qualifyingSources'):
            raise ValueError('Missing qualifying course source')
        records.append(dict(
            id=str(first_id + len(records)), category='Other videos',
            title=title, section='Watch video', text=title, url=video['url'],
            releaseAt=release_at, uploadDate=video['uploadDate'],
            semester='', detail='Video title', concepts=[],
        ))
    return records
