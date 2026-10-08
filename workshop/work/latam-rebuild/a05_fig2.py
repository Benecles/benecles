# Aula 05 Fig. 2: the Gelman judgment page, glossed. Four panels: the reasons, Gargarella I, Gargarella II, SCJ 20/2013.
STYLE = '<style>@media (max-width:860px) and (orientation:portrait){.stage figure svg.fig text{font-size:19px!important}}</style>'
PX0, PX1 = 34, 384          # judgment page
BLOCKS = [  # key, y of label, label, n text lines
    ('226', 112, '§ 226 · VÍTIMA SEM JUIZ', 2),
    ('229', 190, '§ 229 · EFEITO, NÃO ORIGEM', 2),
    ('238', 268, '§§ 238–239 · VOTO NÃO BASTA', 3),
    ('p9', 404, '9 · INVESTIGAR E SANCIONAR', 2),
    ('p11', 482, '11 · A LEI SEM EFEITOS', 2),
]
def block_box(y, n): return (PX0 + 6, y - 20, PX1 - PX0 - 12, 30 + n * 14)

def page(wash=None, dim=False):
    wash = wash or {}
    g = [f'<g{" style=\"opacity:.32\"" if dim else ""}>',
         f'<rect x="{PX0}" y="68" width="{PX1-PX0}" height="476" class="f-paper ink"/>',
         f'<text x="{PX0+16}" y="88" class="t-small" style="font-size:16px;opacity:.6">FUNDAMENTOS</text>']
    for key, y, label, n in BLOCKS:
        if key == 'p9':
            g.append(f'<path d="M{PX0+16} 352H{PX1-16}" class="thin"/>')
            g.append(f'<text x="{PX0+16}" y="374" class="t-small" style="font-size:16px;opacity:.6">PONTOS RESOLUTIVOS</text>')
        if key in wash:
            x, by, w, h = block_box(y, n)
            g.append(f'<rect x="{x}" y="{by}" width="{w}" height="{h}" class="w-{wash[key]}"/>')
        tc = f' tc-{wash[key]}' if key in wash else ''
        g.append(f'<text x="{PX0+16}" y="{y}" style="font-size:16px" class="t-small{tc}">{label}</text>')
        for i in range(n):
            w = (PX1 - PX0 - 32) * (0.62 if i == n - 1 else 1)
            g.append(f'<path d="M{PX0+16} {y+14+i*14}h{w:.0f}" class="thin" style="opacity:.3"/>')
    g.append('</g>')
    return ''.join(g)

def svg(pid, aria, title, body, on=False):
    return (f'<svg class="panel fig figkit{" on" if on else ""}" id="{pid}" viewBox="0 12 600 552" role="img" aria-label="{aria}">{STYLE}'
            f'<text x="34" y="42" style="font-size:16px" class="t-small">{title}</text>{body}</svg>')

MX = 404  # margin column
def gloss(y, head, lines, tone='conc'):
    out = [f'<text x="{MX}" y="{y}" style="font-size:16px" class="t-small tc-{tone}">{head}</text>']
    for i, l in enumerate(lines):
        out.append(f'<text x="{MX}" y="{y+34+i*32}" style="font-size:22px" class="t-hand">{l}</text>')
    return ''.join(out)
def leader(x1, y1, x2, y2, tone='conc'):
    return f'<path d="M{x1} {y1}C{x1-20} {y1} {x2+20} {y2} {x2} {y2}" style="fill:none;stroke:var(--{tone});stroke-width:1.6"/>'

# p0: three reasons, one order
b0 = page({'226': 'dif', '229': 'dif', '238': 'dif', 'p11': 'dif'})
b0 += f'<path d="M{PX1+8} 94V318M{PX1+8} 206H{PX1+18}V478H{PX1+8}" style="fill:none;stroke:var(--dif);stroke-width:1.6"/>'
b0 += gloss(196, 'A CONCLUSÃO', ['três razões', 'sustentam', 'uma ordem'], 'dif')
# p1: Gargarella I attacks 229 and 238–239
b1 = page({'229': 'conc', '238': 'conc'})
b1 += gloss(150, 'GARGARELLA', ['nem toda', 'anistia é igual'])
b1 += leader(MX - 6, 176, PX1 - 4, 184) + leader(MX - 6, 200, PX1 - 4, 274)
b1 += f'<text x="{MX}" y="300" class="t-small" style="font-size:16px;opacity:.6">§ 226: INTACTO</text>'
# p2: Gargarella II attacks the premise behind point 9
b2 = page({'p9': 'conc'})
b2 += gloss(330, 'GARGARELLA', ['reproche não é', 'só castigo'])
b2 += leader(MX - 6, 372, PX1 - 4, 412)
b2 += f'<text x="{MX}" y="440" class="t-small" style="font-size:16px;opacity:.6">VERDADE</text><text x="{MX}" y="462" class="t-small" style="font-size:16px;opacity:.6">REPARAÇÃO</text><text x="{MX}" y="484" class="t-small" style="font-size:16px;opacity:.6">MEMÓRIA</text>'
# p3: SCJ 20/2013 leaves the judgment standing and strikes the execution
b3 = page(dim=True)
LX, LY = MX - 8, 236
law = [f'<text x="{LX}" y="{LY-16}" style="font-size:16px" class="t-small tc-conc">SCJ 20/2013</text>',
       f'<rect x="{LX}" y="{LY}" width="190" height="172" class="f-paper ink"/>',
       f'<text x="{LX+12}" y="{LY+28}" style="font-size:16px" class="t-small">LEI 18.831</text>']
for i, (a, struck) in enumerate([('ART. 1 · REABRE', False), ('ART. 2 · PRAZO', True), ('ART. 3 · CRIME', True)]):
    y = LY + 70 + i * 36
    deco = ' text-decoration="line-through"' if struck else ''
    law.append(f'<text x="{LX+12}" y="{y}" style="font-size:16px" class="t-small{" tc-conc" if struck else ""}"{deco}>{a}</text>')
b3 += ''.join(law)
b3 += f'<text x="{LX}" y="{LY+212}" style="font-size:22px" class="t-hand">a sentença fica;</text><text x="{LX}" y="{LY+244}" style="font-size:22px" class="t-hand">a execução cai</text>'

panels = [svg('p-am0', 'A sentença: três razões e o ponto 11', 'GELMAN VS. URUGUAI · SENTENÇA DE 24/02/2011', b0, on=True),
          svg('p-am1', 'Gargarella contra os §§ 229 e 238–239', 'GELMAN VS. URUGUAI · PRIMEIRA OBJEÇÃO', b1),
          svg('p-am2', 'Gargarella contra a premissa do ponto 9', 'GELMAN VS. URUGUAI · SEGUNDA OBJEÇÃO', b2),
          svg('p-am3', 'A SCJ derruba os arts. 2 e 3 da Lei 18.831', 'URUGUAI, 2013 · A EXECUÇÃO', b3)]
FIG2 = ''.join(panels)
if __name__ == '__main__':
    print(len(FIG2))
