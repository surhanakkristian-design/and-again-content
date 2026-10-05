import json
p='content/5460.json'; d=json.load(open(p))
pend,tower,green=d['taps']
for k in pend['keys']:
    if k['t']==1.5: k.clear(); k.update({"t":1.5,"x":0.74,"y":0.1,"w":0.26,"h":0.3})
add={0.0:(0.71,0.30,0.20,0.55),0.5:(0.68,0.31,0.18,0.45),3.5:(0.37,0.20,0.32,0.40),4.0:(0.0,0.15,0.20,0.55)}
for k in green['keys']:
    if k['t'] in add:
        x,y,w,h=add[k['t']]; t=k['t']; k.clear(); k.update({"t":t,"x":x,"y":y,"w":w,"h":h})
new={"phrase":"to support his sick friend","target":"the green-faced man","voice":"male","keys":json.loads(json.dumps(green['keys']))}
d['taps']=[pend,new,green]
d['notes']+=" | Verifier 2: red-tower phrase replaced (lamp post, Ferris wheel and pendulum ride also tower over the stalls; 'tower towers' tautology). New phrase 2 'to support his sick friend' on the green-faced man = the man in the light blue T-shirt who walks the hunched man in brown out arm in arm at 0.5-4.0. Green-faced man boxes added at 0.0, 0.5, 3.5, 4.0; pendulum box added at 1.5."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
