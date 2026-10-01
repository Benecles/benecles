import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';
const require=createRequire(import.meta.url);
const {chromium}=require('/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../..');
const OUT=path.join(ROOT,'work/vis-catalog');
const LIVE='https://benecles.github.io/ordenacoes-filipinas/';
const courseCodes={
 'controle-de-constitucionalidade':'ctl','direito-constitucional-i':'dci','direito-latino-americano':'dla',
 'metodologia-juridica':'met','processo-civil-i':'pci','teoria-do-delito':'tdl',
 'teoria-geral-dos-contratos':'tgc','processo-penal':'ppn','direito-administrativo':'dad'
};
const esc=s=>String(s??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
const csv=s=>'"'+String(s??'').replaceAll('"','""')+'"';
function genre(x){
 const s=(x.text+' '+x.classes+' '+x.aria+' '+x.id).toLowerCase();
 if(/\b(map|mapa|cartogra|geogr|territ|coast|latitude|longitude)\b/.test(s)||x.paths>20&&x.images>0) return 'map';
 if(/timeline|cronolog|linha do tempo|\bdates\b/.test(s))return 'timeline';
 if(/tree|arvore|árvore|genealog|hierarch|hierarquia/.test(s))return 'tree';
 if(/scale|escala|grada|eixo|axis|régua|regua/.test(s)||x.lines>8&&x.rects<4&&x.texts<12)return 'scale';
 if(/decis|fluxo|flow|etapa|processo|decisao|decisão/.test(s)&&x.markers>0)return 'flow-or-decision';
 if(x.markers>2&&x.paths>4&&x.lines>3)return 'flow-or-decision';
 if(/matriz|tabela|quadro|matrix|table|grid/.test(s)||x.rects>=8&&x.texts>=8)return 'matrix-or-table';
 if(/camada|estrato|strata|stack|pirâmide|piramide/.test(s)||x.rects>=3&&x.rects>=x.texts/2)return 'strata-or-stack';
 if(/compar|contraste|versus|diferença|diferenca/.test(s)||x.rects>=2&&x.texts>=6&&x.ratio>1.35)return 'comparison';
 if(/rota|trajeto|percurso|linha|route|rail|estrada|caminho/.test(s)||x.lines>3&&x.ratio>1.4)return 'route-or-line';
 return 'other';
}
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const context=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'light',reducedMotion:'reduce',deviceScaleFactor:1});
const page=await context.newPage();
const dirs=(await fs.readdir(path.join(ROOT,'courses'),{withFileTypes:true})).filter(d=>d.isDirectory()).map(d=>d.name).sort();
let rows=[];
for(const course of dirs){
 const dir=path.join(ROOT,'courses',course);
 const pages=(await fs.readdir(dir)).filter(f=>f.endsWith('.html')).sort();
 for(const file of pages){
  const abs=path.join(dir,file);
  await page.goto('file://'+abs,{waitUntil:'load',timeout:45000}).catch(async()=>await page.goto('file://'+abs,{waitUntil:'domcontentloaded',timeout:45000}));
  await page.evaluate(()=>document.fonts?.ready);
  const pageInfo=await page.evaluate(()=>({title:document.title,bodyClass:document.body.className}));
  const items=await page.evaluate(()=>{
   document.querySelectorAll('svg.panel').forEach(s=>{s.style.display='block';s.style.visibility='hidden';});
   return [...document.querySelectorAll('svg')].map((svg,index)=>{
   const r=svg.getBoundingClientRect(), view=svg.getAttribute('viewBox')||'', parts=view.trim().split(/[ ,]+/).map(Number), cls=svg.getAttribute('class')||'';
   const w=r.width||parseFloat(svg.getAttribute('width'))||0,h=r.height||parseFloat(svg.getAttribute('height'))||0;
   const text=[...svg.querySelectorAll('text')].map(t=>t.textContent.trim()).filter(Boolean).join(' ');
   const rects=svg.querySelectorAll('rect').length, lines=svg.querySelectorAll('line,polyline').length, paths=svg.querySelectorAll('path').length, markers=svg.querySelectorAll('marker').length;
   const colors=new Set(); for(const e of [svg,...svg.querySelectorAll('*')]){const c=getComputedStyle(e);for(const v of [c.fill,c.stroke])if(v&&v!=='none'&&v!=='rgba(0, 0, 0, 0)')colors.add(v);}
   const figure=svg.closest('figure'), caption=figure?.querySelector('figcaption')?.innerText?.trim()||'';
   const ancestors=[];for(let e=svg.parentElement;e&&e!==document.body;e=e.parentElement)ancestors.push(e.className?.baseVal||e.className||'');
   return {index:index+1,view,w,h,smallView:parts.length===4&&parts[0]===0&&parts[1]===0&&parts[2]===10&&parts[3]===10,cls,id:svg.id||'',aria:svg.getAttribute('aria-label')||'',caption,text,rects,lines,paths,markers,colors:[...colors].sort(),elements:svg.querySelectorAll('*').length,texts:svg.querySelectorAll('text').length,bytes:new TextEncoder().encode(svg.outerHTML).length,ratio:w/h,ancestors,front:location.pathname.endsWith('/index.html')||location.pathname.endsWith('/front.html')};
  });
  });
  for(const item of items){
   if(item.smallView||item.w<120)continue;
   const isPanel=/\bpanel\b/.test(item.cls)||item.ancestors.some(a=>/panel/.test(a));
   const kind=item.front?'front':(/hero/.test(item.cls)||/hero/.test(item.ancestors.join(' '))?'hero':(isPanel?'panel':'other'));
   const code=courseCodes[course]||course.replace(/[^a-z]/g,'').slice(0,3);
   const pcode=file.replace(/\.html$/,'').replace(/^aula-/,'a').replace(/^unidade-/,'u').replace(/^suplemento-/,'s').replace(/[^a-z0-9]+/g,'-');
   const id=`${code}-${pcode}-s${item.index}`;
   await page.evaluate(({index})=>{
    const svg=document.querySelectorAll('svg')[index-1];
    document.querySelectorAll('.panel').forEach(p=>p.classList.remove('on'));
    document.querySelectorAll('svg').forEach(s=>{if(s!==svg){s.style.visibility='hidden';s.style.display='none';}});
    svg.style.display='block';svg.style.visibility='visible';svg.style.width='320px';svg.style.height='auto';svg.style.maxWidth='none';svg.style.opacity='1';svg.style.position='static';svg.style.transform='none';
    if(svg.classList.contains('panel'))svg.classList.add('on');
   },{index:item.index});
   const svg=page.locator('svg').nth(item.index-1);
   const box=await svg.boundingBox();
   if(!box||box.width<100)throw new Error(`Missing drawable box ${id} ${JSON.stringify(box)}`);
   const thumb=path.join(OUT,'thumbs',id+'.png');await fs.mkdir(path.dirname(thumb),{recursive:true});
   await svg.screenshot({path:thumb,animations:'disabled',timeout:30000});
   const cap=item.caption||item.aria;
   const structure={text:item.text,classes:item.cls,aria:item.aria,id:item.id,paths:item.paths,lines:item.lines,markers:item.markers,rects:item.rects,texts:item.texts,ratio:item.ratio};
   let generator='inline';
   if(item.front)generator='front build';
   else if((await fs.stat(path.join(ROOT,'courses',course,'maps.py')).catch(()=>null)))generator='maps.py';
   rows.push({id,course,page:file,svg_index:item.index,kind,caption:cap,bytes:item.bytes,element_count:item.elements,distinct_colours:item.colors.length,text_count:item.texts,generator,genre_guess:genre(structure),live_url:LIVE+`courses/${course}/${file}`,_thumbBytes:(await fs.stat(thumb)).size});
  }
 }
}
await browser.close();
rows.sort((a,b)=>a.genre_guess.localeCompare(b.genre_guess)||a.course.localeCompare(b.course)||a.page.localeCompare(b.page)||a.svg_index-b.svg_index);
const cols=['id','course','page','svg_index','kind','caption','bytes','element_count','distinct_colours','text_count','generator','genre_guess'];
await fs.writeFile(path.join(OUT,'catalog.csv'),[cols.join(','),...rows.map(r=>cols.map(k=>csv(r[k])).join(','))].join('\n')+'\n');
const genreNames=[...new Set(rows.map(r=>r.genre_guess))].sort();
function sheet(group,title){let cards='';for(let i=0;i<group.length;i+=6){cards+='<div class="row">'+group.slice(i,i+6).map(r=>`<a class="card" href="${esc(r.live_url)}"><img loading="lazy" src="thumbs/${esc(r.id)}.png"><b>${esc(r.id)}</b><small>${r.element_count} elements · ${esc(r.caption)}</small></a>`).join('')+'</div>';}
return `<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>${esc(title)} · figure catalogue</title><style>body{font:14px system-ui;background:#f6f4ef;color:#222;margin:28px}h1{font-size:24px}nav{display:flex;gap:12px;flex-wrap:wrap;margin:16px 0 28px}nav a{color:#694b35}.row{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:12px;margin:0 0 14px}.card{box-sizing:border-box;background:#fff;border:1px solid #ddd;padding:9px;color:inherit;text-decoration:none;min-width:0}.card img{width:100%;height:180px;object-fit:contain;background:#fffdf8}.card b,.card small{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.card small{font-size:11px;color:#666;margin-top:4px}@media(max-width:900px){.row{grid-template-columns:repeat(3,minmax(0,1fr))}}@media(max-width:520px){.row{grid-template-columns:repeat(2,minmax(0,1fr))}}</style><h1>${esc(title)} (${group.length})</h1><nav>${genreNames.map(g=>`<a href="index-${g}.html">${g} (${rows.filter(r=>r.genre_guess===g).length})</a>`).join('')}<a href="index.html">all figures (${rows.length})</a></nav><p>Genre labels are heuristic guesses based on text and SVG structure, including element counts, markers, and line or axis cues.</p>${cards}</html>`}
await fs.writeFile(path.join(OUT,'index.html'),sheet(rows,'All figures'));
for(const g of genreNames)await fs.writeFile(path.join(OUT,`index-${g}.html`),sheet(rows.filter(r=>r.genre_guess===g),g));
const total=rows.reduce((n,r)=>n+r._thumbBytes,0);const counts=Object.fromEntries(genreNames.map(g=>[g,rows.filter(r=>r.genre_guess===g).length]));
console.log(JSON.stringify({figures:rows.length,thumbnailBytes:total,genreCounts:counts,pages:dirs.length},null,2));
