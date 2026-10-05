import json
p='content/864.json'; d=json.load(open(p))
def setk(ti,t,box):
    for k in d['taps'][ti]['keys']:
        if k['t']==t:
            k.clear(); k['t']=t
            if box: k.update(dict(zip('xywh',box)))
            else: k['off']=True
setk(0,4.0,(0.57,0,0.43,1)); setk(1,4.0,(0.28,0.22,0.28,0.45))
setk(0,6.0,(0.23,0.22,0.77,0.78)); setk(1,6.0,(0,0.24,0.22,0.17))
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
