import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def key(tap,t): return next(k for k in tap['keys'] if abs(k['t']-t)<1e-6)
# 7064
d=load(7064); red,green,blue=d['taps']
key(red,3.2).update(x=0.64,w=0.36); key(green,3.2).update(w=0.52)
k=key(red,3.7); k.update(x=0.59,y=0.22,w=0.41,h=0.58)
key(green,3.7).update(w=0.49)
i=[n for n,k in enumerate(blue['keys']) if abs(k['t']-3.7)<1e-6][0]
blue['keys'][i]={"t":3.7,"x":0.40,"y":0.14,"w":0.19,"h":0.16}
d['nouns'][0].update(x=0.22,y=0.27)
save(7064,d)
# 7068
d=load(7068); waiter,goats,wtr=d['taps']
for t,x in [(0.2,0.43),(0.7,0.45),(1.2,0.53),(1.7,0.60),(2.2,0.55),(2.7,0.41)]:
    key(waiter,t).update(w=round(0.82-x,2))
for t in [0.2,0.7,1.2,1.7,2.2,2.7,3.2]:
    key(wtr,t).update(x=0.82,w=0.18)
save(7068,d)
