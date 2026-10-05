import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setkey(d,target,t,**kw):
    n=0
    for tap in d['taps']:
        if tap['target']==target:
            for k in tap['keys']:
                if k['t']==t:
                    k.clear(); k['t']=t; k.update(kw); n+=1
    assert n
d=load(702)
setkey(d,'the woman',7.0,x=0.24,y=0.13,w=0.5,h=0.87)
d['answer']=["She","is","putting on","her","sneakers."]
save(702,d)
d=load(705)
setkey(d,'the man',5.0,x=0.57,y=0.15,w=0.43,h=0.85)
setkey(d,'the man',7.5,x=0.53,y=0.24,w=0.47,h=0.76)
d['answer']=["She","is","sneezing","into","her","arm."]
save(705,d)
d=load(707)
setkey(d,'the person in grey',5.5,x=0.82,y=0.36,w=0.18,h=0.26)
save(707,d)
