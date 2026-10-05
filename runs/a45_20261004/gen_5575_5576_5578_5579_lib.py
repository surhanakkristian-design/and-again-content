import json, os
TIMES=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def B(rows):
    out=[]
    for t,r in zip(TIMES,rows):
        if r is None: out.append({"t":t,"off":True}); continue
        x0,y0,x1,y1=[max(0.0,min(1.0,v)) for v in r]
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
def write(mid,d):
    p=os.path.join(os.path.dirname(os.path.abspath(__file__)),"content",f"{mid}.json")
    json.dump(d,open(p,"w"),indent=1,ensure_ascii=False)
