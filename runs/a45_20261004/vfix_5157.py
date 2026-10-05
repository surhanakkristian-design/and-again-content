import json
p='content/5157.json'; c=json.load(open(p))
add={7.5:(0.45,0.43,0.11,0.17),8.0:(0.37,0.42,0.09,0.17),9.5:(0.21,0.41,0.10,0.19),10.0:(0.33,0.39,0.10,0.18)}
dl={8.0:(0.19,0.38,0.18,0.27),9.5:(0.31,0.35,0.18,0.27),10.0:(0.43,0.41,0.19,0.20)}
for ti,m in ((0,add),(2,dl)):
    t=c['taps'][ti]
    for i,k in enumerate(t['keys']):
        if k['t'] in m:
            x,y,w,h=m[k['t']]; t['keys'][i]={'t':k['t'],'x':x,'y':y,'w':w,'h':h}
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
