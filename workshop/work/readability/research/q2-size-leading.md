# READ-1, question 2: body size and leading

## Finding

Screen-reading evidence does not establish a single ideal body size or line-height for long-form prose at a 76ch measure, nor does it show that line-height should automatically increase as measure widens. Controlled studies give mixed results: larger text improved outcomes in one study of readers with dyslexia, while line-spacing effects were weak or mixed; a newer eye-tracking passage study found small processing benefits from wider spacing, alongside less accurate return sweeps. No study here tested the site's serif face, Portuguese prose, 76ch measure, or a long legal reading session. [Rello et al. 2013](https://pielot.org/pubs/Rello2013-W4A-SizeMatters.pdf); [Vasilev et al. 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10600290/); [Dyson 2004](https://doi.org/10.1080/01449290410001715714)

## Evidence and quality

- **Controlled study, font size and line spacing:** Rello and colleagues tested 28 participants with dyslexia reading six Wikipedia entries, varying size (10–26 pt) and line spacing (0.8–1.8). Larger sizes improved several objective and subjective measures up to about 18–22 pt; line spacing showed no significant fixation-duration effect, while the widest spacing (1.8) produced lower comprehension than the tightest (0.8). The authors recommend 18 pt for their target group and web context. [Study and results](https://pielot.org/pubs/Rello2013-W4A-SizeMatters.pdf)
- **Controlled study, line spacing:** Vasilev and colleagues used eye tracking with 36 native English-speaking undergraduate participants without known reading difficulties. They read four-line newspaper excerpts in 19-pt Inconsolata at three line spacings. Wider spacing modestly shortened word fixation durations and increased skipping, but also increased corrective eye movements after return sweeps; the authors report a 2–3 ms-per-word saving from wider spacing and caution that the difference was subtle. The study manipulated spacing, not line length. [Study and results](https://pmc.ncbi.nlm.nih.gov/articles/PMC10600290/)
- **Expert convention, with an evidence caveat:** Dyson's review reports the typographic argument that long lines need more interlinear space to help readers find the next line on a return sweep. The review also says systematic joint testing of type size, line length, and spacing had not been replicated for screens, and notes confounds in the available studies. This is a design convention, not a demonstrated scaling formula for screen CSS. [Review](https://doi.org/10.1080/01449290410001715714)
- **Opinion / preference:** There is no source-grounded basis here for calling one exact `rem` size or unitless `line-height` optimal at 76ch. Preference can guide the specimen comparison, but should be labeled as such.

## Limits

The 2013 sample was specifically people with dyslexia and the study used only the first three paragraphs of web articles; its point sizes cannot be translated directly into CSS pixels without controlling display scale and viewing conditions. The 2023 study used short English passages, a monospaced face, and a laboratory eye-tracking setup; its fixation measures are not a direct test of comprehension or sustained legal reading. The 2004 review describes older screen studies and highlights methodological gaps. None tests interactions between this site's wide measure and leading, so the claim that wider measures require wider leading remains unproven for this use.

## CSS implication

Keep body size and line-height as separate variables in the later specimen. At the site's wide measure, compare the current values with a modestly larger body size and a modestly more open leading while holding face, measure, and passage constant. Treat the comparison as a preference-led design test: studies support avoiding cramped text and justify testing more open leading, but they do not determine a numeric CSS value or require line-height to grow with measure. Preserve reader zoom and browser text resizing.

## Sources

- Rello, Pielot, Marcos, and Carlini, “Size Matters (Spacing not): 18 Points for a Dyslexic-friendly Wikipedia,” W4A 2013. [Author-hosted paper](https://pielot.org/pubs/Rello2013-W4A-SizeMatters.pdf)
- Vasilev et al., “The role of visual crowding in eye movements during reading: Effects of text spacing,” 2023. [Full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC10600290/)
- Dyson, “How physical text layout affects reading from screen,” *Behaviour & Information Technology* 23(6), 2004. [Publisher record](https://doi.org/10.1080/01449290410001715714)
