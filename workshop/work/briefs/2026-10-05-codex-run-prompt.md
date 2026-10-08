You are the orchestrator for the study site (Ordenações Filipinas). Run the whole queue below to completion, in parallel streams, without waiting on the CEO between items.

SETUP
1. git pull both repos: ~/Developer/ordenacoes-filipinas (site; push to main = deploy) and ~/Developer/ordenacoes-filipinas-workshop (workshop). The shared site checkout is on codex/controle-a08 with a local merge commit; sort that out first (push or rebase), don't lose work.
2. Read in full: workshop CEO.md (source of truth; "Since 05/10 evening" and "Next up" supersede the RESUME HERE section of work/briefs/2026-10-04-orchestrator-prompt.md), protocols/Writing Standard.md (Part D now has a preamble plus D9 and D10; E2/E3 were rewritten for source blocks), BUGS.md, ~/.codex/AGENTS.md.
3. Replace the stale agents/Luna1.md registry entry with your own (task, owned paths, streams); keep it current; delete it when done. Create and keep RUN-0510.md in the workshop root as the run ledger (each item: status, branch, PR, checks, notes).

OPERATING RULES (chairman)
- No gates: you merge your own PRs once their checks pass. The CEO reviews what lands on the live site.
- One issue = one branch = one PR = one merge; every merge adds an ISSUES.md line (site repo).
- Desktop first: breakscan at 1280 only. No phone work until desktop is perfect (log phone findings, don't fix them).
- Site-edit procedure and gotchas: see the CEO.md Gotchas (offline_build, then git checkout -- assets/front.css specimen/register.html, then polish capture, then rm -rf tools/polish/specimen, then git add, then check_all; serve your own checkout on your own port and pass --base-url to breakscan).
- Quote only from source files on disk, never from model memory. Never reorganise ~/Documents/UFRGS 2026-2. Nothing on the Desktop.
- Workers: fork_turns "none"; parallelism up to 16; chunk big jobs to 6 units or fewer; scripts over browser driving for checks.

THE QUEUE: four streams, run concurrently
A. Text, Latam (needs B's component for source blocks; start TXT-L1 immediately):
  A1. workshop #58 TXT-L1: AP + deslop pass on the Latam front, Aula 01, Aula 02. Span-level edits only; the map work from site PR #78 must not regress.
  A2. LAT-1 (workshop #25), remaining lessons, each rebuilt by the recipe in CEO.md State, now with source blocks (E2): 08 (blueprint APPROVED; facts already verified in CEO.md), 04/07/09 (apply panel.md's REVISE points to the blueprint first), 03 (panel the blueprint first), then the revisão as the eixo workbench, then cartoes.html from one case-data file, then RETRO.md.
B. Source blocks, workshop #60 SRC-1: block component, specimen/fonte.html, noindex + robots.txt, match-check script; then the Latam pilot (feeds A2).
C. Engineering, workshop #57 SLOP-2 plus its addendum (comment on #57 and work/briefs/2026-10-05-anti-slop-addendum.md): RESOURCES.md first (read and decide on every resource; verify the papers' numbers and correct the Writing Standard preamble), then STYLE.md, the PT linter rate rules with tests, corpus discovery (work/slop-bench/), the span-level critic, and AGENTS.md wiring. Once the linter lands, every later writer in A runs through it.
D. Backlog: workshop #59 MOT-1 (interaction motion); open site PRs #69 PHN-1 (rebase, main wins on Latam; phone parts can wait under desktop-first), #68 BIO-2, #65 Contratos A01, #51 Delito U01, #55/#60 Controle A07/A09, each per its last verdict; then the Controle waves (#15/#13), PIPE-C (#12), FIG-2/CAST-1 (#10/#17), PIPE-5 (#5).

DONE / REPORT
When a stream empties, rebalance its workers to the others. When everything is done, or you are blocked on a decision only the chairman can make, write a final summary at the top of RUN-0510.md (merged PRs with live URLs, what's left, open decisions), then tell the chairman. The CEO runs the final aesthetics QA of the Latam front, Aula 01 and Aula 02 after A1 merges; post in workshop #58 when it has.
