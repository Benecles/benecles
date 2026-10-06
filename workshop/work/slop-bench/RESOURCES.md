# SLOP-2 resource decisions

Scope: Portuguese legal-teaching prose. These resources inform editorial checks; none validates AI authorship detection for this genre. A match is a prompt to inspect meaning, not a verdict. Legal accuracy, source fidelity, and instruction take priority over novelty or detector scores.

## Research and measurement

### SlopBench — Roongta, Gaddipati & Huynh (arXiv:2609.33905)
**Claim/evidence.** Evaluates 18 models across four English writing domains; measures task-relative length, repeated openings, paragraph rhythm, and fixed constructions. Composite rankings shift under reweighting and showed no reliable association with crowd Elo (n=18, r=−0.115, 95% CI [−0.55, +0.37], p=.65). [Paper](https://arxiv.org/html/2609.33905).
**Decision: ADAPT.** Inspect length fit, repeated templates, paragraph rhythm, and constructions as separate dimensions. Reject English tells, weights, rankings, and thresholds for Portuguese legal teaching; the benchmark excludes truth and pedagogical utility.

### Shaib et al., “Measuring AI ‘Slop’ in Text” (arXiv:2509.19163)
**Claim/evidence.** Taxonomy and annotation study across 150 news articles and 100 QA passages. Binary judgments showed low inter-annotator agreement (pairwise κ −.15, .29, .06; Gwet AC1 .12, .42, .28), with domain-dependent criteria; scalable automated measurement remains open. [Paper](https://arxiv.org/html/2509.19163).
**Decision: ADOPT the multidimensional framing; ADAPT the criteria.** Keep factuality, relevance, density, repetition, coherence, and tone separate. Reject one binary slop score or claims that a detector can settle quality; English news/QA is not Portuguese legal teaching.

### Paech et al., “Antislop” (ICLR 2026)
**Claim/evidence.** English creative-writing experiments report 83–92% pattern suppression by FTPO with quality within 1% of baseline; tested model and prompts are narrow. The framework also supports contextual soft suppression. [Proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/467746c8e15fbfca34dcf23be9ef9229-Abstract-Conference.html), [paper](https://arxiv.org/pdf/2510.15061).
**Decision: ADAPT caution, REJECT its training results as our expected effects.** Pattern frequency can motivate review, never a global ban. Keep legal terms and contextually necessary phrases.

### Auto-Antislop
**Claim/evidence.** The [official repository](https://github.com/sam-paech/auto-antislop) samples a chosen prompt set, identifies model-specific overrepresented n-grams, builds preference data, and fine-tunes with FTPO.
**Decision: REJECT as a writing-gate component; ADAPT the model-specific profiling idea.** This is model profiling/training, not editorial review; any later corpus work needs our own Portuguese data and validation.

### Antislop Sampler
**Claim/evidence.** The [official repository](https://github.com/sam-paech/antislop-sampler) provides sampler code and English pattern lists; the paper describes backtracking and soft/hard suppression.
**Decision: REJECT the lists/runtime as a direct gate; ADAPT contextual flags only.** English lists do not establish Portuguese legal patterns, and even the source permits needed terms in context.

### Pew Research Center, “How Much of the Internet Is Written With AI?” (20 Aug 2026)
**Claim/evidence.** The [report](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/) and [methodology](https://www.pewresearch.org/data-labs/2026/08/20/methodology-ai-content/) describe 490,000 English pages (10,000 from each of 49 crawls), classified with Open Pangram; authors caution that pages can be misclassified and punctuation alone is not proof.
**Decision: ADAPT.** Corpus-level vocabulary/construction trends can suggest what to inspect. Reject its English features as a Portuguese blacklist or individual authorship test; one detector underlies the measurements.

### Sourati et al., “The shrinking landscape of linguistic diversity in the age of large language models” (Nature Human Behaviour, 2026)
**Claim/evidence.** Across three studies, seven datasets, and over 880,000 texts, the article reports LLM polishing/rewriting reduced writing-complexity variance by 21–50% (P ≤ .05). [Version of record](https://www.nature.com/articles/s41562-026-02550-0).
**Decision: ADAPT.** Preserve meaningful variation during edits; use the range only as this study's result, not a prediction for any lesson or Portuguese legal text. It supports checking for flattening, not making prose quirky.

### Kim & Jurgens, “Interpreting Style Representations via Style-Eliciting Prompts” (Findings ACL 2026, 2039)
**Claim/evidence.** Evaluates 1,010 style features across 26 dimensions; learned style-eliciting prompts outperform the tested direct exemplar-imitation baselines on English online Q&A tasks. Formal prose transfer is unclear. [ACL Anthology](https://aclanthology.org/2026.findings-acl.2039/).
**Decision: ADAPT.** Describe target qualities explicitly and inspectably rather than relying on “write like this sample.” The method is learned and does not validate Portuguese legal teaching.

### Baumler et al., “Can You Make It Sound Like You?” (ACL 2026 Long Papers, 2030)
**Claim/evidence.** In an 81-participant preregistered personal-writing study, human post-edits moved drafts toward participants' unassisted writing but remained closer to LLM output; edited texts were more homogeneous. [ACL Anthology](https://aclanthology.org/2026.acl-long.2030/).
**Decision: ADAPT.** Substantive revision should serve the teaching purpose; surface polish alone does not establish voice. Do not use embedding metrics as a slop detector or generalize the result to legal prose.

### Wang et al., “Catch Me If You Can? Not Yet” (Findings EMNLP 2025, 532)
**Claim/evidence.** Evaluates style imitation for 400+ authors across news, email, forums, and blogs, with 40,000+ generations per model; implicit everyday styles are harder to imitate than structured genres. [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.532/).
**Decision: ADAPT.** Evaluate multiple local dimensions, replacing authorship metrics with legal fidelity, register, clarity, and teaching fit. Do not infer legal-prose results.

### Jemama & Kumar, IEEE 11267719, “How Well Do LLMs Imitate Human Writing Style?”
**Claim/evidence.** Publisher record describes training-free style/authorship verification using character n-grams and transformer embeddings on academic essays and cross-domain pairs. [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11267719).
**Decision: REJECT as policy evidence; ADAPT only as a benchmark hypothesis.** Narrow essay evaluation does not establish Portuguese legal-teaching quality or safe style generation.

### Suzgun, Melas-Kyriazi & Jurafsky, “Prompt-and-Rerank” (EMNLP 2022, main.141)
**Claim/evidence.** Generates candidate style-transfer outputs and reranks by textual similarity, target-style strength, and fluency across seven style-transfer datasets. [ACL Anthology](https://aclanthology.org/2022.emnlp-main.141/).
**Decision: ADAPT.** Candidate selection can add legal meaning, factual fidelity, and pedagogical accessibility; generic style-transfer scores alone are insufficient.

## Guides, repositories, and tools

### adewale/anti-slop-writing
**Claim/evidence.** Offers concrete-detail and paragraph-relation prompts, plus tuning/holdout/adversarial false-positive and rewrite-quality evaluation structures. [Repository](https://github.com/adewale/anti-slop-writing).
**Decision: ADOPT selectively.** Require claims to earn importance through a legal carrier and transitions to express real relations. Adapt eval discipline for rules and critic prompts; retain real legal parallelism and reject English tell lists as Portuguese checks.

### ameenmo/humanize-skill
**Claim/evidence.** Avoids authorship verdicts, preserves quotations/terms of art, and exempts legal/reference prose from casual voice and synonym cycling. [Skill](https://github.com/ameenmo/humanize-skill/blob/main/SKILL.md).
**Decision: ADOPT Preserve/Conform modes.** Conform to STYLE.md for site prose; Preserve when editing chairman-authored text. Use minimum effective edits and keep legal terms exact.

### SlopDetector, “The Fingerprints of Machine Prose”
**Claim/evidence.** Describes itself as a style linter, not an authorship detector; documents English corpus limits and warns against grading or accusation from matches. [Method and limits](https://about.slopdetector.me/).
**Decision: ADOPT the separation of lint from authorship judgment; REJECT its score/pattern list as a grading rubric.** Treat findings as review prompts only.

### tropes.fyi and tropes-md
**Claim/evidence.** Opinionated catalogue of sentence, paragraph, tone, formatting, and composition patterns, with AI-assisted content disclosed. [Project](https://tropes.fyi/), [catalogue](https://tropes.fyi/tropes-md).
**Decision: ADOPT selectively as review questions; REJECT counts and universal bans.** Inspect unsupported abstraction, self-narration, and needless repetition. Preserve real legal contrasts, triads, fragments, and terminology.

### se-uhd/ai-slop-skill
**Claim/evidence.** Layered rules, optional register guidance, quote preservation, and export to AGENTS.md. [Repository](https://github.com/se-uhd/ai-slop-skill).
**Decision: ADAPT its wiring and preserve-meaning-before-simplification principle.** Reject English trope-catalogue dependency and blanket sentence-length targets.

### hannsxpeter/humanizer
**Claim/evidence.** Stresses rhythm variety, voice, and real details rather than synonym replacement. [Skill](https://github.com/hannsxpeter/humanizer/blob/main/SKILL.md).
**Decision: ADAPT conservative rhythm variety when it aids comprehension; REJECT detector-evasion or word-list substitutions.** Correctness and formality are not tells.

### eric-sabe/slop-lint
**Claim/evidence.** Corpus discovery against a baseline; README treats many phrase hits as warnings but makes em dash a hard failure. [Repository](https://github.com/eric-sabe/slop-lint).
**Decision: ADOPT discovery machinery; REJECT its em-dash hard fail.** Calibrate patterns to local Portuguese legal prose.

### conorbronsdon/avoid-ai-writing
**Claim/evidence.** `references/patterns.md` maps detectors and gives a tolerance matrix by context. [Pattern guide](https://github.com/conorbronsdon/avoid-ai-writing/blob/main/references/patterns.md).
**Decision: ADOPT contextual tolerance and pattern clusters; ADAPT genre profiles.** Reject English thresholds and use as editorial aid, not detector calibration.

### keez97/humanizer
**Claim/evidence.** Includes no-fabrication and uncertainty safeguards but mandates deliberate imperfections in long-form writing. [Skill](https://github.com/keez97/humanizer/blob/main/SKILL.md).
**Decision: ADOPT anti-fabrication and uncertainty preservation; REJECT planted imperfections.** Never add awkwardness, tangents, fake hesitation, or errors to simulate humanity.

### Bouchard, “Anti-Slop AI Writing Guide”
**Claim/evidence.** Workflow template centers purpose, audience, structure, evidence, source checks, and a final editorial pass. [Full guide](https://github.com/louisfb01/ai-engineering-cheatsheets/blob/main/Anti_Slop_AI_Writing_Guide.md).
**Decision: ADOPT audience/outcome-first planning and source verification; ADAPT to legal question, governing source, reasoning, and learning objective.** Reject fixed em-dash/word bans, zero-targets, and marketing voice as universal rules.

### bheijden/slop (CEO read first-hand, 05/10)
**Claim/evidence.** A prose linter whose 78 `ai-tells` rules each record a matched human/AI corpus result; it ships rules that discriminate in the right direction and parks the ones measured backwards. Measured-positive: "genuinely" (×53), `not-x-but-y`, `semicolon-correction`, `colon-appositive` (rate), `rather-than` (rate), `load-bearing-adverbs`, `nominalisation-pileup`, `paren-scarcity`; em dashes measured as **not** a tell. [Repository](https://github.com/bheijden/slop).
**Decision: ADOPT the method and the measured rules (ported to Portuguese as RATE rules); REJECT its em-dash rule as slop evidence.** Rules ship only with tests and a false-positive note; rates, not single hits, for ordinary constructions.

### NousResearch autonovel, ANTI-SLOP.md (CEO read first-hand, 05/10)
**Claim/evidence.** Field guide: slop = low information density + predictable structure + unnatural vocabulary; separates vocabulary tells from structural ones (topic-sentence machine, list abuse, symmetry addiction, hedge parade, transition-word paragraph openers, "not just X but Y", false depth). [File](https://github.com/NousResearch/autonovel/blob/master/ANTI-SLOP.md).
**Decision: ADOPT the structural tells** as `transition-opener`, `hedge-stack`, `uniform-paragraphs` and the D10 restatement ban; **REJECT** its English vocabulary tiers as a Portuguese list and its blog/notebook tone advice (wrong register).

### hardikpandya/stop-slop (CEO read first-hand, 05/10)
**Claim/evidence.** Short agent skill: binary contrasts, negative listings, dramatic fragmentation, rhetorical setups, false agency, vague declaratives, quotable closers; five-dimension 1–10 score (directness, rhythm, trust, authenticity, density). [SKILL.md](https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md).
**Decision: ADOPT** fragmentation (`fragment-run`), rhetorical setups (`teaser-hook`, `reader-steer-question`) and its density/directness dimensions in the critic; **REJECT** "no passive ever", "kill all adverbs", "you beats people" and "no em dashes": legal prose needs agentless passives for rules and must not address the reader (D7).

### MariusAure/anti-slop-writing, writing.md v7 (CEO read first-hand, 05/10)
**Claim/evidence.** One system prompt: fulfil the job first; avoid-list items are warning lights, not bans; meaning test (restate the boring version), fungibility test (could the sentence sit in any article?), evidence test, fit test; never invent detail to seem human. [writing.md](https://github.com/MariusAure/anti-slop-writing/blob/main/writing.md).
**Decision: ADOPT** the meaning and fungibility tests in the critic and in Writing Standard Part D's preamble spirit; **ADOPT** "do not humanize". Nothing here is lintable; it governs judgment.

## Cross-source policy

1. Preserve legal meaning, source scope, quotations, statutory wording, terms of art, and real uncertainty.
2. Describe the target register positively in Portuguese; use local examples as evidence, not as a style to imitate wholesale.
3. Lint for reader-facing defects and measured local frequency. Findings prompt review; only explicit budgets fail a run.
4. Patch flagged spans only. Never infer authorship or add deliberate errors, fragments, slang, fake opinions, or invented anecdotes.
