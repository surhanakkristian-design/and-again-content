import json
def ed(i, fn):
    p=f'content/{i}.json'; d=json.load(open(p)); fn(d); json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
def k(d,ti,t): return next(x for x in d['taps'][ti]['keys'] if x['t']==t)
def f244(d):
    k(d,2,1.0).update(h=0.35); k(d,0,1.0).update(y=0.36,h=0.64)
def f245(d):
    k(d,0,6.0).update(y=0.28,h=0.50); k(d,1,6.0).update(y=0.10,h=0.90); k(d,0,7.5).update(y=0.22,h=0.58)
def f248(d):
    for t in (6.5,7.0,7.5,8.0,8.5,9.0):
        k(d,2,t).update(y=0.40,h=0.23); k(d,1,t).update(y=0.30,h=0.70)
ed(244,f244); ed(245,f245); ed(248,f248)
