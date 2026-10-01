# VIS-2 figure catalogue

Catalogue source: the `origin/main` snapshot used to create branch `codex/vis-2`.
The inventory covers every HTML file directly inside `courses/*/` and includes
SVG elements with rendered width at least 120px, except SVGs whose viewBox is
exactly `0 0 10 10`. Each included SVG has one 320px-wide light-mode PNG in
`thumbs/` (the thumbnails are git-ignored and are not committed).

`genre_guess` is an explicit heuristic guess, not a human-curated classification.
The rules use accessible/caption text plus SVG text, element counts, markers,
rectangles, lines and aspect ratio. `index.html` groups by genre and course;
`index-<genre>.html` contains one sheet per genre. Cards link to the live page.

Generate with `node work/vis-catalog/catalog.mjs`. Run the one-pass inventory,
thumbnail and local-sheet check with `node work/vis-catalog/check.mjs`.

## Build result

- Qualifying figures and catalogue rows: 784
- Unique ids: 784
- Rendered thumbnails: 784 (7,796,247 bytes; 7.44 MiB)
- Genre sheets plus all-figures sheet: 10; local file URLs loaded successfully
- Mechanical check: PASS (784 qualifying SVGs = 784 rows = 784 thumbnails;
  all ids unique; all sheets' card counts match; thumbnail set is below 60 MB)

| Heuristic genre guess | Figures |
| --- | ---: |
| comparison | 23 |
| flow-or-decision | 47 |
| map | 15 |
| matrix-or-table | 37 |
| other | 447 |
| route-or-line | 24 |
| scale | 25 |
| strata-or-stack | 148 |
| tree | 18 |
