import json, sys
def K(times, boxes):
    # boxes: dict t -> (x,y,w,h) or None
    out=[]
    for t in times:
        b=boxes.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b
            x=max(0,round(x,2)); y=max(0,round(y,2))
            w=round(min(w,1-x),2); h=round(min(h,1-y),2)
            out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
def write(mid, d):
    json.dump(d, open(f"content/{mid}.json","w"), indent=1, ensure_ascii=False)
