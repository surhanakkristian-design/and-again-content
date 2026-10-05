import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(c,target,t,box):
    for tap in c['taps']:
        if tap['target']==target:
            for j,k in enumerate(tap['keys']):
                if abs(k['t']-t)<1e-6:
                    tap['keys'][j]={'t':k['t'],'x':box[0],'y':box[1],'w':box[2],'h':box[3]}
c=load(4025)
setk(c,'the kitten',5.0,(0.0,0.33,0.42,0.40)); setk(c,'the ball',5.0,(0.42,0.59,0.18,0.15))
setk(c,'the kitten',5.5,(0.0,0.32,0.39,0.42)); setk(c,'the ball',5.5,(0.39,0.59,0.18,0.15))
setk(c,'the ball',9.0,(0.62,0.24,0.18,0.14))
save(4025,c)
c=load(4026)
c['answer']=["She","is","riding","over","the","smooth","water."]
save(4026,c)
c=load(4027)
setk(c,'the cow',7.5,(0.36,0.0,0.23,0.57))
save(4027,c)
c=load(4028)
setk(c,'the flag',5.0,(0.57,0.14,0.18,0.22)); setk(c,'the flag',5.5,(0.53,0.10,0.18,0.22))
c['stillS']=5.0
c['nouns']=[{'word':'a dog','x':0.52,'y':0.56,'voice':'female'},{'word':'a flag','x':0.66,'y':0.25,'voice':'female'},{'word':'a road','x':0.5,'y':0.85,'voice':'female'}]
c['answer']=["It","is","riding","a","skateboard","on","a","road."]
save(4028,c)
