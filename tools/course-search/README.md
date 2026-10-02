# Search EECS 245

A static Smart Search overlay for **eecs245.org**. It combines local semantic embeddings, exact terms, and mathematical concept recognition. One card per document, with links to each matching section, problem, activity, or lecture page. All six category buttons start selected. Each category initially shows three documents with a Show more button. Notes reveal matching sections when clicked. The sort toggle switches between relevance and chronological course order (oldest first). Published solution explanations are included in the same cards as the questions.

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

The quantized Apache-licensed all-MiniLM-L6-v2 model runs inside a browser worker. Document embeddings are computed in advance with the same model and mean pooling. Query embeddings and cosine ranking happen on the student's device. No paid model, API key, question endpoint, analytics, cookies, or student-query storage. The browser downloads the model and index from the same site; queries are never placed in network requests or URLs. Hosting providers still receive normal asset requests, including visitor IP addresses. External source links open without a referrer.

The first visit downloads approximately 45 MB of model/runtime assets; the model is cached by Transformers.js for later visits. Exact search works while the semantic model loads and remains available if it fails. Semantic thresholds suppress unrelated results. Formula tags recognize vector inner products, including `\\vec u \\cdot \\vec v` and vector transpose products, so a formula-only question is findable by “dot product”. These tags supplement embeddings, since a general language model alone is unreliable on mathematical notation.

## Corpus and release boundary

`source-manifest.json` records source hashes and public repository commits. `search-index.json` records the coverage count. The current snapshot covers all 47 published note pages (including the appendix), 10 lecture PDFs, 4 homework handouts, 5 lab handouts, and 9 past exams: **75 documents**. Duplicate PDF/HTML versions of the same questions use their canonical HTML document. Topic worksheets repeat past-exam questions; their canonical exam locations are used to avoid duplicate cards.

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

Programming notebooks, lab recap sections, and practice/mock exams are excluded. Queries share case and whitespace normalization, course-topic aliases, and conservative spelling correction before keyword matching and semantic embedding. For example, “absolute”, “absolute loss”, “mean absolute error”, and “MAE” use the same query; “absolute value” remains distinct. Squared-loss and dot-product aliases work similarly. Aliases connect related course search topics, rather than asserting that a single-example loss and an averaged error metric are identical mathematical quantities.

Spelling correction uses unique close matches from curated course vocabulary, preserves known corpus words and short mathematical symbols, and displays corrections in the interface. Ambiguous corrections remain unchanged. Keyword ranking rewards informative terms and headings, saturates repeated words, and allows substantial partial matches for longer queries. Semantic results are merged with keyword results using reciprocal-rank fusion so keyword passages remain available after the model loads. Equivalent queries share bounded in-memory caches; queries and corrections remain on the student's device. Changes to aliases and ranking do not require regenerating document embeddings.

## Integrated course-site build

The course site replaces the built-in Jekyll search with a **New: Smart Search** header button and a **⌘ F** hint. Clicking it or pressing Cmd+F (Ctrl+F on other platforms) opens a native modal over the current page and blurs the course site. Escape, the close button, or clicking the backdrop closes it and restores focus. The search model and index load only when the layer is first opened; later opens retain the query and cached model. The sidebar search link and built-in Lunr search are removed. The iframe app is served under `/assets/course-search/` and communicates with its parent only through origin-checked focus/close messages.

The website's existing deployment workflow runs `tools/course-search/scripts/rebuild_for_jekyll.sh` before Jekyll. This checks out current public notes and exam sources, composes exam questions, reuses hash-verified lecture OCR or extracts newly changed PDFs, rebuilds the index, and regenerates embeddings only when embedding inputs change. Jekyll then copies the generated assets into the deployed site. A website build refreshes the search; notes/exam changes alone require running the website's existing build-site workflow manually. No scheduled automation or query service is needed.

For a manual local refresh from the website checkout: `cd tools/course-search && npm ci`, then run `bash tools/course-search/scripts/rebuild_for_jekyll.sh` from the website root before `bundle exec jekyll build`. Linux OCR fallback requires Poppler and Tesseract; unchanged lecture PDFs reuse the checked-in local Vision transcripts.

## Lecture recording search

The sixth category, **Lecture recordings**, uses the same local keyword search,
worker, model, embedding build, filtering, previews, and chronological sort as
other materials. Recording cards show transcript excerpts and timestamp links.
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
timed WebVTT/SRT export from the authorized player track or CAEN support; a
management timed-download control could not be verified in this environment.
The importer rejects untimed text instead of estimating timings.

Exports are cached with source URL, acquisition method, SHA-256 and import time.
The build verifies provenance and hashes, parses timestamped cues, strips caption
markup, removes exact duplicate cues, and creates coherent overlapping passages.
It prefers sentence endings after 30 seconds, aims for 60 seconds, caps at 90
seconds, and overlaps roughly 15 seconds of whole cues. Gaps and dense speech
can produce shorter passages. The pinned local MiniLM tokenizer enforces the
254-token content budget (plus two special tokens); no caption passage is silently
truncated. Exceptionally long individual cues require a better timed export.

### Coverage and remaining acceptance check

`metadata.recordings` reports each published lecture as available, missing,
pending, or invalid, with a reason and cue/passages counts where available. The
UI always displays the number with cached captions and identifies omitted
lectures. “Available” means a valid cached export, not a guarantee that the
provider captioned every second. First/last cue times are retained for auditing.
Missing captions do not block unrelated search categories or the website build.

On 2026-10-02: **0 of 10 published recordings have cached captions**. Cloudflare
blocked the cloud browser on Lecture 2 after one reload. To finish real-data
acceptance: import authorized exports, rebuild, search `absolute loss`, verify
Lecture 2 around 27:10, and open its timestamp link. Do not use the supplied cue
summary as transcript text. Synthetic tests remain exclusively in `test/`.

`npm test` includes caption parsing, release/cache gates, token limits, moment
merging/deduplication, keyword and semantic integration, coverage, category
filtering, and chronological sorting. Search queries remain on the student's
device. Opening a recording explicitly navigates to Leccap; no Leccap requests
are made by the search app itself.
