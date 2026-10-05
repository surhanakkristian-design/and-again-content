import json
p='content/5077.json'; c=json.load(open(p))
c['stillS']=7.0
pos={'a pillar':(0.17,0.10),'glasses':(0.44,0.26),'headphones':(0.43,0.44),'flashcards':(0.56,0.79)}
for n in c['nouns']: n['x'],n['y']=pos[n['word']]
for t in c['taps']:
  for k in t['keys']:
    if k['t']==8.5 and t['target']=='the student': k['x']=0.0; k['w']=1.0
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
