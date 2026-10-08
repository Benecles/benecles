# ORDER curation-build-direito-constitucional-i-r1

Redo generation 1 for `curation-build-direito-constitucional-i`.
Token budget: 900000.

## Exact failure and correction

Both runner attempts of the original order ended with this check output:

`FAIL: usage: check_build.py metodologia-juridica`

The original queue check invoked the shared `curation/check_build.py` while another curation build was running. The shared checker entry point was temporarily incompatible with the Constitucional I invocation, so the mechanical check failed before validating this course. Do not edit the shared `check_build.py` or another course's checker. Use a course-specific wrapper named `curation/check_build_direito-constitucional-i.py`, following the existing wrappers for Processo Civil I, Metodologia Jurídica, and Latam; it should call the shared checker's `main()` with the requested course argument. All curation-build rows share the `curation-builds` queue lock, so this order waits until the currently running builds finish and cannot race another course on the shared checker.

## Inputs and scope

- Approval marker: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/APPROVED-direito-constitucional-i`
- Approved plan: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/direito-constitucional-i-plan.csv`
- Staging site: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site`
- Publish checkout, read only: `/Users/benecles/Documents/Codex/2026-09-05/okay-couple-things-so-first-of/work/study-lab-publish`
- Expected GATE: `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r1-GATE.md`

Implement exactly the approved figure-curation plan for `direito-constitucional-i`. The plan alone controls figure insertions, removals, redraws, and reclassifications. Figure counts may change only as the plan directs. Keep every lesson byte outside planned figure insertions/removals unchanged from the immutable published baseline. Add no unrelated polish or content.

Inspect the current staged pages and artifacts from the two failed attempts first. Preserve all affected pre-edit staging pages under `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program-old/curation-build-direito-constitucional-i/` without overwriting any existing copy. Preserve published baselines at the matching paths under `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/curation-build-direito-constitucional-i/direito-constitucional-i/`; never replace an existing baseline. Reuse valid work from the failed attempts. If planned edits are already complete, do not rebuild them: finish the correct plan check, jank scan, captures, and fresh GATE handoff.

Run the course-specific wrapper with `direito-constitucional-i`, then scan the full course with `gates/jank.mjs`. Capture affected pages at desktop and phone, light and dark, and inspect the captures. Write the expected GATE in at most 50 lines with exact changed paths, staging URLs, decisions and doubts, and required `SHIPCHANGE`, `SHIPCHECK: PASS`, 1–3 absolute `SHIPCROP`, and exact-file `SHIPCOPY` entries. `SHIPCOPY` baselines must use the immutable baseline root above and include only changed live lesson pages. Do not edit or ship from the publish checkout.

## Done-condition

Every approved plan item is implemented; the course-specific plan checker and full-course jank scan exit 0; non-figure lesson bytes match the immutable baseline except planned figure insertions/removals; and the fresh GATE contains complete ship metadata.

## Mechanical queue check

`python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/curation/check_build_direito-constitucional-i.py direito-constitucional-i && /Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/gates/jank.mjs --site /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/site --course direito-constitucional-i --out /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r1-jank.csv && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r1-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r1-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r1-GATE.md && grep -q '^SHIPCROP: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r1-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r1-GATE.md`
