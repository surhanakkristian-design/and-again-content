import json
def ed(vid, target, t, **kw):
    p=f'content/{vid}.json'; c=json.load(open(p)); n=0
    for tap in c['taps']:
        if tap['target']==target:
            for k in tap['keys']:
                if abs(k['t']-t)<.01: k.update(kw); n+=1
    assert n; json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
ed(418,'the man',8.0,y=0.30,h=0.44)
ed(418,'the man',9.0,y=0.37,h=0.55)
ed(422,'the bag',5.0,h=0.78)
ed(424,'the woman',8.0,w=0.43)
ed(424,'the man',8.0,x=0.44,w=0.53)
ed(424,'the woman',8.5,w=0.39)
ed(424,'the man',8.5,x=0.40,w=0.58)
