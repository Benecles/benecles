# front-drawings-r2 — repair the failed handoff check

Token budget: 30,000.

This is the second and final redo generation of `front-drawings`. The first redo, `front-drawings-r1`, staged the requested transit map, stratigraphic section, and railway drawing. Its two runner attempts failed before validating that work because the queue invoked the nonexistent `program/checks/check_front_drawings.py`. The actual checker is `program/checks/check_front_drawings_r1.py`; it reads the r1 capture report and gate note itself. The existing r1 gate records 12 clean viewport/theme states and passing course-front checks.

Do not redesign or rebuild the drawings when the corrected checks pass. Reuse the staged r1 pages, data, immutable pre-edit baselines, and captures. Run the actual r1 capture checker and the D1 course-link checker. Write `relay-design-2026-09-29/program/front-drawings-r2-GATE.md` (≤50 lines) as a fresh ship handoff explaining that no page changes were needed because only the queue checker path was wrong. Include the three staging URLs and the required `SHIPCHANGE`, `SHIPCHECK: PASS`, `SHIPCROP`, and `SHIPCOPY` lines. Reuse the immutable baseline at `program/ships/baselines/front-drawings-r1/courses`; do not overwrite it or any `program-old` copy. The SHIPCOPY file list is `direito-constitucional-i/index.html,processo-civil-i/index.html,controle-de-constitucionalidade/index.html` from `relay-design-2026-09-29/site` to the publish root.

If a corrected check exposes a genuine defect in the staged drawings, fix only that reported defect in the D1 source data and regenerate only the affected front, preserving all existing baselines. Do not add content or change unrelated front layout. This generation is the last permitted redo; if its two runner attempts still fail, document it as blocked for Claude.

Done-condition: the actual r1 capture checker and the D1 front checker exit 0, and the new r2 gate note exists with all required ship metadata. Queue check:

```sh
python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/checks/check_front_drawings_r1.py && python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/d1/check_front.py direito-constitucional-i processo-civil-i controle-de-constitucionalidade && test -s /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/front-drawings-r2-GATE.md && grep -q '^SHIPCHANGE: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/front-drawings-r2-GATE.md && grep -q '^SHIPCHECK: PASS' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/front-drawings-r2-GATE.md && grep -q '^SHIPCOPY: ' /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/front-drawings-r2-GATE.md
```
