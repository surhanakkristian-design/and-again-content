import json,sys
def keys(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
def write(d, times):
    for tp in d["taps"]:
        tp["keys"]=keys(times, tp.pop("boxes"))
    json.dump(d, open(f"content/{d['mediaId']}.json","w"), indent=1, ensure_ascii=False)
