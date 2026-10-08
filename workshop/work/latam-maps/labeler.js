window.placeLabels = function(svg, opts={}) {
  const VB = svg.viewBox.baseVal;
  const pts = [];
  svg.querySelectorAll(opts.routes||'path.draw').forEach(p => { const L = p.getTotalLength(); for (let s = 0; s <= L; s += 3) { const q = p.getPointAtLength(s); pts.push([q.x, q.y]); } });
  const rects = [...(opts.blocks||[])];
  const groups = [...svg.querySelectorAll(opts.groups||'g.pop')].filter(g => g.querySelector('circle') && [...g.querySelectorAll('text')].some(t=>t.textContent.trim()));
  svg.querySelectorAll('g.pop rect').forEach(r=>{const b=r.getBBox(); if(b.width>100) rects.push([b.x-6,b.y-6,b.width+12,b.height+12]);});
  const pins = groups.map(g => { const c = g.querySelector('circle'); return [+c.getAttribute('cx'), +c.getAttribute('cy')]; });
  const pinRects = pins.map(([x,y])=>[x-10,y-10,20,20]);
  const ov = (A, B) => Math.max(0, Math.min(A[0]+A[2], B[0]+B[2]) - Math.max(A[0], B[0])) * Math.max(0, Math.min(A[1]+A[3], B[1]+B[3]) - Math.max(A[1], B[1]));
  const out = []; const placed = [];
  const order = groups.map((g,i)=>i);
  order.forEach(gi => { const g = groups[gi];
    const ts = [...g.querySelectorAll('text')].filter(t=>t.textContent.trim());
    const W = Math.max(...ts.map(t => t.getComputedTextLength())), H = 18*ts.length;
    const [px, py] = pins[gi];
    let best = null;
    for (const r of [16, 24, 34, 48, 66, 90, 120, 150]) for (let a = 0; a < 360; a += 10) {
      const rad = a * Math.PI / 180, ax = px + r * Math.cos(rad), ay = py + r * Math.sin(rad);
      const anchor = Math.cos(rad) > .3 ? 'start' : Math.cos(rad) < -.3 ? 'end' : 'middle';
      const x0 = anchor === 'start' ? ax : anchor === 'end' ? ax - W : ax - W / 2;
      const y0 = Math.sin(rad) > .3 ? ay : Math.sin(rad) < -.3 ? ay - H : ay - H / 2;
      const box = [x0 - 5, y0 - 3, W + 10, H + 6];
      if (box[0] < VB.x + 8 || box[1] < VB.y + 6 || box[0] + box[2] > VB.x + VB.width - 8 || box[1] + box[3] > VB.y + VB.height - 6) continue;
      let cost = r * 0.5;
      for (const [qx, qy] of pts) if (qx > box[0] && qx < box[0] + box[2] && qy > box[1] && qy < box[1] + box[3]) cost += 300;
      for (const R of rects) cost += ov(box, R) * 5;
      pinRects.forEach((R,j)=>{ cost += ov(box,R)*10; });
      for (const B of placed) cost += ov(box, B) * 20;
      const lead = r > 26;
      if (lead) { for (const [qx, qy] of pts) { const t = ((qx-px)*(ax-px)+(qy-py)*(ay-py))/((ax-px)**2+(ay-py)**2); if (t>0.2&&t<1){const dx=px+t*(ax-px)-qx, dy=py+t*(ay-py)-qy; if (dx*dx+dy*dy<6) cost+=200;} } }
      if (!best || cost < best.cost) best = { cost, anchor, ax, ay, x0, y0, box, r, W, H, lead };
    }
    placed.push(best.box);
    const tx = best.anchor==='start'?best.x0:best.anchor==='end'?best.x0+best.W:best.x0+best.W/2;
    out.push({ gi, text: ts.map(t=>t.textContent), pin: [px, py], anchor: best.anchor, tx: Math.round(tx*10)/10, ty: Math.round((best.y0 + 14)*10)/10, r: best.r, cost: Math.round(best.cost), lead: best.lead ? [Math.round(best.ax*10)/10, Math.round(best.ay*10)/10] : null });
  });
  return out;
};
window.applyLabels = function(svg, res, opts={}){
  const groups = [...svg.querySelectorAll(opts.groups||'g.pop')].filter(g => g.querySelector('circle') && [...g.querySelectorAll('text')].some(t=>t.textContent.trim()));
  res.forEach(o=>{ const g=groups[o.gi]; const ts=[...g.querySelectorAll('text')].filter(t=>t.textContent.trim());
    ts.forEach((t,i)=>{t.setAttribute('x',o.tx); t.setAttribute('y',o.ty+i*18); t.setAttribute('text-anchor',o.anchor);});
    let l=g.querySelector('path'); if(o.lead){ if(!l){l=document.createElementNS('http://www.w3.org/2000/svg','path'); l.setAttribute('style','fill:none;stroke:var(--ink-2);stroke-width:.9'); g.insertBefore(l,ts[0]);} l.setAttribute('d',`M${o.pin[0]} ${o.pin[1]}L${o.lead[0]} ${o.lead[1]}`);} else if(l) l.remove(); });
};
window.joinRoutes = svg => svg.querySelectorAll('path.draw').forEach(p=>{const d=p.getAttribute('d'); p.setAttribute('d', d[0]+d.slice(1).replace(/M/g,'L'));});
window.still = svg => { svg.querySelectorAll('.draw,.pop,.fade').forEach(e=>{e.style.animation='none';e.style.opacity=1;e.style.strokeDashoffset=0;}); };
'loaded'
window.probe = function(svg, sel='path.draw'){
  const pts=[]; svg.querySelectorAll(sel).forEach((p,i)=>{const L=p.getTotalLength(); for(let s=0;s<=L;s+=2){const q=p.getPointAtLength(s); pts.push([q.x,q.y,i]);}});
  const hits=[]; svg.querySelectorAll('text').forEach(t=>{ if(!t.textContent.trim()) return; const b=t.getBBox(); if(!b.width) return; const n=pts.filter(([x,y])=>x>b.x+1&&x<b.x+b.width-1&&y>b.y+2&&y<b.y+b.height-1).length; if(n) hits.push([t.textContent.trim().slice(0,30),n]); });
  // label-label overlaps
  const bs=[...svg.querySelectorAll('text')].filter(t=>t.textContent.trim()).map(t=>[t.textContent.trim().slice(0,20),t.getBBox()]);
  const ov=[]; for(let i=0;i<bs.length;i++)for(let j=i+1;j<bs.length;j++){const a=bs[i][1],b=bs[j][1]; const w=Math.min(a.x+a.width,b.x+b.width)-Math.max(a.x,b.x), h=Math.min(a.y+a.height,b.y+b.height)-Math.max(a.y,b.y); if(w>1&&h>2) ov.push([bs[i][0],bs[j][0]]);}
  return {hits, ov};
};
window.nudge = function(svg, textContent, isos, prefix='lm-', R=40){
  const t=[...svg.querySelectorAll('text')].find(x=>x.textContent.trim()===textContent);
  const pts=[]; isos.forEach(k=>{const p=document.getElementById(prefix+k); if(!p) return; const L=p.getTotalLength(); for(let s=0;s<=L;s+=1.5){const q=p.getPointAtLength(s); pts.push([q.x,q.y]);}});
  const x0=+t.getAttribute('x'), y0=+t.getAttribute('y'); let best=null;
  for(let dx=-R;dx<=R;dx+=3) for(let dy=-R;dy<=R;dy+=3){ t.setAttribute('x',x0+dx); t.setAttribute('y',y0+dy); const b=t.getBBox(); const pad=2; const n=pts.filter(([x,y])=>x>b.x-pad&&x<b.x+b.width+pad&&y>b.y&&y<b.y+b.height).length; const c=n*100+Math.hypot(dx,dy); if(!best||c<best.c) best={c,dx,dy,n}; }
  t.setAttribute('x',x0+best.dx); t.setAttribute('y',y0+best.dy); return [textContent,x0,y0,best];
};
