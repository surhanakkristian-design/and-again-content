import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setk(c,target,t,box):
    for tap in c['taps']:
        if tap['target']==target:
            for k in tap['keys']:
                if abs(k['t']-t)<1e-6:
                    k.clear(); k.update({'t':t,'x':box[0],'y':box[1],'w':box[2],'h':box[3]})
c=load(791); setk(c,'the man in pink',4.5,(0.28,0.45,0.44,0.50)); save(791,c)
c=load(793)
for n in c['nouns']:
    if n['word']=='grass': n['x'],n['y']=0.16,0.65
save(793,c)
c=load(794)
setk(c,'the man in the straw hat',1.0,(0.39,0.34,0.20,0.18))
setk(c,'the small boy',1.0,(0.24,0.53,0.30,0.33))
setk(c,'the man in the straw hat',1.5,(0.36,0.28,0.25,0.22))
setk(c,'the small boy',1.5,(0.18,0.52,0.44,0.46))
setk(c,'the man in the straw hat',3.5,(0.00,0.38,0.54,0.62))
save(794,c)
