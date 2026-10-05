import json
p='content/718.json';c=json.load(open(p))
new={'the woman in the green coat':{0.0:(0.00,0.40,0.74,0.60),0.5:(0.00,0.44,0.60,0.56)},
     'the birds':{0.0:(0.50,0.03,0.50,0.36),0.5:(0.33,0.02,0.67,0.41)}}
for t in c['taps']:
    for k in t['keys']:
        v=new.get(t['target'],{}).get(k['t'])
        if v: k['x'],k['y'],k['w'],k['h']=v
json.dump(c,open(p,'w'),ensure_ascii=False,indent=2)
