# Study Pack Architecture

The design document for how teaching material in this corpus is structured. This governs the briefs given to Luna; the briefs handle execution, this handles architecture. Written 2026-08-28 after the first rewrite pass fixed prose quality but left the underlying structure untouched.

## The diagnosis: we inherited the wrong skeleton

Every file in every course exists because a source document existed. `06 Natureza do vício` exists because there was a slide deck about it. `Semana 3` exists because the course has fifteen weeks. The corpus is organized as a **deck inventory and a calendar**, not as a concept map.

This is the root problem, and it explains why the material still read as a fact-dump even after the prose was cleaned up: the sentences inside each box got better, but the boxes were drawn by someone else, for a different purpose.

**A slide deck is designed to be spoken over.** The professor supplies the connective tissue live: why this matters, how it relates to last week, what question it answers. The deck carries the nouns; the professor carries the model. Converting a deck 1:1 into prose preserves the nouns and silently drops the model, which is the only part that was actually teaching. That is what happened here, at scale, across three courses.

The peer notes used as the earlier benchmark are the best reference available and worth using as one, especially for formatting. They just aren't a ceiling. They're also organized as "what was said, in the order it was said," so treating them as the target caps the work at good lecture notes. Use them for what they're good at; aim past them on structure.

## What a unit is for

A unit's job is to leave the reader holding a mental model they can run — one they can apply to a case they have never seen. Not a set of retrievable facts. The test is not "can they recall the four theories of conduct," it is "given a messy fact pattern, can they tell which filter it fails and why."

Facts are the material the model is built from. They must all still be there, correct and cited. But their arrangement is determined by the model being built, not by the order the source happened to present them.

## The shape of a unit

Every teaching unit follows this arc. The section names are illustrative, not mandatory boilerplate to paste in.

1. **The problem.** What breaks without this concept? Open with the failure the concept was invented to prevent, not with a definition. The reader must know what question is on the table before receiving any answer to it.
2. **The shape of the answer.** One short paragraph, or better a diagram, giving the whole mechanism at low resolution. This is the frame every later fact gets hung on. Without it, the reader is holding parts with no slots.
3. **The components.** Each smallest part, explained on its own terms, with its role in the frame stated explicitly as it is introduced. A component introduced without naming its slot is a fact with nowhere to land.
4. **The assembly.** How the parts combine, where they interact, what happens at the seams. This is the section most commonly missing entirely, and it is the one that converts a parts list into a model.
5. **The model under load.** Worked cases, including at least one where the naive application of the model gives the wrong answer. Edge cases are where a model is actually learned; a model only ever seen succeeding is memorized, not understood.
6. **Boundaries.** What this model does not cover, what is genuinely contested, and what the next unit adds. Contested doctrine is real content and belongs here, stated once and cleanly.

## The spine: a course is one model, not fifteen

Units are not independent essays. Each course has a single organizing question, and every unit is a stop along it. The spine gets stated in the course opener and re-invoked in one sentence at the top of each unit ("we are now inside filter three").

- **Teoria do Delito.** The spine is a cascade with exit points: *did something happen → was it human conduct → does it match a type → is it nevertheless permitted → can this person be blamed → what follows.* Every week is a zoom into one stage of that cascade. Semana 1 already builds this correctly; the remaining weeks must announce their position in it rather than restarting from zero.
- **Controle de Constitucionalidade.** The spine is a pipeline: *what is the parameter → what is the object → who decides → by what route → with what effect in time and scope.* All twenty-two topics are stops on that pipeline. Currently they read as twenty-two standalone essays, which is why the same cases get fully re-explained in adjacent files.
- **Metodologia Jurídica.** Spine to be determined on reading; likely chronological-argumentative rather than procedural, which is fine, but it must be identified and stated rather than defaulting to lecture order.

Where the spine and the source's file boundaries disagree, **the spine wins.** This means file boundaries may move, and content may be redistributed across files. That is a rebuild, not an edit, and should be planned as one.

## Use the whole toolkit

Prose is one instrument among several and is currently doing work other instruments do better.

