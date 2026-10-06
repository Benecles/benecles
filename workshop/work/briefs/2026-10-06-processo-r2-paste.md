You are the Luna orchestrator (Luna, high) for the study site Ordenações Filipinas. Your job: rebuild the course Direito Processual Civil I from scratch, end to end, as the house's first reference course.

1. git pull ~/Developer/ordenacoes-filipinas (site; push to main = deploy) and ~/Developer/ordenacoes-filipinas-workshop (workshop).
2. Read, in full: workshop work/briefs/2026-10-06-processo-r2.md (the master brief: what to build, the inputs, the stages, the exam bank, staging, done-when), then protocols/Source Pipeline.md, protocols/Writing Standard.md, protocols/Design Direction.md, protocols/Visual Genres.md, protocols/Visual Casting.md, site specimen/casa.html, BUGS.md, ~/.codex/AGENTS.md, and CEO.md's newest section.
3. You own the HOW: split the stages into worker tasks (fork_turns "none"; Sol only for S0 and the S5a panel, Luna for everything else per the Pipeline's model table), run them in parallel where the stages allow, and check every output before the next stage uses it.
4. Coordination: one GitHub issue per stage on the workshop (labels codex, pipeline, course:processo-civil-i; the umbrella issue is PROC-R2), ledger RUN-PROC-R2.md in the workshop root, a registry file in agents/. Questions for the chairman go in plain words at the top of the ledger.
5. Land through the staging branch codex/processo-r2. The final swap PR to main waits for the CEO to read the staging build. Everything else you merge yourself after your checks.
Start with S0 and S1 together; P2 lessons are first in S5.
