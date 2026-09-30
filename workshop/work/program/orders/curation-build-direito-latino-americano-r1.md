# ORDER curation-build-direito-latino-americano-r1

TOKEN BUDGET: 900000 tokens.

## Approved input

Implement the approved plan at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/direito-latino-americano-plan.csv`. Its approval marker is `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/APPROVED-direito-latino-americano`.

Staging root: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29`. Publish checkout is read-only: `/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish`.

## Why this redo exists

Both attempts of `curation-build-direito-latino-americano` failed the queue check. Its last check output shows the course plan checker passed and the jank scan completed with 78 panel rows and zero janky. The check then failed because the required file `relay-design-2026-09-29/program/curation-build-direito-latino-americano-GATE.md` was absent. The retry must write the exact order-specific gate note and a complete ship map. The prior failed run did not produce a gate note or ship request.

## Work

Follow the current `program/preamble.md` before editing: derive the plan's exact target paths; inspect pending ship requests and their `SHIPCOPY` maps; preserve any unshipped staged owner; otherwise refresh each target from the current published file and take an immutable baseline from that same live file. Never overwrite an existing backup. Preserve the previous failed attempt's files before refreshing or changing them.

Implement only the approved figure-curation plan. The plan is the sole authority for figure insertions, removals, redraws, reclassifications, and allowed figure counts. Keep lesson text outside figures byte-for-byte unchanged except for figure insertions/removals explicitly required by the plan. Do not add unrelated polish or content. Use the course-specific checker `curation/check_build_direito-latino-americano.py`, then run the course jank scanner. Capture the changed lessons in desktop/phone and light/dark states, inspect those captures, and write the required order-specific gate note with exact changed paths, staging URLs, judgments and doubts.

Gate note: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r1-GATE.md` (50 lines maximum). Include `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP` paths, and exact-file `SHIPCOPY` entries. Put immutable staged pre-edit snapshots under `relay-design-2026-09-29/program-old/curation-build-direito-latino-americano-r1/`. Put immutable current-live baselines at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-direito-latino-americano-r1-current-live/direito-latino-americano/`. Include only changed live lesson pages in `SHIPCOPY`.

## Done-condition

Every approved plan item is implemented; the course-specific plan checker and jank scanner both exit 0; non-figure text matches the immutable pre-edit baseline except for plan-authorized figure insertions/removals; and the order-specific gate contains a complete exact ship map.

## Mechanical queue check command

```sh
python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/check_build_direito-latino-americano.py direito-latino-americano && /Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course direito-latino-americano --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r1-jank.csv && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r1-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r1-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r1-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r1-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-latino-americano-r1-GATE.md
```
