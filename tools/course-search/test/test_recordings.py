import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from recordings import parse_captions, passages, discover, collect, CACHE_PREFIX, PLAYER, token_counts

class Captions(unittest.TestCase):
    def test_vtt_srt_markup_settings_duplicates(self):
        raw=b'WEBVTT\r\n\r\na\r\n00:00:01.500 --> 00:00:04.000 align:start\r\n<v Suraj>Hello &amp; welcome</v>\r\n\r\nNOTE ignored\r\nnote\r\n\r\nb\r\n00:00:01.500 --> 00:00:04.000\r\nHello &amp; welcome'
        cues=parse_captions(raw)
        self.assertEqual(cues,[dict(start=1.5,end=4,text='Hello & welcome')])
        self.assertEqual(parse_captions(b'1\n01:02:03,456 --> 01:02:05,000\nHello')[0]['start'],3723.456)
    def test_invalid(self):
        for raw in [b'<html>Just a moment</html>',b'WEBVTT',b'00:01.000 --> 00:00.000\nBad',b'00:99.000 --> 01:00.000\nBad',b'not captions']:
            with self.assertRaises(ValueError):parse_captions(raw)
    def test_passages_overlap_and_budget(self):
        cues=[dict(start=i*5,end=i*5+5,text='Synthetic caption sentence.') for i in range(30)]
        chunks=passages(cues,[12]*len(cues))
        self.assertEqual(chunks[0]['start'],0)
        self.assertEqual(chunks[-1]['end'],150)
        self.assertLess(chunks[1]['start'],chunks[0]['end'])
        self.assertTrue(all(c['end']-c['start']<=90 for c in chunks))
        dense=passages(cues,[100]*len(cues))
        self.assertTrue(all(c['end']-c['start']<=10 for c in dense))
        with self.assertRaises(ValueError):passages(cues,[300]*len(cues))
    def test_real_tokenizer_budget(self):
        cues=[dict(start=i*5,end=i*5+5,text='The median minimizes absolute loss for these observations.') for i in range(30)]
        chunks=passages(cues,token_counts([c['text'] for c in cues]))
        self.assertTrue(all(n<=254 for n in token_counts(['0:00–1:00. . '+c['text'] for c in chunks])))
    def test_publication_and_cache_gate(self):
        with tempfile.TemporaryDirectory() as root:
            repo=Path(root)
            def git(*args):return subprocess.check_output(['git','-C',root,*args],stderr=subprocess.DEVNULL)
            git('init');git('config','user.name','Test');git('config','user.email','test@example.org')
            (repo/'_modules').mkdir()
            path=repo/'_modules/week-01.md'
            path.write_text('---\ndays:\n  - date: "2020-01-01"\n    events:\n      - name: LEC 2\n        type: lecture\n        title: Test\n        recording: '+PLAYER+'fixture\n  - date: "2999-01-01"\n    events:\n      - name: LEC 3\n        type: lecture\n        recording: '+PLAYER+'future\n---\n')
            git('add','.');git('commit','-m','published links')
            now=dt.datetime.now(dt.timezone.utc)
            self.assertEqual(len(discover(repo,now)),1)
            self.assertEqual(collect(repo,now)[1]['available'],0)
            cache=repo/CACHE_PREFIX;cache.mkdir(parents=True)
            raw=b'WEBVTT\n\n00:00:01.000 --> 00:00:06.000\nSynthetic test absolute loss sentence.'
            (cache/'fixture.vtt').write_bytes(raw)
            import hashlib
            meta=dict(status='available',recordingUrl=PLAYER+'fixture',sha256=hashlib.sha256(raw).hexdigest(),sourceUrl='https://example.org/export',method='test fixture',importedAt=now.isoformat())
            (cache/'fixture.json').write_text(json.dumps(meta))
            self.assertEqual(collect(repo,now)[1]['available'],0) # dirty files excluded
            git('add','.');git('commit','-m','cache captions')
            rows,coverage,_=collect(repo,dt.datetime.now(dt.timezone.utc))
            self.assertEqual(coverage['available'],1);self.assertEqual(len(rows),1)
            self.assertEqual(rows[0]['start'],1);self.assertTrue(rows[0]['url'].endswith('?start=0'))
            meta['sha256']='wrong';(cache/'fixture.json').write_text(json.dumps(meta))
            git('add','.');git('commit','-m','mismatch')
            self.assertEqual(collect(repo,dt.datetime.now(dt.timezone.utc))[1]['recordings'][0]['status'],'invalid')

if __name__=='__main__':unittest.main()
