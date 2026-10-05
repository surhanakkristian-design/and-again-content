import json,sys
def K(times, spec):
    out=[]
    for t in times:
        v=spec.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def write(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1)
