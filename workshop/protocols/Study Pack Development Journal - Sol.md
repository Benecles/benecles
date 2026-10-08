# Study Pack Development Journal

Started 2026-08-29. This is the durable record of the iterative rebuild of the three 2026/2 study packs. It records what was tried, what the artifacts showed, what failed, and which lessons should become reusable process rather than remain local fixes.

## Operating model

Sol owns architecture, experimental design, integration, and final review. Luna agents may execute bounded corpus-scale reads or rewrites, but may not delegate further. Every substantial pass follows this loop:

1. State a falsifiable problem and establish a baseline.
2. Declare exact scope, writable paths, required outputs, and preservation requirements.
3. Preserve every file that may be changed.
4. Prototype on a small but representative slice.
5. Verify content against its source and report input and output word counts.
6. Build only from the declared manifest.
7. Run mechanical lint, unit-level pedagogical review, page renders, and document-level contact sheets.
8. Record the result, including failed hypotheses and follow-up changes to the method.
9. Scale only after the prototype survives review.

The governing architectural doctrine remains `Study Pack Architecture.md`. The existing `Reconstruction Pipeline Protocol.md` governs high-fidelity source reconstruction. This journal records empirical refinements to both.

## Baseline: 2026-08-29

### Declared artifacts

| Course | Manifest files | Selected words | PDF pages | Lint errors | Lint warnings |
|---|---:|---:|---:|---:|---:|
| Teoria do Delito | 22 | 140,400 | 458 | 0 | 24 |
| Controle de Constitucionalidade | 22 | 88,910 | 262 | 4 | 90 |
| Metodologia Juridica | 16 | 103,919 | 214 | 0 | 21 |
| **Total** | **60** | **333,229** | **934** | **4** | **135** |

All manifest entries exist. The builder's declared manifests, rather than directory contents, are the reader-facing source of truth.

### Known defects and hypotheses

1. **Teoria do Delito:** the prose architecture has been rebuilt, but three Semana 1 diagrams remain hand-authored SVG with known collision and maintainability defects. The other nineteen units have no diagrams. Hypothesis: converting the existing visuals to readable Mermaid source creates a stable semantic baseline before the claim-manifest experiment.
2. **Controle de Constitucionalidade:** the corpus remains organized as a deck inventory. Hypothesis: a course pipeline built around parameter, object, decision-maker, route, and effects will reduce repetition and give each topic a defined role.
3. **Metodologia Juridica:** no defensible course spine has yet been established. Hypothesis must be inferred from the full corpus before any rewrite begins.
4. **Lint semantics:** the current callout-starvation warning appears on almost every long teaching file. It is useful as an alarm, but not as a requirement to add callouts. Any future metric should measure cognitive mode and structural function, not decorated block count.
5. **Claim provenance:** scoped claim envelopes may prevent diagrams from dropping qualifications or strengthening contested doctrine. This remains an experiment, not an accepted production requirement.

### Parallel audit pass

Three read-only Luna audits were dispatched, one per course. Each agent was explicitly prohibited from delegating. Their remit is evidence gathering and bounded prototype design, not editing. Sol will compare the reports, choose the first implementation pass, and record the decision here.

## Decision log

### D001: Audit before rewriting

The project will not begin with three simultaneous corpus rewrites. The first pass is read-only and course-specific. This preserves the ability to compare architectures and prevents the same untested solution from propagating across all 934 pages.

### D002: One changed variable in the first Teoria experiment

Mermaid conversion and claim manifests solve different problems. The existing Semana 1 diagrams will first be converted from coordinate-based SVG authoring to Mermaid while preserving their semantics. Claim manifests will then be tested against that stable baseline. This avoids attributing improvements to two interventions at once.

### D003: Rendered baseline confirms different defect classes

Nine 30-page contact sheets were rendered, using opening, middle, and closing windows from every PDF.

