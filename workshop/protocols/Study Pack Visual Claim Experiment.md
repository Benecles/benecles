# Study Pack Visual Claim Experiment

Version 0.1, started 2026-08-29. This protocol tests whether scoped claim manifests reduce substantive errors in legal diagrams after Mermaid has become the stable authoring format.

## Question

Does generating a diagram from explicit scoped claims produce fewer unsupported, inverted, strengthened, weakened, conflated, or materially incomplete legal relationships than authoring the same Mermaid diagram directly from the source?

The outcome is semantic correctness. Appearance, elegance, and preference are secondary observations and cannot decide the experiment.

## Preconditions

1. Both conditions use Mermaid and the same build pipeline.
2. Every candidate has a declared source span and representation type.
3. The direct-authoring and manifest-authoring conditions receive the same content scope and pedagogical objective.
4. Reviewers do not see condition labels, claim manifests, author names, or generation history.
5. The writer of a candidate does not review that candidate.

## Phases

### Phase 0: renderer baseline

Convert the three existing Semana 1 Teoria do Delito SVGs to direct-authored Mermaid. Verify legal edges, PDF rendering, EPUB conformance, and accessibility text. This phase changes authoring format only and is not evidence for or against claim manifests.

### Phase 1: schema falsification pilot

Create manifest-derived variants of the same three visuals. Use the pilot to discover where the proposed schema fails on:

- a multi-stage filter cascade with exit conditions;
- one fact evaluated through different legally relevant norms;
- physical coercion, moral coercion, absence of conduct, and affected exigibility.

Three pairs are too small to validate the architecture. The pilot succeeds only if it produces concrete schema revisions and a review instrument that can score errors without knowing the condition.

### Phase 2: paired substantive sample

Select 20 to 30 visuals across the three courses. Deliberately include:

- cumulative and alternative requirements;
- necessary and sufficient conditions;
- rebuttable presumptions;
- rules with exceptions and exceptions to exceptions;
- majority and minority positions;
- changes across time or institutional context;
- court-specific rules;
- holdings dependent on material facts;
- generalization from a holding;
- terms that are commonly conflated;
- procedures with actor, route, state, and effect transitions.

Each candidate receives a direct-authored variant and a claim-manifest variant.

## Conditions

### Condition A: direct authoring

The writer reads the declared source span and the representation brief, then authors Mermaid directly. It may keep private notes but may not create or consume a structured claim manifest.

### Condition B: claim-mediated authoring

The writer first extracts scoped claim envelopes and typed relations. The visual is then projected only from those claims. A projection inherits the whole envelope unless it explicitly narrows it. If the representation cannot show a material condition or attribution, the claim cannot support that edge or node.

The writer must not see Condition A.

## Minimal claim envelope

```yaml
claim_id: TD-S01-C001
kind: majority_doctrine
proposition:
  subject: coacao_fisica_irresistivel
  relation: excludes
  object: conduct
scope:
  when:
    - external_force_fully_controls_body
  unless: []
  jurisdiction: BR
  temporal: null
authority:
  position: majority
  source_refs:
    - source_id: semana01
      locator: lines 93-95, 127-152
alternatives: []
```

Permitted `kind` values remain: statute, binding holding, case reasoning, majority doctrine, minority doctrine, professor framing, and illustrative simplification.

Use typed relations between envelopes when one envelope cannot remain independently accurate:

- `exception_to`
- `disputes`
- `limits`
- `distinguishes`
- `generalizes`
- `depends_on`
- `cumulative_with`
- `alternative_to`
- `supersedes`

For holdings, material facts, issue, disposition, and any generalization basis are mandatory.

## Visual manifest

```yaml
visual_id: TD-S01-V03-B
source_claims:
  - TD-S01-C001
  - TD-S01-C002
projections:
  - claim: TD-S01-C001
    element: edge
    from: bodily_control_absent
    to: no_conduct
    scope_rendered: true
    rendering_note: complete external domination appears in the source node
  - claim: TD-S01-C002
    element: edge
    from: bodily_control_present
    to: exigibility_review
    scope_rendered: true
    rendering_note: moral coercion remains conduct and affects culpability analysis
```

