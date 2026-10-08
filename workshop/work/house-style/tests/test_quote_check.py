#!/usr/bin/env python3
"""Plain-assert tests for quote_check.py. Run: python3 work/house-style/tests/test_quote_check.py"""
import io, sys
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import quote_check as qc

FX = HERE / "quote_fixtures"
corpus = qc.Corpus(FX / "corpus")

# normalization: hyphenation, page marker, footnote digit, quote marks, case
assert "instrumento; 2 a demanda" in corpus.texts["plain"][0]
assert "fatos jurídicos" in corpus.texts["plain"][0], "page marker + hyphen break must join"
assert qc.locate(corpus, "o seu instrumento; a demanda é o conteúdo")[0] == "no-digits"

# known-good page: passes, nothing unmatched, exam block is a warning only
fails, warns, n = qc.check_page(FX / "good.html", corpus)
assert not fails, fails
assert n == 6, n  # 1 + 2 + 2 + 1 exam segment; the 2-word quote is under the 6-word floor
assert any("unverifiable" in w for w in warns), warns
assert not any("cut without" in w for w in warns), warns

# known-bad page: invented quote fails, silent parenthetical cut and silent paragraph skip warn
fails, warns, n = qc.check_page(FX / "bad.html", corpus)
assert len(fails) == 1 and "o juiz sempre pode alterar" in fails[0], fails
assert any("cut without" in w and "a causa de pedir" in w for w in warns), warns
assert any("cut without" in w and "primeira frase" in w for w in warns), warns

# CLI exit codes
args = ["--corpus", str(FX / "corpus")]
with redirect_stdout(io.StringIO()):
    assert qc.main([str(FX / "good.html")] + args) == 0
    assert qc.main([str(FX / "bad.html")] + args) == 1

print("test_quote_check: all passed")
