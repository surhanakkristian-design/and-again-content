import json
p='content/4928.json'; d=json.load(open(p))
for n in d['nouns']:
    if n['word']=='dungarees': n.update(x=0.44,y=0.57)
    if n['word']=='a mixer tap': n.update(x=0.84,y=0.49)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
