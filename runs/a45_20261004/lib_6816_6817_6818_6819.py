import json, sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(boxes):
    out=[]
    for t,b in zip(T,boxes):
        if b is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=b
        x0=max(0,x0);y0=max(0,y0);x1=min(1,x1);y1=min(1,y1)
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
def write(mid, d):
    json.dump(d, open(f"content/{mid}.json","w"), indent=1, ensure_ascii=False)
