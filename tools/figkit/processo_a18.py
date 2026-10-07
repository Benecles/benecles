"""Aula 18 statute specimen: CPC art. 370 as an official document."""
import os
from pathlib import Path

import figkit


def panel():
    """The reader selects one of the statute's two operative thresholds."""
    return '''<figure class="figkit-document" id="pci-a18-art370">
<style>
#pci-a18-art370{max-width:920px;margin:26px auto 30px;border:1.5px solid var(--ink);background:var(--paper);box-shadow:6px 6px 0 var(--grid-major);color:var(--ink)}
#pci-a18-art370 .document-control{margin:0;padding:14px 20px 12px;border:0;border-bottom:1px solid var(--rule);display:flex;flex-wrap:wrap;align-items:center;gap:8px 18px}
#pci-a18-art370 .document-control legend{padding:0 10px 0 0;font:600 10.5px/1.4 var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}
#pci-a18-art370 .document-control label{display:inline-flex;align-items:center;gap:7px;font:500 12px/1.4 var(--mono);color:var(--ink)}
#pci-a18-art370 .document-control input{accent-color:var(--conc);width:15px;height:15px;margin:0}
#pci-a18-art370 .document-sheet{padding:clamp(20px,4vw,38px) clamp(20px,5vw,50px) 24px;background:linear-gradient(90deg,var(--paper-2),var(--paper) 16%,var(--paper) 84%,var(--paper-2))}
#pci-a18-art370 .document-heading{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding-bottom:12px;border-bottom:1.5px solid var(--ink);font:600 10.5px/1.5 var(--mono);letter-spacing:.09em;text-transform:uppercase;color:var(--ink-2)}
#pci-a18-art370 .article-number{margin:22px 0 8px;font:700 12px/1.4 var(--mono);letter-spacing:.1em;text-transform:uppercase;color:var(--ink-2)}
#pci-a18-art370 .document-sheet p{max-width:58ch;margin:0;font:400 clamp(19px,2.1vw,23px)/1.62 var(--serif);color:var(--ink)}
#pci-a18-art370 .document-sheet .sole{margin-top:20px;padding-top:17px;border-top:1px solid var(--rule)}
#pci-a18-art370 .par-label{font:600 11px/1.5 var(--mono);letter-spacing:.06em;text-transform:uppercase;color:var(--ink-2)}
#pci-a18-art370 [data-focus]{padding:0 .06em;-webkit-box-decoration-break:clone;box-decoration-break:clone;transition:background-color .18s ease}
#pci-a18-art370:has(#pci-a18-focus-necessary:checked) #pci-a18-necessary{background:var(--dif-wash);box-shadow:0 .08em 0 var(--dif)}
#pci-a18-art370:has(#pci-a18-focus-limit:checked) #pci-a18-limit{background:var(--conc-wash);box-shadow:0 .08em 0 var(--conc)}
#pci-a18-art370 figcaption{padding:10px 20px 12px;border-top:1px solid var(--rule);font:500 10.5px/1.5 var(--mono);letter-spacing:.06em;color:var(--ink-2)}
@media(max-width:560px) and (orientation:portrait){#pci-a18-art370 .document-control{padding:12px 14px}#pci-a18-art370 .document-sheet{padding:20px 16px}#pci-a18-art370 figcaption{padding:9px 14px}}
@media(prefers-reduced-motion:reduce){#pci-a18-art370 [data-focus]{transition:none}}
</style>
<fieldset class="document-control"><legend>Realçar no texto</legend>
<label><input id="pci-a18-focus-necessary" type="radio" name="pci-a18-focus" value="necessary" checked><span>Provas necessárias</span></label>
<label><input id="pci-a18-focus-limit" type="radio" name="pci-a18-focus" value="limit"><span>Limite à diligência</span></label>
</fieldset>
<div class="document-sheet">
<div class="document-heading"><span>Código de Processo Civil</span><span>Lei nº 13.105/2015</span></div>
<div class="article-number">Art. 370</div>
<p>Caberá ao juiz, de ofício ou a requerimento da parte, determinar as provas <span id="pci-a18-necessary" data-focus="necessary">necessárias</span> ao julgamento do mérito.</p>
<p class="sole"><span class="par-label">Parágrafo único.</span> O juiz indeferirá, em decisão fundamentada, as <span id="pci-a18-limit" data-focus="limit">diligências inúteis ou meramente protelatórias</span>.</p>
</div>
<figcaption>O caput autoriza a prova necessária ao mérito; o parágrafo único exige fundamentação para indeferir a diligência inútil ou meramente protelatória.</figcaption>
</figure><span class="src" hidden data-src="CPC, art. 370."></span>'''


def specimen_page():
    css = (Path(__file__).resolve().parents[2] /
           'courses' / 'processo-civil-i' / 'assets' / 'curso.css').as_uri()
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Figkit · Processo Aula 18</title>
<link rel="stylesheet" href="{css}">
<style>body{{max-width:1040px;margin:0 auto;padding:28px 18px;background:var(--paper);color:var(--ink)}}h1{{font:750 28px/1.1 var(--sans)}}.probe-note{{max-width:70ch;font:16px/1.5 var(--serif);color:var(--ink-2)}}</style></head><body>
<h1>Documento · art. 370</h1><p class="probe-note">A marca acompanha a seleção entre a condição de necessidade e o limite do parágrafo único.</p>
{panel()}</body></html>'''


if __name__ == '__main__':
    figkit.WARN.clear()
    probe = os.environ.get('FIGKIT_PROBE')
    if probe:
        Path(probe).write_text(specimen_page(), encoding='utf-8')
        print(probe)
    print('\n'.join(figkit.WARN) or 'no text warnings')
