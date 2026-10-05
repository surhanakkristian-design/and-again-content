import json
def ed(i, tgt, t, **kw):
    p='content/%d.json'%i; d=json.load(open(p))
    for tap in d['taps']:
        if tap['target']==tgt:
            for k in tap['keys']:
                if k['t']==t: k.update(kw)
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
ed(650,'the woman',1.0,y=0.15,h=0.72)
ed(650,'the dog',9.0,y=0.62,h=0.38)
ed(651,'the man',4.0,x=0.24,w=0.26)
ed(651,'the man',4.5,x=0.29,w=0.18)
ed(651,'the man',5.0,x=0.30,w=0.18)
ed(651,'the man',7.5,w=0.48)
ed(653,'the man',10.0,x=0.46,w=0.54)
