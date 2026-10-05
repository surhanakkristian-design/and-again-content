import json
p='content/4705.json'; c=json.load(open(p))
for t in c['taps']:
    if t['target']=='the police officer':
        for k in t['keys']:
            if k['t']==5.0: k.clear(); k.update({'t':5.0,'x':0.82,'y':0.78,'w':0.18,'h':0.22})
            if k['t']==5.5: k.clear(); k.update({'t':5.5,'x':0.82,'y':0.72,'w':0.18,'h':0.28})
for n in c['nouns']:
    if n['word']=='a stroller': n['x']=0.67; n['y']=0.74
json.dump(c,open(p,'w'),indent=2,ensure_ascii=False)
