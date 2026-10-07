"""Aula 12 statute cut: CPC arts. 125 II and 129 as one responsive document.
Run python3 tools/figkit/processo_a12.py to insert the component. Set FIGKIT_PROBE
for a standalone browser probe. The text remains real, selectable HTML and reflows as one sheet.
"""
import os
from pathlib import Path

import figkit

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / 'courses' / 'processo-civil-i' / 'aula-12.html'


def panel():
    return '''<figure class="figkit-document" id="pci-a12-art125-129" aria-label="Código de Processo Civil, artigos 125, inciso II, e 129">
<style>
#pci-a12-art125-129{max-width:920px;margin:28px auto 32px;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major);color:var(--ink)}
#pci-a12-art125-129 .document-heading{display:flex;justify-content:space-between;gap:8px 18px;flex-wrap:wrap;padding:13px 20px 12px;border-bottom:1.5px solid var(--ink);font:600 10.5px/1.5 var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--ink-2)}
#pci-a12-art125-129 .document-sheet{padding:clamp(20px,4vw,38px) clamp(20px,5vw,50px) 26px;background:linear-gradient(90deg,var(--paper-2),var(--paper) 14%,var(--paper) 86%,var(--paper-2))}
#pci-a12-art125-129 .article{margin:0}.document-sheet .article+.article{margin-top:23px;padding-top:20px;border-top:1px solid var(--rule)}
#pci-a12-art125-129 .article-number{margin:0 0 8px;font:700 11px/1.5 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2)}
#pci-a12-art125-129 p{max-width:58ch;margin:0;font:400 clamp(19px,2.1vw,23px)/1.62 var(--serif);color:var(--ink)}
#pci-a12-art125-129 .sole{margin-top:15px;padding-top:14px;border-top:1px dashed var(--rule)}
#pci-a12-art125-129 .par-label{font:600 10.5px/1.5 var(--mono);letter-spacing:.07em;text-transform:uppercase;color:var(--ink-2)}
#pci-a12-art125-129 [data-mark="regress"]{background:var(--conc-wash);box-shadow:0 .08em 0 var(--conc);-webkit-box-decoration-break:clone;box-decoration-break:clone}
#pci-a12-art125-129 [data-mark="result"]{background:var(--dif-wash);box-shadow:0 .08em 0 var(--dif);-webkit-box-decoration-break:clone;box-decoration-break:clone}
#pci-a12-art125-129 mark{color:inherit}
#pci-a12-art125-129 figcaption{padding:11px 20px 13px;border-top:1px solid var(--rule);font:500 11px/1.5 var(--mono);letter-spacing:.045em;color:var(--ink-2)}
@media(max-width:560px) and (orientation:portrait){#pci-a12-art125-129 .document-heading{padding:11px 14px}#pci-a12-art125-129 .document-sheet{padding:20px 16px}#pci-a12-art125-129 figcaption{padding:9px 14px}}
</style>
<div class="document-heading"><span>Código de Processo Civil</span><span>Lei nº 13.105/2015</span></div>
<div class="document-sheet">
<section class="article" aria-labelledby="pci-a12-art125-heading"><h3 id="pci-a12-art125-heading" class="article-number">Art. 125</h3><p>II - àquele que estiver obrigado, por lei ou pelo contrato, a indenizar, <mark data-mark="regress">em ação regressiva</mark>, o prejuízo de <mark data-mark="result">quem for vencido no processo</mark>.</p></section>
<section class="article" aria-labelledby="pci-a12-art129-heading"><h3 id="pci-a12-art129-heading" class="article-number">Art. 129</h3><p>Se o denunciante for <mark data-mark="result">vencido</mark> na ação principal, o juiz passará ao julgamento da denunciação da lide.</p><p class="sole"><span class="par-label">Parágrafo único.</span> Se o denunciante for <mark data-mark="regress">vencedor</mark>, a ação de denunciação não terá o seu pedido examinado, sem prejuízo da condenação do denunciante ao pagamento das verbas de sucumbência em favor do denunciado.</p></section>
</div>
<figcaption>O pedido regressivo permanece distinto; o resultado da demanda principal define quando o art. 129 manda examiná-lo.</figcaption>
</figure><span class="src" hidden data-src="CPC, art. 125, II, e art. 129."></span>'''


def specimen_page():
    css = (ROOT / 'courses' / 'processo-civil-i' / 'assets' / 'curso.css').as_uri()
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Figkit · Processo Aula 12</title><link rel="stylesheet" href="{css}"><style>body{{max-width:1040px;margin:0 auto;padding:28px 18px;background:var(--paper);color:var(--ink)}}h1{{font:750 28px/1.1 var(--sans)}}.probe-note{{max-width:70ch;font:16px/1.5 var(--serif);color:var(--ink-2)}}</style></head><body><h1>Documento · arts. 125 e 129</h1><p class="probe-note">A página de lei reúne o vínculo regressivo e a condição que orienta o julgamento.</p>{panel()}</body></html>'''


def main():
    figkit.WARN.clear()
    html = PAGE.read_text(encoding='utf-8')
    marker = '<!-- FIGKIT A12 -->'
    if marker in html:
        PAGE.write_text(html.replace(marker, panel(), 1), encoding='utf-8')
    elif 'id="pci-a12-art125-129"' not in html:
        raise SystemExit('Aula 12 figure marker not found')
    probe = os.environ.get('FIGKIT_PROBE')
    if probe:
        Path(probe).write_text(specimen_page(), encoding='utf-8')
        print(probe)
    print('\n'.join(figkit.WARN) or 'no text warnings')


if __name__ == '__main__':
    main()
