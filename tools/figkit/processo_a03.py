"""Processo Civil I · Aula 03: a two-question litisconsortium classifier."""
from pathlib import Path
import os, re

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / 'courses' / 'processo-civil-i' / 'aula-03.html'


def instrument():
    return '''<figure class="a03-classifier" id="a03-classifier" aria-labelledby="a03-title" aria-describedby="a03-caption a03-result">
  <div class="a03-classifier__head">
    <span class="label">Duas perguntas independentes</span>
    <h3 id="a03-title">Classifique a pluralidade</h3>
  </div>
  <form class="a03-classifier__questions" id="a03-questions">
    <fieldset>
      <legend><span>01</span>Todos devem participar?</legend>
      <label><input type="radio" name="participacao" value="necessaria"><span>Sim</span></label>
      <label><input type="radio" name="participacao" value="facultativa"><span>Não</span></label>
    </fieldset>
    <fieldset>
      <legend><span>02</span>O mérito exige decisão uniforme?</legend>
      <label><input type="radio" name="uniformidade" value="unitario"><span>Sim</span></label>
      <label><input type="radio" name="uniformidade" value="simples"><span>Não</span></label>
    </fieldset>
  </form>
  <div class="a03-classifier__matrix">
    <table>
      <caption>As respostas independentes definem quatro combinações possíveis</caption>
      <thead><tr><th scope="col">Participação</th><th scope="col">Mérito uniforme</th><th scope="col">Sem dever de uniformidade</th></tr></thead>
      <tbody>
        <tr><th scope="row">Obrigatória</th><td id="a03-nu" data-combination="necessaria-unitario"><strong>Necessário e unitário</strong><span>Todos participam; o mérito é uniforme.</span></td><td id="a03-ns" data-combination="necessaria-simples"><strong>Necessário e simples</strong><span>Todos participam; o mérito pode variar.</span></td></tr>
        <tr><th scope="row">Facultativa</th><td id="a03-fu" data-combination="facultativa-unitario"><strong>Facultativo e unitário</strong><span>A reunião é opcional; o mérito é uniforme.</span></td><td id="a03-fs" data-combination="facultativa-simples"><strong>Facultativo e simples</strong><span>A reunião é opcional; o mérito pode variar.</span></td></tr>
      </tbody>
    </table>
  </div>
  <p class="a03-classifier__result" id="a03-result" role="status" aria-live="polite">Escolha uma resposta em cada pergunta para localizar a combinação.</p>
  <figcaption id="a03-caption">A exigência de participação não determina, sozinha, se o mérito deve ser julgado de modo uniforme (CPC, arts. 114–116).</figcaption>
</figure>'''


def mixed_poles():
    """The real 2015/1 exam arrangement: two people in each pole."""
    return '''<figure class="a03-figure" id="a03-mixed-poles" aria-labelledby="a03-mixed-title">
<svg class="fig figkit" viewBox="0 0 820 300" role="img" aria-labelledby="a03-mixed-title a03-mixed-desc">
<title id="a03-mixed-title">Avaliação 1 de 2015/1: pluralidade nos dois polos</title><desc id="a03-mixed-desc">Gustavo e Maique aparecem como autores no mesmo processo; Valter e Os Galos Primos aparecem como réus. Há pluralidade ativa e passiva, configuração mista.</desc>
<text x="410" y="30" text-anchor="middle" class="kicker">AVALIAÇÃO 1 · 2015/1 · Q3(e)</text>
<text x="105" y="70" text-anchor="middle" class="side">AUTORES</text><text x="715" y="70" text-anchor="middle" class="side">RÉUS</text>
<path d="M410 54V267" class="axis"/><text x="410" y="286" text-anchor="middle" class="tiny">UM PROCESSO</text>
<circle cx="105" cy="130" r="28" class="person"/><circle cx="105" cy="210" r="28" class="person"/>
<text x="155" y="136" class="name">Gustavo</text><text x="155" y="216" class="name">Maique</text>
<circle cx="715" cy="130" r="28" class="person"/><circle cx="715" cy="210" r="28" class="person"/>
<text x="665" y="136" text-anchor="end" class="name">Valter</text><text x="665" y="216" text-anchor="end" class="name">Os Galos Primos</text>
<path d="M350 114V226M470 114V226" class="bracket"/>
</svg><figcaption>Dois autores e dois réus no mesmo processo formam pluralidade ativa e passiva: litisconsórcio misto.</figcaption></figure>'''


