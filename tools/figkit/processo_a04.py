"""Processo Civil I · Aula 04: read the admission and regime tests in the CPC."""
from pathlib import Path
import os

import figkit


ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "courses" / "processo-civil-i" / "aula-04.html"


def panel():
    """One statute sheet with the operative clauses from CPC arts. 119 and 124."""
    return '''<figure id="pci-a04-statute" class="panel on a04-statute" aria-label="Texto dos arts. 119 e 124 do Código de Processo Civil, com as cláusulas de ingresso e de classificação da assistência destacadas">
<style>
#pci-a04-statute.panel{position:relative;inset:auto;opacity:1;transition:none;width:100%;height:auto;aspect-ratio:auto;max-height:none}#pci-a04-statute{display:block;width:100%;max-width:none;aspect-ratio:auto;max-height:none;margin:0;position:relative;overflow:visible;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major);color:var(--ink)}
#pci-a04-statute .a04-sheet{padding:clamp(16px,2vw,25px) clamp(16px,2.4vw,30px) 14px}
#pci-a04-statute .a04-heading{display:flex;justify-content:space-between;gap:8px 16px;flex-wrap:wrap;padding-bottom:10px;border-bottom:1.5px solid var(--ink);font:600 10px/1.45 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
#pci-a04-statute .a04-section{margin-top:14px}
#pci-a04-statute .a04-section+.a04-section{padding-top:14px;border-top:1px solid var(--grid-major)}
#pci-a04-statute .a04-label{display:block;margin-bottom:5px;font:600 9.5px/1.4 var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--conc)}
#pci-a04-statute .a04-label.regime{color:var(--dif)}
#pci-a04-statute .a04-number{margin:0 0 5px;font:700 11px/1.35 var(--mono);letter-spacing:.08em;color:var(--ink-2)}
#pci-a04-statute p{max-width:none;margin:0;font:400 clamp(15px,1.18vw,18px)/1.5 var(--serif);color:var(--ink)}
#pci-a04-statute .a04-sole{margin-top:9px;padding-top:8px;border-top:1px solid var(--grid)}
#pci-a04-statute .a04-par{font:600 10px/1.4 var(--mono);letter-spacing:.04em;text-transform:uppercase;color:var(--ink-2)}
#pci-a04-statute .a04-focus{padding:0 .04em;-webkit-box-decoration-break:clone;box-decoration-break:clone;font-weight:600}
#pci-a04-statute .a04-entry{background:var(--conc-wash);box-shadow:inset 0 -.08em 0 var(--conc)}
#pci-a04-statute .a04-regime{background:var(--dif-wash);box-shadow:inset 0 -.08em 0 var(--dif)}
#pci-a04-statute .a04-case{margin-top:12px;padding-top:9px;border-top:1px solid var(--grid-major);font:600 9.5px/1.45 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2)}
#pci-a04-statute figcaption{position:static;display:block;padding:8px 12px;border:0;border-top:1px solid var(--ink);background:var(--paper-2);font:500 9.5px/1.45 var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--ink-2)}
@media(max-width:560px) and (orientation:portrait){#pci-a04-statute .a04-sheet{padding:15px 14px 12px}#pci-a04-statute .a04-section{margin-top:12px}#pci-a04-statute .a04-section+.a04-section{padding-top:12px}}
@media(prefers-reduced-motion:reduce){#pci-a04-statute .a04-focus{transition:none}}
</style>
<div class="a04-sheet">
  <div class="a04-heading"><span>Código de Processo Civil</span><span>Intervenção de terceiros</span></div>
  <section class="a04-section" aria-labelledby="pci-a04-art119">
    <span class="a04-label">Requisito de ingresso</span>
    <h4 class="a04-number" id="pci-a04-art119">Art. 119</h4>
    <p>Pendendo causa entre 2 (duas) ou mais pessoas, o <span class="a04-focus a04-entry">terceiro juridicamente interessado</span> em que a <span class="a04-focus a04-entry">sentença seja favorável a uma delas</span> poderá intervir no processo para assisti-la.</p>
    <p class="a04-sole"><span class="a04-par">Parágrafo único.</span> A assistência será admitida em qualquer procedimento e em todos os graus de jurisdição, recebendo o assistente o processo no estado em que se encontre.</p>
  </section>
  <section class="a04-section" aria-labelledby="pci-a04-art124">
    <span class="a04-label regime">Relação que define o regime</span>
    <h4 class="a04-number" id="pci-a04-art124">Art. 124</h4>
    <p>Considera-se litisconsorte da parte principal o assistente sempre que a <span class="a04-focus a04-regime">sentença influir na relação jurídica</span> entre ele e o <span class="a04-focus a04-regime">adversário do assistido</span>.</p>
  </section>
  <div class="a04-case">RE 550.769 QO/RJ · SINDIFUMO · 28 fev. 2008</div>
</div>
<figcaption>Fig. 1 · CPC · arts. 119 e 124</figcaption>
</figure>'''


def specimen_page():
    css = (ROOT / "courses" / "processo-civil-i" / "assets" / "curso.css").as_uri()
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Figkit · Processo Civil Aula 04</title><link rel="stylesheet" href="{css}">
<style>body{{max-width:1083px;margin:0 auto;padding:28px 18px 60px;background:var(--paper);color:var(--ink)}}h1{{font:750 28px/1.1 var(--sans)}}.probe-note{{max-width:70ch;font:16px/1.5 var(--serif);color:var(--ink-2)}}#pci-a04-statute{{max-width:920px;margin:26px auto}}</style></head><body>
<h1>Estatuto · arts. 119 e 124</h1><p class="probe-note">A admissão e a escolha do regime dependem de relações jurídicas distintas.</p>
{panel()}</body></html>'''


def install():
    source = PAGE.read_text(encoding="utf-8")
    start = source.find('<figure id="pci-a04-statute"')
    end_at = source.find("</figure>", start)
    if start < 0 or end_at < 0 or source.find('<figure id="pci-a04-statute"', start + 1) >= 0:
        raise SystemExit(f"expected exactly one generated statute figure in {PAGE}")
    end = end_at + len("</figure>")
    PAGE.write_text(source[:start] + panel() + source[end:], encoding="utf-8")
    return PAGE


if __name__ == "__main__":
    figkit.WARN.clear()
    probe = os.environ.get("FIGKIT_PROBE")
    if probe:
        Path(probe).write_text(specimen_page(), encoding="utf-8")
        print(probe)
    print("\n".join(figkit.WARN) or "no text warnings")
