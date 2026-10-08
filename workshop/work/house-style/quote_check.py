#!/usr/bin/env python3
"""quote_check.py: every quoted passage in a .fonte block must exist verbatim in the course corpus.

Ruling 14 (work/briefs/2026-10-07-processo-r2-decisions.md): quotes are pasted by script, cuts are
marked "[...]". For each page this finds every <aside|div class="fonte ..."> with a <blockquote>,
splits each quote on "[...]" / "[…]", and looks up every segment of 6+ words in the corpus after
normalization (unescape, strip tags, NFC, lowercase, page markers, OCR hyphenation, quote marks,
whitespace; a second pass also drops standalone 1-3 digit tokens, i.e. OCR'd footnote calls).

FAIL  a segment of 6+ words is not in the corpus.
WARN  "cut without [...]": a segment is only found as pieces with words missing between them, or two
      adjacent segments not separated by "[...]" sit 4+ words apart in the source.
WARN  "Questão de prova" blocks with no match (two-column exam OCR interleaves words: unverifiable).

Usage: quote_check.py PAGE.html [PAGE.html ...] [--corpus DIR]
Default corpus: work/pipeline/<course>/chapters (recursive *.txt), <course> from courses/<course>/...
Exit 1 on any FAIL.
"""
import argparse, html, re, sys, unicodedata
from pathlib import Path

WORKSHOP = Path(__file__).resolve().parents[2]
MIN_WORDS = 6
GAP_WARN = 4          # words of source skipped without a marker
CHAIN_WINDOW = 120    # max words between pieces/segments still read as one passage

PAGE_MARK = re.compile(r"=+\s*p\.\s*[\divxlc]+[^=\n]*=+", re.I)
HYPHEN_BREAK = re.compile(r"(\w)[-­‐‑][ \t]*\r?\n\s*(\w)")
QUOTES = re.compile("[\"'“”„‟‘’‚‛«»‹›`´]")
DIGITS = re.compile(r"(?<!\S)\d{1,3}(?!\S)")
ELLIPSIS = re.compile(r"\[\s*(?:\.\s*\.\s*\.|…)\s*\]")
TAG = re.compile(r"<[^>]+>")


def base_norm(s, is_html=False):
    if is_html:
        s = re.sub(r"</p\s*>|<br\s*/?>", "\n", s, flags=re.I)
        s = TAG.sub("", s)
        s = html.unescape(s)
    s = unicodedata.normalize("NFC", s)
    s = PAGE_MARK.sub(" ", s)
    s = HYPHEN_BREAK.sub(r"\1\2", s)
    s = s.lower().replace(" ", " ").replace("­", "")
    s = QUOTES.sub("", s)
    return " ".join(s.split())


# variants, tried in order; each applied identically to corpus and quote
VARIANTS = [
    ("plain", lambda s: s),
    ("no-digits", lambda s: " ".join(DIGITS.sub(" ", s).split())),
    ("no-digits-no-hyphen", lambda s: " ".join(DIGITS.sub(" ", s).replace("-", "").split())),
]


class Corpus:
    def __init__(self, root):
        files = sorted(Path(root).rglob("*.txt"))
        if not files:
            sys.exit(f"quote_check: no *.txt under {root}")
        self.names = [str(f.relative_to(root)) for f in files]
        base = [base_norm(f.read_text(encoding="utf-8", errors="replace")) for f in files]
        self.texts = {name: [fn(t) for t in base] for name, fn in VARIANTS}

    def find(self, variant, needle, file_i=None, start=0):
        """Return (file index, char start, char end) of first occurrence, or None."""
        texts = self.texts[variant]
        rng = [file_i] if file_i is not None else range(len(texts))
        for i in rng:
            p = texts[i].find(needle, start if file_i is not None else 0)
            if p >= 0:
                return i, p, p + len(needle)
        return None

    def words_between(self, variant, i, a, b):
        return len(self.texts[variant][i][a:b].split())


def fonte_blocks(page):
    """Yield (header text, [quote html, ...]) for every .fonte element holding a blockquote."""
    for m in re.finditer(r"<(aside|div)\b[^>]*\bclass=\"([^\"]*)\"[^>]*>", page):
        if "fonte" not in m.group(2).split():
            continue
        tag, depth, pos = m.group(1), 1, m.end()
        opener, closer = re.compile(rf"<{tag}\b", re.I), re.compile(rf"</{tag}\s*>", re.I)
        while depth:
            o, c = opener.search(page, pos), closer.search(page, pos)
            if not c:
                break
            if o and o.start() < c.start():
                depth, pos = depth + 1, o.end()
            else:
                depth, pos = depth - 1, c.end()
        body = page[m.end():pos]
        quotes = re.findall(r"<blockquote\b[^>]*>(.*?)</blockquote>", body, re.S | re.I)
        if not quotes:
            continue
        h = re.search(r"<header\b[^>]*>(.*?)</header>", body, re.S | re.I)
        header = " ".join(html.unescape(TAG.sub(" ", h.group(1))).split()) if h else "(no header)"
        line = page.count("\n", 0, m.start()) + 1
        yield line, header, quotes


