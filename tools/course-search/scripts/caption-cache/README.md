# Authorized caption exports

This directory intentionally contains no transcript fixtures. As of 2026-10-02,
10 released recordings are linked by the schedule, but none could be imported:
the cloud browser remained on Cloudflare verification for Lecture 2 after one
reload. No verification was bypassed and no timestamps were fabricated.

The build reads only committed `<recording-id>.vtt` and `<recording-id>.json`
pairs. Use `scripts/import_captions.py` to validate a local WebVTT or SRT export
and write its SHA-256, source URL, import time, and acquisition method. `.vtt`
is the cache filename for either accepted format; the parser detects timing
syntax. Never commit cookies, access tokens, HTML challenge pages, or private
recordings. Review caption exports before committing them to this public repo.

A recording awaiting caption generation may instead have a committed JSON file
with `status: "pending"` and a `reason`. Missing, pending, and invalid caches are
reported separately in `metadata.recordings.recordings`; none produce results.
Removing the published schedule link also removes its cached transcript from
the next generated search index. Old cached files should also be removed from
this public repository if a recording is withdrawn.
