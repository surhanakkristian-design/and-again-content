"""Build TINDER_SENTENCES_EN.html (self-contained review page) from slices/*_final.jsonl."""
import json, glob, os, html
H = os.path.dirname(os.path.abspath(__file__))
IDX = json.load(open(os.path.join(H, 'media_index.json')))
rows = []
for p in sorted(glob.glob(os.path.join(H, 'slices', 's*_final.jsonl'))):
    for l in open(p):
        if l.strip():
            r = json.loads(l); m = IDX[str(r['id'])]
            rows.append({'id': r['id'], 'w': m['words'].split(' (')[0], 'g': m['grp'], 'l': m['lvl'], 'c': m['cats'] or '',
                         't': m['media_type'], 'th': m['thumbnail_url'] or '', 'ts': r['ts'], 'fs': r['fs'], 'tp': r['tp'],
                         'fp': r['fp'], 'tone': r['tone'], 'dev': r['device'], 'tense': r['tense'], 'pop': r.get('pop', ''),
                         'd': m['asset_description']})
data = json.dumps(rows, ensure_ascii=False).replace('</', '<\\/')
page = r"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tinder Texts Review</title>
<style>
:root{--bg:#f6f5f2;--card:#fff;--ink:#1d1d1b;--mut:#6b6a66;--line:#e3e1dc;--ok:#1f7a3f;--okbg:#e6f4ea;--no:#b3261e;--nobg:#fbe9e7;--acc:#AC3C72}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#151514;--card:#1f1f1d;--ink:#eceae6;--mut:#a3a19c;--line:#34332f;--ok:#7fd49a;--okbg:#17301f;--no:#f2998f;--nobg:#3a1c19}}
:root[data-theme="dark"]{--bg:#151514;--card:#1f1f1d;--ink:#eceae6;--mut:#a3a19c;--line:#34332f;--ok:#7fd49a;--okbg:#17301f;--no:#f2998f;--nobg:#3a1c19}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.4 -apple-system,system-ui,Segoe UI,sans-serif}
header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:12px 16px;z-index:2}
h1{font-size:18px;margin:0 0 8px}.f{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
select,input{font:inherit;padding:5px 8px;border:1px solid var(--line);border-radius:8px;background:var(--card);color:var(--ink)}
input[type=search]{min-width:0;flex:1 1 160px}select{max-width:100%}.meta{color:var(--mut);font-size:13px}
main{max-width:1100px;margin:0 auto;padding:12px 16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(min(320px,100%),1fr));gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px;display:flex;gap:10px}
.card img{width:84px;height:150px;object-fit:cover;border-radius:8px;background:var(--line);flex:none}
.b{flex:1;min-width:0;overflow-wrap:anywhere}.s{padding:5px 8px;border-radius:8px;margin:3px 0;font-weight:600}
.t{background:var(--okbg);color:var(--ok)}.x{background:var(--nobg);color:var(--no)}
.p{padding:2px 8px;border-radius:6px;margin:3px 0;font-size:14px}.p.t{font-weight:500}.p.x{font-weight:500}
.n{float:right;font-weight:400;font-size:12px;opacity:.8;margin-left:6px}.tag{font-size:12px;color:var(--mut)}
.w{font-weight:700;color:var(--acc)}nav{display:flex;gap:8px;justify-content:center;padding:16px}
button{font:inherit;padding:6px 14px;border-radius:8px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}
details{font-size:12px;color:var(--mut);margin-top:4px}
</style></head><body>
<header><h1>Tinder texts (English)</h1><div class="f">
<select id="g"><option value="">All levels</option><option>A</option><option>B</option></select>
<select id="len"><option value="">All lengths</option><option value="s">TRUE ≤ 30</option><option value="l">TRUE &gt; 30</option></select>
<select id="dev"></select><select id="tone"></select><select id="tense"></select><select id="cat"></select>
<input id="q" type="search" placeholder="Search word, text, id"><span class="meta" id="cnt"></span></div></header>
<main id="m"></main><nav><button id="pv">Previous</button><span class="meta" id="pg"></span><button id="nx">Next</button></nav>
<script>
const D=__DATA__;const $=i=>document.getElementById(i);const PER=60;let page=0,F=D;
function opts(id,key,label){const v=[...new Set(D.map(r=>r[key]))].filter(Boolean).sort();$(id).innerHTML=`<option value="">All ${label}</option>`+v.map(x=>`<option>${x}</option>`).join('')}
opts('dev','dev','devices');opts('tone','tone','tones');opts('tense','tense','tenses');opts('cat','c','categories');
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function apply(){const g=$('g').value,len=$('len').value,dv=$('dev').value,tn=$('tone').value,te=$('tense').value,c=$('cat').value,q=$('q').value.toLowerCase();
F=D.filter(r=>(!g||r.g==g)&&(!len||(len=='s')==(r.ts.length<=30))&&(!dv||r.dev==dv)&&(!tn||r.tone==tn)&&(!te||r.tense==te)&&(!c||r.c==c)&&(!q||(r.id+' '+r.w+' '+r.ts+' '+r.fs+' '+r.tp+' '+r.fp).toLowerCase().includes(q)));page=0;draw()}
function draw(){const n=Math.max(1,Math.ceil(F.length/PER));page=Math.min(page,n-1);$('cnt').textContent=F.length+' media';$('pg').textContent=`Page ${page+1} of ${n}`;
$('m').innerHTML=F.slice(page*PER,page*PER+PER).map(r=>`<div class="card"><img loading="lazy" src="${esc(r.th)}" alt=""><div class="b">
<div class="tag"><span class="w">${esc(r.w)}</span> · #${r.id} · ${r.l} · ${r.t} · ${esc(r.c)}</div>
<div class="s t">${esc(r.ts)}<span class="n">${r.ts.length}</span></div><div class="s x">${esc(r.fs)}<span class="n">${r.fs.length}</span></div>
<div class="p t">${esc(r.tp)}<span class="n">${r.tp.length}</span></div><div class="p x">${esc(r.fp)}<span class="n">${r.fp.length}</span></div>
<div class="tag">${r.tone} · ${r.dev} · ${r.tense}${r.pop?' · '+esc(r.pop):''}</div><details><summary>description</summary>${esc(r.d)}</details></div></div>`).join('');window.scrollTo(0,0)}
['g','len','dev','tone','tense','cat'].forEach(i=>$(i).onchange=apply);$('q').oninput=apply;
$('pv').onclick=()=>{if(page>0){page--;draw()}};$('nx').onclick=()=>{page++;draw()};apply();
</script></body></html>"""
out = os.path.join(H, 'TINDER_SENTENCES_EN.html')
open(out, 'w').write(page.replace('__DATA__', data))
print(out, len(rows))
