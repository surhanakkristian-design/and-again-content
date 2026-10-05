import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
d=load(4410)
bag={3.0:(.08,.78,.40,.22),3.5:(.08,.78,.40,.22),4.0:(.06,.78,.40,.22),5.5:(.66,.72,.34,.25)}
n=0
for k in d['taps'][2]['keys']:
    if k['t'] in bag:
        x,y,w,h=bag[k['t']]; k.pop('off',None); k.update(x=x,y=y,w=w,h=h); n+=1
d['notes']+=" VERIFIER: bag box moved onto the bag at 5.5 s; the same bag is now boxed at 3-4 s."
save(4410,d); print(4410,n)
d=load(4411)
hh={3.0:.65,3.5:.65,5.0:.55,5.5:.58,9.0:.64}
n=0
for k in d['taps'][2]['keys']:
    if k['t'] in hh: k['h']=hh[k['t']]; n+=1
d['notes']+=" VERIFIER: man's box shortened at 3, 3.5, 5, 5.5, 9 s so it no longer holds her sock / boot."
save(4411,d); print(4411,n)
