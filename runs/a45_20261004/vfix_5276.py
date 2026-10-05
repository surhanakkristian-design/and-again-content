import json
p='content/5276.json'; c=json.load(open(p))
for n in c['nouns']:
    if n['word']=='a chocolate-chip cookie': n['y']=0.735
    if n['word']=='a paper plate': n['y']=0.655
json.dump(c,open(p,'w'),indent=2,ensure_ascii=False)
