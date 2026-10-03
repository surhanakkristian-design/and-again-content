# A31: distractor lists per video (key word) = other key words of the same group and level
# minus: R1 words linked to the same media, R2 same translation / display form in any of the
# 9 languages, R3 same English stem or shared content token, R4 the word (or an inflected form)
# occurs in the video's description or transcript, R5 the look's "generic" words of the
# group+level, R6 the look's per-video exclusions, R7 second-look removals (audit_removed.json).
from load import *
import json,re,glob,os,statistics
A=json.load(open("out/media_assign.json")); A={int(k):v for k,v in A.items()}
links=collections.defaultdict(set)
for r in cm: links[r["media_id"]].add(r["concept_id"])
STOP=set("a an the to of up out in on off at for with be get go do make take have one's your someone something sb sth and or over down away back into from by".split())
def norm(s): return re.sub(r"\s+"," ",re.sub(r"[^\w\s]"," ",(s or "").casefold())).strip()
def stem(t):
    for suf in ("ing","ed","es","s","er","ly"):
        if t.endswith(suf) and len(t)-len(suf)>=3: return t[:-len(suf)]
    return t
def toks(w): return {stem(t) for t in norm(w).split() if t not in STOP}
def forms(c):
    out=set()
    for l,r in loc[c].items():
        for v in (r["translation"],r["display_form"]):
            if v: out.add((l,norm(v)))
    return out
F={}; T={}
def same_tr(a,b):
    for c in (a,b):
        if c not in F: F[c]=forms(c)
    return bool(F[a]&F[b])
def text_has(word,text):
    ts=[t for t in norm(word).split() if t not in STOP]
    if not ts: return False
    tt={stem(t) for t in text.split()}
    return all(stem(t) in tt for t in ts)
look={}; generic=collections.defaultdict(set); missing=[]
for name in json.load(open("packets/dist/index.json")):
    f=f"packets/dist_out/{name}.json"
    if not os.path.exists(f): missing.append(name); continue
    o=json.load(open(f)); g,lv=int(name[1:3]),name[4]
    generic[(g,lv)]|={int(x) for x in o.get("generic",[])}
    for m,xs in o["exclude"].items(): look[int(m)]={int(x) for x in xs}
aud={}
if os.path.exists("out/audit_removed.json"): aud={int(k):set(v) for k,v in json.load(open("out/audit_removed.json")).items()}
pool=collections.defaultdict(set)
for m,a in A.items(): pool[(a["group"],a["level"])].add(a["concept"])
res={}; why=collections.Counter(); nolook=[]
for m,a in A.items():
    key=a["concept"]; text=norm((media[m]["asset_description"] or "")+" "+(media[m]["transcript"] or ""))
    if m not in look: nolook.append(m)
    keep=[]
    for c in sorted(pool[(a["group"],a["level"])]-{key}):
        if c in links[m]: why["R1"]+=1; continue
        if same_tr(key,c): why["R2"]+=1; continue
        if toks(concepts[key]["word"])&toks(concepts[c]["word"]): why["R3"]+=1; continue
        if text_has(concepts[c]["word"],text): why["R4"]+=1; continue
        if c in generic[(a["group"],a["level"])]: why["R5"]+=1; continue
        if c in look.get(m,()): why["R6"]+=1; continue
        if c in aud.get(m,()): why["R7"]+=1; continue
        keep.append(c)
    # same part of speech first (a wrong word of the key's kind reads best), then the rest
    pos=concepts[key]["part_of_speech"]
    keep.sort(key=lambda c:(concepts[c]["part_of_speech"]!=pos,c))
    res[m]=keep
json.dump({str(m):v for m,v in res.items()},open("out/distractors.json","w"))
n=[len(v) for v in res.values()]
print("packets missing",len(missing),"videos without look",len(nolook))
print("videos",len(res),"words",len({A[m]["concept"] for m in res}),"avg",round(statistics.mean(n),1),"median",statistics.median(n),"min",min(n),"zero",sum(x==0 for x in n),"<3",sum(x<3 for x in n),"<5",sum(x<5 for x in n))
print(dict(why))