- **Diagrams are badly underused: there are currently zero in the entire corpus.** Law is highly structured and unusually diagrammable. The delito cascade is a flowchart with labeled exits. The choice of control route is a decision tree. Norm hierarchy is a layered stack. Dependency between a struck-down statute and its regulation (*arrastamento*) is a graph. Time-based distinctions (recepção vs. inconstitucionalidade originária) are timelines. Each of these is currently a paragraph doing a diagram's job badly. Prefer inline SVG or mermaid; confirm the build pipeline renders the chosen format before committing to it at scale.
- **Callouts by function, distributed throughout.** `[!INFO]` framing, `[!EXAMPLE]` worked application, `[!QUOTE]` binding text, `[!CAUTION]` contested or easily-confused, `[!NOTE]` aside. Roughly one per major section, in the body where the reader hits the relevant thing, never clustered at the top as a header ornament.
- **Tables whenever three or more items share attributes.** Comparison, classification, case chronology.
- **Anticipate the question in the text.** The reader cannot interrupt. Where a reader would predictably object or confuse two things, write that objection into the page as a callout and answer it. This is the single most effective substitute for the missing feedback loop.

## Non-negotiables carried forward

- No meta-commentary about sources, provenance, or what the pipeline could not access. If a gap affects a specific claim, it is one `[!CAUTION]` line next to that claim.
- No zero-information restatement. Every sentence must assert something the previous one did not.
- No em dashes.
- Preserve before rewrite: copy aside first, always, regardless of git status.
- Every fact, citation, article number, and case reference survives the restructuring exactly as verified. Rearranging is permitted; losing or upgrading certainty is not.

## Tooling

Installed and verified 2026-08-28.

**Diagrams are authored in mermaid, not hand-written SVG.** `mmdc` (mermaid-cli) is installed globally and configured to drive the system Chrome rather than downloading its own Chromium. Point it at a puppeteer config containing the Chrome path:

```json
{ "executablePath": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  "args": ["--no-sandbox", "--disable-gpu"] }
```

```
mmdc -p puppeteer.json -i diagram.mmd -o diagram.svg
```

The reason is error-proofing, not convenience. Hand-written SVG uses absolute coordinates (`M730 210 V255 H470`), which cannot be reviewed by reading: an arrow landing on the wrong box is invisible in the source. The first diagram produced this way asserted that *coação física irresistível* sits on the "had bodily control" branch, contradicting the table printed directly beneath it. In mermaid the same relationship is `Q -->|não| SEM`, which is readable, reviewable, and obviously wrong when it is wrong.

Author in `.mmd`, compile to static SVG at build time, embed the SVG. That output works in both the Chrome PDF path and the EPUB path with no runtime JavaScript dependency.

**Pagination engine is an open benchmark, not a commitment.** Chrome lacks running headers (`string-set` / `running()`) and cross-reference page numbers (`target-counter`); Paged.js and Vivliostyle both support them. Neither has demonstrated boring reliability on a 470-page generated document, and paged-media engines in this space still have real fragmentation and convergence bugs. Settle it with a bake-off, not in advance: take one ugly representative 40 to 60 page slice containing long tables, headings landing near page boundaries, diagrams, links and awkward callouts, render it through plain Chromium, Paged.js and Vivliostyle, and measure correctness and reproducibility rather than aesthetics.

Until then, bookmarks plus a hyperlinked table of contents are sufficient to unblock editorial work. Running heads are useful but not essential, and a hyperlinked "see §7.4" is more robust than a printed page number anyway. Do not hold the redesign hostage to pagination infrastructure.

**PDF rendering is currently Chrome headless print-to-pdf**, not ReportLab. Chrome renders inline SVG and full CSS natively, including the callout styling, with no JS requirement. Declare `background` directly on `@page` alongside the margin value or continuation pages lose their background. Chrome emits harmless `task_policy_set` noise on stderr; check for the "bytes written" line rather than treating stderr as failure.

**`tools/lint_study_packs.py`** mechanically checks what was previously caught by reading files one at a time: em dashes, broken section numbering, callout starvation and top-clustering, meta-commentary phrases, malformed tables, and diagrams that merely duplicate an adjacent table. It skips archived material and operator-facing scaffolding (blueprints, registers, handoffs) since the reader-facing rules do not apply to those.

Run it before any editorial read, so human attention goes to judgment rather than to defects a regex can find. On first run it caught four section-numbering breaks in Controle, two of which had been missed by manual reading, and confirmed the callout-clustering pattern across all twenty-two files rather than the fourteen that had actually been read.

