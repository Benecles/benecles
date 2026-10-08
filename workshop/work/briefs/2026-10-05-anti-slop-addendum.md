# SLOP-2 addendum: read every resource, verify every number (CEO, 05/10)

The chairman wants each resource below **meaningfully considered**: read it at the source, decide what to adopt, adapt, or reject for Portuguese legal-teaching prose, and record the decision with a reason in `work/slop-bench/RESOURCES.md` (one entry per resource: what it claims, what we take, what we reject, why). The CEO read only bheijden/slop, avoid-ai-writing, autonovel ANTI-SLOP, stop-slop, MariusAure/anti-slop-writing and Bouchard's workflow. Everything else reached the brief through a second-hand summary.

## Verify before the standard cites it
Writing Standard Part D's preamble cites these findings second-hand. Open each paper, check the number, and correct the preamble (or confirm it) in the same PR:
- SlopBench (arXiv 2609.33905): models *more* lexically diverse than human references; the four slop distributions (length, opening constructions, paragraph rhythm, fixed constructions).
- Shaib et al., *Measuring AI "Slop" in Text* (arXiv 2509.19163): low agreement on binary judgments; decomposed dimensions.
- Paech et al., *Antislop* (ICLR 2026) + auto-antislop + antislop-sampler: model-specific overrepresentation, up to 1,000×; FTPO results.
- Pew (20/08/2026), 490k Common Crawl pages: em dash, Oxford comma, vocabulary, negative-parallelism trends.
- Nature Human Behaviour (s41562-026-02550-0): LLM rewrites reduce complexity variance 21–50%.
- ACL 2026 findings 2039 (attribute descriptions beat raw exemplars); ACL 2026 long 2030 (post-edited LLM drafts stay LLM-like); EMNLP 2025 findings 532 and IEEE 11267719 (few-shot style matching); EMNLP 2022 main 141 (candidate reranking).
If a link is dead or a claim doesn't hold, say so and drop it.

## Tools the first brief missed (consider each; the CEO's expectation in brackets)
- **adewale/anti-slop-writing**: tuning, holdout, adversarial false-positive and rewrite-quality evals. [Adopt the eval discipline: every linter rule and the critic prompt get tuning and holdout cases, including legitimate legal "não… mas" and statutory triads as false-positive tests.]
- **ameenmo/humanize-skill**: Preserve vs Conform. [Our gate is Conform to STYLE.md for site prose; Preserve applies when the chairman's own text is edited. Make the mode explicit in the critic.]
- **slopdetector.me, "The Fingerprints of Machine Prose"**: 97 patterns, regexes, AI/human rates, false-positive notes. [Primary pattern source for the linter alongside bheijden/slop; port to Portuguese, keep rates.]
- **tropes.fyi** (+ tropes-md): sentence, paragraph, tone, formatting, composition tropes. [Second pattern source, especially manufactured revelation, tricolon abuse, formatting grammar.]
- **se-uhd/ai-slop-skill**: review → report → revise, tropes.fyi pulled in dynamically, rules exported to AGENTS.md. [Model the wiring on it.]
- **hannsxpeter/humanizer**: VOICE.md from a writing sample, keeps real quirks. [Informs STYLE.md exemplars.]
- **eric-sabe/slop-lint**: corpus discovery against your own baseline. [Use its discovery machinery; reject its em-dash hard fail.]
- **conorbronsdon/avoid-ai-writing**: already the main source; also read its `references/patterns.md` detector-mode mapping and tolerance matrix, which the CEO skipped.
- **keez97/humanizer**: planted imperfections. [Reject, with the reason recorded.]
- **Bouchard's guide**: read in full (the CEO only read the workflow); the freeze-then-review step belongs in our wiring.

Done when `RESOURCES.md` has an entry for every item above, Part D's preamble is verified or corrected, and the #57 build reflects the adopted items.
