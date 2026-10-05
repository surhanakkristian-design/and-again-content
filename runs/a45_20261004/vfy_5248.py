import json
p='content/5248.json'; c=json.load(open(p))
w={7.0:dict(x=0.46,y=0.41,w=0.18,h=0.18),7.5:dict(x=0.46,y=0.41,w=0.18,h=0.18),8.0:dict(x=0.44,y=0.42,w=0.19,h=0.18),9.0:dict(x=0.46,y=0.43,w=0.19,h=0.2)}
for tap in c['taps'][:2]:
    for k in tap['keys']:
        for t,v in w.items():
            if abs(k['t']-t)<.01: k.pop('off',None); k.update(v)
c['notes']+=' VERIFIER: the coral-jacket rider on a white scooter in the palm shot is the same woman (same bob, white top, jeans, white scooter); boxed at 7.0-8.0 and 9.0 (hidden behind a man at 8.5, unclear at 6.5).'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
