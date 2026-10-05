import json
p='content/7186.json'; d=json.load(open(p))
d['taps'][2]['phrase']='to pull up the blanket'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
