# Master brief · SLOP-2: the anti-slop pipeline (CEO → orchestrator, 05/10)

**What it is.** A writing-quality gate that sits after every writer on this project (lessons, cards, fronts, briefs' visible text). It measures where our prose drifts from a defined target style and fixes those spans locally. It is *not* a "humanizer" and not an AI detector. The chairman asked for every useful idea in his research to be implemented; this brief is the CEO's cut of that research. The HOW is yours.

**Read first:** `protocols/CUFRGS Writing Standard.md`, Part D (now with the new preamble, D9 density limits, D10 the five pathologies). That is the policy; this brief is the machinery.

## The principle the build must embody
Don't teach the model to "sound human". Give it a defined target distribution, measure where its output deviates, and correct those deviations as locally as possible. Every full-draft rewrite re-imposes model house style (LLM rewrites cut complexity variance 21–50%; post-edited LLM drafts stay LLM-like), so **no stage may rewrite unflagged text**.

## The five parts

### 1. `STYLE.md`: a positive target (in `protocols/`)
Derived from the human writing we consider good, not from a blacklist. Research (ACL 2026 style steering) shows explicit natural-language attribute descriptions beat "write like this sample". Build it by measuring a human reference corpus (part 3) and writing the values as attributes, e.g.: information density high; paragraph length highly variable; sentence length moderately variable; argument causal, not rhetorical; transitions mostly implicit; headings only for navigation; lists only for enumerable material; conclusions optional; restatement very low; metacommentary none; qualification only where doubt exists; examples concrete (articles, votes, dates); rhetorical symmetry low; rhetorical questions rare. Numbers come from the corpus, not from this list. Add 3–8 short exemplar passages (human, Portuguese, legal-teaching register) beside the attributes, never 50.

### 2. Deterministic linter: extend `protocols/tools/slop_lint.py`
- Implement every ⚙ item in Writing Standard D9 as a **rate** rule (per 1,000 words, with minimum-length gates as in bheijden/slop: ≥ 250 words, ≥ 5 sentences, ≥ 2 matches), Portuguese patterns. Keep existing D1–D8 rules.
- Port, in Portuguese, the measured-positive rules from bheijden/slop `rules/ai-tells.json`: `not-x-but-y`, `semicolon-correction`, `colon-appositive`, `rather-than` (rate), `load-bearing-adverbs`, `nominalisation-pileup`, `triad-density`, `paren-scarcity` (zero parentheses in a long page). **Skip** rules its own audit measured as backwards or evidence-free, and **never** treat em dashes as slop (house style only, C10).
- Each rule ships with: the pattern, a one-line fix, positive and negative test sentences, and a false-positive note (legal "não… mas" distinctions, statutory triads, enumerated requisitos are legitimate).
- Output: per page, findings with line, rule, matched span, fix; a density summary; JSON mode for agents. Findings never fail a run alone; `--max-per-1000 N` budgets do.

### 3. Corpus discovery: find *our* models' slop (`work/slop-bench/`)
Antislop (Paech et al., ICLR 2026) and slop-lint show model slop is model-specific; universal lists miss it.
- **Human reference corpus**, genre-matched: Portuguese legal-teaching prose we consider good. Sources: the course books on disk (Mendes, Barroso, Lenza, Caio Mário, Venosa, Faccini, Engelmann & Bandeira, Gargarella…), excerpts already in `work/book-extracts/`, decisions' ementas. Local only; no upload. ~200k words is enough.
- **Model corpus**: our live lesson pages (written by Codex/Luna and Claude) plus fresh generations on 30 representative lesson tasks from each model we use.
- Compare word, bigram, trigram and construction frequencies; publish the overrepresented list with ratios (`report.md`) and turn the strong, discriminating ones into linter rules (backtested: a rule must fire more on the model corpus than on the human corpus, or it does not ship). Rerun when we change models.

### 4. The critic: a span-level structural judge
A separate reviewer pass (a different model from the writer when possible; Luna is fine). It reads a frozen draft plus `STYLE.md` and Writing Standard Part D and returns **spans only**: for each, the dimension, the reason, and the smallest replacement. It does not rewrite unaffected text. Dimensions: information density, restatement, fake contrast, fake nuance, causal depth (circular explanations), forced symmetry, metadiscourse, significance inflation, conclusion pressure, formatting pressure, and D10's five pathologies. Hard rule in its prompt: **a finding needs a reason; appearing on a tell list is not one.** A 0–100 score per dimension with quoted evidence, so drafts can be compared.

### 5. Wiring
`writer → draft → slop_lint → critic → span patches → final`, with the Source Pipeline's existing S5 writer stage feeding it. Where cheap, generate 3 candidates and pick by (content correctness, instruction compliance, style similarity, density, slop penalty) before patching; don't iterate one draft forever. Put the gate's instructions in `~/.codex/AGENTS.md` so every Codex writer inherits it. Keep the permanent writer instruction short (the seven-point priority list in Part D's preamble), never a 20k-token manifesto.

**Never:** a humanizer that plants errors, fragments or slang; vocabulary-diversity targets; banning em dashes as slop; whole-page "make it cleaner" rewrites; open-weights sampler or FTPO work (we run closed models; note it in `report.md` as the path if that changes).

**Done when:** linter rules with tests pass; `report.md` lists the discovered tells with ratios; the critic prompt exists and has been run on Latam Aulas 01 and 02 with its span report saved; AGENTS.md carries the gate; ISSUES.md line.

---

# Brief · TXT-L1: AP + deslop pass on the Latam front, Aula 01 and Aula 02

**What.** The chairman asked that these three pages follow the AP Stylebook "where appropriate" and the new anti-slop rules. Source: `~/Downloads/ap-stylebook.pdf` (AP Stylebook 2000). Pages are Portuguese, so apply only the transferable AP principles, never English mechanics (serial-comma rules, abbreviations like "Sept.", US state names):
- **First reference identifies; later references shorten.** Full name and role at first mention ("Manuel José Cepeda Espinosa, relator"), surname after. Spanish names: paternal surname on second reference (AP "Spanish names").
- **Acronyms spelled out at first use** unless universal to this reader (STF passes; ECI, TCP, SCJ, CIDH, OC are spelled out once per page).
- **Titles:** formal title before a name, lowercase descriptive titles ("o presidente", "o ministro"); full court names capitalized (AP "court names").
- **Numbers:** figures for 10 and above, words for one to nine except dates, ages, articles, votes and percentages; votes as "por 5 a 4"; large sums with figures ("4,5 trilhões"); years as figures, never starting a sentence with a spelled year.
- **Dates:** figures, no ordinals except the Portuguese "1º"; a consistent pattern per page.
- **Attribution:** every claim about what a court, author or law said names it; no "especialistas", "a doutrina" without names (also D5).
- **Foreign terms** in italics with a gloss at first use if not obvious ("*chuzadas*", the illegal wiretaps…); Spanish court names glossed once.
- **Plain words** over inflated ones.
Then a Part D read (D1–D10, density by `slop_lint`) with **span-level** fixes only: no paragraph rewrites, keep every fact, keep the figures, defs SVGs, bet and quiz verbatim (the CEO's map work merged in PR #78 must not regress). Log every change in a diff report.

**Done when:** three pages pass slop_lint and check_all, a change log is saved beside the script, breakscan 1280 is 0 on the three pages, ISSUES.md line, PR merged. The CEO then runs the final aesthetics QA on all three pages.
