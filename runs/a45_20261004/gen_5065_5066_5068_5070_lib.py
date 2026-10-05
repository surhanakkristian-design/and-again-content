import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; w=min(w,round(1-x,2)); h=min(h,round(1-y,2))
            out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
    return out
def write(mid, c):
    times=json.load(open(f'frames/{mid}/packet.json'))['times']
    for tap in c['taps']: tap['keys']=K(times, tap.pop('box'))
    json.dump(c, open(f'content/{mid}.json','w'), indent=1, ensure_ascii=False)
