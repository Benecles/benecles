"""Aula 10: pair each factual issue with evidence and burden; mark § 1's window.

Sources: the Aula 10 compendium's CPC art. 357, II–III and § 1, and art. 373.
The first panel is a reusable relation, with no case facts filled in. The second
shows order and duration only: there is no implied calendar date or appeal route.
"""
from figkit import line, svg, t


def issue_links_panel():
    """An issue's two attached determinations, drawn as one branching relation."""
    o = ''
    o += t(38, 51, 'ART. 357 · II–III', size=13, weight=700, fill='var(--ink-2)')
    o += t(962, 51, 'PARA CADA QUESTÃO', size=12, weight=700,
           fill='var(--ink-2)', anchor='end')

    # One fork per factual issue: its two ends stay visibly joined to that issue.
    # The circle is an empty statutory slot, not a fictional case fact.
    o += line(256, 164, 433, 164, tone='ink', w=4)
    o += f'<path d="M433 164Q472 164 510 129L578 94" style="fill:none;stroke:var(--conc);stroke-width:4;stroke-linecap:round"/>'
    o += f'<path d="M433 164Q472 164 510 199L578 234" style="fill:none;stroke:var(--dif);stroke-width:4;stroke-linecap:round"/>'
    o += f'<circle cx="198" cy="164" r="58" style="fill:var(--paper);stroke:var(--ink);stroke-width:3"/>'
    o += f'<circle cx="198" cy="164" r="38" style="fill:none;stroke:var(--ink-2);stroke-width:1.5;stroke-dasharray:3 5"/>'
    o += f'<circle cx="600" cy="85" r="18" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:3"/>'
    o += f'<circle cx="600" cy="243" r="18" style="fill:var(--dif-wash);stroke:var(--dif);stroke-width:3"/>'
    o += t(198, 169, 'FATO', size=16, weight=700, anchor='middle')
    o += t(198, 251, 'QUESTÃO DE FATO', size=13, weight=700, anchor='middle')
    o += t(639, 82, 'MEIOS DE PROVA', size=15, weight=700, fill='var(--conc)')
    o += t(639, 105, 'ADMITIDOS', size=12, weight=600, fill='var(--conc)')
    o += t(639, 240, 'ÔNUS DA PROVA', size=15, weight=700, fill='var(--dif)')
    o += t(639, 263, 'ART. 373', size=12, weight=600, fill='var(--dif)')
    return svg('20 24 960 266', o, cls='fig', ident='pci-a10-issue-links',
               label='Cada questão de fato se liga aos meios de prova admitidos e à definição do ônus da prova, observado o art. 373')


def stability_panel():
    """The common five-day adjustment window follows sanitation; stability closes it."""
    o = ''
    o += t(36, 48, 'ART. 357 · § 1º', size=13, weight=700, fill='var(--ink-2)')
    # The interval begins at sanitation and its endpoint is the statutory stability point.
    o += f'<rect x="95" y="151" width="858" height="20" rx="10" style="fill:var(--conc-wash);stroke:var(--conc);stroke-width:2"/>'
    for x, tone in ((95, 'ink'), (953, 'dif')):
        o += line(x, 136, x, 186, tone=tone, w=2.5)
        o += f'<circle cx="{x}" cy="161" r="5" style="fill:var(--paper);stroke:var(--{tone});stroke-width:2"/>'
    o += f'<path d="M95 96V108H953V96" style="fill:none;stroke:var(--conc);stroke-width:2;stroke-linejoin:round"/>'
    o += t(524, 83, 'PRAZO COMUM · 5 DIAS', size=14, weight=700,
           fill='var(--conc)', anchor='middle')
    o += t(524, 204, 'PEDIR ESCLARECIMENTOS OU SOLICITAR AJUSTES',
           size=11.5, weight=600, anchor='middle')
    o += t(95, 218, 'SANEAMENTO', size=12, weight=700, anchor='start')
    o += t(95, 238, 'REALIZADO', size=11, weight=600, anchor='start')
    o += t(953, 218, 'DECISÃO ESTÁVEL', size=12, weight=700,
           fill='var(--dif)', anchor='end')
    o += t(953, 238, 'FINDO O PRAZO', size=11, weight=600,
           fill='var(--dif)', anchor='end')
    return svg('20 24 960 236', o, cls='fig', ident='pci-a10-stability',
               label='Após o saneamento, prazo comum de cinco dias para as partes pedirem esclarecimentos ou solicitarem ajustes; findo o prazo, a decisão se torna estável')


def replacement_mapping():
    """Pass to inject.inject for this page alone once same-id SVG slots exist."""
    return {'pci-a10-issue-links': issue_links_panel(),
            'pci-a10-stability': stability_panel()}
