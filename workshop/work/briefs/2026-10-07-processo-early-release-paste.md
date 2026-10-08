CEO update, 07/10, TOP PRIORITY (ahead of the S5c house pass): the Processo exam was postponed a couple of weeks, so ship an early release of three pages straight to main. This is separate from the codex/processo-r2 swap. Pull the workshop first; read FLIGHT-LOG F-028–F-030 and rulings 9–13 in work/briefs/2026-10-07-processo-r2-decisions.md.

1. Aula 01 (Petição inicial, demanda e emenda), written fresh from its approved blueprint, to the house bar from the start:
   - add the blueprint addendum (its source blocks with pages, its thread from the exam bank);
   - checks: house_check PASS with no article warning, slop_gate PASS, marks_lint 0, check_all, breakscan 1280.
2. Revisão para a P1 (courses/processo-civil-i/revisao-p1.html), rebuilt as the exam-bank workbench for the P1 topics (weeks 1–9):
   - one block per topic, in syllabus order;
   - each block has the rule (the governing CPC articles quoted once as .fonte dec), then every P1 question from work/pipeline/processo-civil-i/exam-bank.json on that topic, then a short answer frame (how to attack this kind of question);
   - questions are verbatim with their source exam; answers are collapsed (details/summary): official key, verified answer, basis;
   - the 2025/2 exam is labelled Prof. Sérgio Mattos;
   - no exam dates anywhere;
   - house layer loaded (casa.css/casa.js); slop_gate on our prose only; check_all; breakscan 1280.
3. Course front: the staging front (codex/processo-r2 commit 2dfd6c5 and later), adapted for main:
   - every lesson that isn't live on main (Aulas 12–18, and anything not yet rebuilt or present) is shown but unlinked, marked "em breve";
   - the existing live pages for Aulas 02–11 stay linked as they are;
   - Aula 01 and the revisão link to the new pages;
   - no exam dates; check_all; breakscan 1280.
Ship each page as its own PR from a branch off main (codex/proc-early-*), using the site-edit procedure, and merge it after its checks. Then merge main into codex/processo-r2 so staging carries the three pages. Log the three merges with live URLs at the top of RUN-PROC-R2.md, then resume the S5c house pass.
