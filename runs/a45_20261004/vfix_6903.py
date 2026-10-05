import json
p='content/6903.json'; c=json.load(open(p))
split={0.2:0.40,0.7:0.39,2.2:0.43}
for tap in c['taps']:
    for k in tap['keys']:
        t=round(k['t'],2)
        if t not in split or k.get('off'): continue
        s=split[t]
        if tap['target']=='the painting': k['w']=round(s,2)
        else:
            r=k['x']+k['w']; k['x']=round(s+0.01,2); k['w']=round(r-k['x'],2)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
