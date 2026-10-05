# Search EECS 245

A static Smart Search overlay for **eecs245.org**. It combines local semantic embeddings, exact terms, and mathematical concept recognition. One card per document, with lecture PDFs and recordings combined into one lecture card. Cards link to each matching section, problem, activity, lecture page, or recording moment. All five category buttons start selected, ordered Lectures, Notes, Homeworks, Labs, Past exams. Each category initially shows three documents with a Show more button. Notes reveal matching sections when clicked. The sort toggle switches between relevance and chronological course order (oldest first). Published solution explanations are included in the same cards as the questions.

## Run and deploy

Requires Node 22 or newer.

```sh
npm ci
npm test
npm run build
npm start
```

Standalone development preview: http://localhost:3245. The course website builds and deploys this app as an overlay through its existing GitHub Pages workflow; no separate domain or hosting service is needed. See the integrated build instructions below.

## Search and privacy

The quantized Apache-licensed all-MiniLM-L6-v2 model runs inside a browser worker. Document embeddings are computed in advance with the same model and mean pooling. Query embeddings, keyword matching, and ranking happen on the student's device. No paid model, API key, question endpoint, analytics, cookies, or student-query storage. The browser downloads the model and index from the same site; queries are never placed in network requests or URLs. Hosting providers still receive normal asset requests, including visitor IP addresses. External source links open without a referrer.

The first visit downloads approximately 45 MB of model/runtime assets; the model is cached by Transformers.js for later visits. Results combine BM25-style keyword ranking with semantic similarity using reciprocal-rank fusion. Explicit resource-only requests navigate directly to matching indexed sections. Queries run after a 350 ms typing pause, or immediately on Enter. Existing results remain visible until the new query finishes; outdated queries cannot replace them. The interface waits for the local model on first use and asks for a refresh if loading fails, rather than silently switching search modes. Semantic thresholds suppress unrelated results. Formula tags recognize vector inner products, including `\\vec u \\cdot \\vec v` and vector transpose products, so a formula-only question is findable by “dot product”. These tags supplement embeddings, since a general language model alone is unreliable on mathematical notation.

## Corpus and release boundary

`source-manifest.json` records source hashes and public repository commits. `search-index.json` records the coverage count. The current snapshot covers all 47 published note pages (including the appendix), 10 lecture PDFs, 4 homework handouts, 5 lab handouts, 9 past exams, and 10 lecture recordings: **85 documents / 4,683 passages**. Duplicate PDF/HTML versions of the same questions use their canonical HTML document. Topic worksheets repeat past-exam questions; their canonical exam locations are used to avoid duplicate cards.

Only committed, published public sources are indexed; the private repository and local uncommitted edits are never read. Release timestamps use the first addition of each source to public repository history (a conservative date for exam questions migrated into their current format). The deployment contains eligible material only: hiding future records in browser code would expose them. Rebuilding is required to add later releases. Earlier release snapshots are not offered by the public UI.

All 195 lecture pages have text-layer extraction or local Vision OCR. Handwriting and formulas in OCR can be imperfect; previews label OCR and link to the original page. Raster-only diagrams are not interpreted. Public exam practice notices remain on the linked source pages.

## Refresh the index

The importer reads committed course repositories under `EECS245_SOURCES` (default: `/Users/surajrampure/Desktop/245`, with `notes` and `website`). Check that these match their remote published commits before indexing. It also needs a current published `eecs245/exams` clone at `EECS245_EXAMS`; run that repository's `scripts/build.sh --compose-only` to compose pages from committed question sources. Override paths using environment variables.

Lecture OCR caches live at `EECS245_OCR`. The local `scripts/ocr.swift` extracts PDF text or uses macOS Vision for scanned pages. Compile it with `swiftc scripts/ocr.swift -o /tmp/eecs245-ocr`; run it on each published lecture PDF and save its one-line JSON output as `<pdf-stem>.json` in that directory. Refresh the cache whenever a lecture PDF changes.

```sh
python3 scripts/build_search_index.py
npm run embed
npm test
npm run build
```

The model files are pinned in `model-manifest.json` and self-hosted under `public/models/`; no runtime downloads from Hugging Face or a CDN. The static deployment excludes the earlier chat prototype and its backend. Model/runtime licenses are shipped in `dist/licenses/`.

