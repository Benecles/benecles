# Finding

Use a small, consistent gap between prose paragraphs and no first-line indent in the web specimen. The research located here does not establish that spacing is universally easier than indentation: Frase and Schwartz tested meaningfully segmented sentences and indentation, not paragraph-gap spacing against first-line indents. Their five experiments (72 adult participants) found faster sentence-verification responses for meaningfully segmented and indented text than standard text, while indentation added no significant response-time benefit once the text was meaningfully segmented ([primary study, *Journal of Educational Psychology*, 1979](https://doi.org/10.1037/0022-0663.71.2.197)). That supports clear grouping as a design aim, not a particular web paragraph style.

For ordinary prose on screen, prefer left alignment with a ragged right edge as the conservative default. In two experiments, Trollip and Sales found slower reading of computer-generated fill-justified passages, with no detected comprehension difference ([primary study, *Human Factors*, 1986](https://doi.org/10.1177/001872088602800204)). The result is not universal: an eight-experiment sequence found no general reading difference among justification methods ([primary study, *Information & Management*, 1998](https://doi.org/10.1016/S0378-7206(98)00059-7)); a review likewise reports mixed findings and cautions against definitive generalization ([Lonsdale, 2014 review of typographic-feature evidence](https://eprints.whiterose.ac.uk/id/eprint/82895/11/VisibleLanguage-48-3_28-67-Lonsdale-TypeFeatures.pdf)).

`text-wrap: pretty` is a layout hint: the browser may use a slower wrapping algorithm to improve line endings and reduce orphans; it does not guarantee widow/orphan control. CSS behavior is browser-specific ([MDN property reference and compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap), [CSS Text Level 4 draft](https://drafts.csswg.org/css-text-4/#text-wrap)). `hyphens: auto` relies on a correctly declared language and an available language dictionary; exact breaks can vary by browser ([MDN `hyphens` reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)). Portuguese dictionary support is present in current major browser families but differs by browser and version ([compatibility table for Portuguese dictionaries](https://caniuse.com/mdn-css_properties_hyphens_language_portuguese)).

# Evidence and quality

- **Controlled study, limited transfer:** Frase and Schwartz (1979) used five sentence-verification experiments with 72 adults reading technical passages. The manipulation concerned meaningful phrase segmentation and indentation. It did not compare paragraph spacing with paragraph indentation, and it did not study web reading. The paper itself says line length and margin justification had minor cognitive relevance in that task ([study](https://doi.org/10.1037/0022-0663.71.2.197)).
- **Controlled study, computer-generated text:** Trollip and Sales (1986) compared fill-justified text, produced with variable word spaces, with ragged-right text. They report slower reading for justified text and no comprehension difference ([study](https://doi.org/10.1177/001872088602800204); [PubMed record](https://pubmed.ncbi.nlm.nih.gov/3733103/)).
- **Controlled studies, conflicting result:** Coll, Fjermestad, and Coll's eight-experiment sequence found no overall difference among justification techniques, tempering a blanket claim for ragged-right text ([study](https://doi.org/10.1016/S0378-7206(98)00059-7)).
- **Review, not a new experiment:** Lonsdale summarizes mixed alignment results and notes limitations in sample sizes and generalizability; it describes rivers and excessive hyphenation as practical typography concerns rather than a settled universal comprehension effect ([review PDF](https://eprints.whiterose.ac.uk/id/eprint/82895/11/VisibleLanguage-48-3_28-67-Lonsdale-TypeFeatures.pdf)).
- **Browser documentation, not readability evidence:** MDN describes `pretty` as favoring layout over speed and `hyphens: auto` as dependent on language and dictionary support. Compatibility tables are version-specific, so the CSS should degrade safely ([`text-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap); [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens); [Portuguese dictionary support](https://caniuse.com/mdn-css_properties_hyphens_language_portuguese)).
- **Expert convention/opinion:** Choosing modest paragraph spacing for a web specimen is a convention-led visual choice for making paragraph boundaries apparent. These studies do not prove it superior to indents, nor set a best spacing value.

# Limits

The retrieved evidence does not directly test paragraph gap versus first-line indent in Brazilian Portuguese long-form web prose. The indentation experiment's task and text type differ from sustained legal reading, while the justification studies use older typesetting and participant contexts. Evidence does not support saying ragged-right always improves comprehension or that automatic hyphenation improves readability. `pretty` is an appearance feature, not an experimentally established comprehension intervention. Neither CSS property guarantees identical behavior across browsers.

# CSS implication

For the specimen only, signal each paragraph with modest bottom margin and `text-indent: 0`; avoid stacking a full blank line on top of the existing leading. Keep prose `text-align: left`. Treat hyphenation as optional progressive enhancement, with the document language set to `pt-BR`; test actual breaks in target browsers before adopting it. `text-wrap: pretty` may be declared as progressive enhancement, with ordinary wrapping as fallback; do not describe it as a widow/orphan guarantee. These are specimen hypotheses for comparison, not a site-wide recommendation.

```css
.prosa p {
  text-align: left;
  text-indent: 0;
  margin-block: 0 0.65em; /* specimen value, not a research-derived threshold */
  hyphens: auto;
}
.prosa {
  text-wrap: pretty;
}
```

# Sources

1. Frase, L. T., & Schwartz, B. J. (1979). “Typographical Cues That Facilitate Comprehension.” *Journal of Educational Psychology*, 71(2), 197–206. [https://doi.org/10.1037/0022-0663.71.2.197](https://doi.org/10.1037/0022-0663.71.2.197)
2. Trollip, S. R., & Sales, G. (1986). “Readability of Computer-Generated Fill-Justified Text.” *Human Factors*, 28(2), 159–163. [https://doi.org/10.1177/001872088602800204](https://doi.org/10.1177/001872088602800204)
3. Coll, J. H., Fjermestad, J., & Coll, R. (1998). “An eight experiment sequence to determine reading equality.” *Information & Management*, 34(4), 231–242. [https://doi.org/10.1016/S0378-7206(98)00059-7](https://doi.org/10.1016/S0378-7206(98)00059-7)
4. Lonsdale, M. (2014). “Typographic Features of Text: Outcomes from Research and Practice.” *Visible Language*, 48(3), 29–67. [PDF](https://eprints.whiterose.ac.uk/id/eprint/82895/11/VisibleLanguage-48-3_28-67-Lonsdale-TypeFeatures.pdf)
5. MDN contributors. “text-wrap.” [Reference and browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap).
6. MDN contributors. “hyphens.” [Reference and browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens).
7. Can I Use. “CSS property: hyphens: Hyphenation dictionary for Portuguese.” [Versioned browser support table](https://caniuse.com/mdn-css_properties_hyphens_language_portuguese).
