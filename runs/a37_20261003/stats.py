from load import *
import collections
G=json.load(open("data/groups.json"))
cnt=collections.Counter((v["group"],v["level"]) for v in twd.values())
tot=0
print(sorted(set(v["level"] for v in twd.values())))
for g in G:
    i=int(g["id"]); a=cnt[(i,"A")]; b=cnt[(i,"B")]
    k=max(1,min(round((a+b)/30), min(a,b)//8))
    tot+=k
    print(i,g["name"]["en"],a,b,k, len(media[int(g["rep_media_a"])]["asset_description"] or ""))
print(tot, sum(len(m["asset_description"] or "") for i,m in media.items() if i in twd)/len(twd))
