import json
p='content/4470.json'; c=json.load(open(p))
d={7.5:(0,0.70,0.93,0.30),8.0:(0,0.69,0.92,0.31),8.5:(0.33,0.27,0.65,0.73)}
for t in c['taps']:
    for i,k in enumerate(t['keys']):
        if k['t'] in d:
            x,y,w,h=d[k['t']]; t['keys'][i]={'t':k['t'],'x':x,'y':y,'w':w,'h':h}
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
