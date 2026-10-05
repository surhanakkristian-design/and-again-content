import json
c=json.load(open('content/388.json'))
for n in c['nouns']:
    if n['word']=='a pen': n.update(x=0.84,y=0.82)
    if n['word']=='homework': n.update(x=0.52,y=0.91)
json.dump(c,open('content/388.json','w'),indent=1,ensure_ascii=False)
