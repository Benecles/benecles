window.__check = (doc, win) => {
  const out = { page: win.location.pathname.split('/').pop(), problems: [] };
  const P = (m) => out.problems.push(m);
  const ids = [...doc.querySelectorAll('[id]')].map(e => e.id);
  const dup = ids.filter((v, i) => ids.indexOf(v) !== i);
  if (dup.length) P('duplicate ids: ' + [...new Set(dup)].join(','));
  doc.querySelectorAll('.step').forEach((s, i) => {
    const id = s.dataset.panel;
    if (!id || !doc.getElementById(id)) P('step ' + i + ' bad data-panel ' + id);
    if (!s.querySelector('.src')) P('step ' + i + ' missing .src');
  });
  doc.querySelectorAll('.scrolly').forEach((b, i) => { if (!b.querySelector('.panel.on')) P('scrolly ' + i + ' no initial .on panel'); });
  [...doc.querySelectorAll('svg.panel, .hero svg')].forEach(svg => {
    const vb = svg.viewBox.baseVal; if (!vb || !vb.width) return;
    const boxes = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim()).map(t => { try { return { t, b: t.getBBox() }; } catch (e) { return null; } }).filter(Boolean);
    const name = svg.id || 'hero';
    boxes.forEach(({ t, b }) => { if (b.x < vb.x - 1 || b.x + b.width > vb.x + vb.width + 1 || b.y < vb.y - 1 || b.y + b.height > vb.y + vb.height + 1) P(name + ': out of bounds "' + t.textContent.trim().slice(0, 40) + '"'); });
    for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
      const a = boxes[i].b, c = boxes[j].b;
      const ox = Math.min(a.x + a.width, c.x + c.width) - Math.max(a.x, c.x), oy = Math.min(a.y + a.height, c.y + c.height) - Math.max(a.y, c.y);
      if (ox > 2 && oy > 3) P(name + ': overlap "' + boxes[i].t.textContent.trim().slice(0, 25) + '" × "' + boxes[j].t.textContent.trim().slice(0, 25) + '"');
    }
    const rects = [...svg.querySelectorAll('rect')].map(r => { try { return r.getBBox(); } catch (e) { return null; } }).filter(r => r && r.width < vb.width * 0.95);
    boxes.forEach(({ t, b }) => {
      const sx = b.x + 1, sy = b.y + b.height / 2;
      const host = rects.filter(r => sx >= r.x && sx <= r.x + r.width && sy >= r.y && sy <= r.y + r.height).sort((p, q) => p.width * p.height - q.width * q.height)[0];
      if (host && b.x + b.width > host.x + host.width + 1) P(name + ': overflows box "' + t.textContent.trim().slice(0, 40) + '"');
    });
    if (/fill="#|stroke="#/.test(svg.outerHTML)) P(name + ': hex colour');
  });
  out.steps = doc.querySelectorAll('.step').length; out.panels = doc.querySelectorAll('svg.panel').length; out.julgados = doc.querySelectorAll('.julgado').length; out.srcs = doc.querySelectorAll('.src').length;
  out.words = doc.body.innerText.split(/\s+/).length; out.links = [...doc.querySelectorAll('.endnav a')].map(a => a.getAttribute('href')).join(' ');
  out.hscroll = doc.documentElement.scrollWidth > win.innerWidth + 1;
  return out;
};
window.__runAll = async (pages, w) => {
  const res = [];
  for (const p of pages) {
    const f = document.createElement('iframe'); f.style.cssText = 'position:fixed;left:-3000px;top:0;width:' + (w||1280) + 'px;height:900px'; f.src = p + '?t=' + Date.now(); document.body.appendChild(f);
    const ok = await new Promise(r => { f.onload = () => r(true); setTimeout(() => r(false), 8000); });
    if (!ok) { res.push({ page: p, problems: ['did not load'] }); f.remove(); continue; }
    await new Promise(r => setTimeout(r, 500));
    try { res.push(window.__check(f.contentDocument, f.contentWindow)); } catch (e) { res.push({ page: p, problems: ['error ' + e.message] }); }
    f.remove();
  }
  return res;
};
