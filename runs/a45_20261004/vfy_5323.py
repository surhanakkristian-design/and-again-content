import json
p='content/5323.json'; c=json.load(open(p))
for k in c['taps'][2]['keys']:
    if abs(k['t']-7.0)<.01: k.clear(); k.update({'t':7.0,'x':0.80,'y':0.47,'w':0.20,'h':0.38})
    if abs(k['t']-8.0)<.01: k.update({'x':0.68,'w':0.32})
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
