import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setkey(tap,t,**kw):
    for k in tap['keys']:
        if abs(k['t']-t)<1e-6: k.update(kw)
d=load(5539); b=d['taps'][2]
setkey(b,1.7,x=0.0,w=0.31); setkey(b,3.7,x=0.19,w=0.15); save(5539,d)
d=load(5541); w=d['taps'][0]
setkey(w,0.2,y=0.33,h=0.67); setkey(w,0.7,y=0.33,h=0.67); setkey(w,1.2,y=0.35,h=0.65); setkey(w,1.7,y=0.35,h=0.65); save(5541,d)
d=load(5543)
for n in d['nouns']:
    if n['word']=='bees': n.update(x=0.74,y=0.17)
    if n['word']=='a hive': n.update(x=0.58,y=0.72)
    if n['word']=='smoke': n.update(x=0.9,y=0.81)
save(5543,d)
