import json
p='content/5363.json'; c=json.load(open(p))
for n in c['nouns']:
    if n['word']=='a race number': n.update(word='a bum bag', x=0.38, y=0.52)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
