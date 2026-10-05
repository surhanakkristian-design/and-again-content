import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def key(tap,t): return next(k for k in tap['keys'] if abs(k['t']-t)<1e-6)
def setk(tap,t,**kw):
    k=key(tap,t); k.clear(); k.update({'t':t,**kw})
d=load(61); assert d['taps'][1]['phrase']=='to sit down on a bench'
d['taps'][1]['phrase']='to sit on a bench'; save(61,d)
d=load(65); assert d['taps'][2]['phrase']=='to lie on the wooden floor'
d['taps'][2]['phrase']='to lie on the floorboards'
setk(d['taps'][0],3.0,x=0,y=0,w=0.84,h=0.55); setk(d['taps'][1],3.0,x=0.84,y=0,w=0.16,h=0.55); save(65,d)
d=load(66); assert d['taps'][2]['phrase']=='to sit by the window'
d['taps'][2]['phrase']='to lie by the window'
setk(d['taps'][0],9.5,x=0.15,y=0.25,w=0.36,h=0.42); setk(d['taps'][2],9.5,x=0,y=0.3,w=0.15,h=0.14)
setk(d['taps'][0],10.0,x=0.12,y=0.25,w=0.38,h=0.45); setk(d['taps'][2],10.0,x=0,y=0.3,w=0.12,h=0.14)
save(66,d)
