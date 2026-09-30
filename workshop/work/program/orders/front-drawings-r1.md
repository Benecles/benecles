ORDER front-drawings-r1 (redo generation 1; token budget 1500000)

Claude rejected `front-drawings` in `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/rejected/front-drawings.md`. Complete the original three-front drawing task from `orders/front-drawings.md`, correcting every stated reason. The rejection says the legal content is right, but the three results were still boxes/cards/arrows.

Required forms:
- Controle: transit map “três caminhos até o STF”: blue difuso route (juiz/tribunal → reserva de plenário → STF via RE/repercussão geral); red concentrado trunk with ADI, ADC, ADO, ADPF branches merging at the STF interchange; gray state route (state/municipal law → TJ/ADI estadual → STF by RE only for mandatory-reproduction norms). Use station dots with labels beside them, no text containers; phone route vertical. Keep each station linked to its lesson.
- Constitucional I: bottom-up stratigraphic section: Formação (01–03), Constituição/controle/reforma (04–06), Normas/interpretação (07–11), Direitos fundamentais (12–25). Put the rights catalogue inside the top layer as labeled “cores” (liberdades, propriedade, liberdade sexual, sociais e moradia, ambiente, identidade indígena); mark P1 (01–04) with a bracket. No cards or staircase indents.
- Processo Civil: railway line/timetable from petição inicial to sentença, in this sequence: petição inicial e pedido → indeferimento liminar/audiência → citação e intimação → resposta do réu → intervenção de terceiros → nulidades → julgamento. Show branch tracks only for actual procedural forks; station labels link to their lessons.

Before edits, preserve the current rejected staged pages and `d1/data` JSON under `R/program-old/front-drawings-r1/` without overwriting anything. Restore the three drawing fields to their pre-front-drawings state using `R/program-old/front-drawings/<course>/index.html` as the rendered reference, then implement the accepted forms through `R/d1/data/<course>.json` and render only with `python3 R/d1/front.py <course>`. Copy the current published fronts into `R/site` first to establish the live baseline. Do not hand-edit rendered index pages. Keep label text at least 11px rendered at 390 and 1280, with zero geometry collisions/overflow. Remove interface narration such as “cada entrada abre uma aula”; use only course lesson titles and content.

Capture the three `.front-drawing` diagrams in desktop/phone, light/dark under `R/program/front-drawings-r1-captures/`. Read `gates/README.md` for the manifest format. Write `R/program/front-drawings-r1-GATE.md` (≤50 lines), staging URLs, exact paths, decisions and doubts. Include the preamble's SHIPCHANGE/SHIPCHECK/SHIPCROP/SHIPCOPY lines; SHIPCOPY must contain exactly these three live pages and use baseline root `/Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/ships/baselines/front-drawings-r1/courses`.

Done-condition: all three required forms are implemented through the D1 generator; `check_front_drawings_r1.py` reports all 12 capture states clear; `d1/check_front.py` passes all three fronts; the GATE and immutable baselines exist.

Mechanical queue check command: `python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/program/checks/check_front_drawings_r1.py && python3 /Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/d1/check_front.py direito-constitucional-i processo-civil-i controle-de-constitucionalidade`

SHIP_GATE=/Users/benecles/Documents/Codex/2026-09-23/you-h/work/relay-design-2026-09-29/program/front-drawings-r1-GATE.md
