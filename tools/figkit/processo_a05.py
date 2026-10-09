"""Regenerate the two inline figures in Processo Civil I Aula 05.

The SVGs remain in the lesson as the editable source. This page-specific generator
applies the route and crop-safe label geometry, then writes only those SVG elements.
Run: python3 tools/figkit/processo_a05.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / 'courses' / 'processo-civil-i' / 'aula-05.html'


def svg_for(source, title_id):
    m = re.search(r'<svg\b[^>]*aria-labelledby="' + re.escape(title_id) + r'[^\"]*"[^>]*>', source)
    if not m:
        raise SystemExit(f'Aula 05: figure root for {title_id} not found')
    depth = 0
    for tag in re.finditer(r'<svg\b|</svg>', source[m.start():]):
        depth += 1 if tag.group(0) == '<svg' else -1
        if depth == 0:
            return m.start(), m.start() + tag.end(), source[m.start():m.start() + tag.end()]
    raise SystemExit(f'Aula 05: unclosed SVG for {title_id}')


def fig1(svg):
    svg = re.sub(r'<svg\b', '<svg id="pci-a05-cobranca-route"', svg, count=1) if 'id="pci-a05-cobranca-route"' not in svg else svg
    if '<marker id="a05-cobranca-arrow"' not in svg:
        svg = svg.replace('<title id="a05fig1-title">', '<defs><marker id="a05-cobranca-arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0 0L10 5L0 10Z" fill="var(--ink)"/></marker></defs><title id="a05fig1-title">', 1)
    route = '<path d="M534 240H650V368H750" fill="none" stroke="var(--ink)" stroke-width="5" marker-end="url(#a05-cobranca-arrow)"/>'
    svg = svg.replace(route, '')
    base = '<path d="M534 240H650M650 112V368" fill="none" stroke="var(--grid-major)" stroke-width="3"/>'
    if base not in svg:
        raise SystemExit('Aula 05 Fig. 1: expected pale network path not found')
    svg = svg.replace(base, base + route, 1)
    return svg


def fig2(svg):
    svg = re.sub(r'<svg\b', '<svg id="pci-a05-idpj-timing"', svg, count=1) if 'id="pci-a05-idpj-timing"' not in svg else svg
    svg = svg.replace('x="960" y="214" text-anchor="middle"', 'x="875" y="214" text-anchor="start"')
    svg = svg.replace('x="960" y="239" text-anchor="middle"', 'x="875" y="239" text-anchor="start"')
    svg = svg.replace('x="960" y="376" text-anchor="middle"', 'x="875" y="376" text-anchor="start"')
    svg = svg.replace('x="960" y="401" text-anchor="middle"', 'x="875" y="401" text-anchor="start"')
    for y in ('214', '239', '376', '401'):
        svg = svg.replace(f'x="840" y="{y}" text-anchor="start"', f'x="875" y="{y}" text-anchor="start"')
    return svg


def main():
    source = PAGE.read_text(encoding='utf-8')
    replacements = []
    for title, make in [('a05fig1-title', fig1), ('a05fig2-title', fig2)]:
        start, end, svg = svg_for(source, title)
        replacements.append((start, end, make(svg)))
    for start, end, svg in reversed(replacements):
        source = source[:start] + svg + source[end:]
    PAGE.write_text(source, encoding='utf-8')
    print('Regenerated Aula 05 figures: cobrança route to Francisco; Fig. 2 labels inset.')


if __name__ == '__main__':
    main()
