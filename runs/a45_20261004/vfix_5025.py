import json
p='content/5025.json'; c=json.load(open(p))
def setk(tap,t,**v):
    for k in tap['keys']:
        if abs(k['t']-t)<0.01: k.clear(); k.update({'t':t,**v})
blue,teach,floor=c['taps']
setk(teach,8.5,x=0.53,y=0.27,w=0.18,h=0.20)
setk(floor,8.5,x=0.30,y=0.47,w=0.31,h=0.25)
setk(teach,9.0,x=0.44,y=0.26,w=0.18,h=0.22)
setk(floor,9.0,x=0.20,y=0.48,w=0.41,h=0.24)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
