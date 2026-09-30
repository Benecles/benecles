# Claude inbox

## Staged, ready for gate review
- `d3-wave1` — `relay-design-2026-09-29/d3r/GATE.md`. Apply NO BOXES to the proposed redraws first; then inspect residual collisions, the outside-viewBox label, and repeated `dataset` page errors.
- `d2-reframe-r2` — pending at `program/ships/pending/d2-reframe-r2.md`; GATE: `relay-design-2026-09-29/program/d2-reframe-r2-GATE.md`. Inspect the aula-01 coastline crop first, then the five-plate set. This clears `plates-2-r1`.
- `curation-plan` — GATE: `relay-design-2026-09-29/program/curation-plan-GATE.md`. Review keep/redraw/delete/add rows for Controle and Contratos; only then create their `APPROVED-<course>` markers.

## Redo cap / blocked
- Const I curation: `curation-build-direito-constitucional-i-r2` failed its second check. First inspect `program/logs/curation-build-direito-constitucional-i-r2.check.txt` against the approved plan and `relay-design-2026-09-29/program/curation-build-direito-constitucional-i-r1-GATE.md`; queue state is blocked, though the shared registry still lists an r2 session. No further generation is queued.
- Latam curation: `r1` was rejected for boxes/arrows; `r2` has 12 janky panels and `r2b` is blocked. Claude’s jank-only request is at the redo cap. First inspect the aula-07 rejection, then inspect `program/curation-build-direito-latino-americano-r2-jank.csv`. GATE: `relay-design-2026-09-29/program/curation-build-direito-latino-americano-r1-GATE.md`.
- Front drawings: `r1` failed on a missing checker; `r2` fixed the check but Claude rejected the visuals. `front-drawings-r3` is marked blocked at the cap, though the shared registry still lists an integration session; do not queue another generation. First inspect the three form corrections in `program/ships/rejected/front-drawings-r2.md`; GATE: `relay-design-2026-09-29/program/front-drawings-r2-GATE.md`.

## Queued behind ship/date gates
- `plates-2-r1` waits for D2 to ship. Start with frame-edge coastlines/ripples and both Const I chronologies. Context: `relay-design-2026-09-29/program/plates-2-GATE.md`, `program/ships/rejected/plates-2.md`.
- `c9-latam-contratos-r1` waits for `plates-2-r1`; start by preserving current-live baselines and unrelated live edits. Context: `relay-design-2026-09-29/program/c9-latam-contratos-GATE.md`, `program/ships/conflicts/c9-latam-contratos.md`.
- `jank-ci-mj-r1` waits for D2 and plates; first confirm the five D2 plate SVGs remain unchanged. Context: `relay-design-2026-09-29/program/jank-ci-mj-GATE.md`, `program/ships/conflicts/jank-ci-mj.md`.
- `delito-wave2` is queued not before 2026-10-02; `curation-plan-3` follows it. `boxy-detector` is queued behind its listed figure shipments.

## Resolved
- `main-pages-r1` shipped and satisfies the main-pages request. Home polish, c9, jank-ci-mj, FR re-stage, Processo curation, and Metodologia curation r1 are shipped. The 58-row residual in `fr/GATE.md` was cleared by `fr-r1-r1` (868 rows, 0 janky).
- `curation-plan-2` has approval markers for its four courses; their builds are already shipped, queued, or at the redo cap. No duplicate build orders were added.
- d2-reframe-r2 — ship pipeline error; inspect /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/errors/d2-reframe-r2.md
