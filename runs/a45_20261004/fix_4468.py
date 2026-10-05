import json
p='content/4468.json'; c=json.load(open(p))
man={0.0:(0,0.42,0.78,0.36),0.5:(0,0.08,0.48,0.60),1.0:(0,0.22,0.32,0.40),1.5:(0,0.22,0.42,0.36),
     7.5:(0.56,0.15,0.24,0.16),8.0:(0.80,0.36,0.20,0.14),8.5:(0.80,0.33,0.20,0.14)}
por={7.5:(0.05,0.31,0.87,0.69),8.0:(0.17,0.19,0.63,0.81),8.5:(0.19,0.17,0.61,0.83)}
def ap(t,d):
    for i,k in enumerate(t['keys']):
        if k['t'] in d:
            x,y,w,h=d[k['t']]; t['keys'][i]={'t':k['t'],'x':x,'y':y,'w':w,'h':h}
ap(c['taps'][0],man); ap(c['taps'][1],man); ap(c['taps'][2],por)
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
