# ORDER curation-build-direito-latino-americano-r2

TOKEN BUDGET: 500000 tokens.

## Why this order exists

This is chunk 1 of the second and final redo generation for `curation-build-direito-latino-americano`. Claude rejected `curation-build-direito-latino-americano-r1` on 2026-09-30: the aula-07 “genealogy” used three text boxes joined by arrows, contrary to the owner’s NO BOXES rule. The exact rejection is `program/ships/rejected/curation-build-direito-latino-americano-r1.md`. Claude asked for a vertical stem with three nodes, court and year beside each node, a one-line serif gloss, and edge marks `retoma` / `amplia às prisões`.

## Inputs and scope

Implement the approved plan at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/direito-latino-americano-plan.csv`, approval marker `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/APPROVED-direito-latino-americano`.

This order owns only `aula-03.html` through `aula-08.html` (six lessons). Apply those lessons’ approved add/redraw operations, retain all approved keep rows, and preserve all text outside figure blocks byte-for-byte from the new current-live baselines. Redraw the aula-07 ECI figure as the requested stem-and-node genealogy. Do not use text boxes connected by arrows or lines. Leave `aula-09.html` to the next chunk, `curation-build-direito-latino-americano-r2b`.

Before editing, follow `program/preamble.md`: inspect ship maps for ownership, preserve existing staging snapshots without overwriting, and refresh these six lesson files from the current publish checkout. Make immutable baselines from those same current-live files at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-direito-latino-americano-r2-current-live/direito-latino-americano/`. The rejected r1 staging is reference material only; do not use it as the baseline or copy it wholesale over current live.

Do not edit the publish checkout. Capture changed pages in desktop/phone and light/dark states and write `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2-GATE.md` (≤50 lines) with exact changed paths, staging URLs, doubts, `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP` paths and exact-file `SHIPCOPY` metadata using the r2 baseline above.

## Done-condition

The approved plan actions for aulas 03–08 are staged, including the no-box aula-07 genealogy; counts match the plan; non-figure bytes match the immutable r2 baselines; the chunk checker and full-course jank scan both exit 0; and the fresh GATE contains complete ship metadata for only the six chunk pages.

## Mechanical queue check

```sh
python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/checks/check_curation_build.py --course direito-latino-americano --baseline /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-direito-latino-americano-r2-current-live/direito-latino-americano --pages aula-03.html aula-04.html aula-05.html aula-06.html aula-07.html aula-08.html && /Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course direito-latino-americano --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2-jank.csv && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2-GATE.md
```
