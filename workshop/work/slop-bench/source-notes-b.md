# SLOP-2 source notes — batch B

## 1. Pew Research Center, “How Much of the Internet Is Written With AI?” (20 Aug 2026)

**Source:** [Report](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/) · [Methodology](https://www.pewresearch.org/data-labs/2026/08/20/methodology-ai-content/)

**Claim checked:** The report analyzed 490,000 English-language pages sampled from Common Crawl.

**Evidence:** Its methodology says it randomly sampled 10,000 pages from each of 49 crawls, January 2021–July 2026, totaling 490,000. It analyzed page text with Open Pangram, an AI-authorship detector. The report says about 10% of all pages in the July 2026 sample showed significant signs of AI authorship, and more than one-third of the post-ChatGPT pages did. Pew explicitly cautions that individual pages can be misclassified and that punctuation alone (such as an em dash) is not proof of AI authorship.

**Decision — ADAPT.** Use its corpus-level signal that certain vocabulary and constructions have become more common as a reason to inspect repetitive phrasing. Do not turn its listed words, punctuation, or “negative parallelism” into a Portuguese legal-writing blacklist or use them to label an individual passage. The sample is English-language, public-web content, and the result depends on one detector.

## 2. Sourati et al., “The shrinking landscape of linguistic diversity in the age of large language models,” *Nature Human Behaviour* (2026)

**Source:** [Version of record](https://www.nature.com/articles/s41562-026-02550-0) · [DOI](https://doi.org/10.1038/s41562-026-02550-0)

**Claim checked:** LLM polishing or rewriting is associated with lower linguistic diversity; reported complexity-variance reductions are 21–50%.

**Evidence:** The article abstract reports three studies, seven datasets in different domains, and more than 880,000 texts. It says LLM polishing/rewriting retained core content while reducing writing-complexity variance by 21–50% across datasets and models (P ≤ 0.05), and describes amplification of dominant patterns alongside suppression of others.

**Decision — ADAPT.** Keep a gate criterion that revisions preserve the author’s meaningful variation and voice while improving clarity. Treat the quantitative range as the paper’s measured result, not a predicted effect for course pages: it does not establish that a particular Portuguese legal lesson will be homogenized by a given edit. The source supports checking for flattening, not prescribing stylistic eccentricity for its own sake.

## 3. Kim & Jurgens, “Interpreting Style Representations via Style-Eliciting Prompts,” Findings of ACL 2026, paper 2039

**Source:** [ACL Anthology record and paper](https://aclanthology.org/2026.findings-acl.2039/) · [DOI](https://doi.org/10.18653/v1/2026.findings-acl.2039)

**Claim checked:** Explicit descriptions of stylistic attributes can be more useful for style steering than asking an LLM to imitate a raw target-text exemplar.

**Evidence:** The paper builds prompts from 1,010 style features across 26 dimensions, generates synthetic text from those prompts, and trains a decoder to recover prompts from style embeddings. In its style-control comparison, decoded prompts beat the tested LLM imitation baselines, which were prompted to mimic a target text; in a separate human-writing task, decoded prompts produced text closer in the evaluated style space than the tested baselines. The authors limit the study to English and online question-answering text, and say generalization to formal prose or technical documentation remains unclear.

**Decision — ADAPT.** Prefer a short, concrete description of the intended writing qualities over “write like this sample” as a stand-alone instruction. This is a design cue, not a direct test of that simple choice: the winning method uses a learned decoder and style vectors, and the experiments do not cover Portuguese legal teaching.

## 4. Baumler et al., “Can You Make It Sound Like You? Post-Editing LLM-Generated Text for Personal Style,” ACL 2026 Long Papers, paper 2030

**Source:** [ACL Anthology record and paper](https://aclanthology.org/2026.acl-long.2030/) · [DOI](https://doi.org/10.18653/v1/2026.acl-long.2030)

**Claim checked:** Human post-editing improved perceived/model-measured personal style but did not fully remove LLM-like style traces.

**Evidence:** In a preregistered online study of 81 participants, participants planned content and then wrote or post-edited LLM-generated drafts for personal-writing tasks. Embedding-based measurements found post-edited drafts more similar to participants’ unassisted writing and less similar to raw LLM output, but still closer to LLM text than to participants’ control writing. Post-edited texts were more stylistically homogeneous than unassisted human texts. Participants’ perceived self-similarity did not track those embedding measurements closely. The paper studies English personal tasks and one LLM-draft workflow; its results are not a test of legal or instructional writing.

**Decision — ADAPT.** A human revision pass should change the reasoning, examples, emphasis, and phrasing for the lesson’s actual teaching purpose; surface edits alone are not evidence that a draft has acquired an instructor’s voice. Do not treat the study’s embedding metric as a slop detector or assume that its exact result transfers to Portuguese course content.
