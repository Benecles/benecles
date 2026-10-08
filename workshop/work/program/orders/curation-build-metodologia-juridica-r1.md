# ORDER curation-build-metodologia-juridica-r1

Redo generation 1 for `curation-build-metodologia-juridica`. Token budget: 900000 tokens.

## Exact previous check failure

The original order exhausted both runner attempts. Its last course-check output reported:

- `FAIL courses/metodologia-juridica/aula-03.html: baseline=1, expected=2, actual=2; bytes outside figure blocks changed`
- `FAIL courses/metodologia-juridica/aula-05.html: baseline=1, expected=1, actual=2`

The prior gate also recorded seven phone-panel jank findings in plan-kept figures: aula-01 figures 1 and 2, aula-02 figure 1, aula-06 figure 2, and aula-14 figure 2. The old gate is blocked and is not approval to ship.

## Corrective work

Implement only the approved plan at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/metodologia-juridica-plan.csv`; its approval marker is `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/APPROVED-metodologia-juridica`.

First preserve this failed generation's current staging files and evidence under `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program-old/curation-build-metodologia-juridica-r1/`, without overwriting any existing copy. Follow `program/preamble.md` for current-live refresh and immutable baselines. Use a new baseline root at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-metodologia-juridica-r1-current-live/metodologia-juridica/`; never replace the original order's baselines or any existing r1 baseline.

For aula-03, restore every byte outside approved figure edits to the new immutable live baseline while retaining only plan-authorized figure changes. For aula-05, inspect its approved plan row and remove or correct the extra figure so the actual count equals the plan's expected count of one. Do not alter figure counts beyond the plan. Re-run the exact plan checker and the full-course jank scan. Clear any measured jank while preserving approved figure content/count and all non-figure lesson text; include any changed CSS or other live files in the new gate's exact ship map. Do not add unrelated polish or content.

Capture changed pages in desktop/phone and light/dark states; inspect those captures. Write a fresh GATE at `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-metodologia-juridica-r1-GATE.md` (at most 50 lines). Include exact changed paths and staging URLs, judgment calls and doubts, `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP` paths, and exact-file `SHIPCOPY` entries using the immutable r1 current-live baseline above. List only changed live files.

## Done-condition

Every approved plan action is implemented; aula-03 non-figure bytes match its immutable current-live baseline; every page's figure count matches the approved plan; the course-specific plan checker and full-course jank scanner both exit 0; and the fresh GATE has complete ship metadata.

## Mechanical queue check

`python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/check_build_metodologia-juridica.py metodologia-juridica && /Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course metodologia-juridica --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-metodologia-juridica-r1-jank.csv && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-metodologia-juridica-r1-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-metodologia-juridica-r1-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-metodologia-juridica-r1-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-metodologia-juridica-r1-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-metodologia-juridica-r1-GATE.md
