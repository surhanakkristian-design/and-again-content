import json
p='content/302.json'; d=json.load(open(p))
k=[k for k in d['taps'][1]['keys'] if k['t']==10.0][0]; k['x']=0.45; k['w']=0.55
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/303.json'; d=json.load(open(p))
assert d['taps'][2]['phrase']=='to wear big glasses'
d['taps'][2]['phrase']='to touch a pink flower'
d['notes']=d['notes'].replace("; 'to wear big glasses' is a state","; verifier: third phrase changed from the state 'to wear big glasses' to the action 'to touch a pink flower' (1.0-1.5 s)")
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
