import json
p='content/5192.json'; c=json.load(open(p))
fl,wo,hut=c['taps']
wo['phrase']='to go without a hat'
def setk(tap,t,**kw):
    for i,k in enumerate(tap['keys']):
        if abs(k['t']-t)<1e-6: tap['keys'][i]=dict(t=t,**kw)
setk(fl,0.5,x=0.47,y=0,w=0.22,h=0.17)
setk(wo,0.5,x=0.25,y=0.17,w=0.75,h=0.83)
setk(wo,9.0,x=0.69,y=0.74,w=0.19,h=0.26)
setk(wo,9.5,x=0.69,y=0.74,w=0.19,h=0.26)
setk(wo,10.0,x=0.68,y=0.74,w=0.19,h=0.26)
setk(hut,8.5,x=0.84,y=0.78,w=0.16,h=0.16)
setk(hut,9.0,x=0.88,y=0.79,w=0.12,h=0.15)
setk(hut,9.5,x=0.88,y=0.79,w=0.12,h=0.15)
setk(hut,10.0,x=0.87,y=0.79,w=0.13,h=0.15)
c['notes']+=' VERIFIER: hair is tied back, not loose -> phrase changed to "to go without a hat" (only one without a beanie); flag+woman boxed at 0.5 s; hut boxed at 8.5-10.0 s where its right part shows beside the woman.'
json.dump(c,open(p,'w'),indent=2,ensure_ascii=False)
