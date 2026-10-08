# Master brief · READ-1: research round on reading comfort (CEO → orchestrator, 05/10)

**What it is.** The chairman wants the long prose easier on the eyes. This is a research round that ends in a specimen the chairman can flip through, not a site-wide change. Desktop first.

**Questions to answer, each with the evidence quality stated (controlled study / large field data / expert convention / opinion):**
1. Measure: after WIDE-1 (76ch on desktop), what range does the evidence support for screen reading (Dyson; Legge; Rello et al.; Nielsen Norman)? Is 76ch right for our serif at 19 px?
2. Size and leading: body size and line-height for long-form screen reading at our measure; does leading need to grow with the wider measure?
3. Contrast and paper: our warm paper + ink vs. alternatives; pure black on white vs. softened ink; the night mode's contrast (halation in dark mode, weight compensation).
4. Typeface: x-height, stroke contrast, optical sizing (`font-optical-sizing`, `opsz` axis), and whether our reading serif is the best choice among free faces with good Portuguese diacritics (Source Serif 4, Literata, Newsreader, Charter…). Variable fonts also serve MOT-1's weight-on-hover.
5. Rhythm: paragraph spacing vs. indents; `text-wrap: pretty` (no orphans/widows); `hyphens: auto` with `lang="pt-BR"`; ragged right vs. justified (evidence says ragged right on screen; confirm).
6. Distraction: the graph-paper background behind text (the chairman found the grid too strong before), sticky elements, motion near text, link styling inside paragraphs, bold density.
7. Navigation aids for long reads: a progress cue, chapter landmarks, comfortable scroll targets; anything with evidence for comprehension rather than decoration.

**Output.**
- `work/readability/REPORT.md`: one section per question, the finding, the evidence grade with links, and a recommendation for our site in CSS terms.
- `specimen/leitura.html` (site): the same real lesson passage (a Latam Aula 05 stretch with a source block) rendered in switchable variants (current vs. recommended vs. one bolder alternative) with a small toggle bar, so the chairman can compare on his own screen. Each variant states what changed.
- No change to live lessons until the chairman picks a variant; then a follow-up issue applies it.

**Never:** cite readability "rules" without a source; recommend dyslexia fonts or other gimmicks without controlled evidence; touch figures; sacrifice the house look (paper, ink, accent colours) without saying so explicitly.