## Correction after P1 (2026-08-29)

P1 found identical defect profiles in both conditions on all three pairs, which looked at first like a null result but was actually an invalid experiment: the run-report showed Condition B's writer extracted claims by reading Condition A's already-finished Mermaid diagram, not the raw source span. Any shared understanding baked into A (correct or not) was available to B for free. This is now a hard rule, not a reminder:

**Condition B's writer must never be given Condition A's Mermaid source, rendered diagram, or claim manifest.** Only the declared source span and the representation brief. If the same person or process produced both, run them as two separate, non-consecutive work sessions with no shared scratch state, and verify after the fact (diff the two prompts/contexts) that B's writer had no path to A's output. The existing rule 5 ("the writer of a candidate does not review that candidate") is necessary but not sufficient; this closes the actual gap P1 exposed.

## Blinding and assignment

1. Give every rendered variant a random review code unrelated to course, condition, or author.
2. Randomize pair order and prevent paired variants from appearing consecutively.
3. Strip source comments, file paths, Mermaid metadata, and manifest references from review copies.
4. Assign review to an agent that did not author either variant and cannot see the condition mapping.
5. Sol adjudicates disagreements against the declared source span after blind scoring is complete.

## Review instrument

Review every substantive edge and node. Mark each defect independently:

| Code | Defect | Test |
|---|---|---|
| U | Unsupported | Does the visual assert a relation absent from the source? |
| I | Inverted | Does direction, branch, polarity, actor, or outcome run opposite to the source? |
| O | Scope omitted | Was a material `when`, `unless`, jurisdictional, temporal, or factual condition dropped? |
| S+ | Strengthened | Did possibility become rule, disagreement become consensus, or persuasive authority become binding? |
| S- | Weakened | Did a requirement or legal consequence become optional or merely illustrative? |
| A | Attribution lost | Was a court, author, majority, minority, or professor position rendered as untyped law? |
| H | Holding generalized | Did a fact-bound holding become a general rule without an explicit basis? |
| C | Conflated | Were legally distinct concepts, routes, effects, or stages merged? |
| M | Materially incomplete | Does omission leave a competent reader with a misleading operational model? |

Record total substantive edges and nodes so error rates are normalized by diagram complexity.

## Primary and secondary metrics

Primary metric:

`substantive relationship defects / substantive edges and nodes`

Secondary metrics:

- number of diagrams with at least one serious defect, where serious means I, O, S+, A, H, C, or M;
- paired difference in defects for each candidate;
- extraction burden measured by claim count, manifest word count, and elapsed execution time when available;
- percentage of claims that require prose-like qualifiers longer than the proposition itself;
- number of claims rejected because the visual could not preserve their scope;
- reviewer confidence and adjudication disagreement.

Appearance ratings may be collected after semantic scoring but remain separate.

## Decision rules

The manifest approach advances beyond the experiment only if:

1. Condition B materially reduces serious relationship defects across the paired sample;
2. the improvement is not confined to one simple representation type;
3. claim extraction does not routinely collapse into long unstructured qualifiers;
4. holding-specific facts and doctrinal attribution survive projection;
5. independent reviewers can apply the scoring instrument with acceptable agreement.

If the manifest schema degenerates into prose fields, repeatedly rejects useful visuals, or merely moves errors from projection into extraction, revise or reject it. A falsified architecture is a successful experiment if it prevents corpus-scale investment.

## Artifacts to retain

- declared candidate list and source spans;
- both Mermaid sources per candidate;
- claim envelopes and visual manifests for Condition B;
- blinded rendered review set;
- condition key stored separately;
- raw review sheets;
- adjudication notes;
- aggregate results and protocol revisions.

All experiment artifacts are operator-facing and must remain outside reader build manifests.
