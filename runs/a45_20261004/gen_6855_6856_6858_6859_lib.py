import json
def K(times, rows):
    out=[]
    for t,r in zip(times,rows):
        if r is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=r; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(x2-x,2),"h":round(y2-y,2)})
    return out
def write(vid, d):
    json.dump(d, open(f'content/{vid}.json','w'), indent=1, ensure_ascii=False)
