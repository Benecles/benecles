from figkit import t, line, svg

def protocol():
    o=''
    o += t(28,42,'RECIBO DE PRÁTICA DO ATO',size=16,weight=700)
    o += t(28,67,'PEDIDO DE INFORMAÇÃO · ÚLTIMO DIA',size=11,fill='var(--ink-2)',weight=600)
    o += line(28,82,572,82,w=1.5)
    # Two actual receipt tracks; the time limit is encoded by a boundary, not prose cells.
    for y,lab,tone,end,limit in [(156,'PETIÇÃO EM PAPEL','dif',350,420),(330,'ATO ELETRÔNICO','conc',490,490)]:
        o += t(34,y-32,lab,size=13,weight=700,fill=f'var(--{tone})')
        o += line(45,y,555,y,w=2,tone='muted')
        o += line(45,y-12,45,y+12,w=2)
        o += line(555,y-12,555,y+12,w=2)
        o += f'<circle cx="{end}" cy="{y}" r="12" style="fill:var(--{tone}-wash);stroke:var(--{tone});stroke-width:2"/>'
        o += t(45,y+31,'INÍCIO',size=10,fill='var(--ink-2)')
        o += t(555,y+40,'FIM DO DIA',size=10,fill='var(--ink-2)',anchor='end')
        o += line(limit,y-24,limit,y+25,tone=tone,w=2.4)
        o += t(limit,y-38,'CORTE',size=10,fill=f'var(--{tone})',anchor='middle',weight=700)
        o += t(34,y+59,'EXPEDIENTE DO FÓRUM' if tone=='dif' else '24:00 · HORÁRIO DO JUÍZO',size=11,fill='var(--ink)',weight=600)
    o += t(300,240,'O REGISTRO PRECISA FICAR ANTES DO CORTE',size=11,anchor='middle',weight=600)
    return svg('18 20 564 385',o,cls='fig',ident='pci-a06-protocol',label='Dois recibos de prática do ato com cortes distintos no último dia: expediente do fórum para papel e meia-noite do juízo para ato eletrônico')

def carta():
    o=''
    # The underlying object is a letter document, not prose placed in ruled cells.
    o += '<path d="M104 34H430L500 104V402H104Z" style="fill:var(--paper);stroke:var(--ink);stroke-width:2"/>'
    o += '<path d="M430 34V104H500" style="fill:none;stroke:var(--ink);stroke-width:1.5"/>'
    o += t(126,72,'CARTA · CPC 260',size=13,weight=700)
    o += t(126,118,'JUÍZO DE ORIGEM',size=10,fill='var(--ink-2)',weight=600)
    o += t(126,140,'JUÍZO DE CUMPRIMENTO',size=10,fill='var(--ink-2)',weight=600)
    o += line(126,156,474,156,w=1)
    o += t(126,184,'ATO OBJETO',size=10,fill='var(--dif)',weight=700)
    o += line(126,198,460,198,tone='muted',w=1)
    o += line(126,210,430,210,tone='muted',w=1)
    o += t(126,245,'PEÇAS',size=10,fill='var(--ink-2)',weight=700)
    o += t(126,267,'PETIÇÃO · DESPACHO · PROCURAÇÃO',size=10,weight=600)
    o += t(126,302,'PRAZO · INTIMAÇÃO DA EXPEDIÇÃO',size=10,weight=600)
    o += line(126,326,460,326,w=1)
    o += t(126,350,'ASSINATURA DO JUIZ',size=10,fill='var(--ink-2)',weight=600)
    o += line(126,360,276,360,w=1)
    o += t(28,435,'RECUSA: REQUISITO AUSENTE · INCOMPETÊNCIA · DÚVIDA DE AUTENTICIDADE',size=10,fill='var(--conc)',weight=700)
    o += t(28,462,'DECISÃO MOTIVADA  ·  DEVOLUÇÃO / REMESSA COMPETENTE',size=10,weight=600)
    o += t(28,489,'CARTA CUMPRIDA → RETORNO EM 10 DIAS',size=10,fill='var(--ink-2)',weight=600)
    return svg('18 14 564 500',o,cls='fig',ident='pci-a06-letter',label='Espécime material de carta precatória com juízos, objeto, peças, prazo, intimação e assinatura, acompanhado dos fundamentos de recusa e retorno')

if __name__ == '__main__':
    print(protocol()); print(carta())