## Visual QA: look at the pages

Reading markdown source cannot tell you what a two hundred page document feels like to flip through. Two checks, both cheap, both required before a build is called done.

**Page-level.** Render pages back to images and inspect the actual output, not the HTML that produced it. Looking for: overflow and clipping, broken page breaks, orphaned headings, diagram labels too small to read, tables that became unreadable, footnote failures, bad crops.

**Contact sheets.** `tools/contact_sheet.py` renders 30 pages at a time into a labelled grid. This catches the defect class that is invisible both in source and one page at a time: long runs of visually identical pages. Run it across the whole document, not a sample.

```
python3 tools/contact_sheet.py "<pack>.pdf" sheet.png 20 30
```

The first contact sheet run on this corpus (Controle, pages 21 to 50) showed three tables and zero diagrams across thirty pages, with unbroken runs of five and six pages of undifferentiated justified prose. The only visual landmarks were chapter openers. That is the strongest available evidence for the whole architecture change, and none of it was visible from the markdown.

**Density: an alarm, never a requirement.** An earlier draft of this document said "no run of more than three consecutive pages without a visual landmark." That is a bad rule as written, because any number handed to a bulk agent becomes a quota, and the quota is met with a decorative shaded rectangle on page four.

The rule is therefore: **if three or more consecutive pages contain only continuous exposition, flag the region for editorial inspection.** It never requires inserting anything. A reviewer decides whether the material genuinely has another representation available.

And a landmark only counts if it does at least one of these jobs:

- reduces dimensionality (twenty facts become a matrix)
- exposes structure not visible in prose (hierarchy, sequence, branching)
- externalizes a comparison
- provides retrieval or navigation (digest, case cluster, review object)
- changes the cognitive operation (from reading an explanation to testing or applying it)

A pull quote, a colored panel, an icon, or a restyled paragraph scores zero.

**The better metric: mode entropy over a rolling window.** What actually matters is not whether something is graphical but whether twelve consecutive pages are all the same cognitive mode. Tag each block by mode (exposition, rule, example, comparison, case, synthesis, retrieval) and measure variety across a window. A sequence of `exposição → regra → exemplo → comparação → caso → síntese` is strong even when half those blocks are visually modest. A window that reads `exposição → exposição → exposição` is the defect, whatever it looks like.

## Semantic components, not improvised markup

Presentation should be decided by a design system, not reinvented per page by whoever wrote that section. A case must not look different on page 147 than on page 12, because visual consistency is what lets a reader recognise an object type at a glance instead of re-reading to identify it.

Fix a small vocabulary and give each member a component with fixed styling: case, statute or provision, rule, exception, definition, doctrinal controversy, comparison, procedural sequence, timeline, hierarchy, exam note, worked example, quotation, review or summary.

The writing agent's job is to *identify* that a passage is a case, a rule with exceptions, a comparison, a chronology. The design system decides how that looks. This is mostly a CSS and convention investment, not a tooling one.

### Representation-selection rules

These convert editorial judgment into a procedure that can actually be followed. When the underlying material has one of these shapes, the default output is the named form, not prose:

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
| Cases citing cases | Network graph |
| Elements of a legal test | Checklist or decision tree |
| Statutory language | Provision block |
| Distinction that decides exam answers | Exam callout |

The editorial pass is explicitly authorised to say "this 1,200-word explanation is structurally a comparison and must not remain 1,200 words of prose." That sentence is the bridge between the presentation system and the pedagogy: a chronology rendered as a timeline is not decoration, it is the mental model made visible.

A component system alone would only produce a beautifully consistent fact dump. These rules are what stop that.

### Extraction before selection

Do not ask the writing agent "is this passage structurally a comparison?" That is exactly the judgment it is worst at, and it will answer by feel. Split it in two: the agent makes small local extraction judgments, deterministic code decides what representation is plausible.

For a candidate unit, extract into a rigid schema before any presentation decision is made: entities, relations as (subject, predicate, object) triples, ordered events, decision conditions, exceptions, attributed disagreements. Then selection is close to mechanical:

