# Luna Autonomous Brief: Architect, Build, Deploy

Written 2026-08-30. This replaces the old mode where Claude hand-wrote a detailed brief for every unit before you touched it. Read this whole document before starting anything. It is long because it is meant to let you work without a per-unit brief from Claude — everything you'd normally ask for is in here or pointed to from here.

## What changed and why

Old mode: Claude decided the spine, the unit boundaries, the diagram plan, wrote a brief, you executed it faithfully, Claude reviewed. This produced high-fidelity output but scaled to about two units of new architecture at a time before it became the bottleneck.

New mode: **you now own architecture, drafting, and orchestrating your own subagents, end to end, per course or per batch.** Where no spine or unit blueprint exists yet, you derive one from this brief and the source corpus. Where one exists, you extend it. You dispatch your own subagents to parallelize drafting when that's faster than drafting serially yourself. Claude's job moves downstream: audit what you staged against source, run the mechanical build/verify gate, promote what passes, fix or bounce back what doesn't.

This is a real speed-for-precision tradeoff, made deliberately. The expectation is not that every batch you produce is perfect. The expectation is that it's checkable fast and bounded in blast radius, so fixing it is cheaper than the old mode's upfront precision was. Sections below tell you exactly what "checkable fast and bounded" requires from you mechanically — that part is not optional even though the content-quality bar is now more forgiving.

## What "we'll just fix it" actually covers, and what it doesn't

This distinction matters more than anything else in this document. Read it twice.

**Cheap to fix after the fact, so don't over-invest upfront:** prose quality and rhythm, whether a given passage is the ideal representation choice (table vs. diagram vs. prose) versus merely an acceptable one, missing visual landmarks, uneven callout distribution, structural rough edges, a unit boundary that turns out slightly wrong. Draft these fast. Claude will catch and fix the ones that matter during audit, and it's genuinely cheaper for Claude to fix twenty of these than for you to deliberate over each one before writing it.

**Not cheap to fix after the fact — hold a hard line on these regardless of how loose the new mode feels:**

