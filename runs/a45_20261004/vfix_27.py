import json
p='content/27.json'; d=json.load(open(p))
def setk(ti,t,box):
    for k in d['taps'][ti]['keys']:
        if abs(k['t']-t)<1e-6:
            k.clear(); k['t']=t
            if box is None: k['off']=True
            else: k.update(dict(zip('xywh',box)))
W,C,B=0,1,2
setk(W,3.0,(0.00,0.15,0.80,0.37)); setk(C,3.0,(0.50,0.53,0.38,0.19)); setk(B,3.0,(0.15,0.73,0.85,0.27))
setk(W,3.5,(0.00,0.02,0.92,0.64)); setk(C,3.5,(0.48,0.67,0.52,0.33))
setk(C,7.0,(0.57,0.61,0.40,0.18)); setk(B,7.0,(0.10,0.80,0.90,0.20))
setk(B,9.0,(0.78,0.82,0.22,0.18))
setk(W,15.0,(0.00,0.36,0.87,0.30))
d['taps'][B]['phrase']='to lie on the desk'
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
