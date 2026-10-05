import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from other_videos import collect


class OtherVideosTests(unittest.TestCase):
    def setUp(self):
        self.videos = json.loads((Path(__file__).resolve().parents[3] /
                                 '_data/other-videos.json').read_text())

    def test_approved_videos_are_unique_title_only_direct_links(self):
        records = collect(self.videos, '2026-10-05T00:00:00-04:00', 100)
        self.assertEqual(len(records), 42)
        self.assertEqual(len({r['url'] for r in records}), 42)
        self.assertEqual(records[0]['id'], '100')
        self.assertTrue(all(r['text'] == r['title'] and r['concepts'] == []
                            and r['category'] == 'Other videos' for r in records))

    def test_duplicate_wrong_channel_and_2024_videos_are_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Duplicate'):
            collect(self.videos + [self.videos[0]], '2026-10-05T00:00:00Z')
        for field, value in [('channelId', 'different-channel'),
                             ('uploadDate', '2024-01-01T00:00:00Z'),
                             ('qualifyingSources', [])]:
            video = copy.deepcopy(self.videos[0])
            video[field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                collect([video], '2026-10-05T00:00:00Z')
