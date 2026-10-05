import json
p='content/5463.json'; c=json.load(open(p))
for tap in c['taps']:
    for k in tap['keys']:
        if k.get('off') or k['t']<1.9: continue
        t=k['t']
        if abs(t-2.5)<.01: nx=0.06
        elif 2.9<t<4.6: nx=0.03
        else: nx=round(max(0,k['x']-0.04),2)
        k['w']=round(k['x']+k['w']-nx,2); k['x']=nx
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
