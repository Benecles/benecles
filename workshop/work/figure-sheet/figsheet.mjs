#!/usr/bin/env node
// Figure contact sheet: every <figure> on the given pages, cropped and laid out on ONE labelled image,
// so a reviewer (CEO, orchestrator, or a writer before handing in) judges all figures in one look.
//   node work/figure-sheet/figsheet.mjs --base-url http://127.0.0.1:8796 --out /tmp/sheet.png \
//        courses/processo-civil-i/aula-14.html courses/processo-civil-i/aula-15.html ...
// Options: --cols 4 (tiles per row) · --tile 560 (tile width px) · --width 1440 (page viewport)
// Also writes OUT_DIR/<sheet>-crops/<page>-fig<N>.png for a closer look at any single figure.
import { createRequire } from 'node:module';
import fs from 'node:fs/promises';
import path from 'node:path';
const require = createRequire(import.meta.url);
const { chromium } = require('/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

const args = process.argv.slice(2), opt = { cols: 4, tile: 560, width: 1440 }, pages = [];
for (let i = 0; i < args.length; i++) {
  const a = args[i];
  if (a === '--base-url') opt.base = args[++i]; else if (a === '--out') opt.out = args[++i];
  else if (a === '--cols') opt.cols = +args[++i]; else if (a === '--tile') opt.tile = +args[++i];
  else if (a === '--width') opt.width = +args[++i]; else pages.push(a);
}
if (!opt.base || !opt.out || !pages.length) { console.error('usage: figsheet.mjs --base-url URL --out sheet.png page.html ...'); process.exit(2); }
const cropDir = opt.out.replace(/\.png$/, '') + '-crops';
await fs.mkdir(cropDir, { recursive: true });

const browser = await chromium.launch({ headless: true, executablePath: CHROME });
const ctx = await browser.newContext({ viewport: { width: opt.width, height: 1000 }, deviceScaleFactor: 1, serviceWorkers: 'block', reducedMotion: 'reduce' });
const page = await ctx.newPage();
const tiles = [];
for (const p of pages) {
  const short = path.basename(p, '.html');
  await page.goto(new URL(p, opt.base.replace(/\/?$/, '/')).href, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts && document.fonts.ready);
  const figs = await page.$$('figure');
  let n = 0;
  for (const f of figs) {
    const box = await f.boundingBox();
    if (!box || box.width < 40 || box.height < 40) continue;
    n++;
    await f.scrollIntoViewIfNeeded(); await page.waitForTimeout(400);   // let draw/pop animations settle
    const file = path.join(cropDir, `${short}-fig${n}.png`);
    await f.screenshot({ path: file });
    const cap = (await f.evaluate(el => (el.querySelector('figcaption')?.textContent || '').trim())).slice(0, 90);
    tiles.push({ label: `${short} · Fig. ${n}`, cap, file });
  }
  if (!n) tiles.push({ label: `${short} · no figures`, cap: '', file: null });
}

// lay the crops out in a grid and screenshot the grid
const cells = await Promise.all(tiles.map(async t => {
  const img = t.file ? `<img src="data:image/png;base64,${(await fs.readFile(t.file)).toString('base64')}">` : '<div class="none">sem figuras</div>';
  const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;');
  return `<div class="t"><div class="im">${img}</div><b>${esc(t.label)}</b><i>${esc(t.cap)}</i></div>`;
}));
const W = opt.cols * (opt.tile + 24) + 24;
await page.setViewportSize({ width: W, height: 800 });
await page.setContent(`<style>body{margin:0;padding:12px;background:#d9d5cb;font:13px/1.3 Menlo,monospace;display:grid;grid-template-columns:repeat(${opt.cols},${opt.tile}px);gap:12px}
.t{background:#fff;padding:8px;border:1px solid #9a9488}.im{height:${Math.round(opt.tile * .72)}px;display:flex;align-items:center;justify-content:center;background:#f4f1ea;overflow:hidden}
.im img{max-width:100%;max-height:100%;object-fit:contain}.none{color:#b8603f}b{display:block;margin-top:6px}i{display:block;color:#555;font-style:normal;font-size:11px;height:2.6em;overflow:hidden}</style>${cells.join('')}`);
await page.screenshot({ path: opt.out, fullPage: true });
await browser.close();
console.log(`${tiles.filter(t => t.file).length} figures from ${pages.length} pages -> ${opt.out} (crops in ${cropDir})`);
