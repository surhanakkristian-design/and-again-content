import json
p='content/5019.json'; d=json.load(open(p))
man=d['taps'][2]['keys']; w=[d['taps'][0]['keys'],d['taps'][1]['keys']]
def g(keys,t): return next(k for k in keys if abs(k['t']-t)<1e-6)
g(man,3.0).update(w=0.2,h=0.24)
g(man,11.0).update(h=0.25)
g(man,11.5).update(w=0.14)
for ks in w:
    g(ks,11.5).update(x=0.15,w=0.83)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
