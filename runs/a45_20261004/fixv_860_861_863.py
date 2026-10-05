import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def setkey(tap,t,box):
    for n,k in enumerate(tap['keys']):
        if abs(k['t']-t)<0.01:
            tap['keys'][n]={'t':k['t'],'x':box[0],'y':box[1],'w':box[2],'h':box[3]}; return
    raise SystemExit('no key')
c=load(860)
assert c['taps'][2]['phrase']=='to walk around the car'
c['taps'][2]['phrase']='to walk past the car'
n=c['nouns'][3]; assert n['word']=='a bucket'
c['nouns'][3]={'word':'a woman','x':0.14,'y':0.45,'voice':'female'}
save(860,c)
c=load(861); setkey(c['taps'][2],8.0,(0.80,0.31,0.20,0.14)); save(861,c)
c=load(863)
setkey(c['taps'][0],1.5,(0.33,0.17,0.45,0.80)); setkey(c['taps'][2],1.5,(0.78,0.36,0.22,0.14))
setkey(c['taps'][0],3.5,(0.20,0.46,0.80,0.54)); save(863,c)
