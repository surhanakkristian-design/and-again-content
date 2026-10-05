import json
p='content/5078.json'; c=json.load(open(p))
for t in c['taps']:
  if t['target']=='the bearded man':
    for i,k in enumerate(t['keys']):
      if k['t']==7.0: t['keys'][i]={'t':7.0,'x':0.0,'y':0.0,'w':0.2,'h':0.17}
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
