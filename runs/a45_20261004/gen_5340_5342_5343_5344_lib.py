import json, sys
def K(rows):
    out=[]
    for r in rows:
        if r[1] is None: out.append({"t":r[0],"off":True})
        else: out.append({"t":r[0],"x":r[1],"y":r[2],"w":r[3],"h":r[4]})
    return out
def write(mid, d):
    json.dump(d, open(f"content/{mid}.json","w"), indent=1, ensure_ascii=False)
