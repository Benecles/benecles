# ORDER curation-build-direito-constitucional-i-r2

Redo generation 2 and final permitted redo for `curation-build-direito-constitucional-i`.

TOKEN BUDGET: 900000 tokens.

## Exact failures being corrected

The original order exhausted both runner attempts because its queue check called the shared `check_build.py` with `direito-constitucional-i`; the checker printed `FAIL: usage: check_build.py metodologia-juridica` and never validated the course.

Redo generation 1 also exhausted both attempts. Its plan checker reported these non-figure byte mismatches: `aula-01.html`, `aula-02.html`, `aula-03-republica.html`, `aula-04.html`, `aula-05.html`, `aula-06-casos-precatorios.html`, `aula-06-casos.html`, `aula-06.html`, `aula-09.html`, `aula-10.html`, `aula-13.html`, `aula-14.html`, `aula-15-casos.html`, `aula-15.html`, `aula-16-casos.html`, `aula-16.html`, `aula-17.html`, `aula-18-limites.html`, `aula-24.html`, and `aula-25.html`.

It also reported plan count mismatches: `aula-15-casos.html` expected 1 / actual 2; `aula-15.html` expected 1 / actual 2; `aula-17.html` expected 1 / actual 2; `aula-18-casos.html` expected 0 / actual 1; `aula-19-casos.html` expected 1 / actual 2; `aula-21.html` expected 2 / actual 1; `aula-22-retrocesso.html` expected 2 / actual 1; `aula-22.html` expected 2 / actual 1; and `aula-23.html` expected 3 / actual 1. Its old GATE also said the full-course jank scan failed with 23 janky rows, all then attributed to the overlapping `jank-ci-mj` stage. The earlier `jank-ci-mj` order has since shipped; refresh from the current published baseline and run the full scan again.

## Approved scope and inputs

Implement only `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/direito-constitucional-i-plan.csv`, approved by `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/APPROVED-direito-constitucional-i`.

Follow `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/preamble.md` in full. Derive target pages from the plan, inspect current ship maps, preserve any still-unshipped owner, then refresh each unowned target from the current publish checkout and create immutable baselines from those same live files. The old r1 GATE and baselines are historical evidence, not this generation's baseline. Save r1 staging pages/evidence under `relay-design-2026-09-29/program-old/curation-build-direito-constitucional-i-r2/` without overwriting anything.

Figure counts may change only as the approved plan says. Keep all bytes outside planned figure insertions/removals identical to this generation's immutable current-live baseline. Correct every count and non-figure mismatch listed above. Do not add unrelated edits. Capture affected pages in desktop/phone and light/dark states and inspect the captures.

Use the new immutable baseline root `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-direito-constitucional-i-r2-current-live/direito-constitucional-i/`. Update the shared curation checker to accept `CURATION_BUILD_BASELINE_ROOT` as an optional baseline-root override while preserving its current default behavior for other courses; the r2 queue check below uses that variable. The course-specific wrapper must still validate this course's plan and non-figure bytes against the r2 baseline.

Write `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r2-GATE.md` (≤50 lines), with exact changed paths, staging URLs, judgment calls/doubts, `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP` paths, and exact-file `SHIPCOPY` entries using the immutable r2 current-live baselines. Include only files changed by this order.

## Done-condition

Every approved plan operation is implemented; the r2 course checker confirms all plan counts and unchanged non-figure bytes; the full-course jank scan exits 0; the changed-page captures are inspected; and the fresh GATE has complete ship metadata.

## Mechanical queue check

```sh
CURATION_BUILD_BASELINE_ROOT=/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-direito-constitucional-i-r2-current-live/direito-constitucional-i python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/check_build_direito-constitucional-i.py direito-constitucional-i && /Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course direito-constitucional-i --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r2-jank.csv && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r2-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r2-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r2-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r2-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r2-GATE.md
```
