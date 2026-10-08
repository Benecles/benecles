#!/usr/bin/env python3
"""Compare candidate Portuguese legal prose with staged lesson-page proxies.

Uses only the Python standard library. Results are descriptive corpus contrasts,
not an authorship detector or a claim that either corpus is representative.
"""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[2]
EXTRACTS = ROOT / "work/controle-depth/extracts"
STAGING = ROOT / "work/staging/courses"
REPORT = ROOT / "work/slop-bench/report.md"
TOKEN_RE = re.compile(r"[^\W_]+(?:['’][^\W_]+)?", re.UNICODE)

# Concrete Portuguese constructions to inspect. These are exploratory queries,
# not claims that any construction is undesirable or diagnostic of authorship.
CONSTRUCTIONS = (
    "não apenas", "não só", "mais do que", "não se trata de",
    "nesse sentido", "diante desse cenário", "é importante destacar",
    "vale destacar", "em outras palavras", "por outro lado",
    "de um lado", "de outro lado", "em suma", "portanto",
    "assim,", "cabe observar", "cumpre destacar", "sob essa perspectiva",
)


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.hidden_depth = 0
        self.stack = []
        self.parts = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        hidden = tag in {"script", "style", "noscript", "template"}
        hidden |= "hidden" in attrs or attrs.get("aria-hidden", "").lower() == "true"
        hidden |= "display:none" in attrs.get("style", "").replace(" ", "").lower()
        void = tag in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
        effective_hidden = bool(self.hidden_depth or hidden)
        if not void:
            self.stack.append((tag, effective_hidden))
        if effective_hidden and not void:
            self.hidden_depth += 1

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                removed = self.stack[i:]
                del self.stack[i:]
                self.hidden_depth -= sum(1 for _, hidden in removed if hidden)
                break

    def handle_data(self, data):
        if not self.hidden_depth:
            self.parts.append(data)


def html_visible_text(raw):
    parser = VisibleText()
    parser.feed(raw)
    return " ".join(parser.parts)


def tokens(text):
    return [unicodedata.normalize("NFC", m.group(0)).casefold() for m in TOKEN_RE.finditer(text)]


def counters(words):
    result = {1: Counter(), 2: Counter(), 3: Counter()}
    for n in result:
        result[n].update(" ".join(words[i:i+n]) for i in range(max(0, len(words)-n+1)))
    return result


def read_corpora():
    refs = sorted(EXTRACTS.glob("*.txt"))
    pages = sorted(STAGING.glob("*/aula-*.html"))
    if not refs or not pages:
        raise SystemExit(f"Missing inputs: {len(refs)} extracts, {len(pages)} pages")
    ref_text = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in refs)
    page_text = "\n".join(html_visible_text(p.read_text(encoding="utf-8", errors="replace")) for p in pages)
    return refs, pages, tokens(ref_text), tokens(page_text)


def freq(counter, total, term):
    return counter[term] * 10000 / total if total else 0


def fmt_num(n):
    return f"{n:,}".replace(",", " ")