- two or more entities sharing three or more predicates → comparison candidate
- three or more events carrying temporal or ordering relations → timeline candidate
- conditions under which outcomes differ → decision tree or flowchart candidate
- a general proposition plus explicit defeaters → rule and exception structure
- the same legal question with incompatible propositions attributed to different courts or authors → controversy comparison
- ordered procedural acts with actors and state transitions → procedural flow

The thresholds are adjustable; the point is that the agent populates the schema and code proposes the representation. The renderer then consumes the extracted facts rather than regenerating them from memory.

Worked exemplars should teach the agent to populate the schema, not to imitate finished pages. Include negative exemplars, which are more useful to an obedient agent than positive ones: *these paragraphs mention A and B but do not compare them along shared dimensions, so do not build a comparison.*

## Claim provenance: one source of truth per assertion

The conduct-branch diagram that asserted *coação física irresistível* sits on the "bodily control present" branch, contradicting the table beneath it, was not a Mermaid bug and not a review failure. It was a **single source of truth** bug. Prose and diagram were written independently from the same understanding, which gave the doctrine two chances to be stated and one chance to diverge.

Prose, table and diagram are three projections of one doctrinal model, not three independent statements of it.

**Do not atomize claims into sentences.** The indivisible unit is *the smallest proposition that remains legally non-misleading when displayed on its own*. "X exclui conduta, mas só quando Y, e a doutrina minoritária discorda" must not become three claims, because the first one becomes false the moment it is separated from the second.

The unit is therefore a **scoped claim envelope**, not a triple:

```json
{ "claim_id": "C184",
  "kind": "doutrina majoritária",
  "proposition": { "subject": "coação física irresistível",
                   "relation": "exclui",
                   "object": "conduta" },
  "scope": { "when": ["a força domina integralmente o corpo"],
             "unless": [],
             "jurisdiction": "BR",
             "temporal": null },
  "authority": { "position": "majoritária",
                 "source_refs": ["Brandão p. 2", "art. 13 CP"] },
  "alternatives": [] }
```

`when` and `unless` are kept apart deliberately. "X produces Z **when** Y" and "X ordinarily produces Z **unless** Y" are different logical shapes and must not collapse into one qualifier string.

Complexity that does not fit inside one envelope goes into typed relations *between* envelopes, producing a small argument graph rather than one bloated blob: `exception_to`, `disputes`, `limits`, `distinguishes`, `generalizes`.

Two tests fix the granularity:

- **Standalone-display test.** If this claim were printed alone on a study card, would a competent reader come away with a materially false understanding? If yes, it has been fragmented too far.
- **Independent-change test.** Could this qualification or disagreement change without changing the underlying proposition? If yes, it belongs in its own envelope related back.

**Holdings carry their facts.** For `kind: holding`, `material_facts`, `issue` and `disposition` are first-class, and *the holding on these facts* is a different claim from *the general rule extracted from it*. Converting one into the other requires an explicit `generalization_basis` field, which makes an extremely dangerous compression operation visible to review. Without it, "the court held X given A, B and C" silently becomes "Rule: X."

**The projection rule, which is what makes verification work:** a projection inherits the entire claim envelope unless it explicitly narrows it. A diagram may not consume C184 as the edge `coação física → exclui → conduta` while silently discarding `scope.when`. If the diagram has no room to express the scope condition, it may not use that claim for that edge.

```json
{ "visual_id": "V27",
  "claims_used": ["C184", "C187"],
  "transformations": ["C184 rendered as edge A→B with scope shown on node A"] }
```

Verification then becomes small and answerable: does this visual entail anything its claims do not support, and does it invert, omit, strengthen, weaken or conflate any relation. Part of it stops being judgment entirely — if a claim says `X → ausência de conduta` and the diagram parses as `X → conduta presente`, that is a contradiction in a graph, not a matter of opinion.

**The `kind` field is mandatory.** Brazilian legal material mixes statutory text, binding holdings, case reasoning, majority doctrine, minority doctrine, the professor's framing, and deliberate teaching simplifications. Without a type, a perfectly verified diagram can still commit a subtler offence: faithfully rendering one author's contested position as though it were the law. This corpus already contains that failure mode, with a rhetorical criticism ("gambiarra constitucional") sitting next to actual doctrinal categories.

