import json
p='content/4894.json'; c=json.load(open(p))
c['taps'][1]['phrase']='to stand on the black line'
for n in c['nouns']:
    if n['word']=='a basketball hoop': n['y']=0.26
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