Programming notebooks, lab recap sections, and practice/mock exams are excluded. Queries share case and whitespace normalization, course-topic aliases, and conservative spelling correction before semantic embedding. For example, “absolute”, “absolute loss”, “mean absolute error”, and “MAE” use the same query; “absolute value” remains distinct. Squared-loss and dot-product aliases work similarly. Aliases connect related course search topics, rather than asserting that a single-example loss and an averaged error metric are identical mathematical quantities.

Spelling correction uses unique close matches from curated course vocabulary, preserves known corpus words and short mathematical symbols, and displays corrections in the interface. Ambiguous corrections remain unchanged. The semantic ranker includes exact-term and mathematical-concept boosts; its ranking is combined with keyword evidence in a single result set. The “How matches work” disclosure uses the course author’s explanation of chunking, 384-dimensional vectors, and cosine similarity, with a link to the all-MiniLM-L6-v2 model. Match details do not display numeric similarity scores. Resource requests such as “HW 4 problem 3”, “lecture 8 projection”, “lab 4 activity 2”, “note 3.4”, and “fa25-mt1 problem 4” constrain both retrieval paths before ranking. The remaining topic words supply the query embedding. Missing resources return no matches, rather than falling back to unrelated materials. Resource-only requests do not need query inference, and different resource requests with the same topic reuse the cached topic embedding. Equivalent queries share bounded in-memory caches; queries and corrections remain on the student's device. Changes to aliases and ranking do not require regenerating document embeddings.

## Integrated course-site build

The course site replaces the built-in Jekyll search with a **New: Smart Search** header button and a **⌘ F** hint. Clicking it or pressing Cmd+F (Ctrl+F on other platforms) opens a native modal over the current page and blurs the course site. Escape, the close button, or clicking the backdrop closes it and restores focus. The search model and index load only when the layer is first opened; later opens retain the query and cached model. The sidebar search link and built-in Lunr search are removed. The iframe app is served under `/assets/course-search/` and communicates with its parent only through origin- and source-checked focus, close, and font messages. The search interface uses the parent site’s computed body font, including its Palatino preference, and follows font changes while open.

The website's existing deployment workflow runs `tools/course-search/scripts/rebuild_for_jekyll.sh` before Jekyll. This checks out current public notes and exam sources, composes exam questions, reuses hash-verified lecture OCR or extracts newly changed PDFs, rebuilds the index, and regenerates embeddings only when embedding inputs change. Jekyll then copies the generated assets into the deployed site. A website build refreshes the search; notes/exam changes alone require running the website's existing build-site workflow manually. No scheduled automation or query service is needed.

For a manual local refresh from the website checkout: `cd tools/course-search && npm ci`, then run `bash tools/course-search/scripts/rebuild_for_jekyll.sh` from the website root before `bundle exec jekyll build`. Linux OCR fallback requires Poppler and Tesseract; unchanged lecture PDFs reuse the checked-in local Vision transcripts.

## Other videos

`_data/other-videos.json` is the explicit list of instructor videos approved for
search. Each entry includes its original title, direct YouTube URL, upload date,
channel ID, and qualifying course sources. The production builder reads the
committed list and indexes one title-only record per video. The Other videos
filter controls these results, which open YouTube directly. Exam walkthroughs
also match searches for their exam and problem number. No captions are fetched.

The initial list contains 42 videos from rampureatumich embedded in the notes,
linked through past homepage playlists, or walking through EECS 245 exams.
Uploads from 2024 are excluded.

## Lecture recording search

The first category, **Lectures**, uses the same local semantic search,
worker, model, embedding build, filtering, previews, and chronological sort as
other materials. Recording cards show a cached original player thumbnail and a short transcript excerpt.
Click a lecture card to reveal separate recording timestamps and PDF page links.
The purple Lectures filter controls both recordings and PDFs; their matching
locations appear in the combined card. Combining formats does not add their scores together. Expanded
cards stay open through semantic updates and sorting, and reset for a new query.
Preview thumbnails are cached under `public/recording-previews/` with provenance;
search never contacts Leccap to load them.
Hits from one recording share one card regardless of `?start=`. Overlapping or
nearby hits (up to a 10-second gap) merge into moments no longer than 120 seconds;
the best matching excerpt survives. Links start five seconds before the displayed
moment, clamped to zero, for context. Other categories keep their existing behavior.

