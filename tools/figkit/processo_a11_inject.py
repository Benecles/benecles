"""Page-specific Aula 11 figure integration; leaves the native docket intact.

Run directly: python3 tools/figkit/processo_a11_inject.py PATH_TO_AULA_11_HTML
The contract inserts the two panels after the one existing docket figure and
is idempotent. It deliberately does not load the global all-pages injector.
"""

from pathlib import Path
import re
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from processo_a11 import EXAM_THREAD, SOURCE, panels


DOCKET_OPEN = '<figure class="docket-figure" aria-labelledby="docket-caption">'
BEGIN = '<!-- figkit:a11:begin -->'
END = '<!-- figkit:a11:end -->'


def inject(path):
    path = Path(path)
    source = path.read_text(encoding="utf-8")
    if source.count(DOCKET_OPEN) != 1:
        raise ValueError(f"expected exactly one native Aula 11 docket in {path}")
    start = source.index(DOCKET_OPEN)
    end = source.find("</figure>", start)
    if end < 0:
        raise ValueError("native Aula 11 docket is unclosed")
    docket_end = end + len("</figure>")
    first, second = panels()
    generated = (f'{BEGIN}<style>.a11-figure-pair{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:22px;margin:30px auto}}'
                 '.a11-figure-pair .figure-sheet{margin:0;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major);padding:16px}'
                 '.a11-figure-pair svg{display:block;width:100%;height:auto}.a11-figure-pair figcaption{margin:12px 0 0;font:15px/1.45 var(--serif);color:var(--ink)}'
                 '</style>'
                 f'<div class="wide a11-figure-pair" data-exam-thread="{EXAM_THREAD}">'
                 f'<figure class="figure-sheet">{first}<figcaption>Se Dalvo for considerado parte ilegítima, a cobrança proposta por Jesse continua em relação a Serotonina.</figcaption></figure>'
                 f'<figure class="figure-sheet">{second}<figcaption>A resposta da P2 de 2015 classifica os dois devedores solidários como litisconsortes simples e facultativos, com posições processuais autônomas.</figcaption></figure>'
                 f'<span class="src" hidden data-src="{SOURCE}" data-exam-thread="{EXAM_THREAD}"></span>'
                 f'</div>{END}')
    existing = re.search(re.escape(BEGIN) + r'.*?' + re.escape(END), source, re.S)
    if existing:
        result = source[:existing.start()] + generated + source[existing.end():]
    else:
        result = source[:docket_end] + generated + source[docket_end:]
    path.write_text(result, encoding="utf-8")
    return 2


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: processo_a11_inject.py PATH_TO_AULA_11_HTML")
    print(f"{sys.argv[1]}: {inject(sys.argv[1])} figures")
