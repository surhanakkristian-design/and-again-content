import json
p='content/7951.json'; d=json.load(open(p))
assert d['taps'][2]['target']=='the man in green'
d['taps'][2]['phrase']='to give a thumbs-up'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
