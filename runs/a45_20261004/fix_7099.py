import json
p='content/7099.json'; d=json.load(open(p))
for k in d['taps'][1]['keys']:
    if k['t'] in (2.2,3.2,3.7): k['w']=0.55
    if k['t'] in (0.7,1.7,2.7): k['x']=0.02; k['w']=0.58
json.dump(d,open(p,'w'),indent=1)