def main():
    refs, pages, ref_words, target_words = read_corpora()
    rc, tc = counters(ref_words), counters(target_words)
    constructions = []
    ref_text = " ".join(ref_words)
    target_text = " ".join(target_words)
    for phrase in CONSTRUCTIONS:
        phrase = " ".join(tokens(phrase))
        a, b = ref_text.count(phrase), target_text.count(phrase)
        constructions.append((phrase, a, b))

    lines = [
        "# SLOP-2 local corpus discovery",
        "",
        "## Scope and provenance",
        "",
        "This is a descriptive comparison of the available Portuguese legal book extracts (reference-candidate set) and visible text from staged lesson HTML pages (target-corpus proxies). The staged pages have unknown writer labels and are **not confirmed model generations**. The extracts are not a matched human control set, and no causal or authorship inference is supported.",
        "",
        "Fresh samples from 30 tasks/models were not supplied. The requested 200,000-token threshold is therefore **not met or validated**; counts below are word-token counts from these files and do not establish any token threshold.",
        "",
        "## Measured corpus",
        "",
        f"- Reference candidates: {len(refs)} `.txt` extracts; {fmt_num(len(ref_words))} word tokens.",
        f"- Target proxies: {len(pages)} `aula-*.html` pages; {fmt_num(len(target_words))} visible-text word tokens.",
        f"- Reference tokenization: Unicode letter/number words, case-folded; HTML visible text excludes script/style/template/noscript and `aria-hidden` content. Navigation and other reader-visible labels remain included.",
        "",
        "## Construction queries",
        "",
        "Rates are occurrences per 10,000 word tokens. Ratios compare target rate/reference rate; `∞` means no occurrence in the reference candidate set, not proof of target-specific style. Repeated phrase occurrences can overlap.",
        "",
        "| Construction | Reference count | Target count | Ref / 10k | Target / 10k | Target ÷ ref |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for phrase, a, b in constructions:
        ar, br = a * 10000 / len(ref_words), b * 10000 / len(target_words)
        ratio = "∞" if a == 0 and b else (f"{br/ar:.2f}×" if ar else "—")
        lines.append(f"| `{phrase}` | {a} | {b} | {ar:.2f} | {br:.2f} | {ratio} |")

    lines += ["", "## Most overrepresented observed words", "",
              "Top 30 words with at least 10 target occurrences and a nonzero reference rate, ranked by target/reference rate ratio.",
              "", "| Word | Ref count | Target count | Ref / 10k | Target / 10k | Ratio |", "|---|---:|---:|---:|---:|---:|"]
    word_candidates = []
    for word, b in tc[1].items():
        if b < 10:
            continue
        a = rc[1][word]
        if a == 0:
            continue
        ar, br = freq(rc[1], len(ref_words), word), freq(tc[1], len(target_words), word)
        word_candidates.append((br/ar, word, a, b, ar, br))
    for ratio, word, a, b, ar, br in sorted(word_candidates, reverse=True)[:30]:
        lines.append(f"| `{word}` | {a} | {b} | {ar:.2f} | {br:.2f} | {ratio:.2f}× |")
    if not word_candidates:
        lines.append("| _No words met the display criteria._ | | | | | |")

    lines += ["", "## Most overrepresented observed n-grams", "",
              "Top 30 observed bigrams/trigrams with at least 5 target occurrences and a nonzero reference rate, ranked by target/reference rate ratio. Counts and rates are shown because high ratios can arise from small baselines. This ranking is a review queue, not a quality score.",
              "", "| n-gram | n | Ref count | Target count | Ref / 10k | Target / 10k | Ratio |", "|---|---:|---:|---:|---:|---:|---:|"]
    candidates = []
    for n in (2, 3):
        for gram, b in tc[n].items():
            if b < 5:
                continue
            a = rc[n][gram]
            if a == 0:
                continue
            ar, br = freq(rc[n], len(ref_words), gram), freq(tc[n], len(target_words), gram)
            candidates.append((br/ar, gram, n, a, b, ar, br))
    for ratio, gram, n, a, b, ar, br in sorted(candidates, reverse=True)[:30]:
        lines.append(f"| `{gram}` | {n} | {a} | {b} | {ar:.2f} | {br:.2f} | {ratio:.2f}× |")
    if not candidates:
        lines.append("| _No n-grams met the display criteria._ | | | | | | |")

    lines += ["", "## Limitations", "",
              "- Corpus sizes, topics, document types, and source-selection processes differ; term distribution is not controlled for lesson topic or legal subject.",
              "- Staged HTML pages may include headings, navigation, captions, and interface labels. The extraction counts rendered text nodes, not browser-computed visibility for CSS classes or external stylesheets.",
              "- Reference extracts may contain OCR/extraction artifacts and represent only the listed files, not Portuguese legal prose generally.",
              "- Counts are corpus-level observations. They do not identify authors, measure quality, or justify banning any phrase; legal and pedagogical context requires human review.",
              "- Word-token counts are not model-token counts. The 200k model-token requirement cannot be inferred from them.",
              "",
              "## Reproduction",
              "",
              "From the repository root run:",
              "", "```sh", "python3 work/slop-bench/corpus_discovery.py", "```", "",
              "The script uses only Python standard-library modules and rewrites this report from the current input files.", ""]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {REPORT.relative_to(ROOT)} ({len(refs)} reference files, {len(pages)} target pages, {len(ref_words)} / {len(target_words)} word tokens)")


if __name__ == "__main__":
    main()
