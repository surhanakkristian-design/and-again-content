import json, sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    out=[]
    for t,r in zip(T,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=r; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    return out
def write(mid,d):
    json.dump(d,open(f'content/{mid}.json','w'),indent=1,ensure_ascii=False)
