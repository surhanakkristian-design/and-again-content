import json
p='content/6954.json'; c=json.load(open(p))
H={0.2:0.41,0.7:0.41,1.2:0.43,1.7:0.44,2.2:0.46,2.7:0.46,3.2:0.50,3.7:0.50}
for k in c['taps'][1]['keys']:
    k['h']=H[round(k['t'],1)]
json.dump(c,open(p,'w'),indent=1)
