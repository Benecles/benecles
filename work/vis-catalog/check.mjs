import fs from 'node:fs/promises';
import path from 'node:path';
import { createRequire } from 'node:module';
const require=createRequire(import.meta.url);
const {chromium}=require('/Users/benecles/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const ROOT=process.cwd(), DIR=path.join(ROOT,'work/vis-catalog');
const csv=await fs.readFile(path.join(DIR,'catalog.csv'),'utf8');
const parseCsv=text=>{const records=[];let row=[],value='',quoted=false;for(let i=0;i<text.length;i++){const c=text[i];if(quoted&&c==='\"'&&text[i+1]==='\"'){value+='\"';i++;}else if(c==='\"')quoted=!quoted;else if(c===','&&!quoted){row.push(value);value='';}else if((c==='\n'||c==='\r')&&!quoted){if(c==='\r'&&text[i+1]==='\n')i++;row.push(value);value='';if(row.some(v=>v!==''))records.push(row);row=[];}else value+=c;}if(value!==''||row.length){row.push(value);records.push(row);}return records;};
const records=parseCsv(csv), heads=records.shift(), rows=records.map(a=>Object.fromEntries(a.map((v,i)=>[heads[i],v])));
const ids=rows.map(r=>r.id), unique=new Set(ids);if(unique.size!==ids.length)throw new Error('duplicate catalogue ids');
const browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true});
const ctx=await browser.newContext({viewport:{width:1440,height:1000},colorScheme:'light',reducedMotion:'reduce'}), page=await ctx.newPage();
let eligible=0;const eligibleKeys=new Set();
for(const d of (await fs.readdir(path.join(ROOT,'courses'),{withFileTypes:true})).filter(x=>x.isDirectory()))for(const file of (await fs.readdir(path.join(ROOT,'courses',d.name))).filter(x=>x.endsWith('.html'))){
 await page.goto('file://'+path.join(ROOT,'courses',d.name,file),{waitUntil:'load',timeout:45000});
 const hits=await page.evaluate(()=>{document.querySelectorAll('svg.panel').forEach(s=>{s.style.display='block';s.style.visibility='hidden';});return [...document.querySelectorAll('svg')].map((s,i)=>{const r=s.getBoundingClientRect(),v=(s.getAttribute('viewBox')||'').trim().split(/[ ,]+/).map(Number);return {i:i+1,w:r.width,small:v.length===4&&v[0]===0&&v[1]===0&&v[2]===10&&v[3]===10};}).filter(x=>!x.small&&x.w>=120).map(x=>x.i);});
 for(const i of hits){eligible++;const code=({'controle-de-constitucionalidade':'ctl','direito-constitucional-i':'dci','direito-latino-americano':'dla','metodologia-juridica':'met','processo-civil-i':'pci','teoria-do-delito':'tdl','teoria-geral-dos-contratos':'tgc','processo-penal':'ppn','direito-administrativo':'dad'})[d.name]||d.name.replace(/[^a-z]/g,'').slice(0,3);const pcode=file.replace(/\.html$/,'').replace(/^aula-/,'a').replace(/^unidade-/,'u').replace(/^suplemento-/,'s').replace(/[^a-z0-9]+/g,'-');eligibleKeys.add(`${code}-${pcode}-s${i}`);}
}
const missingRows=[...eligibleKeys].filter(id=>!unique.has(id)), orphanRows=ids.filter(id=>!eligibleKeys.has(id));
const missingThumbs=[];let thumbBytes=0;for(const id of ids){const f=path.join(DIR,'thumbs',id+'.png');try{thumbBytes+=(await fs.stat(f)).size;}catch{missingThumbs.push(id);}}
const sheets=(await fs.readdir(DIR)).filter(f=>f.endsWith('.html'));let sheetCards=0;for(const f of sheets){await page.goto('file://'+path.join(DIR,f),{waitUntil:'load'});const c=await page.locator('a.card').count();sheetCards+=c;if(f==='index.html'&&c!==rows.length)throw new Error(`all figures sheet ${c} != ${rows.length}`);if(f.startsWith('index-')){const genre=f.slice(6,-5),expect=rows.filter(r=>r.genre_guess===genre).length;if(c!==expect)throw new Error(`${f} has ${c} cards, expected ${expect}`);} }
await browser.close();
if(eligible!==rows.length||missingRows.length||orphanRows.length||missingThumbs.length||thumbBytes>=60*1024*1024)throw new Error(JSON.stringify({eligible,rows:rows.length,missingRows:missingRows.slice(0,5),orphanRows:orphanRows.slice(0,5),missingThumbs:missingThumbs.slice(0,5),thumbBytes,sheetCards}));
const counts=Object.fromEntries([...new Set(rows.map(r=>r.genre_guess))].sort().map(g=>[g,rows.filter(r=>r.genre_guess===g).length]));
console.log(JSON.stringify({PASS:true,eligibleSVGs:eligible,catalogueRows:rows.length,uniqueIds:unique.size,thumbnails:ids.length,thumbnailBytes:thumbBytes,sheets:sheets.length,sheetCards,genreCounts:counts},null,2));
