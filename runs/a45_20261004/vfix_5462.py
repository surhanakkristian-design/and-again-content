import json
p='content/5462.json'; c=json.load(open(p))
for t in c['taps']:
    if t['target']=='the woman in mustard':
        for k in t['keys']:
            if abs(k['t']-4.0)<.01: k.clear(); k.update(t=4.0,x=0.65,y=0.24,w=0.18,h=0.25)
            if abs(k['t']-4.5)<.01: k.clear(); k.update(t=4.5,x=0.65,y=0.24,w=0.19,h=0.23)
for n in c['nouns']:
    if n['word']=='a scarf': n['x'],n['y']=0.19,0.60
    if n['word']=='a ballot box': n['y']=0.51
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