`recordings.py` discovers links and lecture metadata only from committed
`_modules/week-*.md`. It requires a published Leccap link and a lecture date no
later than today in America/Detroit. Link introduction in public Git history is
the release evidence; unpublished/future schedule entries and dirty cache files
are excluded. Existing note, assignment, PDF, and public-exam rules are unchanged.

### Caption acquisition and offline cache

Install `python3 -m pip install -r scripts/requirements.txt` alongside `npm ci`.
Builds **never contact Leccap**. Import an authorized timestamped export first:

```sh
python3 scripts/import_captions.py ucCtbs /path/to/lecture-2.vtt \
  --source-url 'https://leccap.engin.umich.edu/leccap/player/api/webvtt/?rk=ucCtbs' \
  --method 'Authorized player caption-track export'
# Review and commit scripts/caption-cache/ucCtbs.{vtt,json}, then rebuild.
```

The player track URL above and integer `?start=1630` behavior were verified in
the original investigation supplied for this task. They are player interfaces,
not a promised bulk-export API. A successful authorized browser session can save
the actual timestamped caption-track response; do not automate verification,
copy credentials into the repo, or treat a challenge response as captions.

The supported instructor management route is **Manage Recordings → Edit →
Captions → caption provider**. Michigan documents [caption management and
WebVTT/SRT formats](https://teamdynamix.umich.edu/TDClient/76/Portal/KB/Article/5181/How-do-I-add-captions-to-my-Lecture-Recordings)
and [individual transcript downloads](https://teamdynamix.umich.edu/TDClient/47/LSAPortal/KB/ArticleDet?ID=9438).
The documented TXT download is not sufficient if it lacks timestamps. Obtain a
timed WebVTT/SRT export from the authorized player track or CAEN support.
In the verified instructor interface, the selected Whisper provider exposes
original WebVTT in the **Captions** textarea. Export that field read-only;
no Save action or caption edits are needed.
The importer rejects untimed text instead of estimating timings.

Exports are cached with source URL, acquisition method, SHA-256 and import time.
The build verifies provenance and hashes, parses timestamped cues, strips caption
markup, removes exact duplicate cues, and creates coherent overlapping passages.
Zero-duration provider artifacts are omitted without inventing timings; the raw
export remains intact. Reversed timestamps are rejected.
It prefers sentence endings after 30 seconds, aims for 60 seconds, caps at 90
seconds, and overlaps roughly 15 seconds of whole cues. Gaps and dense speech
can produce shorter passages. The pinned local MiniLM tokenizer enforces the
254-token content budget (plus two special tokens); no caption passage is silently
truncated. Exceptionally long individual cues require a better timed export.

### Coverage and real-data validation

`metadata.recordings` reports each published lecture as available, missing,
pending, or invalid, with a reason and cue/passages counts where available. The
UI shows a small indexed-materials footer below a divider. It derives coverage
from the actual records and preserves gaps, using plain hyphens and distinguishing
recording/PDF lecture ranges when they differ. Notes and past exams are linked
with the text “All notes chapters and all past exams” and uniform bullet separators. “Available” means a valid cached export, not a guarantee that the
provider captioned every second. First/last cue times are retained for auditing.
Missing captions do not block unrelated search categories or the website build.

On 2026-10-02: **10 of 10 published recordings have cached captions**. Their
original Whisper WebVTT was exported read-only from the instructor Captions
textarea in an authorized Chrome session. Provenance points to each actual
management page. No verification was bypassed, and no synthetic captions are
published. Four zero-duration provider artifacts were omitted from indexing;
the unmodified exports retain them.

The snapshot adds **15,970 timed cues / 2,445 recording passages** to the existing
75 documents / 2,238 passages. Lecture 2 contains “Yeah, there's an absolute loss
as well.” at 27:10. The real-data semantic/keyword regression checks that this
cue survives in a matching moment and that its playback link includes the
five-second context offset. Chrome playback was verified at 26:40 via the
26:45–28:15 matching moment. Synthetic tests remain exclusively in `test/`.

`npm test` includes caption parsing, release/cache gates, token limits, moment
merging/deduplication, keyword and semantic integration, coverage, category
filtering, and chronological sorting. Search queries remain on the student's
device. Opening a recording explicitly navigates to Leccap; no Leccap requests
are made by the search app itself.
