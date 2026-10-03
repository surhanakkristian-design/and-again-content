from load import *
from groups_def import G
import json,os,math
LANGS=["en","sk","cz","de","ua","es","fr","hu","tr"]
groups=[]; cat2g={}
for gid,src,nm in G:
    name=dict(cats[src[0]]) if len(src)==1 else {}
    name.update(nm); assert set(name)==set(LANGS),(gid,name)
    groups.append(dict(id=gid,name={l:name[l] for l in LANGS},source_category_ids=src,merged=len(src)>1))
    for c in src: cat2g[c]=gid
assert len(cat2g)==40
json.dump(groups,open("out/groups.json","w"),ensure_ascii=False,indent=1)
mg={m:cat2g[next(iter(mc[m]))] for m in live}
mk={m:next(iter(mcon[m][next(iter(mlev[m]))])) for m in live}
ml={m:next(iter(mlev[m])) for m in live}
json.dump({str(m):dict(group=mg[m],level=ml[m],concept=mk[m]) for m in live},open("out/media_assign.json","w"))
gname={g["id"]:g["name"]["en"] for g in groups}
os.makedirs("packets/dist",exist_ok=True); os.makedirs("packets/rep",exist_ok=True)
CH=40; n=0; idx=[]
for g in groups:
  for lv in "AB":
    ms=sorted(m for m in live if mg[m]==g["id"] and ml[m]==lv)
    cs=sorted({mk[m] for m in ms})
    words=[dict(c=c,w=concepts[c]["word"],pos=concepts[c]["part_of_speech"],d=concepts[c]["definition"]) for c in cs]
    k=math.ceil(len(ms)/CH); size=math.ceil(len(ms)/k)
    for i in range(k):
        vids=[dict(m=m,key=mk[m],word=concepts[mk[m]]["word"],desc=media[m]["asset_description"],said=media[m]["transcript"]) for m in ms[i*size:(i+1)*size]]
        name=f'g{g["id"]:02d}_{lv}_{i+1}'
        json.dump(dict(packet=name,group=gname[g["id"]],level=lv,words=words,videos=vids),open(f"packets/dist/{name}.json","w"),ensure_ascii=False,indent=0)
        idx.append(name); n+=1
json.dump(idx,open("packets/dist/index.json","w"))
print("dist packets",n)
so=json.load(open("/Users/kristiansurhanak/Projects/and-again-a31/scripts/wall-files/starter_order.json"))
rep={}; need=[]
for g in groups:
    r={}
    for key,lv in (("A","A"),("B","B")):
        c=[m for m in so[key] if mg.get(m)==g["id"] and ml[m]==lv]
        if c: r[lv]=c[0]
        else: need.append((g["id"],lv))
    c=[m for m in so["media"] if mg.get(m)==g["id"]]
    r["all"]=c[0] if c else None
    rep[g["id"]]=r
rep[1]["A"]=209; rep[1]["all"]=209
json.dump(rep,open("out/rep_from_starter.json","w"),indent=0)
for gid,lv in need:
    ms=sorted(m for m in live if mg[m]==gid and ml[m]==lv)
    json.dump(dict(group=gname[gid],group_id=gid,level=lv,candidates=[dict(m=m,word=concepts[mk[m]]["word"],desc=media[m]["asset_description"],cartoon=None) for m in ms]),open(f"packets/rep/g{gid:02d}_{lv}.json","w"),ensure_ascii=False,indent=0)
print("rep to curate",len(need), "all missing",[g for g in rep if rep[g]["all"] is None])
