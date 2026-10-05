import json
def L(i): return json.load(open(f'content/{i}.json'))
def S(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=L(7892)
d['nouns']=[n for n in d['nouns'] if n['word']!='a beanie']
for n in d['nouns']:
    if n['word']=='snow': n['x'],n['y']=0.2,0.88
d['nouns'].insert(2,{"word":"crampons","x":0.67,"y":0.85,"voice":"female"})
S(7892,d)
d=L(7893)
for n in d['nouns']:
    if n['word']=='a pendant lamp': n['y']=0.18
S(7893,d)
d=L(7894)
for k in d['taps'][2]['keys']:
    if k['t']==3.7:
        k.clear(); k.update({"t":3.7,"x":0.66,"y":0.52,"w":0.22,"h":0.15})
S(7894,d)
