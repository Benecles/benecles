# SLOP-2 source notes — addendum D

Scope: assess the requested writing guides for Portuguese legal teaching. These are editorial heuristics, not evidence of authorship. Preserve legal meaning, statutory wording, terms of art, and useful repetition ahead of stylistic novelty.

## `adewale/anti-slop-writing`

- The repository's central advice is to replace inflated importance with specific detail, name the concrete fact/mechanism, and make paragraph transitions express the actual relation (cause, contrast, dependency, inference, etc.). It also says not to ban dashes or antithesis categorically; check whether they do real work. ([README](https://github.com/adewale/anti-slop-writing); [skill rules](https://github.com/adewale/anti-slop-writing/blob/main/skills/anti-slop-writing/SKILL.md))
- The project is an instruction-only skill and keeps separate machine-readable evals, adversarial false-positive cases, rewrite-quality checks, and rejected edits. That structure is useful if this project later turns its prose criteria into a reusable lint/evaluation protocol; the repository's own README cautions that ceiling-level binary checks show no regression, not proof of improvement. ([README: skill/eval boundary and eval status](https://github.com/adewale/anti-slop-writing))
- **Adopt, selectively:** require a claim to earn its importance with a concrete legal carrier (article, case, procedural act) and require transitions to state a real doctrinal relation. Use “does this contrast or parallelism carry a proved distinction?” as a review question.
- **Adapt:** “sharp detail” means legally precise detail, not conversational color. A paragraph can properly repeat a statutory term or state a rule in formal register. Keep parallel clause structures when they make legal conditions comparable.
- **Reject:** do not import the repo's English-market “AI tell” inventory as a Portuguese checklist or infer machine authorship from any single feature.

## `ameenmo/humanize-skill`

- The skill explicitly says not to issue authorship verdicts or optimize for detection software, not to invent facts/examples/sources, and to keep quotations and legal terms of art verbatim. Its genre exception says legal/reference/specification prose may properly be plain, impersonal, and repetitive; parallel wording should be retained where it supports comparison, and jargon/terms of art must not be renamed. ([SKILL.md](https://github.com/ameenmo/humanize-skill/blob/main/SKILL.md))
- It ranks substantive problems (e.g., unverifiable material claims) above stylistic polish, and directs the editor to preserve facts, exact terms, and the requested voice. ([SKILL.md](https://github.com/ameenmo/humanize-skill/blob/main/SKILL.md))
- **Adopt:** the strongest fit for Brazilian legal-teaching material is its “genre exemption”: no synonym cycling across a single legal concept, no casual second-person voice inserted into reference prose, no “humanization” that changes a legal term, quote, statutory condition, or scope. Also adopt the rule that fact-checking is distinct from style editing.
- **Adapt:** keep its minimum-effective-edit principle, but the course's pedagogical voice and house rules govern. Avoid its global em-dash default as a project rule; punctuation should be judged by clarity and local style, not a universal tell.

## SlopDetector — “The Fingerprints of Machine Prose”

- The page describes itself as a style linter, explicitly not an authorship detector, and warns against using its patterns to accuse people. It says careful formal prose and restricted vocabulary can trigger the same kinds of patterns, and its reported measurements are corpus-bound (63,143 words, English Wikipedia human control frozen at 2017; page labels license CC BY-NC-SA 4.0). ([method, limits, and license](https://about.slopdetector.me/))
- It says its best use is rereading one's own draft or checking a house style, and says it is unsuitable for grading, screening, moderation, or any setting where a false accusation harms someone. It also notes that phrase lists decay as models and writing habits change. ([limits and intended use](https://about.slopdetector.me/))
- **Adopt:** the separation between a prose-quality lint and authorship judgment; report concrete reader-facing issues only. If we use a linter, treat matches as prompts to inspect context, never automatic failures.
- **Reject/adapt:** do not reuse its score/pattern list as a grading rubric or claim its measured English corpus validates Portuguese legal prose. Its own limitations make direct transfer especially weak for formal legal language.

## `tropes.fyi` and `tropes-md`

- `tropes-md` is a downloadable, single-file prompt/catalogue of patterns (e.g., negative parallelism, fragments for manufactured emphasis, premise stacking, invented concept labels, self-echo, repeated restatement). The page discloses that the file was AI-assisted. ([catalogue](https://tropes.fyi/tropes-md))
- The directory's own front page frames the project as an opinionated effort to identify and call out AI writing; the catalogue itself uses strong universal language for some entries. ([about and catalogue purpose](https://tropes.fyi/))
- **Adopt, selectively:** inspect actual repetition, unsupported abstraction, self-narration, fabricated labels, and a thesis restated without new legal consequence. These are useful questions for any teaching prose, independent of authorship.
- **Reject:** no “tropes” count or authorship verdict; no automatic bans on contrast, fragments, triads, em dashes, analogies, or repeated terminology. In doctrinal teaching, “X não é Y” may be the exact legal distinction; repeated terms may preserve referential precision; a short fragment may mark a real procedural consequence. The category label is not enough to diagnose a defect.

## Practical recommendation

Use the sources as a short human-editor prompt, not a detector: (1) identify the legal claim and its source carrier; (2) check that each paragraph adds a rule, reason, application, or consequence; (3) test whether contrasts and transitions express the actual doctrinal relation; (4) remove meta-narration and empty importance language; (5) preserve exact legal terms, quotations, statutory text, and comparison-friendly parallel phrasing. Do not score a writer or student from these patterns.
