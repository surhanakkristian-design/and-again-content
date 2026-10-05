import json
d=json.load(open('content/7883.json'))
for k in d['taps'][2]['keys']:
    if k['t']==0.2: k.update({"x":0.69,"w":0.17})
json.dump(d,open('content/7883.json','w'),indent=1,ensure_ascii=False)
