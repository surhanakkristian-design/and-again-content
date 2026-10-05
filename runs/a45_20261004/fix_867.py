import json
p='content/867.json'; d=json.load(open(p))
def setk(ti,t,box):
    for k in d['taps'][ti]['keys']:
        if k['t']==t:
            k.clear(); k['t']=t; k.update(dict(zip('xywh',box)))
setk(1,5.0,(0.64,0.41,0.36,0.2)); setk(1,5.5,(0.6,0.42,0.4,0.22))
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
