import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
d=load(276)
for k in d['taps'][0]['keys']:
    if abs(k['t']-5.5)<.01: k.update(x=0.00,y=0.18,w=1.00,h=0.23)
save(276,d)
d=load(280)
for n in d['nouns']:
    if n['word']=='a nose': n.update(word='a bed',x=0.87,y=0.66)
d['notes']+=" VERIFIER: 'a nose' replaced by 'a bed' (a kitten was also right at the nose pill)."
save(280,d)
d=load(281)
new={9.0:(0.41,0.14,0.19,0.46),9.5:(0.42,0.15,0.19,0.50),10.0:(0.43,0.16,0.20,0.50)}
for k in d['taps'][2]['keys']:
    for t,(x,y,w,h) in new.items():
        if abs(k['t']-t)<.01: k.update(x=x,y=y,w=w,h=h)
save(281,d)