- **Teoria do Delito:** pages 1 to 30 contain three diagrams, several tables, worked examples, and functional callouts. The middle and closing windows retain useful tables and retrieval objects but contain no comparable diagrams. The architecture pass improved cognitive variety, yet the improvement is concentrated near the opening unit.
- **Controle de Constitucionalidade:** all three windows include occasional comparison or case tables, but most pages remain serial exposition. Chapter openers and top-clustered callouts provide visual interruption without consistently externalizing the course pipeline.
- **Metodologia Juridica:** the middle and closing windows are dominated by continuous exposition, with tables appearing only sporadically. The opening Course Reader adds navigation but not a teaching model. This is the strongest current candidate for a course-level structural intervention once its spine is established.

This inspection changes priority in one respect: diagram conversion remains the safest first implementation pass, but Metodologia may yield the largest pedagogical gain per rebuilt unit. The audit reports will determine which course receives the first substantive rewrite.

### D004: Required output is not the same as required work

The original `tools/job_scope.py` could require an output path to exist, but it could not require a pre-existing file to change. A skipped edit therefore passed whenever the named file already existed. The tool now accepts `required_changes` glob patterns and rejects a run unless each pattern matches a created, modified, or deleted path. Existing job files remain compatible because the field defaults to an empty list.

Reusable lesson: output existence prevents omission only for net-new artifacts. Any workflow that edits established files needs an explicit change requirement or a stronger content invariant.

### D005: Density diagnostics must describe review, not quotas

The linter's former `callout starvation` message said the architecture wanted roughly one callout per major section. Although technically a warning, that wording encouraged mechanical box insertion. The check now identifies an `inspection alarm` and states that decorative callouts do not resolve it. The signal remains useful for locating unusually uniform files while editorial judgment determines whether a definition, example, quotation, or contested claim actually deserves a callout.

### D006: Artifact validation must precede editorial scaling

Installing EPUBCheck exposed three errors in the Teoria EPUB that ZIP integrity could not detect: the XHTML item did not declare its SVG property and the first chapter contained duplicate SVG IDs. The Controle audit also showed that consecutive source callouts were being merged into one rendered box, while every chapter title was emitted twice because both the builder and the Markdown supplied an H1.

The builder now:

- stops a callout body when the next callout marker begins;
- namespaces every inline SVG ID and its fragment references per diagram;
- declares the EPUB `svg` property for chapters containing inline SVG;
- avoids adding a duplicate chapter H1 when the rendered Markdown already begins with one.

All current artifacts were preserved before rebuilding. The rebuilt EPUBs pass EPUBCheck 5.3.0 with zero errors and warnings and contain exactly the manifest-declared chapter counts: 22 for Teoria, 22 for Controle, and 16 for Metodologia. Rendered page inspection confirms that consecutive Controle callouts now appear as distinct boxes and existing Teoria diagrams still render. Duplicate-heading removal reduced the PDFs from 458/262/214 pages to 456/260/213 without changing teaching content.

Reusable lesson: `unzip -t` is a container check, not an ebook check. EPUB conformance and rendered HTML semantics belong in every build verification pass.

### D007: Course spines and prototype order after full audits

The three read-only course audits support distinct architectures rather than one template applied three times.

- **Teoria do Delito:** retain the existing cascade with exit points. The first implementation changes only authoring format for the three Semana 1 diagrams, allowing the later claim-manifest experiment to measure one additional variable.
- **Controle de Constitucionalidade:** use five recurring questions rather than five sealed blocks: parameter, challenged object and diagnosed defect, decision-maker, route or moment, and technique/effect. Temporal reasoning must be split between parameter selection in reception cases and route timing in preventive/repressive control.
- **Metodologia Juridica:** organize the course around the conversion of plural, situated legal materials into usable normative knowledge and then into systems, institutions, national law, and dogmatic concepts. The proposed progression is plural sources → common science → situated case reasoning → institutional practice → normative mediation → local custom → systematic ordering → national institutions → dogmatic concepts.

Prototype order:

1. Teoria Semana 1 Mermaid conversion, because it is bounded and isolates authoring format.
2. Metodologia Aulas 03 and 04, because they form the hinge between casuistic method and colonial institutional application and currently show a combined source/output coverage ratio near 0.44.
3. Controle topics 01 to 03, because they test the transition from parameter/object to institutional actor before the large procedural units.

