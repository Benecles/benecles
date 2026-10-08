ORDER d2-reframe-r1 (redo generation 1; token budget 700000)

Correct the first Claude D2 follow-up: remove the `s/data` label (use `Toulouse · formação`) and move the Coimbra label to open water west of Portugal so no Coimbra→Brazil flow crosses the label. Approval of this request must include Claude's look at the `aula-01` Africa coastline crop; this gate captures all five pages and links that crop first.

Before edits, preserve current staged pages under `R/program-old/d2-reframe-r1/`. Copy the five current published Metodologia pages into `R/site/courses/metodologia-juridica/` to discard unapproved jank-ci-mj staging changes while retaining the shipped D2 baseline. Snapshot those exact live bytes under `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/d2-reframe-r1/metodologia-juridica/`. Rebuild/install only the five D2 figure plates with the existing `R/d2/build_plates.py` and `R/d2/install_plates.py`; do not change text outside figures or alter unrelated non-plate figures.

Capture all five plates at desktop/phone and light/dark. Write `R/program/d2-reframe-r1-GATE.md` (≤50 lines), with exact file list, URLs, results, doubts, SHIPCHANGE/SHIPCHECK/SHIPCROP/SHIPCOPY lines. SHIPCOPY is only the five Metodologia lesson pages and uses `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/d2-reframe-r1/metodologia-juridica` as baseline root. `SHIPCROP` must list the aula-01 desktop crop first, followed by aula-02 and aula-14 desktop crops. The next D2 order cannot run until this one is actually shipped.

Done-condition: Toulouse and Coimbra corrections are staged, text outside the figure plates is unchanged, the five-page plate and geometry checks pass, and the gate includes the specified aula-01 crop.

Mechanical queue check command: `python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/d2/check_plate.py && python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/d2/check_collisions.py`

SHIP_GATE=/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/d2-reframe-r1-GATE.md
