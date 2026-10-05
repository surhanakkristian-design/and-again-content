import json
p='content/5353.json'; d=json.load(open(p))
d['taps'][1]['phrase']="to stare at her screen"
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
