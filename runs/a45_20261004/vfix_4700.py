import json
p='content/4700.json'; c=json.load(open(p))
for i in (0,1):
    for k in c['taps'][i]['keys']:
        if k['t']==5.5: k['w']=0.45
for k in c['taps'][2]['keys']:
    if k['t']==5.5: k['x'],k['y'],k['w'],k['h']=0.48,0.46,0.48,0.26
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
