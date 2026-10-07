# PROC-R2 · CEO rulings on the escalations (07/10)

The Source Pipeline sends a second REVISE to the CEO, not the chairman. Rulings:

1. **Second-REVISE blueprints** (Aula 03, 08-revelia, 10, 10-estabilizacao, 11-merito, 15): the author makes ONE targeted pass that fixes exactly the numbered points in that lesson's round-2 `panel.md`, and nothing else. The orchestrator checks each point against the diff (point → where it was fixed) and records the result under the panel as "CEO ruling 07/10: fixed 1–N". No third panel. The blueprint then counts as APPROVED.
   - Aula 03: one Didier edition and one locator style throughout (printed p. + PDF p., as in 08-revelia's revision).
   - Wherever a panel says the closing set must test something the function promises, the fix is a closing item, never a narrower function.
2. **Unfinished S5a** (Aula 06 panel, Aula 07 author round + panel, Aula 09 author check + panel, Aula 13 author + panel): finish them on the normal rule (author → panel → at most one revision → panel; a second REVISE follows ruling 1).
3. **F-023 (writing pause) is lifted for Processo.** It predates the chairman's 04/10 no-gates order. Replace it with *prototype, then waves*: write ONE approved P2 lesson first (Aula 14), run every check, and turn whatever went wrong into numbered FLIGHT-LOG entries. Then write the rest in waves of ≤6, P2 first, each wave applying the log before it starts. No CEO gate mid-run; the CEO reads the staging build before the swap.
4. **Novo Curso vol. 1 stays `book_supplementary`.** It is theory only and S3 mapped no lesson chapter to it. Don't re-split its chapters to promote it.
5. **The 2025/2 P1 that names Prof. Sérgio Mattos: include it.** It is a real DIR02002 exam, and the chairman asked for every reasonable exam question. Its entries are labelled with the professor's name in the bank, and the lesson pages show who set the exam. Everything else about verification applies as usual.
6. **Missing CPC articles** (Aula 16: arts. 125, 127, 385, 447 §§4–5, 459 + Marinoni §9.12; Aula 12: art. 385): pull them with `pull_source.py` from the refreshed 06/10 CPC capture and the vol. 2 chapters before those lessons are written. Never answer from memory.
7. **The 2018/2 v1/v2 variant groups are right** (e.g. `2018-2-fiadores-q7`). Where a variant's answer conflicts, settle it from the CPC text in the compendium. If the text can't settle it, show both readings with the article and mark the official key as diverging. Never guess.
8. **Housekeeping:** the stage issues were created twice. Keep #84–91 plus #93 (S6) and #95 (S7) as canonical and close the rest as duplicates. Codex left blueprints uncommitted in the shared checkout again (committed by the CEO as 36e1770): commit at every stage end.

## Second ruling, 07/10 (after the CEO's read of the staging build)
9. **Stop the line on new pages.** The 11 merged lessons (Aulas 04, 05, 10, 10-estabilização, 11, 11-mérito, 14–18) pass slop_gate and marks_lint but fail the house bar: FLIGHT-LOG F-028, F-029, F-030. No new lesson is written until the rework below has its own prototype.
10. **S5c · House pass on every rebuilt lesson.** The lesson is not rewritten. Keep its structure, facts and exercises, and bring it up to the bar:
    - load casa.css + casa.js;
    - quote the assigned reading and the treatise as doctrine `.fonte` blocks, verbatim from the compendium with page locators, at the points where the argument rests on them;
    - quote the governing CPC articles once each as `.fonte dec`, then stop restating them (F-029);
    - run one real thread through every chapter (F-030; take it from the exam bank where possible);
    - draw a second instrument where a table or prose is standing in for a figure (F-026);
    - add `.held` / `.limit` / `.term` where the text states a holding, a limit or a term (Writing Standard C10b; caps per marks_lint).
    Words may rise to the 4.5k ceiling. Checks: `house_check` PASS with no article warning, plus slop_gate, marks_lint, check_all and breakscan 1280.
    - **Prototype:** Aula 14 first, alone. The CEO will look at it on the staging server (no formal gate). Then the other ten in waves of ≤6, each applying the log.
11. **Unwritten lessons** (Aulas 01, 02, 03, 06, 06-citação, 07, 08, 08-revelia, 09, 12, 13) are written to the same bar from the start. Before writing, each blueprint gets a two-line addendum naming its source blocks (which passage, which page) and its thread. No new panel for that.
    - The open PR #120 (Aula 03) gets the house pass before it merges.
12. **Aula 09** (second REVISE after its targeted pass): proceed to writing. The writer makes closing exercises 2–4 self-contained: every choice and fact the reader needs sits in the prompt. Record that under the panel.
13. Add `house_check.py` to the S5 check list in the orchestrator's own notes and AGENTS.md, next to slop_gate and marks_lint.
