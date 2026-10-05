import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setkey(tap,t,**kw):
    for k in tap['keys']:
        if k['t']==t:
            k.clear(); k['t']=t; k.update(kw); return
    raise SystemExit('no key')
d=load(111)
w,m,b=d['taps']
setkey(w,5.5,x=0.48,y=0.30,w=0.52,h=0.70)
setkey(w,9.0,x=0.30,y=0.32,w=0.70,h=0.68)
setkey(w,9.5,x=0.10,y=0.30,w=0.70,h=0.70)
setkey(m,9.5,x=0.80,y=0.37,w=0.20,h=0.19)
b['phrase']='to hang from chains'
save(111,d)
d=load(112); d['taps'][2]['phrase']='to carry the man'; save(112,d)
d=load(114); setkey(d['taps'][2],3.0,x=0.08,y=0.47,w=0.18,h=0.14); save(114,d)
d=load(115)
for n in d['nouns']:
    if n['word']=='milk': n['x']=0.90; n['y']=0.80
assert d['answer'][2]=='eating'; d['answer'][2]='having'
save(115,d)
