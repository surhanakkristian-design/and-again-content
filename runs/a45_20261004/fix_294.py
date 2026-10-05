import json
p='content/294.json'; c=json.load(open(p))
def setk(i,t,**kw):
    for n,k in enumerate(c['taps'][i]['keys']):
        if abs(k['t']-t)<0.01: c['taps'][i]['keys'][n]={'t':k['t'],**kw}
setk(1,7.0,x=0.66,y=0.50,w=0.34,h=0.46)
setk(1,7.5,x=0.66,y=0.50,w=0.34,h=0.48)
setk(1,9.0,x=0.66,y=0.43,w=0.34,h=0.45)
setk(1,9.5,x=0.69,y=0.40,w=0.31,h=0.47)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