- **Factual and citation errors.** A wrong date, a misattributed quote, a paraphrase that drifts from what the source actually says. Fixing this after the fact means re-verifying the whole unit against source from scratch, which costs as much as verifying it once at draft time. Verify as you draft, not "someone will check later."
- **File-scope violations.** Touching a file outside your declared scope, especially a live `luna_output/` file. This is exactly the failure class `job_scope.py` exists to make structurally impossible, not just discouraged. See below — this is non-negotiable, not a judgment call.
- **Format defects invisible until render.** The single most expensive mistake made twice already in this exact project (see D014/D015 below): using raw ` ```mermaid ` fenced code blocks instead of the `{{mermaid:diagrams/name.mmd}}` directive. Both are valid markdown. Both pass every lint check. The builder only compiles the second form. The first form ships as literal source text on the page and nobody notices until someone renders the actual PDF. This has cost real rework twice. Check for it yourself before handing off a batch — see the Tooling section.
- **Missing preservation of prior work.** Overwriting an existing file without a preservation copy first. See below — also non-negotiable.
- **Provenance leaks and meta-commentary.** Writing "the deck says," "on page 14," "the source material," anything that exposes the pipeline to the reader instead of just teaching the content. This has already shipped once (Controle CC-01/03) and required a full rewrite pass to remove. Don't write it in the first place; it's no cheaper to catch after than to avoid.

The pattern across all five: these are defects where the cost of fixing scales with how much content was built on top of the mistake before someone caught it, or where the defect is invisible to every automated check except the one specific thing that catches it. Everything else genuinely is cheaper to fix after than to perfect upfront. Spend your effort accordingly.

## The operational contract

1. **Work in staging, never live.** Every batch goes in `Coursework/<course>/luna_output/Operator/<descriptive-batch-name>/`. Never write directly to a file in `luna_output/` itself — that's the live, shipped location, and Claude promotes into it only after audit. This means a bad batch literally cannot corrupt a shipped pack, no matter how bad.

2. **Every subagent dispatch, including your own, goes through `tools/job_scope.py`.** If you're spawning subagents to parallelize a batch, each one gets a job-scope config: declared writable glob patterns, required outputs, `required_changes` if you need to guarantee an existing file was actually touched and not silently skipped. Snapshot before, verify after. This is the one piece of process overhead that is not optional, because it's the actual mechanism that makes "draft fast, audit after" survivable instead of chaotic — it bounds blast radius mechanically instead of relying on anyone's care. Look at `tools/jobs/*.json` for examples already used this project (`claude-metodologia-a03-tail.json` is a clean reference).

3. **Every unit gets the frontmatter scaffold**, in the YAML block at the top of the file:
   ```yaml
   section_id: A0X-0Y          # or whatever ID scheme fits the batch
   introduces: [...]            # concepts this unit newly introduces
   requires: [...]               # section_ids this unit depends on
   source_refs:
     - file: <exact path to the source PDF>
       pages: PDF pp. N-M; páginas impressas X-Y
   authorities: [...]            # every author/case/document cited
   claims_to_verify:
     - <specific date, quote, number, or attribution a reviewer should check against source>
   ```
   `claims_to_verify` is the single highest-leverage field in this whole scaffold. It's what let Claude audit two full batches of 5-8 units each against a badly OCR-corrupted source in a session, by checking flagged claims instead of re-deriving what to check. Populate it honestly — list the things that would actually be wrong if you got them wrong, not a token list to satisfy the schema.

4. **Preserve before rewrite, always, no exceptions.** Before touching any existing file, copy it to a dated `Superseded/` folder next to it first. This applies even with no git tracking, even for a file you're about to improve, even under time pressure. If you're not sure whether something counts as "existing," preserve it.

5. **Run the build/verify gate before calling anything done.** In order:
   - `.venv-luna/bin/python3 tools/lint_study_packs.py "Coursework/<course>/luna_output"` — must show 0 errors. Warnings are review prompts, not blockers, and the "inspection alarm" warning specifically must never be resolved by adding decorative callouts to hit a quota — that's explicitly the wrong response to it.
   - `.venv-luna/bin/python3 tools/rebuild_study_packs.py <teoria|metodologia|controle>` — must complete without error.
   - `.venv-luna/bin/python3 tools/verify_study_packs.py` — checks manifest consistency, PDF page/chapter counts, EPUBCheck (must be 0 errors/0 warnings), and forbidden `foreignObject` (must be 0).
   - Before any of the above, if the batch has diagrams: `grep -c '```mermaid' *.md` on every file in the batch must return 0. If it doesn't, extract the fenced block into a `diagrams/<name>.mmd` file and replace it with `{{mermaid:diagrams/<name>.mmd}}`. Then confirm it compiles: `npx mmdc -i diagrams/<name>.mmd -o /tmp/check.svg -c tools/mermaid-config.json -p tools/mermaid-puppeteer.json` and grep the output for `foreignObject` (must be absent).
   
   A batch that fails any of these is not "basically done, Claude will polish it." It's not done. This gate is cheap to run and catches a large fraction of what would otherwise become Claude's audit burden — running it yourself before handoff is strictly faster for both of you than skipping it.

## Pedagogical doctrine, condensed

Full version in `Study Pack Architecture.md` — read it once if you haven't, it's not long. The load-bearing points:

**What a unit is for.** The reader should come away with a mental model they can run on a case they've never seen, not a set of retrievable facts. Test: not "can they recall the four theories," but "given a messy fact pattern, can they say which filter it fails and why."

**The six-part unit arc** (names illustrative, not literal headers to paste in):
1. The problem — what breaks without this concept, open with the failure it prevents
2. The shape of the answer — one paragraph or a diagram giving the whole mechanism at low resolution, before any component detail
3. The components — each part explained with its role in the frame stated explicitly
4. The assembly — how parts combine, what happens at the seams (most commonly missing entirely; the section that turns a parts list into a model)
5. The model under load — worked cases, including at least one where naive application gives the wrong answer
6. Boundaries — what this doesn't cover, what's contested, what the next unit adds

**The spine.** A course is one organizing question, not fifteen independent essays. State it once at the course level, re-invoke it in one sentence per unit ("we are now inside filter three"). Established spines:
- Teoria do Delito: cascade with exit points (did something happen → human conduct → matches a type → nevertheless permitted → can this person be blamed → what follows)
- Controle de Constitucionalidade: pipeline (parameter → object and defect → decision-maker → route/moment → technique/effect)
- Metodologia Jurídica, Aulas 03-04 (done): plural sources → common science → situated case reasoning → institutional practice. **Aulas 01-02 and 05-15 have no confirmed spine yet — derive one from the source corpus before drafting, using the same audit process D007 used for the other three courses (read the audit, propose a spine, state it once, don't default to lecture order).**

**Representation-selection rules** — when material has one of these shapes, this is the default output, not prose:

| Material | Default representation |
|---|---|
| Chronology | Timeline |
| Procedure or process | Flowchart |
| Rule plus its exceptions | Branching diagram |
| Competing doctrines | Side-by-side comparison |
| Several similar concepts | Matrix |
| Institutional competence | Hierarchy or matrix |
| Procedural history of a case | Procedural track |
| Many cases on one point | Digest table |
| Elements of a legal test | Checklist or decision tree |
| Statutory language | Provision block |
| Distinction that decides exam answers | Exam callout |

You are explicitly authorized to say "this 1,200-word passage is structurally a comparison and must not remain prose."

**Density is an alarm, never a quota.** If three or more consecutive pages are pure exposition, that's worth a look — it never means insert something decorative to break it up. A landmark only counts if it reduces dimensionality, exposes structure, externalizes a comparison, aids retrieval, or changes the cognitive operation (reading vs. testing). A colored panel or restyled paragraph scores zero.

## Non-negotiables (unconditional, regardless of how loose this mode feels)

- No em dashes, anywhere, ever.
- No meta-commentary about sources or the pipeline ("the deck says," "on page X," "the material"). Teach the content directly. If a genuine gap exists, one `[!CAUTION]` line next to the specific affected claim, nothing more.
- No zero-information restatement. Every sentence asserts something the previous one didn't.
- Every fact, citation, article number, case reference, date, and quote must be checkable against an actual source and correct as verified. Rearranging is fine; losing or upgrading certainty is not.
- Diagrams inherit the full scope of whatever claim they render. If a claim has a `when`/`unless` condition and the diagram has no room to express it, that diagram cannot use the claim for that edge — find room or don't use it.

## Known pitfalls — do not re-discover these

Condensed from `Study Pack Development Journal - Sol.md`. Full detail there if you want the "why," including the specific evidence for each.

- **D004 / job-scope:** output existence isn't the same as required work happening. If you need to guarantee an existing file was actually edited (not silently skipped), use `required_changes` glob patterns in the job-scope config, not just `required_outputs`.
- **D005 / density:** never respond to a lint density warning by adding a decorative callout. The warning means "look," not "insert."
- **D006 / D009:** container-level or syntax-level validity does not mean the build pipeline handles it correctly. `unzip -t` passing doesn't mean the EPUB is valid; markdown parsing without error doesn't mean mermaid compiled to native SVG. Always check the actual rendered artifact, not just that a tool exited zero.
- **D010:** use canonical filesystem spelling for scope paths (`Operator`, not `operator`) — the local volume is case-insensitive so a typo silently resolves to the right file while still breaking scope-tracking logic that compares path strings.
- **D012:** whoever prepares a blind review package cannot also be the blind reviewer, even if they're confident they can ignore what they already saw. This only matters if you're running the claim-manifest experiment (see Current State below); for normal drafting it doesn't apply.
- **D013:** a transcript or self-report describing work as done is a claim to verify against actual disk state, not a report to trust. This cuts both ways now — Claude will verify your batches against disk rather than your batch report, and you should hold your own subagents to the same standard rather than trusting their self-reports about what they wrote.
- **D014 / D015 — the big one, worth repeating a third time because it's cost real rework twice already:** mermaid diagrams must use the `{{mermaid:diagrams/name.mmd}}` directive with a separate `.mmd` file, never a raw ` ```mermaid ` fenced block. Both look identical in a markdown preview and both pass lint. Only rendering the actual PDF page reveals the fence-form as literal broken text. Check every batch with `grep -c '```mermaid'` before handoff — it must be 0 everywhere.

## Tooling reference

- `tools/job_scope.py` — mandatory scoping for every dispatch. `verify` mode checks a run against its declared config.
- `tools/lint_study_packs.py <path>` — mechanical checks: em dashes, section-numbering continuity, callout density alarm, meta-commentary phrases, malformed tables, diagram/table redundancy. Run before any human or Claude review.
- `tools/rebuild_study_packs.py <teoria|metodologia|controle>` — builds PDF (Chrome headless print-to-pdf) and EPUB from the course's `build_manifest.toml`. Manifests are explicit ordered file lists, not directory globs — a file not in the manifest never ships, and manifest order is reading order regardless of filename.
- `tools/verify_study_packs.py` — the consolidated release gate: manifest consistency, lint, PDF page/chapter count, EPUBCheck, foreignObject detection. Run this last, always.
- `tools/contact_sheet.py <pdf> <out.png> <start-page> <count>` — renders a page range into a labeled thumbnail grid. Use it to sanity-check document-level rhythm on anything you're not sure about; requires `.venv-luna/bin/python3` specifically (has pymupdf/Pillow).
- Mermaid: `npx mmdc -i diagram.mmd -o diagram.svg -c tools/mermaid-config.json -p tools/mermaid-puppeteer.json`. The config forces `htmlLabels: false` at root — this is required, a flowchart-level-only setting is insufficient in current mermaid-cli and silently re-enables `foreignObject`, which then fails EPUBCheck.

## Current project state (as of 2026-08-30)

- **Teoria do Delito:** 22 chapters, fully architecture-rebuilt, diagrams converted to mermaid. Live and passing. Not a current priority target for new drafting.
- **Controle de Constitucionalidade:** only topics 01-03 have received the architecture rebuild (five-question spine, diagrams, recuperação exercises). Topics 04-22 are still the old deck-inventory prose. **This is the largest remaining body of work and the natural first target for this new autonomous mode** — the spine is already defined (D007: parâmetro → objeto e defeito → ator → rota/momento → técnica e efeito), so this is extension of an established pattern, not spine derivation from scratch.
- **Metodologia Jurídica:** Aulas 03-04 fully rebuilt as of 2026-08-29 (15 unit files, live). Aulas 01-02 and 05-15 are still old prose-pass content with no confirmed spine. Deriving that spine is real architectural work, not extension — budget for it accordingly.
- **Claim-manifest experiment (Teoria):** Phase 1 pilot was invalidated (Condition B's claims were extracted from Condition A's finished diagram instead of independently from source, so both conditions inherited the same errors). A corrected re-run needs Condition B's writer walled off from ever seeing Condition A's output. Low priority — only pursue this if asked specifically, since a 3-pair pilot isn't worth much on its own and the two real diagram defects it did surface have already been fixed directly.

Recommended order, but use judgment: Controle 04-22 first (established spine, highest volume, clearest ROI), Metodologia's remaining spine second (needs real architectural derivation first), claim-manifest re-run only if specifically requested.

## What to hand back to Claude

When a batch is staged and passes your own build/verify gate: leave it in its `Operator/` directory, don't attempt to promote it into live `luna_output/` yourself. State plainly what you drafted, what the job-scope verify said, and flag anything you're genuinely unsure about (a blueprint/source mismatch you resolved by judgment call, a claim you couldn't fully verify, anything unusual). Claude audits from there — checking `claims_to_verify` against actual source, confirming the mermaid-directive check, running the full gate again independently, and promoting or bouncing back with specific fixes.
