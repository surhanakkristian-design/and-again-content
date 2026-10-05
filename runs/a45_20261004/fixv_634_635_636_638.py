import json
def load(i): return json.load(open('content/%d.json'%i))
def save(i,d): json.dump(d,open('content/%d.json'%i,'w'),ensure_ascii=False,indent=1)
def setk(tap,t,box):
    for k in tap['keys']:
        if abs(k['t']-t)<1e-6:
            k.clear(); k['t']=t
            if box is None: k['off']=True
            else: k.update(dict(zip('xywh',box)))
            return
    raise SystemExit('no key %s'%t)
d=load(634); setk(d['taps'][1],9.5,(0.00,0.00,0.40,0.26)); save(634,d)
d=load(635); assert d['taps'][1]['phrase']=='to wear brown sandals'; d['taps'][1]['phrase']='to wear green shorts'; save(635,d)
d=load(636)
duck={5.0:(0.21,0.11,0.19,0.15),5.5:(0.21,0.05,0.19,0.15),6.0:(0.20,0.06,0.19,0.15),6.5:(0.18,0.09,0.20,0.15),
      7.0:(0.16,0.11,0.19,0.15),7.5:(0.18,0.16,0.18,0.15),8.0:(0.20,0.30,0.23,0.22)}
wom={6.5:(0.08,0.24,0.92,0.50),7.0:(0.05,0.26,0.95,0.60),7.5:(0.03,0.31,0.97,0.59),8.0:(0.43,0.00,0.57,0.80)}
for t,b in duck.items(): setk(d['taps'][2],t,b)
for t,b in wom.items(): setk(d['taps'][0],t,b); setk(d['taps'][1],t,b)
save(636,d)
d=load(638); setk(d['taps'][2],3.5,(0.33,0.30,0.19,0.14)); setk(d['taps'][1],3.5,(0.53,0.18,0.47,0.34)); save(638,d)
