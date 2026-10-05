import json
p='content/6909.json'; d=json.load(open(p))
new={0.2:(0.71,0.18),0.7:(0.71,0.18),1.2:(0.74,0.18),1.7:(0.77,0.18),2.2:(0.79,0.18),2.7:(0.81,0.18),3.2:(0.82,0.18),3.7:(0.84,0.16)}
for k in d['taps'][1]['keys']:
    x,w=new[k['t']]; k['x']=x; k['w']=w
json.dump(d,open(p,'w'),indent=1)