Permitted values: `statute`, `binding holding`, `case reasoning`, `majority doctrine`, `minority doctrine`, `professor framing`, `illustrative simplification`.

## Build order

Deliberately less grand than a full pipeline. Each stage has an observed failure behind it and a falsifiable success criterion.

**0. Artifact integrity.** Build from an explicit declared manifest, never from "every file matching a pattern in this directory." Also check ordering, duplicate and superseded content, unreferenced generated assets, expected chapters present, and build provenance. Tiny, deterministic, and it closes a known catastrophic class: a bare `return True` in the file filter put roughly 14,000 words of coverage registers, scrape provenance and abandoned first-pass output into a student's PDF. The underlying defect is that **the filesystem was accidentally functioning as editorial state**. A beautifully typeset wrong corpus is a failed artifact.

**1. Visual claim manifests.** Validate semantic single-source-of-truth on bounded, high-risk material before extending anywhere. Chosen first not because it is the largest eventual payoff but because it has the best combination of observed failure, bounded scope, falsifiable criterion, and architectural learning.

**2. Storyboard dependency QA.** Start requiring `introduces` and `requires` metadata immediately as cheap instrumentation, but do not build the linter yet. Accumulate real dependency graphs from actual units first, then design the checks against those rather than hypothetical ones.

**3. Independent mode classification.** Useful only once the new representations actually exist.

**4. Broaden the claim IR** only where demonstrated useful. Tables next, general prose only if evidence justifies the cost.

### Validating stage 1: run it as an experiment

Take 20 to 30 substantive visuals, deliberately including the ugly cases: conditional rules, exceptions to exceptions, majority and minority disagreement, case-specific holdings, branching procedures, and concepts that are easily conflated. Generate each under both architectures:

- **A:** read source, author Mermaid directly
- **B:** extract scoped claims, build manifest, project to Mermaid

Blind-review both. The metric is not "looks better." It is **unsupported, inverted or materially incomplete legal relationships per edge and node**. There is already a baseline of at least one serious error under architecture A.

If B sharply reduces substantive errors without making extraction prohibitively expensive, that validates not just manifests but the central claim that representation should be downstream of a shared semantic model. Equally important, it shows where the schema breaks before it reaches 974 pages.

**Do not finish the ontology on paper first.** Hand it the thirty nastiest propositions available — cumulative and alternative requirements, necessary versus sufficient conditions, rebuttable presumptions, exceptions to exceptions, court-specific rules, doctrine that changed over time, holdings dependent on material facts, professor simplification against textbook qualification — and let the schema evolve. If it survives, freeze v1. If it degenerates into a 400-word prose `qualifier`, the design has been falsified cheaply, which is the point.

### Mode entropy: separate intent from observation

Never let the writing agent's declared mode be the measured one. It may tag `intended_mode` if that helps generation, but entropy operates on a separately inferred `observed_mode`, produced by a classifier that does not see the claimed label. Otherwise the metric is gamed the same way a page-count rule is: prose dropped inside an `example` wrapper still reads as exposition, and an independent classifier should say so.

Several modes have cheap structural signatures: a comparison needs two or more entities across two or more shared dimensions; a timeline needs three or more ordered events; a case needs court plus facts, issue and disposition; a checklist needs independently evaluable conditions. Others, like distinguishing an example from exposition containing an anecdote, are irreducibly semantic. Use structure to nominate a candidate, then a classifier to confirm with a confidence score.

Treat entropy as a corpus diagnostic, never a build gate. Nobody knows the pedagogically correct value, and a brilliant six-page derivation may legitimately be six pages of exposition. What is actionable is the outlier: *this eighteen-page unit is 94% exposition where comparable units run 55 to 70%.* That is worth a look. It is not proof of a defect.

## Unit storyboards: the missing middle scale

Contact sheets catch thirty identical pages. Page inspection catches clipping and bad breaks. Neither catches a single unit with the right components in the wrong order.

Before writing, each teaching unit produces a short sequence plan. Pedagogy, not layout, and each step declares what it introduces and what it depends on:

```yaml
unit: Erro de tipo
steps:
  - step: enquadramento do problema
    introduces: [erro sobre elemento do tipo]
    requires: []
  - step: regra central
    introduces: [art. 20 CP]
    requires: [erro sobre elemento do tipo]
  - step: exemplo mínimo
    requires: [art. 20 CP]
  - step: distinção ramificada
    introduces: [erro essencial, erro acidental, evitável, inevitável]
    requires: [art. 20 CP]
  - step: consequências por ramo
    requires: [erro essencial, erro acidental]
  - step: contraste com erro de proibição
    requires: [erro essencial, consciência da ilicitude]
  - step: objeto de recuperação
    requires: []
```

The `introduces` and `requires` fields make the storyboard a concept dependency graph, which makes these checks mechanical rather than editorial:

- does a distinction appear before its terms are introduced?
- does an example precede the rule it instantiates?
- does a complication or dissent appear before the baseline doctrine?
- are five concepts introduced before any is resolved?
- does the synthesis reference concepts never developed?
- is any prerequisite introduced later than something that requires it?
- is there a terminal retrieval or synthesis object?

Review the storyboard alongside abbreviated content and thumbnails of the resulting pages, so semantic order and physical presentation are visible together.

## Three QA resolutions

| Scale | Instrument | Catches |
|---|---|---|
| Document | 30-page contact sheet | Visual and editorial rhythm; long runs of sameness |
| Unit | Storyboard plus page thumbnails | Pedagogical sequence; dependency order |
| Page | Single-page render | Clipping, breaks, orphans, unreadable tables, tiny labels |

## Division of labor (revised 2026-08-30)

Superseded version preserved at `Superseded/claude-division-of-labor-update-2026-08-30/`.

**Luna now owns architecture, drafting, and its own subagent orchestration, end to end, per course or unit.** Where a spine or unit blueprint does not yet exist (the rest of Metodologia, Controle 04-22), Luna derives it from this document and the source corpus rather than waiting for Claude to write a per-unit brief. Luna may dispatch its own subagents to parallelize drafting. This is a deliberate speed-over-upfront-precision tradeoff: the previous mode (Claude hand-writes a detailed brief per unit before any drafting starts) produced high-fidelity output but did not scale past two units at a time.

Claude's role shifts from pre-hoc brief-writing to **post-hoc audit and promotion**: verifying drafted content against source, running the mechanical build/verify gate, catching the recurring defect classes this project has already hit once (see the journal's decision log, D001-D015), and promoting a batch from staging into the live manifest only after it clears that gate. Claude does not draft course content directly except as a surgical fix to a specific defect found during audit (as with the Controle CC-01/03 provenance-leak correction and the Teoria diagram fixes).

**The operational contract that makes "draft fast, fix after" survivable rather than chaotic:**

- Luna works in `Operator/<course>/<batch-name>/` staging directories. It never edits a live `luna_output/` file directly. A bad batch therefore cannot corrupt a shipped pack before review.
- Every subagent Luna dispatches, whether for a single unit or a whole course pass, is scoped through `tools/job_scope.py`: declared writable globs, required outputs, snapshot before, verify after. This is the hard control that bounds the blast radius of "whatever it does" — content quality is Luna's judgment call, file scope is not negotiable.
- Every unit gets the frontmatter scaffold already validated in Metodologia A03-A08/A04-01-07: `section_id`, `introduces`, `requires`, `source_refs` (file + specific page range), `authorities`, `claims_to_verify` (the specific dates, quotes, numbers, and attributions a reviewer should check against source). This is what turns a content audit from "read the whole thing and hope" into "check these twelve specific claims."
- See `Study Pack Luna Autonomous Brief.md` for the full operating brief handed to Luna under this mode, including the condensed pitfall list and the non-negotiable rules that survive the new looser posture regardless.

## Process

Still a loop, not a pipeline, but the loop's shape changed. The old cycle put Claude in the middle of every round trip (write brief → Luna executes → Claude reviews → next brief). The new cycle: **Luna architects and drafts a batch in staging, using its own subagents where useful → Claude audits against source and the mechanical gate → Claude either promotes, sends specific fixes back, or fixes small defects directly → repeat.** Claude is no longer upstream of drafting; it is downstream of it.

Each staged batch should still be small enough to actually audit. The frontmatter `claims_to_verify` field is what keeps "small enough to audit" from becoming a bottleneck as batch size grows — a reviewer checks the flagged claims against source rather than re-deriving what to check.
