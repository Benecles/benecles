# Study Pack Prototype Acceptance Rubric

Version 0.1, started 2026-08-29. Use this after a bounded drafting pass and before authorizing a larger batch. It operationalizes the Study Pack Architecture and Reconstruction Pipeline Protocol without converting pedagogical judgment into quotas.

## Review order

Review in this order because later quality cannot compensate for an earlier failure:

1. scope and preservation;
2. source fidelity;
3. dependency and teaching sequence;
4. transfer and retrieval;
5. representation semantics;
6. artifact behavior;
7. document rhythm.

Stop at a hard-gate failure. Record the failure and revise the brief or prototype before scaling.

## A. Scope and artifact integrity: hard gate

- [ ] Every changed path is permitted by the declared job scope.
- [ ] Every required staged output exists.
- [ ] No live teaching file changed during a staging-only pass.
- [ ] Every replaced live file has a preserved pre-pass version.
- [ ] The build uses the declared manifest, with no undeclared or archived content.
- [ ] Expected chapter order and count match the manifest.

Decision: **pass / fail**. A failure rejects the run even if the prose is good.

## B. Source fidelity: hard gate

Review the draft beside the exact cited span, not beside the blueprint alone.

- [ ] Every substantive claim is supported by the declared source span or clearly identified as a bounded pedagogical inference.
- [ ] The draft preserves material conditions, exceptions, actors, dates, jurisdiction, and temporal scope.
- [ ] Possibility has not become rule; disagreement has not become consensus; persuasive or scholarly authority has not become binding law.
- [ ] The text distinguishes the source author from authorities quoted or summarized by that author.
- [ ] Case facts, issue, disposition, and any generalization remain distinct.
- [ ] No fluent connective sentence adds a new historical, causal, or doctrinal claim.
- [ ] Deferred material is explicit in the operator report and is not silently lost.
- [ ] Coverage is proportionate to the source's real density; no numeric target caused padding or compression.

Decision: **pass / revise / fail**. Unsupported or materially strengthened claims are failures. Local wording or qualification defects may be revised and rechecked.

## C. Unit storyboard and dependency order

Mark each item **yes / no / not applicable**, then explain every “no.”

- Does the opening pose the problem the unit equips the reader to solve?
- Does the reader receive a low-resolution shape of the answer before dense detail?
- Is each concept introduced before an example, distinction, consequence, or synthesis requires it?
- Does baseline doctrine precede complications, dissent, and edge cases?
- Are distinctions organized by shared dimensions rather than serial definitions?
- Does the sequence avoid introducing several unresolved concepts at once?
- Does the ending reconnect the parts into the course spine?
- Is there a terminal retrieval or synthesis object?

Record the abbreviated storyboard as ordered steps with `introduces` and `requires`. Reject scaling if a prerequisite appears after the step that needs it.

## D. Transfer and feedback substitute

- [ ] At least one prompt requires application to a new or altered fact pattern, not only recall.
- [ ] The verification key explains the controlling distinction rather than merely naming the answer.
- [ ] The unit anticipates a likely confusion or objection at the point where it arises.
- [ ] Worked examples identify which facts do the legal or conceptual work.
- [ ] Where a naive application would mislead, the unit exposes and corrects that failure.

Callouts are optional. A callout passes only when its function is definition, binding text, example, controversy, caution, quotation, navigation, or retrieval. Decoration does not satisfy this section.

## E. Representation semantics

For every table, diagram, timeline, comparison, or checklist:

- [ ] The representation performs a task prose performs poorly.
- [ ] Every compared item uses shared dimensions; every sequence preserves order; every branch preserves polarity and conditions.
- [ ] No node or edge is unsupported, inverted, strengthened, weakened, conflated, orphaned, or materially incomplete.
- [ ] Attribution and authority type remain visible where their loss would change meaning.
- [ ] An adjacent table or prose block adds accessibility, application, or detail rather than merely duplicating the picture.
- [ ] Labels remain intelligible at final PDF page size and in the EPUB reading context.

For claim-manifest experiments, use the separate blind review instrument and normalize defects by substantive nodes plus edges.

## F. Mechanical and rendered artifact QA: hard gate

- [ ] Reader-facing lint has zero errors; warnings have been reviewed, not mechanically “fixed.”
- [ ] PDF opens, has the expected page size, and contains the expected chapters.
- [ ] EPUBCheck reports zero errors and zero warnings.
- [ ] Page renders show no clipping, overflow, broken tables, orphaned headings, tiny diagram labels, or merged semantic components.
- [ ] Contact sheets show no unexplained long run of a single cognitive mode.
- [ ] Any changed renderer feature has a focused smoke test and a failure guard where practical.

Decision: **pass / fail**. A conformance or clipping defect blocks release.

## G. Scaling decision

Choose one outcome and record the evidence.

- **Accept prototype:** hard gates pass; source review finds no material defect; teaching sequence and transfer object work. Authorize the next bounded batch using the corrected brief.
- **Accept after revision:** the architecture is sound but local claims, order, or representation need correction. Revise this prototype and re-run the affected gates before scaling.
- **Reject and re-brief:** the defect repeats across the sample, the blueprint omitted source structure, the prose is self-similar, or the intervention solves the wrong problem. Change the method before producing more units.

## Required review record

Record:

- course, unit, version, reviewer, and date;
- source span and extracted source word count;
- draft word count as an observation, never a target;
- scope-verifier result;
- source-fidelity defects and their disposition;
- abbreviated storyboard with dependency findings;
- retrieval/application test result;
- representation defects;
- lint, PDF, EPUB, page, and contact-sheet results;
- scaling decision and the exact brief change for the next iteration.
