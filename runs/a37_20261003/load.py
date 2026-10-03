# A32 loader: fresh live snapshot (data/), ids normalised to int.
import json,collections,re
L=lambda n: json.load(open(f"data/{n}.json"))
I=lambda xs:[int(x) for x in xs]
twd={int(r["media_id"]):dict(concept=int(r["concept_id"]),group=int(r["group_id"]),level=r["level"],dist=I(r["distractor_concept_ids"]),fb=I(r["fallback_concept_ids"])) for r in L("twd")}
media={int(m["id"]):m for m in L("media")}
concepts={int(c["id"]):c for c in L("concepts")}
links=collections.defaultdict(set)
for r in L("concept_media"): links[int(r["media_id"])].add(int(r["concept_id"]))
loc=collections.defaultdict(dict)
for r in L("loc"): loc[int(r["concept_id"])][r["language_code"]]=r
groups={int(g["id"]):g["name"]["en"] for g in L("groups")}
BP=31
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
_F={}
def same_tr(a,b):
    for c in (a,b):
        if c not in _F: _F[c]=forms(c)
    return bool(_F[a]&_F[b])
def text_has(word,text):
    ts=[t for t in norm(word).split() if t not in STOP]
    if not ts: return False
    tt={stem(t) for t in text.split()}
    return all(stem(t) in tt for t in ts)
def mtext(m): return norm((media[m]["asset_description"] or "")+" "+(media[m]["transcript"] or ""))