Controle's four numbering errors are being repaired in a separate mechanical pass before substantive rewriting. This keeps later lint comparisons attributable to the architecture pass.

### D008: Representation-aware lint must survive format migration

The diagram/table redundancy check searched only for closing inline SVG tags and used a non-multiline table regex. It therefore missed the known Semana 1 adjacency and would have become fully blind after migration to Mermaid directives. The check now recognizes both inline SVG and `{{mermaid:...}}` directives and correctly locates following Markdown tables across lines. It remains an advisory review signal because a table may legitimately provide an accessible textual projection of a richer diagram.

### D009: A diagram renderer needs ebook-native output and a legibility gate

The first Mermaid build rendered correctly in Chrome but failed EPUBCheck with 46 XHTML errors. Mermaid's default HTML labels had inserted 92 `foreignObject` elements and HTML paragraphs into inline SVG. Switching only `flowchart.htmlLabels` off was insufficient in Mermaid CLI 11.16.0 because the root-level setting takes precedence. The production config now sets root `htmlLabels: false`, the builder passes that config explicitly, and the build fails if any compiled SVG still contains `foreignObject`.

Native SVG text exposed a second defect that the HTML renderer had hidden: `<small>` tags in diagram labels became literal words. The three sources now use native line breaks without HTML styling. EPUBCheck then passed, but page inspection showed the horizontal cascade was too wide to study. Reorienting it vertically made the labels readable. Visual QA also found an orphaned participation-review component, which was connected back to the typicity/imputation question.

Reusable lesson: diagram acceptance has four separate gates: semantic edge review, native-output conformance, rendered legibility at final page size, and connectivity review. Passing syntax or EPUB validation alone is not enough.

### D010: Scope paths must use canonical filesystem spelling

The first Metodologia calibration job declared a lowercase `operator` target while also ignoring the existing uppercase `Operator` tree. On the case-insensitive local volume, the path resolved to the intended file, but the ignore rule removed it from the snapshot and produced a false undershoot. Future jobs use the canonical `Operator` spelling and never ignore a tree that contains the writable target. The calibration job definition was corrected, and the first multi-file drafting job watches the course while permitting only explicit staged outputs.

### D011: Prototype acceptance needs ordered gates, not one aggregate score

`Study Pack Prototype Acceptance Rubric.md` now separates hard failures from editorial diagnostics. Scope, preservation, source fidelity, manifest integrity, EPUB conformance, and rendered clipping are gates. Dependency order, transfer quality, representation choice, and document rhythm are judgment records. Callout counts, page runs, word counts, and mode entropy remain observations rather than pass thresholds.

`tools/verify_study_packs.py` consolidates the release-critical mechanical checks without mutating artifacts: manifest count, reader-facing lint, PDF metadata, EPUB chapter count, EPUBCheck, and forbidden `foreignObject` detection. Its first full run passed all three current packs: Teoria 22 chapters/457 pages, Controle 22/260, and Metodologia 16/213, with zero lint errors and zero EPUB errors or warnings.

## Iteration records

### Mechanical pass C0: Controle numbering baseline

Scope: four files with known H2 numbering breaks. Every original was preserved byte-for-byte under `luna_output/Superseded/sol-numbering-fix-2026-08-29/`.

Changes:

- `02 Pressupostos.md`: section 8 became 7.
- `13 Estado de coisas inconstitucional.md`: section 13 became 12.
- `19 Ações constitucionais diretas e mecanismos processuais.md`: section 14 became 13.
- `20 Controle nos tribunais, ADI estadual, repercussão geral e súmula vinculante.md`: sections 11 and 12 became 9 and 10.

All four word counts remained identical. The job-scope validator accepted exactly four modified teaching files and four created preservation copies. Whole-course lint moved from 4 errors and 90 warnings to 0 errors and 90 warnings. The pre-build PDF and EPUB were then preserved under `Study Packs/Superseded/sol-pre-controle-numbering-build-2026-08-29/`. Rebuilt artifacts contain 22 chapters, the PDF remains 260 A4 pages, and EPUBCheck reports 0 errors and 0 warnings.

