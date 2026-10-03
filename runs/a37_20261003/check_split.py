import json,sys,re,collections
i=int(sys.argv[1])
lines=[l.split("\t") for l in open(f"packets/split_{i}.tsv").read().split("\n") if l and not l.startswith("#")]
lev={int(l[0]):l[1] for l in lines}
head=open(f"packets/split_{i}.tsv").readline()
lo,hi=map(int,re.search(r"allowed (\d+)\.\.(\d+)",head).groups())
d=json.load(open(f"out/split_{i}.json"))
err=[]
seen=collections.Counter(m for g in d["groups"] for m in g["media"])
for m in lev:
    if seen[m]!=1: err.append(f"media {m} placed {seen[m]} times")
for m in seen:
    if m not in lev: err.append(f"media {m} is not in this old group")
if not lo<=len(d["groups"])<=hi: err.append(f"{len(d['groups'])} groups, allowed {lo}..{hi}")
names=set()
for g in d["groups"]:
    a=sum(lev.get(m)=="A" for m in g["media"]); b=sum(lev.get(m)=="B" for m in g["media"])
    for n in [g["en"]]+g.get("alt",[]):
        if not re.fullmatch(r"[A-Z][a-z]+",n): err.append(f"name {n!r} is not one title-case word")
    if g["en"] in names: err.append(f"name {g['en']} twice")
    names.add(g["en"])
    if len(g.get("alt",[]))<2: err.append(f"{g['en']}: 2 alternative names needed")
    if a<6 or b<6: err.append(f"{g['en']}: A {a}, B {b} (floor 6 / 6)")
    print(f"  {g['en']}: A {a}, B {b}")
print("OK" if not err else "ERRORS:\n"+"\n".join(err))
