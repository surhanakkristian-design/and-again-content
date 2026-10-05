import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def key(d,ti,t): return next(k for k in d['taps'][ti]['keys'] if k['t']==t)
d=load(272)
d['taps'][2]['phrase']='to produce a blue flame'
k=key(d,0,3.5); k.update(y=0,h=0.7)
k=key(d,2,3.0); k.update(y=0.74,h=0.26)
save(272,d)
d=load(273)
d['taps'][0]['phrase']='to go behind the hills'
save(273,d)
d=load(274)
key(d,0,0.0).update(y=0.38,h=0.62)
key(d,0,1.0).update(y=0.22,h=0.78)
k=key(d,0,3.0); k.clear(); k.update(t=3.0,x=0.25,y=0.88,w=0.57,h=0.12)
key(d,1,3.0).update(y=0.72,h=0.16)
save(274,d)
