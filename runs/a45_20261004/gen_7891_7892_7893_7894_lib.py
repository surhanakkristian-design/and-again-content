import json, sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(lst):
    out=[]
    for t,b in zip(T,lst):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=b; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
def write(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)
