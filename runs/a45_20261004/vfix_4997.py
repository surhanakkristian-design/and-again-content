import json
p='content/4997.json'; d=json.load(open(p))
top={8.0:0.17,8.5:0.13,9.0:0.16,9.5:0.19,10.0:0.10,10.5:0.13,11.0:0.17,11.5:0.15,12.0:0.17}
right={8.0:0.84,8.5:0.86,9.0:0.89,9.5:0.90,10.0:0.85,10.5:0.85,11.0:0.87,11.5:0.90,12.0:0.84}
for t in d['taps']:
  if t['target']!='the man': continue
  for k in t['keys']:
    if k['t'] in top:
      bot=k['y']+k['h']; r=max(k['x']+k['w'],right[k['t']])
      k['y']=top[k['t']]; k['h']=round(bot-k['y'],2); k['w']=round(r-k['x'],2)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
