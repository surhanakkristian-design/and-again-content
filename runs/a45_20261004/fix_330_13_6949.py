import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setkey(d,target,t,**kw):
    for tap in d['taps']:
        if tap['target']==target:
            for i,k in enumerate(tap['keys']):
                if k['t']==t: tap['keys'][i]={'t':t,**kw}
# 13
d=load(13); setkey(d,'the woman',3.0,x=0,y=0,w=1,h=0.5); save(13,d)
# 330
d=load(330)
setkey(d,'the girl',4.5,x=0,y=0.17,w=0.66,h=0.83)
setkey(d,'the man',4.5,x=0.66,y=0.16,w=0.34,h=0.56)
setkey(d,'the girl',5.5,x=0.07,y=0.27,w=0.53,h=0.73)
setkey(d,'the man',5.5,x=0.60,y=0.38,w=0.18,h=0.18)
d['notes']+=" Verifier: man is visible (small, at the plane door) at 5.5 s -> box added, girl's box narrowed there (her right elbow falls outside); 4.5 s split moved to 0.66 so her hand with the card is in her box."
save(330,d)
# 6949
d=load(6949)
d['nouns']=[{'word':'chocolate','x':0.55,'y':0.28,'voice':'female'},
            {'word':'a dress','x':0.2,'y':0.38,'voice':'female'},
            {'word':'a hand','x':0.32,'y':0.73,'voice':'female'}]
d['notes']+=" Verifier: 'a cup' replaced by 'a dress' (the glass cup is full of chocolate, so 'chocolate' was also right at that pill)."
save(6949,d)
