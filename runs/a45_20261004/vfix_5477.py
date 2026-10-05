import json
p='content/5477.json'; c=json.load(open(p))
for n in c['nouns']:
    if n['word']=='snow': n.update(word='the sky', x=0.5, y=0.22)
json.dump(c,open(p,'w'),indent=1)
