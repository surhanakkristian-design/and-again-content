import json
d=json.load(open('content/735.json'))
for tap in d['taps']:
    for k in tap['keys']:
        if tap['target']=='the man' and k['t']<=1.5:
            t=k['t']; k.clear(); k['t']=t; k['off']=True
        if tap['target']=='the cat' and k['t']==0.0:
            k.update(x=0.14,y=0.39,w=0.5,h=0.21)
json.dump(d,open('content/735.json','w'),indent=1,ensure_ascii=False)
