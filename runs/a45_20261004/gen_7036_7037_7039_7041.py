import json, sys
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(rows):
    out=[]
    for t,r in zip(T,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
def write(vid, d):
    json.dump(d, open(f'content/{vid}.json','w'), indent=1, ensure_ascii=False)
