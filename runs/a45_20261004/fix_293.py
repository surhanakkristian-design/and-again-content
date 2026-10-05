import json
p='content/293.json'; c=json.load(open(p))
def setk(i,t,**kw):
    for n,k in enumerate(c['taps'][i]['keys']):
        if abs(k['t']-t)<0.01: c['taps'][i]['keys'][n]={'t':k['t'],**kw}
setk(1,3.5,x=0.64,y=0.66,w=0.36,h=0.34)
setk(2,9.5,x=0.60,y=0.43,w=0.18,h=0.14)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
