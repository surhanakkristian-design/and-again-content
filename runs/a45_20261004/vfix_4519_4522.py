import json
p='content/4519.json'; c=json.load(open(p))
for n in c['nouns']:
    if n['word']=='ash': n['x'],n['y']=0.30,0.80
assert c['answer'][2]=='lighting'; c['answer'][2]='building'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4522.json'; c=json.load(open(p))
for t in c['taps']:
    if t['phrase']=='to hold chopsticks': t['phrase']='to laugh at the camera'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
