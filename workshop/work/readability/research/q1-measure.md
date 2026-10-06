# Finding

The strongest direct screen study here supports a medium measure near 55 characters per line for sustained reading, with no basis for treating 76 CSS `ch` as 76 characters. NN/G’s 50–75-character range is a useful expert convention, not a replicated universal optimum. At 19px, 76ch may be visually comfortable in this serif, but the cited evidence cannot establish that: measure must be counted in the rendered face and tested in the specimen.

# Evidence and quality

- **Controlled study — Dyson & Haselgrove (2001).** The experiment varied screen lines of 25, 55, and 100 characters and reading at normal or fast speeds. The authors report that 55-character lines produced the highest comprehension and were read faster than short lines; 55 also outperformed 100 on comprehension. This is direct evidence for a medium measure, but only at the tested points, not a test of a 50–75 band or a 76-character cutoff. [Article and abstract](https://www.sciencedirect.com/science/article/pii/S1071581901904586).
- **Expert convention — Nielsen Norman Group.** Its chunking guidance says short lines are “around 50–75 characters,” alongside short paragraphs and visual hierarchy. It offers this as a practical scannability convention, not a reported controlled line-length experiment. [NN/G guidance](https://www.nngroup.com/articles/chunking/).
- **Controlled perceptual research — Legge et al. (2007).** Their work defines visual span as the horizontal set of letters that can be recognized reliably without eye movement and examines its relationship to reading speed. Experiments use small samples (including five young adults per experiment) and RSVP/letter-recognition tasks; they do not compare paragraph column widths or recommend a characters-per-line range. It supplies a mechanism, not a width target. [Journal of Vision paper](https://legge.psych.umn.edu/sites/legge.psych.umn.edu/files/2020-08/Legge%20Cheung%20Yu%20Chung%20Lee%20Owens%202007%20The%20case%20for%20the%20visual%20span%20as%20a%20sensory%20bottleneck%20in%20reading.pdf).
- **Controlled web-reading experiment — Rello, Pielot & Marcos (2016).** With 104 participants reading Wikipedia articles in Arial on a 17-inch monitor, the study varied 10–26 point type and 0.8–1.8 line spacing. It found no line-length effect because it did not manipulate line length. It therefore cannot validate 76ch or a serif-specific measure. [CHI paper](https://www.pielot.org/pubs/Rello2016-Fontsize.pdf).
- **Field data:** none of these named sources provides large-scale field data establishing an optimal line length for this use.

# Limits

Dyson’s three tested lengths are coarse and its result does not identify a continuous optimum. The NN/G recommendation is practical guidance rather than a controlled estimate. Legge’s visual-span work concerns letter recognition and eye movements, while Rello et al. focus on font size and line spacing in Arial. Neither transfers directly to a 19px reading serif or Portuguese legal prose. No named source tests this typeface, this population, or this CSS measure.

CSS `ch` is based on the advance width of the font’s “0” glyph, not a promise that a line holds that number of proportional characters. Actual character count varies with the face and text. A 76ch declaration therefore cannot be compared numerically with Dyson’s 55 characters per line without measuring rendered text.

# CSS implication

Treat 50–75 rendered characters per line as a comparison range, with roughly 55 as the evidence-led starting point for a specimen variant. Keep 76ch as the current comparison condition; measure its actual average and maximum characters per line in the reading serif at 19px. The specimen should let the chairman compare the current width with a narrower condition before any site-wide recommendation.

# Sources

- Dyson, M. C. & Haselgrove, M. (2001), “The influence of reading speed and line length on the effectiveness of reading from screen,” *International Journal of Human-Computer Studies* 54(4), 585–612. [Publisher record](https://www.sciencedirect.com/science/article/pii/S1071581901904586).
- Legge, G. E. et al. (2007), “The case for the visual span as a sensory bottleneck in reading,” *Journal of Vision* 7(2):9. [Full paper](https://legge.psych.umn.edu/sites/legge.psych.umn.edu/files/2020-08/Legge%20Cheung%20Yu%20Chung%20Lee%20Owens%202007%20The%20case%20for%20the%20visual%20span%20as%20a%20sensory%20bottleneck%20in%20reading.pdf).
- Rello, L., Pielot, M. & Marcos, M.-C. (2016), “Make It Big! The Effect of Font Size and Line Spacing on Online Readability,” CHI ’16. [Full paper](https://www.pielot.org/pubs/Rello2016-Fontsize.pdf).
- Nielsen Norman Group, “How Chunking Helps Content Processing.” [Guidance](https://www.nngroup.com/articles/chunking/).
