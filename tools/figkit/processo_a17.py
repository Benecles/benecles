"""Processo Civil I · Aula 17: the native decision form for CPC art. 373.

The chosen cast is a working HTML form, not an SVG retyping of legal text. The statute remains
selectable text for phone and print; the controls progressively enhance its default caput state.
Run `python3 tools/figkit/processo_a17.py` to insert the component in the lesson. Set FIGKIT_PROBE
to write a standalone specimen page for visual inspection.
"""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / 'courses' / 'processo-civil-i' / 'aula-17.html'


def instrument():
    return '''<figure class="a17-instrument" id="art373-instrument" aria-labelledby="a17-form-title">
  <div class="a17-instrument__head">
    <span class="label">CPC · instrumento de decisão</span>
    <h3 id="a17-form-title">Art. 373 · ônus da prova</h3>
  </div>
  <div class="a17-instrument__body">
    <div class="a17-statute">
      <span class="art-head">Regra legal · caput e §§ 1º–2º</span>
      <p>Art. 373. O ônus da prova incumbe:</p>
      <p>I - ao autor, quanto ao fato constitutivo de seu direito;</p>
      <p>II - ao réu, quanto à existência de fato impeditivo, modificativo ou extintivo do direito do autor.</p>
      <p>§ 1º Nos casos previstos em lei ou diante de peculiaridades da causa relacionadas à impossibilidade ou à excessiva dificuldade de cumprir o encargo nos termos do caput ou à maior facilidade de obtenção da prova do fato contrário, poderá o juiz atribuir o ônus da prova de modo diverso, desde que o faça por decisão fundamentada, caso em que deverá dar à parte a oportunidade de se desincumbir do ônus que lhe foi atribuído.</p>
      <p>§ 2º A decisão prevista no § 1º deste artigo não pode gerar situação em que a desincumbência do encargo pela parte seja impossível ou excessivamente difícil.</p>
    </div>
    <form class="a17-controls" id="a17-controls" aria-describedby="a17-result">
      <label for="a17-fato">Qual é o tipo de fato?</label>
      <select name="fato" id="a17-fato">
        <option value="constitutivo" selected>Constitutivo do direito</option>
        <option value="impeditivo">Impeditivo do direito</option>
        <option value="modificativo">Modificativo do direito</option>
        <option value="extintivo">Extintivo do direito</option>
      </select>
      <label for="a17-hipotese">Há hipótese para redistribuir o encargo?</label>
      <select name="hipotese" id="a17-hipotese">
        <option value="nenhuma" selected>Nenhuma · aplica-se o caput</option>
        <option value="lei">Previsão legal</option>
        <option value="dificuldade">Impossibilidade ou excessiva dificuldade do encargo do caput</option>
        <option value="facilidade">Maior facilidade para obter a prova do fato contrário</option>
      </select>
      <fieldset>
        <legend>Salvaguardas do § 1º</legend>
        <label class="check-line"><input type="checkbox" name="fundamentada" value="sim"> Decisão fundamentada</label>
        <label class="check-line"><input type="checkbox" name="oportunidade" value="sim"> Oportunidade para cumprir o encargo</label>
      </fieldset>
      <label for="a17-cumprivel">A parte que receberá o encargo pode cumpri-lo?</label>
      <select name="cumprivel" id="a17-cumprivel">
        <option value="sim" selected>Sim</option>
        <option value="nao">Não · seria impossível ou excessivamente difícil</option>
      </select>
      <div class="a17-result" id="a17-result" data-state="default" role="status" aria-live="polite">
        <strong class="a17-result__title">Mantém-se a regra do caput</strong>
        <p class="a17-result__text">O ônus ordinário cabe ao autor quanto ao fato constitutivo.</p>
      </div>
    </form>
  </div>
  <figcaption>Fig. 1 · O art. 373 parte da distribuição legal e limita a redistribuição</figcaption>
</figure>'''


def specimen_section():
    return f'''<section class="ref native-ref"><header><span class="g">Instrumento · formulário de decisão</span><span class="v">verbo · decidir</span></header>
<h2>Processo · Aula 17 · art. 373</h2><p>O leitor seleciona o tipo de fato e testa as hipóteses e salvaguardas legais para a redistribuição.</p><p class="r">primeira ocorrência · Aula 17</p>
{instrument()}</section>'''


def specimen_page():
    css = (ROOT / 'courses' / 'processo-civil-i' / 'assets' / 'aula-17.css').as_uri()
    js = (ROOT / 'courses' / 'processo-civil-i' / 'assets' / 'aula-17.js').as_uri()
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Figkit · Processo Civil Aula 17</title><link rel="stylesheet" href="{css}">
<style>body{{max-width:1180px;margin:0 auto;padding:24px 16px 80px;background:var(--paper);color:var(--ink)}}h1{{font:750 30px/1.1 var(--sans)}}.native-ref{{border-top:1.5px solid var(--ink);padding:16px 0 26px}}.native-ref header{{display:flex;gap:14px;font:600 11px var(--mono);letter-spacing:.1em;text-transform:uppercase}}.native-ref .g{{color:var(--conc)}}.native-ref .v{{color:var(--ink-2)}}.native-ref h2{{font:700 22px/1.2 var(--sans);margin:8px 0 6px}}.native-ref p{{font:16px/1.5 var(--serif,serif);max-width:66ch;margin:0 0 6px}}.native-ref p.r{{font:11px var(--mono);letter-spacing:.06em;color:var(--muted)}}</style></head><body>
<h1>Figuras · referências</h1><p>Instrumento nativo de decisão construído a partir do art. 373.</p>{specimen_section()}
<script src="{js}"></script></body></html>'''


def install():
    source = PAGE.read_text(encoding='utf-8')
    start = source.find('<figure class="a17-instrument"')
    end_at = source.find('</figure>', start)
    if start < 0 or end_at < 0 or source.find('<figure class="a17-instrument"', start + 1) >= 0:
        raise SystemExit(f'expected exactly one generated art. 373 form in {PAGE}')
    end = end_at + len('</figure>')
    PAGE.write_text(source[:start] + instrument() + source[end:], encoding='utf-8')
    return PAGE


if __name__ == '__main__':
    probe = os.environ.get('FIGKIT_PROBE')
    if probe:
        Path(probe).write_text(specimen_page(), encoding='utf-8')
        print(probe)
    else:
        print(install())
    print('no text warnings')
