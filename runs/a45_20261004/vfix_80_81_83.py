import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
d=ld(80)
for n in d['nouns']:
    if n['word']=='flowers': n['x'],n['y']=0.62,0.15
sv(80,d)
d=ld(81)
assert d['taps'][0]['phrase']=='to dance in a white dress'
d['taps'][0]['phrase']='to dance in a dress'
sv(81,d)
d=ld(83)
t=d['taps'][2]; assert t['target']=='the dog'
new={7.0:dict(t=7.0,x=0.12,y=0.86,w=0.88,h=0.14),7.5:dict(t=7.5,x=0.20,y=0.84,w=0.80,h=0.16)}
t['keys']=[new.get(k['t'],k) for k in t['keys']]
sv(83,d)
