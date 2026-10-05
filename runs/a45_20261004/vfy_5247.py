import json
p='content/5247.json'; c=json.load(open(p))
man={2.5:dict(x=0.57,y=0,w=0.43,h=0.61),3.0:dict(x=0.53,y=0,w=0.47,h=0.5)}
dog={2.5:dict(x=0.82,y=0.62,w=0.18,h=0.26),3.0:dict(x=0.82,y=0.51,w=0.18,h=0.28)}
for idx,d in ((1,man),(2,dog)):
    for k in c['taps'][idx]['keys']:
        for t,v in d.items():
            if abs(k['t']-t)<.01: k.pop('off',None); k.update(v)
c['notes']+=' VERIFIER: dog is visible at the right edge at 2.5-3.0 s, boxed there (man box cut above it).'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
