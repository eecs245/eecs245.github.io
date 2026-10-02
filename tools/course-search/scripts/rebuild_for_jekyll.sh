#!/usr/bin/env bash
# Run before Jekyll. The browser never sends queries to this build process.
set -euo pipefail
APP_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WEBSITE_ROOT="$(cd "$APP_ROOT/../.." && pwd)"
SOURCE_ROOT="$(mktemp -d)"
trap 'rm -rf "$SOURCE_ROOT"' EXIT
ln -s "$WEBSITE_ROOT" "$SOURCE_ROOT/website"
git clone --filter=blob:none --no-checkout https://github.com/eecs245/notes.git "$SOURCE_ROOT/notes"
git -C "$SOURCE_ROOT/notes" sparse-checkout set 00_math_foundations 01_introduction_to_supervised_learning 02_simple_linear_regression 03_vectors 04_linear_independence 05_matrices 06_linear_transformations_and_projections 07_regression_using_linear_algebra 08_gradients 09_eigenvalues_and_eigenvectors 10_singular_value_decomposition
git -C "$SOURCE_ROOT/notes" checkout main
git clone --filter=blob:none --no-checkout https://github.com/eecs245/exams.git "$SOURCE_ROOT/exams"
git -C "$SOURCE_ROOT/exams" sparse-checkout set src scripts _data resources
git -C "$SOURCE_ROOT/exams" checkout main
bash "$SOURCE_ROOT/exams/scripts/build.sh" --compose-only
export EECS245_SOURCES="$SOURCE_ROOT"
export EECS245_EXAMS="$SOURCE_ROOT/exams"
export EECS245_OCR="$APP_ROOT/scripts/ocr-cache"
cd "$APP_ROOT"
python3 scripts/ocr_cache.py
python3 scripts/build_search_index.py
npm run embed
npm test
npm run build -- --embedded
mkdir -p "$WEBSITE_ROOT/assets/course-search"
cp -R dist/. "$WEBSITE_ROOT/assets/course-search/"