def segments(quote_html):
    """Split a blockquote into segments. Returns [(text, joined_to_previous_without_marker)]."""
    out = []
    paras = re.findall(r"<p\b[^>]*>(.*?)</p>", quote_html, re.S | re.I) or [quote_html]
    marker_pending = False
    for para in paras:
        parts = ELLIPSIS.split(para)
        for k, part in enumerate(parts):
            t = base_norm(part, is_html=True).strip(" .;,:")
            joined = bool(out) and k == 0 and not marker_pending
            marker_pending = False
            if not t:
                marker_pending = True if k else marker_pending
                continue
            out.append((t, joined))
        if ELLIPSIS.search(para.rstrip()[-12:] if para else ""):
            marker_pending = True
    return out


def locate(corpus, seg):
    for name, fn in VARIANTS:
        n = fn(seg)
        hit = corpus.find(name, n)
        if hit:
            return name, hit
    return None


def pieces(corpus, seg):
    """Greedy split of an unmatched segment into in-order corpus pieces. Returns gaps list or None."""
    for name, fn in VARIANTS:
        words = fn(seg).split()
        texts = corpus.texts[name]
        for i in range(len(texts)):
            k, pos, gaps, ok = 0, 0, [], True
            first = True
            while k < len(words):
                # longest prefix of words[k:] present in file i at/after pos (binary search: monotone)
                lo, hi, best = 1, len(words) - k, None
                while lo <= hi:
                    mid = (lo + hi) // 2
                    p = texts[i].find(" ".join(words[k:k + mid]), pos)
                    if p >= 0:
                        best, lo = (mid, p), mid + 1
                    else:
                        hi = mid - 1
                if not best or (best[0] < 3 and k + best[0] < len(words)):
                    ok = False
                    break
                n, p = best
                if not first:
                    gap = corpus.words_between(name, i, pos, p)
                    if gap > CHAIN_WINDOW:
                        ok = False
                        break
                    gaps.append(gap)
                first = False
                pos = p + len(" ".join(words[k:k + n]))
                k += n
            if ok and gaps:
                return gaps
    return None


def check_page(path, corpus):
    page = Path(path).read_text(encoding="utf-8")
    fails, warns, checked = [], [], 0
    for line, header, quotes in fonte_blocks(page):
        exam = "questão de prova" in header.lower()
        label = f"L{line} [{header}]"
        for q in quotes:
            prev = None   # (variant, file, end) of previous located segment
            for seg, joined in segments(q):
                if len(seg.split()) < MIN_WORDS:
                    prev = None
                    continue
                checked += 1
                hit = locate(corpus, seg)
                if hit:
                    variant, (fi, a, b) = hit
                    if joined and prev and prev[0] == variant and prev[1] == fi:
                        nxt = corpus.find(variant, dict(VARIANTS)[variant](seg), fi, prev[2])
                        if nxt:
                            gap = corpus.words_between(variant, fi, prev[2], nxt[1])
                            if GAP_WARN <= gap <= CHAIN_WINDOW:
                                warns.append(f"{label} cut without [...]: {gap} source words skipped before “{seg[:60]}”")
                    prev = (variant, fi, b)
                    continue
                prev = None
                gaps = pieces(corpus, seg)
                if gaps and max(gaps) >= GAP_WARN:
                    warns.append(f"{label} cut without [...]: source words skipped {gaps} inside “{seg[:120]}”")
                elif gaps:
                    pass  # tiny drift (<4 words): treat as match
                elif exam:
                    warns.append(f"{label} unverifiable (exam OCR): “{seg[:120]}”")
                else:
                    fails.append(f"{label} not in corpus: “{seg[:120]}”")
    return fails, warns, checked


def infer_course(path):
    parts = Path(path).resolve().parts
    if "courses" in parts and parts.index("courses") + 1 < len(parts):
        return parts[parts.index("courses") + 1]
    sys.exit(f"quote_check: cannot infer course from {path}; pass --corpus")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pages", nargs="+")
    ap.add_argument("--corpus")
    a = ap.parse_args(argv)
    cache, bad = {}, False
    for page in a.pages:
        root = a.corpus or str(WORKSHOP / "work/pipeline" / infer_course(page) / "chapters")
        if root not in cache:
            cache[root] = Corpus(root)
        fails, warns, n = check_page(page, cache[root])
        print(f"{'FAIL' if fails else 'PASS'} {page} ({n} segments checked, {len(fails)} unmatched, {len(warns)} warnings)")
        for f in fails:
            print("  FAIL", f)
        for w in warns:
            print("  WARN", w)
        bad |= bool(fails)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
