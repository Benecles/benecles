#!/usr/bin/env node
/** Figure jank scanner (Claude, 2026-09-30). Read-only against the target site.
 * usage: node jank.mjs --site <site dir> --course <slug> [--course <slug>...] [--page aula-03.html ...] --out <file.csv> [--base-url http://127.0.0.1:8767/]
 * exit code 1 if any panel has tiny/collide/outside/spill > 0 (so workers can loop until 0)
 * For every <figure> in every page of the course, at 390px and 1280px, per SVG panel:
 *   tiny    = labels rendering under 11px on screen
 *   collide = label boxes overlapping another label (>2px both ways)
 *   outside = labels spilling past the SVG's own box
 *   spill   = labels whose centre sits in a <rect> but whose box runs past that rect's edge
 * A figure with any count > 0 is janky; `examples` shows the first offenders. */
import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';
const require = createRequire(import.meta.url);
const { chromium } = require('/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const a = { courses: [], pages: [], base: 'http://127.0.0.1:8767/' };
for (let i = 2; i < process.argv.length; i++) {
  const k = process.argv[i], v = process.argv[++i];
  if (k === '--site') a.site = v; else if (k === '--course') a.courses.push(v); else if (k === '--out') a.out = v; else if (k === '--base-url') a.base = v; else if (k === '--page') a.pages.push(v);
}

const probe = () => {
  const rows = [];
  const figs = [...document.querySelectorAll('body figure')];
  figs.forEach((fig, fi) => {
    const svgs = [...fig.querySelectorAll('svg')].filter(s => !s.parentElement.closest('svg'));
    svgs.forEach((svg, si) => {
      const sr = svg.getBoundingClientRect();
      if (sr.width < 5) return;
      const ctm = svg.getScreenCTM(); if (!ctm) return;
      const scale = Math.hypot(ctm.a, ctm.b);
      const rect = (b, matrix = ctm) => { const p = svg.createSVGPoint(); const pts = [[b.x, b.y], [b.x + b.width, b.y], [b.x, b.y + b.height], [b.x + b.width, b.y + b.height]].map(([x, y]) => { p.x = x; p.y = y; return p.matrixTransform(matrix); });
        const xs = pts.map(q => q.x), ys = pts.map(q => q.y); return { l: Math.min(...xs), r: Math.max(...xs), t: Math.min(...ys), b: Math.max(...ys) }; };
      const clipToNestedViewports = (bounds, text) => {
        let clipped = { ...bounds };
        let ancestor = text.parentElement?.closest('svg');
        while (ancestor && ancestor !== svg) {
          if (getComputedStyle(ancestor).overflow !== 'visible') {
            const viewport = ancestor.getBoundingClientRect();
            clipped = { l: Math.max(clipped.l, viewport.left), r: Math.min(clipped.r, viewport.right),
              t: Math.max(clipped.t, viewport.top), b: Math.min(clipped.b, viewport.bottom) };
            if (clipped.r <= clipped.l || clipped.b <= clipped.t) return null;
          }
          ancestor = ancestor.parentElement?.closest('svg');
        }
        return clipped;
      };
      const texts = [];
      for (const t of svg.querySelectorAll('text')) {
        const s = (t.textContent || '').trim(); if (!s) continue;
        const cs = getComputedStyle(t); if (cs.display === 'none' || cs.visibility === 'hidden') continue;
        let bb; try { bb = t.getBBox(); } catch { continue; } if (!bb.width) continue;
        const own = t.getScreenCTM(); const sc = own ? Math.hypot(own.a, own.b) : scale;
        const bounds = clipToNestedViewports(rect(bb, own || ctm), t);
        if (!bounds) continue;
        texts.push({ s: s.slice(0, 40), r: bounds, px: parseFloat(cs.fontSize) * sc, el: t });
      }
      const boxes = [...svg.querySelectorAll('rect')].map(r => { try { const bb = r.getBBox(); return bb.width > 20 && bb.height > 12 ? rect(bb, r.getScreenCTM() || ctm) : null; } catch { return null; } }).filter(Boolean)
        .filter(b => (b.r - b.l) < sr.width * 0.9);
      const ex = []; let tiny = 0, collide = 0, outside = 0, spill = 0;
      texts.forEach(x => { if (x.px < 10.95) { tiny++; ex.length < 4 && ex.push(`tiny ${x.px.toFixed(1)}px "${x.s}"`); } });
      for (let i = 0; i < texts.length; i++) for (let j = i + 1; j < texts.length; j++) {
        const p = texts[i].r, q = texts[j].r;
        const ox = Math.min(p.r, q.r) - Math.max(p.l, q.l), oy = Math.min(p.b, q.b) - Math.max(p.t, q.t);
        if (ox > 2 && oy > 2) { collide++; ex.length < 4 && ex.push(`collide "${texts[i].s}" × "${texts[j].s}"`); }
      }
      texts.forEach(x => { const r = x.r; if (r.l < sr.left - 2 || r.r > sr.right + 2 || r.t < sr.top - 2 || r.b > sr.bottom + 2) { outside++; ex.length < 4 && ex.push(`outside "${x.s}"`); } });
      texts.forEach(x => { const cx = (x.r.l + x.r.r) / 2, cy = (x.r.t + x.r.b) / 2;
        const host = boxes.filter(b => cx > b.l && cx < b.r && cy > b.t && cy < b.b).sort((m, n) => (m.r - m.l) * (m.b - m.t) - (n.r - n.l) * (n.b - n.t))[0];
        if (host && (x.r.l < host.l - 2 || x.r.r > host.r + 2)) { spill++; ex.length < 4 && ex.push(`spill "${x.s}"`); } });
      const cap = fig.querySelector('figcaption');
      rows.push({ fig: fi + 1, panel: si + 1, caption: cap ? cap.textContent.trim().replace(/\s+/g, ' ').slice(0, 60) : '', labels: texts.length, tiny, collide, outside, spill, examples: ex.join(' | ') });
    });
  });
  return rows;
};

const browser = await chromium.launch({ executablePath: CHROME, headless: true });
let bad = 0;
const out = ['course,page,viewport,fig,panel,caption,labels,tiny,collide,outside,spill,examples'];
const q = s => '"' + String(s).replace(/"/g, '""') + '"';
for (const course of a.courses) {
  const pages = (await fs.readdir(path.join(a.site, 'courses', course))).filter(f => /\.html$/.test(f) && f !== 'index.html' && !/cartoes|original|\.pre-/.test(f)).filter(f => !a.pages.length || a.pages.includes(f)).sort();
  for (const vp of [{ n: 'phone', w: 390, h: 844 }, { n: 'desktop', w: 1280, h: 960 }]) {
    const ctx = await browser.newContext({ viewport: { width: vp.w, height: vp.h } });
    const page = await ctx.newPage();
    for (const p of pages) {
      try {
        await page.goto(new URL(`courses/${course}/${p}`, a.base).href, { waitUntil: 'load', timeout: 30000 });
        await page.evaluate(() => document.fonts && document.fonts.ready);
        for (const r of await page.evaluate(probe)) (r.tiny + r.collide + r.outside + r.spill > 0 && bad++), out.push([course, p, vp.n, r.fig, r.panel, q(r.caption), r.labels, r.tiny, r.collide, r.outside, r.spill, q(r.examples)].join(','));
      } catch (e) { out.push([course, p, vp.n, 0, 0, q('LOAD ERROR ' + e.message.slice(0, 60)), 0, 0, 0, 0, 0, '""'].join(',')); }
    }
    await ctx.close();
  }
}
await browser.close();
await fs.writeFile(a.out, out.join('\n') + '\n');
console.log(`${out.length - 1} panel rows, ${bad} janky → ${a.out}`);
process.exit(bad ? 1 : 0);