def didier_case():
    """A real case thread, with the absent co-borrower outside the filed action."""
    return '''<figure class="a03-figure" id="a03-didier-case" aria-labelledby="a03-didier-title">
<svg class="fig figkit" viewBox="0 0 820 300" role="img" aria-labelledby="a03-didier-title a03-didier-desc">
<title id="a03-didier-title">REsp 1.222.822, como relatado por Didier</title><desc id="a03-didier-desc">Mutuários casados figuram na relação de financiamento. Só o marido ajuizou a ação revisional. O STJ reconheceu litisconsórcio ativo necessário no relato de Didier; ele critica a consequência.</desc>
<text x="410" y="30" text-anchor="middle" class="kicker">FINANCIAMENTO IMOBILIÁRIO · RESP 1.222.822</text>
<text x="130" y="75" text-anchor="middle" class="side">MUTUÁRIOS</text><text x="410" y="75" text-anchor="middle" class="side">AÇÃO REVISIONAL</text><text x="690" y="75" text-anchor="middle" class="side">RESULTADO RELATADO</text>
<circle cx="90" cy="145" r="25" class="person"/><circle cx="170" cy="145" r="25" class="person"/>
<text x="90" y="198" text-anchor="middle" class="name">marido</text><text x="170" y="198" text-anchor="middle" class="name">esposa</text>
<path d="M95 235H165" class="relation"/><text x="130" y="260" text-anchor="middle" class="tiny">contrato comum</text>
<path d="M210 145H320" class="relation filed"/><circle cx="410" cy="145" r="50" class="docket"/><text x="410" y="141" text-anchor="middle" class="inside">só o marido</text><text x="410" y="161" text-anchor="middle" class="inside">ajuizou</text>
<path d="M460 145H620" class="relation outcome"/><path d="M620 108H760V182H620Z" class="paper"/><text x="690" y="137" text-anchor="middle" class="inside">extinta sem</text><text x="690" y="157" text-anchor="middle" class="inside">mérito</text>
<text x="410" y="286" text-anchor="middle" class="tiny">STJ: necessidade ativa · crítica de Didier: barreira à revisão</text>
</svg><figcaption>O caso atribuído a Didier põe em discussão a participação necessária no polo ativo; a unidade do mérito exige análise própria.</figcaption></figure>'''


def specimen_section():
    return f'''<section class="ref native-ref"><header><span class="g">Instrumento · classificação em dois eixos</span><span class="v">verbo · classificar</span></header>
<h2>Processo · Aula 03 · litisconsórcio</h2><p>Duas respostas independentes localizam o caso em uma das quatro combinações do CPC.</p><p class="r">novo componente · pci-a03-classifier</p>
{instrument()}</section>'''


def specimen_figures():
    return f'''<section class="ref native-ref"><header><span>Objeto · polos da demanda</span><span class="v">verbo · localizar</span></header>
<h2>Processo · Aula 03 · Avaliação 1 de 2015/1</h2><p>A posição dos litigantes e a quantidade em cada lado permitem classificar a configuração.</p><p class="r">novos componentes · pci-a03-mixed-poles / pci-a03-didier-case</p>
{mixed_poles()}{didier_case()}</section>'''


def specimen_page():
    css = '../courses/processo-civil-i/assets/aula-03.css'
    js = '../courses/processo-civil-i/assets/aula-03.js'
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Figkit · Processo Civil Aula 03</title><link rel="stylesheet" href="../courses/processo-civil-i/assets/curso.css"><link rel="stylesheet" href="{css}">
<style>body{{max-width:1180px;margin:0 auto;padding:24px 16px 80px;background:var(--paper);color:var(--ink)}}h1{{font:750 30px/1.1 var(--sans)}}.native-ref{{border-top:1.5px solid var(--ink);padding:16px 0 26px}}.native-ref header{{display:flex;gap:14px;font:600 11px var(--mono);letter-spacing:.1em;text-transform:uppercase}}.native-ref .g{{color:var(--conc)}}.native-ref .v{{color:var(--ink-2)}}.native-ref h2{{font:700 22px/1.2 var(--sans);margin:8px 0 6px}}.native-ref p{{font:16px/1.5 var(--serif,serif);max-width:66ch;margin:0 0 6px}}.native-ref p.r{{font:11px var(--mono);letter-spacing:.06em;color:var(--muted)}}</style></head><body>
<h1>Instrumento · duas perguntas</h1><p>Uma resposta sobre participação e outra sobre uniformidade localizam a combinação processual.</p>{specimen_section()}
<script src="{js}"></script></body></html>'''


def install():
    source = PAGE.read_text(encoding='utf-8')
    marker = '<!-- FIGKIT: A03 CLASSIFIER -->'
    if source.count(marker) == 1:
        updated = source.replace(marker, instrument())
    else:
        start = source.find('<figure class="a03-classifier"')
        end_at = source.find('</figure>', start)
        if start < 0 or end_at < 0 or source.find('<figure class="a03-classifier"', start + 1) >= 0:
            raise SystemExit(f'expected one A03 figure marker or figure in {PAGE}')
        end = end_at + len('</figure>')
        updated = source[:start] + instrument() + source[end:]
    PAGE.write_text(updated, encoding='utf-8')
    return PAGE


def install_figures():
    source = PAGE.read_text(encoding='utf-8')
    for figure_id, render in (('a03-mixed-poles', mixed_poles), ('a03-didier-case', didier_case)):
        pattern = re.compile(r'<figure class="a03-figure" id="' + re.escape(figure_id) + r'".*?</figure>', re.S)
        source, count = pattern.subn(render(), source, count=1)
        if count != 1:
            raise SystemExit(f'expected one #{figure_id} in {PAGE}')
    PAGE.write_text(source, encoding='utf-8')
    return PAGE


if __name__ == '__main__':
    probe = os.environ.get('FIGKIT_PROBE')
    if probe:
        Path(probe).write_text(specimen_page(), encoding='utf-8')
        print(probe)
    else:
        print(install())
        print(install_figures())
    print('no text warnings')
