import json, sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=r; x=max(0,x); y=max(0,y); w=min(w,1-x); h=min(h,1-y)
            out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
def write(vid,d):
    json.dump(d,open(f'content/{vid}.json','w'),indent=1,ensure_ascii=False)
