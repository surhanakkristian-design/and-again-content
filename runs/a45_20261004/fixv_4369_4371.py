import json
p='content/4369.json'; d=json.load(open(p))
assert d['taps'][1]['phrase']=='to bend down to his legs'; d['taps'][1]['phrase']='to bend down low'
assert d['taps'][2]['phrase']=='to hold a roll up high'; d['taps'][2]['phrase']='to hold a roll high'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/4371.json'; d=json.load(open(p))
new={7.0:(0.0,0.31,0.32,0.69),7.5:(0.0,0.30,0.32,0.70),9.0:(0.0,0.25,0.55,0.75)}
for k in d['taps'][0]['keys']:
    if k['t'] in new: k['x'],k['y'],k['w'],k['h']=new[k['t']]
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
