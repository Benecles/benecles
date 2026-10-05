# Source notes C: style adaptation and candidate selection

## ACL 2026 Findings 2039 — adopt selectively

[Kim & Jurgens, “Interpreting Style Representations via Style-Eliciting Prompts”](https://aclanthology.org/2026.findings-acl.2039/). The paper reports 1,010 style features across 26 categories and evaluates prompt recovery, same-style generation, and steering outputs toward human-written style; their method outperforms direct prompting with target text on style description and imitation. This is a useful practical direction for Portuguese legal-teaching prose: turn references into explicit, inspectable style instructions (e.g. sentence length, register, transitions, explanation-to-quotation balance) instead of asking the model to “write like” an undifferentiated exemplar. Adopt the idea of explicit style elicitation and evaluate it locally; do not present its reported gains as validated for Portuguese, historical legal materials, or teaching quality.

## Findings EMNLP 2025.532 — adapt as a caution and evaluation design

[Wang et al., “Catch Me If You Can? Not Yet: LLMs Still Struggle to Imitate the Implicit Writing Styles of Everyday Authors”](https://aclanthology.org/2025.findings-emnlp.532/). Its abstract describes a large in-context evaluation (over 40,000 generations per model; more than 400 authors; news, email, forums, blogs), with weaker imitation of nuanced informal styles than structured news/email. It evaluates via complementary authorship attribution/verification, style matching, and AI detection. The core implication is that implicit style matching from a few samples is unreliable and should be checked on multiple dimensions. Adapt the multi-metric evaluation idea to Portuguese course material, but replace personal-authorship metrics with human judgments of register, clarity, fidelity to legal concepts, and consistency with the teaching voice. Do not infer legal-prose results from their everyday-author domains.

## IEEE 11267719 — reject as evidence; low-confidence method inspiration only

[IEEE Xplore record: “How Well Do LLMs Imitate Human Writing Style?”](https://ieeexplore.ieee.org/abstract/document/11267719), DOI 10.1109/UEMCON67449.2025.11267719 (Jemama & Kumar; UEMCON 2025). The record describes a training-free authorship-verification/style-imitation framework combining character n-grams and transformer embeddings, tested on academic essays and cross-domain pairs; it reports large benefits for few-shot/completion prompting and high style-match accuracy. These are author-reported results on a narrow essay setup, with no legal-teaching or Portuguese validation, and the extreme completion agreement does not establish pedagogical quality or faithful factual content. Reject as support for a style-generation policy or efficacy claim. If useful, adapt only its basic separation of style similarity from fluency/content checks as a hypothesis for a local benchmark.

## EMNLP 2022 main.141 — adapt the reranking decomposition

[Suzgun, Melas-Kyriazi & Jurafsky, “Prompt-and-Rerank: A Method for Zero-Shot and Few-Shot Arbitrary Textual Style Transfer with Small Language Models”](https://aclanthology.org/2022.emnlp-main.141/). The method generates candidate rewrites using zero/few-shot prompts and reranks them on textual similarity, target-style strength, and fluency; evaluation spans seven style-transfer datasets. Adapt this as a constrained drafting workflow for teaching materials: generate alternatives, then prefer the one that preserves legal meaning, fits the requested register, and reads clearly. For this domain, add explicit checks for legal/factual fidelity and pedagogical accessibility; generic style-transfer scores are insufficient. The reported results do not establish that automated reranking is safe for legal explanations.

## Source check

All four titles, IDs, and summarized abstract-level claims were checked against the publisher primary record (ACL Anthology or IEEE Xplore). No broad factual claim is made beyond those records; transfer recommendations are explicitly framed as proposals for local evaluation.
