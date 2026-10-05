import json
p='content/296.json'; c=json.load(open(p))
def setk(i,t,**kw):
    for n,k in enumerate(c['taps'][i]['keys']):
        if abs(k['t']-t)<0.01: c['taps'][i]['keys'][n]={'t':k['t'],**kw}
setk(1,7.0,x=0.0,y=0.0,w=1.0,h=0.61); setk(2,7.0,x=0.0,y=0.62,w=1.0,h=0.37)
setk(1,7.5,x=0.0,y=0.0,w=1.0,h=0.65); setk(2,7.5,x=0.0,y=0.66,w=1.0,h=0.34)
c['taps'][2]['phrase']='to lie over the fire'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
