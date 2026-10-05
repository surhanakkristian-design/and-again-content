import json
p='content/5314.json'; d=json.load(open(p))
upd={7.0:(0.13,0.62),7.5:(0.12,0.55),8.0:(0.17,0.73),8.5:(0.16,0.74),9.0:(0.18,0.72)}
for k in d['taps'][2]['keys']:
    if k['t'] in upd: k['y'],k['h']=upd[k['t']]
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
