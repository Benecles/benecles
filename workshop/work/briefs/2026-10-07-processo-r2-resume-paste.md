You are the Luna orchestrator (Luna, high) for the study site Ordenações Filipinas, resuming PROC-R2: the from-scratch rebuild of Direito Processual Civil I. The previous window stopped mid-S5a (credit limit, then a bug). Don't restart anything that is done.

1. git pull ~/Developer/ordenacoes-filipinas, ~/Developer/ordenacoes-filipinas-workshop, and the staging worktree ~/Developer/ordenacoes-filipinas-proc-r2 (branch codex/processo-r2; it holds the new course front, commit 2dfd6c5).
2. Read, in order:
   - workshop RUN-PROC-R2.md (the ledger: what's done);
   - work/briefs/2026-10-07-processo-r2-decisions.md (the CEO's rulings on every open question; they replace the "Chairman questions" section, so move those into a "Resolved 07/10" section);
   - work/briefs/2026-10-06-processo-r2.md (the master brief);
   - FLIGHT-LOG.md (F-023b replaces the F-023 writing pause);
   - protocols/Source Pipeline.md, Writing Standard.md, Design Direction.md, Visual Genres.md, Visual Casting.md, site specimen/casa.html, BUGS.md, ~/.codex/AGENTS.md.
3. What's left, in order:
   a. Apply the rulings: the six second-REVISE blueprints get one targeted pass each, verified point by point; finish Aula 06/07/09/13 S5a; pull the missing CPC articles for Aulas 12 and 16; add the 2025/2 Sérgio Mattos exam to the bank, labelled; close the duplicate stage issues.
   b. S5 prototype: write Aula 14 alone on codex/processo-r2. Every check must pass:
      - slop_gate PASS;
      - marks_lint 0 findings;
      - check_all;
      - breakscan 1280 with no new findings;
      - a 1512 px crop of every figure panel, looked at.
      Log its faults in FLIGHT-LOG.
   c. S5 waves of ≤6 lessons, P2 first, then P1. One PR per lesson into codex/processo-r2. Each wave applies the flight log first.
   d. S7: the revisão as the exam-bank workbench, and cartões generated from the bank.
   e. Make every old Processo URL resolve (kept or redirected). Run check_all on the whole staging course. Then open ONE swap PR codex/processo-r2 → main and do NOT merge it: the CEO reads the staging build first.
4. You own the HOW (fork_turns "none"; Sol only for panels, Luna for the rest). Keep RUN-PROC-R2.md and agents/ current. Commit at the end of every stage; never leave files uncommitted in the shared checkout. A question for the chairman or CEO goes in plain words at the top of the ledger, then carry on with whatever doesn't depend on it.
5. When the swap PR is open, write the final summary at the top of the ledger: lessons built, words per lesson, exam questions in the bank, exclusions, the staging URL and anything you're unsure of. Then stop.
