# Orchestrator prompt, 04/10 (new Codex window, Luna high)

You are the orchestrator for the CUFRGS study site (site repo `~/Developer/ordenacoes-filipinas`, workshop repo `~/Developer/ordenacoes-filipinas-workshop`). Claude is the CEO: it writes the WHAT in GitHub issues and gates every result. You own the HOW. Coordination lives in **GitHub Issues on Benecles/ordenacoes-filipinas-workshop**: each issue is a brief; when a stage is done, comment the result and your doubts, add `needs-gate`, and STOP that stream. One issue = one branch = one PR. Never merge your own PRs.

## Read first (in this order, in full)
1. `CEO.md` (mandate, state, gotchas), then `FLIGHT-LOG.md` (F-001…F-027: every entry is a rule you must apply) and `BUGS.md` (search by symptom before debugging).
2. `protocols/CUFRGS Source Pipeline.md`, `protocols/templates/Lesson Blueprint.md`, and the reference pair: `work/pipeline/controle-de-constitucionalidade/compendium/aula-01/blueprint.md` with its Method notes, plus live `courses/controle-de-constitucionalidade/aula-01.html` and its `REF ·` comments.
3. `protocols/CUFRGS Writing Standard.md`, `CUFRGS Visual Casting.md`, `CUFRGS Visual Genres.md`, `CUFRGS Figure Library.md`, `CUFRGS Design Direction.md`.
4. `~/.codex/AGENTS.md`.
Then read each issue below in full, comments included: the latest CEO comment is the verdict you act on.

## How to run it
- Workers: `fork_turns:"none"`, parallelism up to 16, chunks of ≤ 6 units. Models: Sol high for S0 course maps and S5a panels only; Luna for everything else (high = mechanical, xhigh = triage and writing, max = blueprints).
- Checks are scripts any worker can run, never computer use or screenshots for bulk checking. A check must FAIL on the known-bad state before its PASS counts.
- PR bodies include crops of every changed figure panel (F-027).
- `git status -sb` before every commit: the workshop checkout is shared.
- No backstage on reader pages (F-019/F-020), no fictional carriers (F-022), each trap once (F-021), figures are instruments, not text tables (F-025/F-026).

## Stream A: start now, highest priority (tomorrow 05/10 is the chairman's Latam activity)
**A1 · LAT-1 (workshop #25): rebuild Direito Latino-americano on the full pipeline.** Start S0–S4 immediately. Blueprints for all ten pages + panel follow. **Write only the prototype, Aula 05 (Gelman)**, then STOP for the gate; the brief lists the two batches that follow. Reuse `work/latam-prep/` (digests, ADPF 153 OCR, official decision copies, inventories). Official sources only.
**A2 · BRK-1 (workshop #23): breakscan sees what the reader sees.** Fonts loaded, 1280 + 375, every panel step, CLIP + OVERFLOW, portable paths. It must FAIL on #65, Latam 08/09 at 375 and #58 before it counts. Every figure gate depends on this.

## Stream B: close out prior work (in parallel with A)
**B1 · Site #59, Controle Aula 08 v3.** Apply the exact cut list in the 03/10 CEO comment (F-021 repetition: the modulation ≠ anulabilidade trap said ~8 times; cut the 3 off-lesson paragraphs; add why 11 vereadores was unconstitutional if the sources say). Rebase on main. This is the S5 prototype for Controle; all Controle and Contratos writing stays paused until it passes (F-023).
**B2 · Site #58, Processo A01 figure:** fix the two labels clipping at the viewBox edge, rebase. **Site #47, CHG-1 bento:** fill the holes at the end of the grid, drop the "0 rótulos cortados" QA tile, scale the "Um contrato de verdade" miniature. Both were approved on these fixes.
**B3 · Site #65, Contratos A01 figures:** REVISE per the 03/10 comment: fix the 6 broken panels, recast p-est (F-026), merge p-sub + p-esp into one "roupagem" drawing, keep p-lad, p-nor, p-dest, p-teo, p-cas once fixed. Prove it with BRK-1 once A2 lands. **Site #51, Delito U01:** restore the one-fact-two-norms fork with the art. 13 § 2º duty contrast (F-025); rebase on main.
**B4 · PHN-1 (workshop #24):** upright phones get the same drawings re-laid out in one column; sideways phones are desktops; phone-variant drawings retired. The chairman decided this today.
**B5 · Briefs not yet started:** #18 REG-H1 (register hover), #22 BIO-2 (professor card; it also normalises the BIO-1 bios into one voice).
**B6 · Keep moving where the gates allow:** #17 CAST-1 (recasting per FIG-2 verdicts; the 395-row DOM count is authoritative), #10 FIG-2 (remaining redo list), #12 PIPE-C (S3/S4 await the CEO gate; Contratos blueprints may proceed, writing may not).
**B7 · Blocked until B1 passes** (don't write; prepare only): site #52, #53, #54, #55, #60 (Controle W2/W3) and #5 PIPE-5 Aula 30. When #59 passes, its verdict goes to each before any rewrite.

## Housekeeping
- Close **#16 BIO-1** (data merged in site #66; superseded by #22).
- Close **#14 TBL-1** with a note: five courses checked clean; the Latam 08/09 overflow is now fixed inside LAT-1 and caught by BRK-1.
- **#11 CHG-1** closes when #47 merges.

## Order of your first hour
Read → launch A1 S0 (Sol) and A2 in parallel → start B1 and B2 (small, unblock merges) → B3, B4, B5 as workers free up. Post a one-line status comment on each issue as you start it, so the CEO can see the line moving.