Status: accepted. This is a baseline repair, not a pedagogical iteration.

### Pedagogical pass T1: Teoria Semana 1 Mermaid conversion

Scope: the three existing Semana 1 diagrams only. The teaching file remained 6,822 words. Coordinate-heavy inline SVG was replaced by three readable Mermaid sources and three manifest-safe directives. The Luna execution was bounded by `sol-teoria-mermaid-pass1.json`, prohibited further delegation, preserved the pre-pass source, and passed the job-scope verifier. Sol then performed source, renderer, semantic, and page-level review.

Outcomes:

- `cascata`: converted to a vertical cascade with visible exits and review paths; the participation/authorship review now reconnects to typicity/imputation instead of floating as an orphan.
- `fato → norma → juízo`: preserved one factual event receiving two legally qualified routes and provisional judgments.
- `exclusões da conduta`: distinguishes absence of bodily control from moral coercion, which preserves conduct while moving the issue to exigibility.
- The builder gained relative-path confinement, Mermaid compilation caching, SVG ID namespacing, explicit EPUB SVG declaration, native-label configuration, and a `foreignObject` rejection guard.
- The first post-conversion EPUB failed with 46 errors; this failure led to D009 and was corrected rather than waived.
- Final EPUB: 22 chapters, EPUBCheck 5.3.0 with 0 errors and 0 warnings.
- Final PDF: 457 A4 pages. Page-level inspection of pages 3 to 7 confirms readable labels, no clipping, correct callout separation, and useful variation between diagrams, tables, examples, and prose.
- Whole-course lint: 0 errors and 27 warnings. Three new warnings correctly flag diagram/table adjacency for human redundancy review; inspection found the tables serve as accessible textual projections and application scaffolds rather than mere visual duplicates.

Status: accepted as the authoring-format baseline. It does not yet prove that claim manifests improve fidelity; that remains a separately controlled experiment.

## Handoff note: Sol's session ended on usage limit, Claude resumed 2026-08-29

Sol's session ran out of usage credits mid-review, partway through independently checking the Metodologia M1 batch. Three batches were left staged in `Operator/` folders, none promoted to live. Claude verified all three against the acceptance rubric rather than trusting Sol's own transcript narration, since a transcript describes intent, not necessarily completed disk state. One described action had in fact not happened: Sol's transcript said a "C1.1 correction" was sent for the Controle draft, but no corrected files or job exist on disk. Treat transcript narration as a claim to verify, not a report to trust.

### Pilot P1 adjudication: claim-manifest experiment

Blind scoring was dispatched to a fresh subagent with no access to `run-report.md`, any manifest file, or any `variant-b` file, only the six rendered images (labeled only by pair and X/Y) and the live Semana 1 source text. Claude could not perform the blind review directly, having already read the operator-facing randomization table while auditing the batch; this is itself a process lesson (see below).

**Result: X and Y received the identical defect profile on all three pairs.** No defect was found in one condition and absent in the other. This does not satisfy decision rule 1 in `Study Pack Visual Claim Experiment.md` ("Condition B materially reduces serious relationship defects"), so Phase 1 as executed does not support advancing to Phase 2.

