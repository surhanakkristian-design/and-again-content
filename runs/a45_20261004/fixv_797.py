import json
p='content/797.json'; d=json.load(open(p))
def setk(ti,t,box):
    for i,k in enumerate(d['taps'][ti]['keys']):
        if k['t']==t: d['taps'][ti]['keys'][i]=dict(t=t,**box)
setk(0,5.0,dict(x=0.75,y=0.49,w=0.12,h=0.14))
setk(2,5.0,dict(x=0.66,y=0.49,w=0.09,h=0.14))
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
