import json
p='content/801.json'; d=json.load(open(p))
def setk(ti,t,box):
    for i,k in enumerate(d['taps'][ti]['keys']):
        if k['t']==t: d['taps'][ti]['keys'][i]=dict(t=t,**box)
setk(0,6.0,dict(x=0.33,y=0.37,w=0.31,h=0.36))
setk(2,6.0,dict(x=0.15,y=0.54,w=0.18,h=0.14))
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
