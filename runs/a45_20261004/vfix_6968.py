import json
p='content/6968.json'
d=json.load(open(p))
assert d['taps'][0]['phrase']=='to approach the safari vehicle'
d['taps'][0]['phrase']='to lead the herd'
assert d['taps'][1]['phrase']=='to raise his palm'
d['taps'][1]['phrase']='to hold up his hand'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
