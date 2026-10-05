import json
p='content/7765.json'; c=json.load(open(p))
red={0.2:(0.32,0.28),0.7:(0.32,0.28),1.2:(0.33,0.29),1.7:(0.33,0.29)}
for k in c['taps'][0]['keys']:
    if k['t'] in red: k['y'],k['h']=red[k['t']]
for k in c['taps'][2]['keys']:
    if k['t']==1.2: k['y'],k['h']=0.25,0.23
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
