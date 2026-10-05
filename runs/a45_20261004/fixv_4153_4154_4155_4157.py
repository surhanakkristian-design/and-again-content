import json
p='content/4154.json'; c=json.load(open(p))
for t in c['taps'][:2]:
    for k in t['keys']:
        if k['t']==1.0: k.update(x=0.40,y=0.44,w=0.52,h=0.54)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4155.json'; c=json.load(open(p))
for n in c['nouns']:
    if n['word']=='a plant': n['y']=0.27
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