**Why, on inspection of the run-report:** Condition B was not independently extracted from the raw source prose. The run-report states Variant B "retains the accepted topology" and clarifies labels "where the accepted A label was compressed", meaning claim extraction was performed by reading the already-authored Variant A diagram, not by re-deriving claims from Semana 1 directly. Any error already present in the shared understanding behind A was therefore available to be inherited by B rather than independently caught by it. The experiment as run measures whether re-expressing an existing diagram as claims changes its content (it mostly doesn't); it does not measure whether extracting claims from primary source independently catches more errors than direct authoring, which is the actual hypothesis.

**Correction required before Phase 2:** Condition B's writer must receive only the declared source span and representation brief, explicitly withheld from Condition A's finished diagram, mirroring the existing rule that A's writer must not see B. Re-run Phase 1 (three pairs is enough for a corrected pilot, not for Phase 2) under this constraint before deciding whether to proceed.

**Real defects found regardless of the experiment's validity:** two of the three "accepted A" diagrams are the live, currently shipped diagrams, and the blind reviewer found genuine defects in both, independently confirmed by Claude against source:

- `semana01-cascata.mmd`: the "Revisão: permissão ou participação" node had no inbound edge (a floating annotation) and conflated a cause (permissão found at Q3) with a deferred, unrelated topic (participação/autoria, explicitly deferred to a later week per source line 247). Fixed: the review node is now triggered directly from the `Fato permitido` exit, relabeled to state only what the source supports, and no longer loops back into the tipicidade question.
- `semana01-exclusoes-conduta.mmd`: bundled reflexo, convulsão, inconsciência, and coação física irresistível into one deterministic "sem conduta" exit. The source's own `[!CAUTION]` callout on this exact point says "não se deve transformar 'inconsciência' em resposta única", and the worked case "A crise convulsiva" (5.3) resolves the inconsciência branch conditionally on whether there was a lucid interval, not deterministically. The diagram also stated "exigibilidade afetada" as flat fact where the source table says "possível exclusão de culpabilidade." Fixed: inconsciência/automatismo now branches on the lucid-interval question per the worked case; the culpabilidade outcome is now stated as possible, matching source.

Both fixes preserved the pre-fix files under `diagrams/Superseded/claude-diagram-fix-2026-08-29/`. Rebuilt and verified: `tools/verify_study_packs.py` passes all three packs (Teoria 22 chapters/456 pages, 0 lint errors, EPUBCheck 0/0/0/0, foreignObject=0). Contact sheet of pages 1-15 confirms both corrected diagrams render legibly and without clipping at final page size.

Status: pilot P1 rejected as designed; two real defects in live content found via the pilot and fixed regardless. Journal entry doubles as the correction record for both.

### D012: A reviewer who has seen the condition key cannot blind-score

Claude read the run-report's "operator reproducibility" table (which candidate is X and which is Y per pair) before locating the blind-score package, disqualifying Claude as the blind reviewer for that data. The correct recovery was delegating to a fresh subagent with a scoped prompt that named only the images and source, explicitly excluding the run-report and any manifest/variant-named file.

Reusable lesson: the controller preparing a blind package must not be the one who scores it, even under time pressure, even when the controller is confident they can ignore what they already know. Structural blinding (a separate process invocation with a narrower file allowlist) is the only reliable form; self-discipline is not. This is the same lesson as `job_scope.py`: hard controls over instructions.

### D013: Batches described as complete in a transcript must be checked against disk

Sol's final transcript, delivered secondhand through the user after a usage-limit cutoff, described a "C1.1 correction" as sent. No corresponding job file, snapshot, or corrected staging directory exists anywhere in the repository. The Controle CC-01/02/03 batch in `Operator/sol-cc01-03-v1/` is therefore still the original draft, and it still contains the defect the transcript says was being fixed: pervasive "o deck define...", "o deck afirma...", "O deck chama..." provenance language throughout CC-01, CC-02, and CC-03, which violates the no-meta-commentary standing rule the same way the original 2026-08-27 pass's "Nota sobre a lacuna bibliográfica" did.

This batch is not promoted. It requires a real correction pass, not a re-read of the transcript's description of one.

### Controle CC-01/02/03 corrected and promoted

Claude applied the correction directly rather than dispatching another agent: the architecture underneath the provenance leak was already sound (pipeline diagram, recuperação exercises with answer keys, correct spine ordering), so this was surgical editing, not a rewrite. Every "o deck define/afirma/menciona/chama", "a página X", "as páginas X a Y" and "o material" instance across all three files was rewritten to teach the law directly, matching the standing no-meta-commentary rule already enforced elsewhere in the corpus. One self-flagged item (CC-02's note that the source slide's "65 anos" figure needed verification before publication) was resolved using the same correction already established in the original corpus: EC 122/2022 raised the limit below 70, EC 88/2015 set compulsory retirement at 75, distinct institutes. Internal "CC-01/CC-02/CC-03" cross-references in body text were also replaced with reader-facing phrasing ("o tópico anterior", "o próximo tópico"), since those are operator unit IDs, not content the reader should see exposed.

**Before promoting, content coverage was checked, not assumed.** CC-03 explicitly defers RE 466.343, ADO 26, MI 4.733, and Marbury v. Madison to "tópicos correspondentes." A corpus-wide grep confirmed all four already have substantive treatment elsewhere (files 04, 05, 08, 18, 19, 22), independent of the three files being replaced. The deferral is deduplication, consistent with the redundancy this journal already flagged between files 11 and 12 in the earlier audit; it is not content loss. Old files 01, 02, 03 (8,829 words combined) were preserved under `luna_output/Superseded/claude-cc01-03-promotion-2026-08-29/` before being replaced by the corrected units (3,712 words combined). The reduction is real: it removes duplicated case development and replaces exhaustive prose with a pipeline diagram plus worked recuperação exercises, the format this journal's D003 baseline identified as underused in this course specifically.

**A second defect surfaced only at render time, not at the text level.** The promoted files used raw ` ```mermaid ` fenced code blocks embedded directly in the markdown. The builder's `MERMAID_DIRECTIVE_RE` only recognizes the `{{mermaid:path.mmd}}` directive established for Teoria; it does not compile inline fences. The first rebuild therefore printed the four diagrams as literal source text on the page, a defect invisible in the markdown source and only caught by rendering and reading the actual PDF page. All four diagrams were extracted into `luna_output/diagrams/` as separate `.mmd` files (`cc01-parametro-objeto.mmd`, `cc02-supremacia-rigidez-jurisdicao-1.mmd` and `-2.mmd`, `cc03-guardiao.mmd`) and referenced via directive, matching the Teoria convention. All four compile with zero `foreignObject`. Rebuilt and confirmed by contact sheet: real rendered flowcharts on pages 2, 6, 7, and 11, not code.

Rebuilt and verified: `tools/verify_study_packs.py` passes all three packs (Teoria 22/456, 0 errors; Metodologia 16/213, 0 errors; Controle 22/251, 0 errors, down from 260 pages pre-promotion). This is the first time Controle has diagrams at all.

### D014: A format mismatch between agents is invisible until render

Sol established the `{{mermaid:file.mmd}}` directive convention while working on Teoria. When independent work on Controle used plain ` ```mermaid ` fences instead, both are syntactically valid Markdown, the lint checks pass, and the defect is only visible by actually building the PDF and looking at the page. This is the same class of lesson as D006 (`unzip -t` is a container check, not an ebook check): syntactic validity at the source level does not imply the build pipeline knows what to do with it.

Reusable lesson: when multiple passes or agents produce diagram-bearing content, either enforce one authoring convention with a lint rule that rejects the other form, or make the builder accept both. A rendered-page check remains mandatory regardless, since this is exactly the kind of defect that a linter operating on Markdown text cannot see by construction; only reading the compiled artifact catches it.

## Status after this session

All three packs pass `tools/verify_study_packs.py`: Teoria 22 chapters/456 pages/0 lint errors, Controle 22 chapters/251 pages/0 lint errors, Metodologia 16 chapters/213 pages/0 lint errors. All three EPUBs pass EPUBCheck with zero errors and warnings.

### Metodologia A03-05 through A03-08 drafted and accepted

Dispatched to a Sonnet subagent, scoped and snapshotted with `tools/jobs/claude-metodologia-a03-tail.json`, calibrated against the already-approved A03-01/A03-02/A03-04. Job-scope verify: ACCEPT, 5 created, 0 modified outside scope. Lint: 0 errors.

Claude independently spot-checked three of the four units against the raw Tau Anzoátegui PDF rather than trusting the agent's self-report: A03-05's Palafox "arnês de Saul" quote and the Mariluz Urquijo "escritório/escrevente veterano" passage, A03-07's Bobadilla "cera... como Proteo" and the Cuzco 1582 interrogatório, and A03-08's closing Tau quote ("os ditos de antigos sábios, os aforismos..."). All three checks matched the source word for word, including citation details. A03-06's four-dimension matrix table was checked against its blueprint entry and matches the specified authorities per row. All four mermaid diagrams (A03-05's four-step cycle, A03-07's consultation cycle, A03-08's disposition-to-organization bridge; A03-06 uses a table instead, correctly per its blueprint's "matriz de quatro dimensões") compile with zero `foreignObject`.

A03-08 correctly self-limits: it explicitly declines to develop conciliar/reducción content that belongs to Aula 04, and closes by naming the question A04-01 opens rather than repeating A04-01's own content.

Accepted, not yet promoted. Aula 03 is now complete (A03-01 through A03-08, all eight blueprint units present). Awaiting the parallel A04-03 through A04-07 batch before considering a combined promotion of both Aulas, since promoting Aula 03 alone while Aula 04 stays a mix of old prose-pass content and two new units would leave the course inconsistent mid-build.

### Metodologia A04-03 through A04-07 drafted and accepted

Dispatched to a second, parallel Sonnet subagent, scoped and snapshotted with `tools/jobs/claude-metodologia-a04-tail.json`. The job-scope verifier initially reported REJECT; Claude independently traced this with a custom cross-reference script before accepting the agent's own explanation. Cause: this job's `watch` tree overlapped the sibling A03-tail job's tree, so each job's post-run snapshot diff picked up the other job's legitimate output as an apparent violation. Cross-checking actual created files against this job's own declared writable globs found zero real violations and zero modified live files. Noted as a known limitation of `job_scope.py` (fix deferred: either exclude sibling jobs' declared paths, or snapshot only each job's own scope rather than the shared watch tree), not a defect in the delivered content.

All five files' YAML frontmatter parses cleanly (`yaml.safe_load`). The three diagram-bearing files (A04-05, A04-06, A04-07; A04-03 and A04-04 use tables instead, matching their blueprint entries) compile with zero `foreignObject`.

Content was checked against the raw Flores PDF page images (mandatory given this source's known OCR corruption), not taken on the agent's self-report:

- A04-03: the two-repúblicas comparison (shared Crown/Direito indiano, distinct local authorities), the Matienzo pueblo-de-indios exclusion regulation (mulatos, negros libres, mestiços barred except those serving a cleric or Spaniard, on pain of açoites and perpetual exile), the Santa Fe 1573 founding by Juan de Garay from a mancebo-paraguayo expedition, and the "indiano" (criollo + peninsular) definition all matched source precisely, including citation details (Levaggi, Matienzo's *Gobierno del Perú* p. 47, Planas).
- A04-04: the Trent periodicity requirement (metropolitans every three years, bishops annually, per López de Ayala's translation), the III Concílio de Lima's session dates (15 August 1583, chapter XL; September 1583, chapter XI's 500/400/300/200 threshold; chapter XII on fábricas/engenhos/minas), the 1655 Sínodo de Buenos Aires under bishop Cristóbal de Mancha y Velasco (8th constitution on mandatory Spanish, 14th and 15th constitutions on Jesuit missions converting to paróquias from 1648), and the Solórzano 1648 / encomienda-violence pairing all matched source word for word.
- A04-05: previously verified in full this session (Loayza's 1545-1575 tenure and instructions, the Mexican parallel, the catechism-translation requirement, Toledo's offer to the Jesuits against Borja's resistance). No new discrepancies on this pass.
- A04-06: the Toledo→Felipe II→Ovando→1576 1ª Congregação Provincial→Acosta chain, and the "ênfase em ordenar os pueblos de indios resultou nas reduções" paragraph, matched source essentially verbatim.
- A04-07: the direct Tánacs quote on Spain excluding indiano prelates from Trent was checked against the Spanish original (TÁNACS, cit. p. 138) and is a faithful translation; the closing "espaços cotutelados" synthesis matches Flores's own conclusion paragraph precisely.

One genuine judgment call, independently confirmed correct by Claude rendering and reading PDF page 20 directly: the blueprint described pp. 20-24 as párocos/threshold material, but that content is actually on pp. 16-18; pp. 20-24 hold the Loayza/Mogrovejo genealogy instead. The agent wrote A04-04/A04-05 to match the actual page content rather than the blueprint's mistaken description, and flagged the deviation rather than silently diverging.

Two YAML syntax errors (unclosed leading quotes in list items, A04-03 and A04-04) were self-caught and fixed by the agent before delivery; confirmed clean on Claude's independent parse check.

Accepted. Aula 04 is now complete (A04-01 through A04-07, all seven blueprint units present). Combined with the already-accepted A03 batch, all 15 blueprint units for Aulas 03-04 now exist in staging.

### D015: staged diagram-bearing content must be checked for the directive-vs-fence bug before promotion, not after

Before promoting, Claude grepped all 15 staged files for ` ```mermaid ` fences vs `{{mermaid:...}}` directives. Six files (A03-05, A03-07, A03-08, A04-05, A04-06, A04-07) used raw fences, the exact D014 defect already found and fixed once in Controle. Since D014 was already documented as a reusable lesson, this check was done proactively before build rather than discovered again at render time. All six diagrams were extracted into `luna_output/diagrams/` (`a03-05-ciclo-experiencia.mmd`, `a03-07-ciclo-consulta.mmd`, `a03-08-disposicao-organizacao.mmd`, `a04-05-genealogia-concilio.mmd`, `a04-06-cadeia-jurisdicao.mmd`, `a04-07-tensao-reducao.mmd`) and swapped to directives; all six compile standalone with zero `foreignObject`, and three (A03-08, A04-06, A04-07) were additionally confirmed at the actual rendered PDF page, not just via standalone `mmdc` compilation: legible flowcharts, correct edge labels including dotted "tensão"/"não elimina"/"depende de" relations, no clipping.

Reusable lesson beyond D014 itself: a known defect class, once documented, becomes a pre-promotion checklist item, not just a thing to remember to look for reactively. `grep -c '```mermaid'` across a staging batch is cheap and should run before every promotion involving diagram-bearing content until the builder accepts both forms or a lint rule rejects fences outright.

### Metodologia Aulas 03-04 promoted: 2 monolithic files → 15 unit files

The live manifest listed `03 Aula 03.md` (9,213 words, 2 top-level sections) and `04 Aula 04.md` (6,326 words, 21 sections) as two files. Both were preserved under `luna_output/Superseded/claude-a03-a04-promotion-2026-08-29/` before removal. The 15 staged unit files (after the mermaid-directive fix above) were copied into `luna_output/` under their `A0X-0Y.md` section-id names, `build_manifest.toml`'s `contents` list was edited to reference all 15 in place of the 2 old entries, and the pre-build PDF/EPUB were preserved under `Study Packs/Superseded/claude-a03-a04-promotion-2026-08-29/`. Chapter titles come from each file's own `# H1`, not the filename, so the plain `A0X-0Y.md` names cost nothing at render time.

Whole-course lint after promotion: 29 files, 0 errors, 33 warnings (all "inspection alarm" WARNs on the new small unit files, expected: a 5-9 section unit legitimately needs 0-2 callouts, and the tool's own doctrine forbids resolving this by adding decoration). Rebuilt and verified: `tools/verify_study_packs.py` now reports Metodologia at 29 chapters/295 pages (up from 16/213), 0 lint errors, EPUBCheck 0/0/0/0, foreignObject=0. Teoria and Controle unaffected, still PASS.

Status: promoted and verified, both mechanically (lint, epubcheck, foreignObject) and visually (rendered-page spot checks of three of the six new diagrams). Metodologia's Aulas 03-04 are now fully architecture-rebuilt and live.

Remaining open items, in priority order:
1. The claim-manifest pilot (P1) is rejected as designed and needs Condition B's writer genuinely walled off from Condition A's finished diagram before Phase 2 can proceed; see the P1 adjudication entry above for the exact correction.
2. Controle topics 04-22 have not received the architecture rebuild; only 01-03 have. This is the largest remaining body of work and matches D007's originally proposed five-question spine (parâmetro, objeto e defeito, ator, rota, técnica e efeitos).
3. Metodologia's own course spine, beyond Aulas 03-04, is still unconfirmed for the rest of the course (Aulas 01-02, 05-15 remain in their earlier prose-pass state).
