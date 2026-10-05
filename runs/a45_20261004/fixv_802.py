import json
p='content/802.json'; d=json.load(open(p))
def setk(ti,t,box):
    for i,k in enumerate(d['taps'][ti]['keys']):
        if k['t']==t: d['taps'][ti]['keys'][i]=dict(t=t,**box)
setk(1,10.0,dict(x=0.1,y=0.08,w=0.58,h=0.9))
setk(2,10.0,dict(x=0,y=0.55,w=0.1,h=0.24))
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
