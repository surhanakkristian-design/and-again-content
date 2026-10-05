import json
p='content/5328.json'; d=json.load(open(p))
ch={0.0:0.32,0.5:0.32,7.0:0.24,7.5:0.24,8.0:0.24,8.5:0.24,9.0:0.25,9.5:0.25,10.0:0.26}
for tp in d['taps']:
    for k in tp['keys']:
        if k['t'] in ch:
            ny=ch[k['t']]; k['h']=round(k['h']+k['y']-ny,2); k['y']=ny
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
