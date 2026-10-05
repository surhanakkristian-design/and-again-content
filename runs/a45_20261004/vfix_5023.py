import json
p='content/5023.json'; c=json.load(open(p))
for k in c['taps'][1]['keys']:
    if abs(k['t']-4.5)<0.01:
        k.clear(); k.update({'t':4.5,'x':0.0,'y':0.38,'w':0.18,'h':0.16})
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
