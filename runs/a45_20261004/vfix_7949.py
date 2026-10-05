import json
p='content/7949.json'; d=json.load(open(p))
for k in d['taps'][0]['keys']:
    if k['t']==2.2:
        k.clear(); k.update({"t":2.2,"x":0.82,"y":0.0,"w":0.18,"h":0.9})
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
