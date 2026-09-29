"""The ⓘ button on each course front: a small outlined "i" in the top bar that opens a short card naming the
public sources the course is built on (syllabus books, Moodle slides, leading decisions, statutes). Never the
exhaustive bibliography and never classmates' notes: only what a reader could go and find.
Idempotent: the button lives between FONTES markers. Edit SOURCES and re-run."""
import os, re, html as H

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'courses')
SOURCES = {
    'teoria-do-delito': [
        ('Do programa', ['Cezar Roberto Bitencourt, <i>Tratado de Direito Penal</i>, v. 1', 'Rogério Sanches Cunha, <i>Manual de Direito Penal: Parte Geral</i>',
                         'João Paulo Martinelli e Leonardo Schmitt de Bem, <i>Lições Fundamentais de Direito Penal</i>', 'Francisco de Assis Toledo, <i>Princípios Básicos de Direito Penal</i>']),
        ('Leituras complementares', ['Juarez Tavares, <i>Fundamentos de Teoria do Delito</i>', 'Claus Roxin, <i>Política Criminal e Sistema Jurídico-penal</i>']),
        ('Lei', ['Código Penal, Parte Geral (arts. 13 a 31)']),
    ],
    'controle-de-constitucionalidade': [
        ('Do programa', ['Pedro Lenza, <i>Direito Constitucional Esquematizado</i>', 'Gilmar Mendes e Paulo Gonet Branco, <i>Curso de Direito Constitucional</i>',
                         'Luís Roberto Barroso, <i>O Controle de Constitucionalidade no Direito Brasileiro</i>', 'Dimitri Dimoulis e Soraya Lunardi, <i>Curso de Processo Constitucional</i>']),
        ('Lei e jurisprudência', ['Constituição Federal, arts. 97, 102 e 103; Leis 9.868/1999 e 9.882/1999', 'Jurisprudência do STF indicada em aula']),
    ],
    'teoria-geral-dos-contratos': [
        ('Do programa', ['Caio Mário da Silva Pereira, <i>Instituições de Direito Civil</i>, v. III', 'Sílvio de Salvo Venosa, <i>Direito Civil: Contratos</i>', 'Orlando Gomes, <i>Contratos</i>']),
        ('Do Moodle', ['Slides das aulas da Profa. Giovana Benetti', 'Artigos de Judith Martins-Costa, Antonio Junqueira de Azevedo e Gerson Branco',
                       'Julgados do STJ e do TJSP indicados em aula (entre eles, o caso Zeca Pagodinho)']),
        ('Lei', ['Código Civil, arts. 421 a 480; Código de Defesa do Consumidor']),
    ],
    'processo-civil-i': [
        ('Do programa', ['Fredie Didier Jr., <i>Curso de Direito Processual Civil</i>, v. 1', 'Luiz Guilherme Marinoni, Sérgio Arenhart e Daniel Mitidiero, <i>Novo Curso de Processo Civil</i>']),
        ('Leituras indicadas', ['Elie Pierre Eid, <i>Litisconsórcio unitário: fundamentos, estrutura e regime</i>', 'J. J. Calmon de Passos, <i>Esboço de uma teoria das nulidades aplicada às nulidades processuais</i>',
                                'Paulo Henrique dos Santos Lucon, comentários aos arts. 355 a 357 do CPC']),
        ('Lei', ['Código de Processo Civil (Lei 13.105/2015)']),
    ],
    'direito-constitucional-i': [
        ('Do programa', ['Ingo Wolfgang Sarlet, Luiz Guilherme Marinoni e Daniel Mitidiero, <i>Curso de Direito Constitucional</i>', 'André Ramos Tavares, <i>Curso de Direito Constitucional</i>',
                         'Paulo Bonavides, <i>Curso de Direito Constitucional</i>']),
        ('Lei e jurisprudência', ['Constituição Federal de 1988', 'STF: ADI 3.345 e ADI 3.365 (número de vereadores)']),
    ],
    'direito-latino-americano': [
        ('Do programa', ['Fabiano Engelmann e Júlia Bandeira, “A construção da autonomia política do judiciário na América Latina” (<i>Dados</i>, 2017)']),
        ('Decisões', ['STF: ADPF 153, ADPF 347, STA 175 e RE 566.471 (Tema 6)', 'Corte IDH: Gomes Lund vs. Brasil, Gelman vs. Uruguai e OC‑28/2021',
                      'Corte Constitucional colombiana: T‑153/1998, T‑025/2004, C‑579/2013 e C‑694/2015', 'SCJ do Uruguai (Sentencias 20/2013 e 65/2014) e TCP da Bolívia (SCP 0084/2017)']),
        ('Do Moodle', ['Slides das aulas']),
    ],
}
CSS = ('<style>.topbar{position:relative}.tb-right{display:flex;align-items:center;gap:14px}'
       '.fontes-i{position:static}.fontes-i>summary{list-style:none;cursor:pointer;width:22px;height:22px;border:1.5px solid var(--ink-2);border-radius:50%;'
       'display:grid;place-items:center;font:italic 600 13px/1 var(--serif);color:var(--ink-2);text-transform:none;letter-spacing:0}'
       '.fontes-i>summary::-webkit-details-marker{display:none}.fontes-i>summary:hover,.fontes-i[open]>summary,.fontes-i>summary:focus-visible{border-color:var(--conc);color:var(--conc)}'
       '.fontes-card{position:absolute;right:clamp(16px,4vw,48px);top:calc(100% - 4px);z-index:30;width:min(380px,calc(100vw - 32px));padding:16px 18px 12px;'
       'background:var(--paper);border:1.5px solid var(--ink);box-shadow:6px 6px 0 var(--grid-major);text-transform:none;letter-spacing:0;color:var(--ink)}'
       '.fontes-card h2{font:600 11px var(--mono);letter-spacing:.1em;text-transform:uppercase;margin:0 0 10px}'
       '.fontes-card h3{font:500 10.5px var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--conc);margin:12px 0 4px}'
       '.fontes-card ul{margin:0;padding:0;list-style:none}.fontes-card li{font:14px/1.4 var(--serif);padding:3px 0}'
       '.fontes-card p{font:11px/1.4 var(--mono);color:var(--muted);margin:12px 0 0}</style>')

