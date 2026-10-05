import json
p='content/5366.json'; c=json.load(open(p))
for n in c['nouns']:
    if n['word']=='a hay bale': n.update(word='hay bales', x=0.55, y=0.21)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
