import json, sys
def K(times, boxes):
    out=[]
    for t,b in zip(times, boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
def write(mid, d):
    p=f"/Users/kristiansurhanak/Projects/and-again-content/runs/a45_20261004/content/{mid}.json"
    json.dump(d, open(p,"w"), indent=1, ensure_ascii=False)
