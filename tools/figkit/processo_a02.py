"""Aula 02: measured docket for the Art. 334 hearing intervals."""
import os
import re
from pathlib import Path

from figkit import Timeline, line, svg, t
import figkit


def panel():
    scale = Timeline("pci-a02-s5", 95, 1005, 160, -30, 0, step=10)
    scale.event(-30, 78, "designação", tone="dif", sub="juiz · audiência", anchor="start")
    scale.event(-20, 60, "citação", tone="ink", sub="juízo · réu", anchor="middle", mark="circle")
    scale.event(-10, 78, "petição", tone="conc", sub="réu · desinteresse", anchor="middle", mark="circle")
    scale.event(0, 60, "audiência", tone="ink", sub="dia zero", anchor="end")

    o = t(550, 27, "ART. 334 · MARCOS EM RELAÇÃO À AUDIÊNCIA", size=12,
          fill="var(--ink-2)", anchor="middle", weight=600, caps=True)
    o += scale.svg()

    x30, x20, x0 = scale.x(-30), scale.x(-20), scale.x(0)
    o += line(x30, 226, x0, 226, tone="dif", w=1.8)
    o += line(x30, 219, x30, 233, tone="dif", w=1.8)
    o += line(x0, 219, x0, 233, tone="dif", w=1.8)
    o += t((x30 + x0) / 2, 218, "designação · mínimo 30 dias",
           size=11.5, fill="var(--dif)", anchor="middle", weight=700, ls=".02em")

    o += line(x20, 270, x0, 270, tone="conc", w=1.8)
    o += line(x20, 263, x20, 277, tone="conc", w=1.8)
    o += line(x0, 263, x0, 277, tone="conc", w=1.8)
    o += t((x20 + x0) / 2, 262, "citação · mínimo 20 dias",
           size=11.5, fill="var(--conc)", anchor="middle", weight=700, ls=".02em")

    return svg(
        "35 10 1030 290",
        o,
        cls="fig",
        ident="pci-a02-s5",
        label=(
            "Escala relativa ao dia da audiência, em zero. O juiz designa com pelo menos "
            "30 dias de antecedência; o réu é citado pelo menos 20 dias antes; o réu "
            "pode protocolar o desinteresse com 10 dias de antecedência."
        ),
    )


def probe_page():
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Figkit · Processo Aula 02</title>
<link rel="stylesheet" href="../courses/processo-civil-i/assets/curso.css"><link rel="stylesheet" href="../assets/casa.css">
<style>body{{margin:0;background:var(--paper);color:var(--ink)}}.figure-card{{width:min(1083px,calc(100vw - 96px));margin:34px auto;padding:16px 20px 12px;background:var(--paper);border:1.5px solid var(--ink);box-shadow:6px 6px 0 var(--grid-major)}}.figure-card svg{{display:block;width:100%;height:auto}}.figure-card figcaption{{max-width:70ch;margin:10px auto 0;font:500 12px/1.5 var(--mono);color:var(--ink-2)}}@media(max-width:1099px) and (orientation:portrait){{.figure-card{{width:calc(100vw - 32px)}}}}</style></head><body>
<figure class="figure-card">{panel()}<figcaption>A audiência tem prazos mínimos diferentes para designação, citação e manifestação do réu.</figcaption></figure>
</body></html>"""


def inject_page():
    root = Path(__file__).resolve().parents[2]
    page = root / "courses/processo-civil-i/aula-02.html"
    text = page.read_text(encoding="utf-8")
    marker = "<!-- FIGURE: PCI-A02 -->"
    if text.count(marker) == 1:
        text = text.replace(marker, panel())
    else:
        text, count = re.subn(r'<svg id="pci-a02-s5".*?</svg>', panel(), text, count=1, flags=re.S)
        if count != 1:
            raise SystemExit(f"Expected one figure marker or SVG in {page}")
    page.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    figkit.WARN.clear()
    probe = os.environ.get("FIGKIT_PROBE")
    if probe:
        Path(probe).write_text(probe_page(), encoding="utf-8")
        print(probe)
    else:
        inject_page()
    print("\n".join(figkit.WARN) or "no text warnings")
