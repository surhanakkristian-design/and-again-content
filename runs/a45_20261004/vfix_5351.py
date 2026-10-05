import json
p='content/5351.json'; d=json.load(open(p))
t=d['taps'][2]
t['phrase']="to glitter above the square"
for i,k in enumerate(t['keys']):
    if k['t'] in (3.5,4.0): t['keys'][i]={'t':k['t'],'off':True}
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