def block(slug):
    rows = ''.join(f'<h3>{H.escape(g)}</h3><ul>' + ''.join(f'<li>{x}</li>' for x in xs) + '</ul>' for g, xs in SOURCES[slug])
    return (f'<!-- FONTES:START -->{CSS}<details class="fontes-i"><summary aria-label="Fontes do curso" title="Fontes do curso">i</summary>'
            f'<div class="fontes-card" role="dialog" aria-label="Fontes do curso"><h2>Fontes do curso</h2>{rows}'
            f'<p>As principais, não a bibliografia completa.</p></div></details><!-- FONTES:END -->')

JS = ('<script>(function(){var d=document.querySelector(".fontes-i");if(!d)return;document.addEventListener("click",function(e){if(d.open&&!d.contains(e.target))d.open=false});'
      'document.addEventListener("keydown",function(e){if(e.key==="Escape"&&d.open){d.open=false;d.querySelector("summary").focus()}})})()</script>')

for slug in SOURCES:
    p = os.path.join(ROOT, slug, 'index.html')
    s = open(p).read()
    if '<!-- FONTES:START -->' in s:
        a, b = s.index('<!-- FONTES:START -->'), s.index('<!-- FONTES:END -->') + len('<!-- FONTES:END -->')
        s = s[:a] + block(slug) + s[b:]
    else:
        m = re.search(r'(<nav class="topbar"[^>]*>.*?)(<button class="theme-toggle".*?</button>)(</nav>)', s, re.S)
        s = s[:m.start()] + m.group(1) + '<span class="tb-right">' + block(slug) + m.group(2) + '</span>' + m.group(3) + JS + s[m.end():]
    open(p, 'w').write(s)
    print('fontes:', slug)
