# A37 decision 2: per video the wrong words of its own new group (from the vetted A31/A32 list),
# then the parent's rest, then the other level (only when own + parent are below 5).
import json,sys,collections
from load import twd,concepts
A36_4754=dict(concept=5547,group=20,level="B",dist=[14,20,34,360,690,693,715,826,2920,3291,3646,3758,4963,4993,5938],fb=[])
def build(groups):
    t={m:dict(v) for m,v in twd.items()}; t[4754]=dict(A36_4754)
    gof={m:g["id"] for g in groups for m in g["media"]}
    assert set(gof)==set(t), (len(gof),len(t))
    par={g["id"]:g["parent"] for g in groups}
    words=collections.defaultdict(set)   # (new group, level) -> key concepts
    for m,v in t.items():
        assert par[gof[m]]==v["group"],(m,gof[m],v["group"])
        words[(gof[m],v["level"])].add(v["concept"])
    rows={}
    for m,v in t.items():
        if v["group"]==31:   # Body Parts: the list of A32 (words of other groups) stays whole
            own=list(v["dist"]); rest=[]
        else:
            w=words[(gof[m],v["level"])]
            own=[c for c in v["dist"] if c in w]; rest=[c for c in v["dist"] if c not in w]
        fb=list(rest)
        if len(own)+len(rest)<5: fb+= [c for c in v["fb"] if c not in own and c not in rest]
        rows[m]=dict(media=m,concept=v["concept"],group=gof[m],level=v["level"],own=own,fb=fb,n_parent=len(own)+len(rest),n_all=len(set(own+fb)))
    return rows
if __name__=="__main__":
    groups=json.load(open(sys.argv[1]))
    r=build(groups)
    own5=sum(len(x["own"])<5 for x in r.values()); own0=sum(len(x["own"])==0 for x in r.values())
    eff=lambda x: len(x["own"]) if len(x["own"])>=5 else x["n_all"]
    print("videos",len(r),"own<5:",own5,"own=0:",own0,"after parent <5:",sum(len(x["own"])<5 and x["n_parent"]<5 for x in r.values()),"final <5:",sum(eff(x)<5 for x in r.values()),"final 0:",sum(eff(x)==0 for x in r.values()))
    print("avg own",sum(len(x["own"]) for x in r.values())/len(r),"avg shown",sum(eff(x) for x in r.values())/len(r))
