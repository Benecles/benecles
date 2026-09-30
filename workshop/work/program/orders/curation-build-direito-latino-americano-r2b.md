# ORDER curation-build-direito-latino-americano-r2b

TOKEN BUDGET: 200000 tokens.

## Why this order exists

This is chunk 2 of the second and final redo generation for `curation-build-direito-latino-americano`. It runs only after chunk 1 (`curation-build-direito-latino-americano-r2`) ships. The original approved-plan build was rejected for the aula-07 box-and-arrow genealogy; chunk 1 restages lessons 03–08 and applies that correction. The rejection note is `program/ships/rejected/curation-build-direito-latino-americano-r1.md`.

## Inputs and scope

Implement the approved plan at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/direito-latino-americano-plan.csv`, approval marker `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/APPROVED-direito-latino-americano`.

This order owns only `aula-09.html`. Apply its approved add operation and preserve every byte outside figure blocks from the new current-live baseline. Do not edit lessons owned by chunk 1. Follow `program/preamble.md`: inspect ship maps, preserve the staged snapshot without overwriting, then refresh aula 09 from the current publish checkout after chunk 1 has shipped. Make an immutable baseline at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-direito-latino-americano-r2b-current-live/direito-latino-americano/`.

Do not edit the publish checkout. Capture aula 09 in desktop/phone and light/dark states and write `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2b-GATE.md` (≤50 lines) with exact path, staging URL, doubts, `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP` paths and exact-file `SHIPCOPY` metadata using the r2b baseline above.

## Done-condition

The approved aula-09 plan action is staged; its figure count matches the plan; non-figure bytes match the immutable r2b baseline; the page-scoped checker and full-course jank scan both exit 0; and the fresh GATE contains complete ship metadata only for aula 09.

## Mechanical queue check

```sh
python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/checks/check_curation_build.py --course direito-latino-americano --baseline /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-direito-latino-americano-r2b-current-live/direito-latino-americano --pages aula-09.html && /Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course direito-latino-americano --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2b-jank.csv && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2b-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2b-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2b-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2b-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r2b-GATE.md
```
