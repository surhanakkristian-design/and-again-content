import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
def setkey(tap,t,**v):
    for k in tap['keys']:
        if abs(k['t']-t)<1e-6:
            k.clear(); k['t']=t; k.update(v)
# 5332
c=load(5332); chef=c['taps'][0]
setkey(chef,2.0,x=0.46,y=0.22,w=0.26,h=0.26)
for t in (6.5,7.0,7.5): setkey(chef,t,off=True)
c['notes']+=" | VERIFIER: chef added at 2.0 (jacket visible behind the waitress); chef OFF in the group shots 6.5-7.5: the kitchen chef wears a toque, the hatless man in whites in the group is probably someone else and a second toque chef stands at the back."
save(5332,c)
# 5333
c=load(5333)
for tap in c['taps']: setkey(tap,3.0,x=0.0,y=0.2,w=0.88,h=0.8)
save(5333,c)
# 5334
c=load(5334)
for tap in c['taps'][:2]: tap['target']="the man in the denim jacket"
c['question']="What is the man in denim carrying?"
c['nouns'][0]={"word":"an American flag","x":0.53,"y":0.28,"voice":"male"}
c['notes']+=" | VERIFIER: target renamed (other men have beards too: white goatee, red beard); question renamed; 'a beard' replaced by 'an American flag' (two beards visible at the still)."
save(5334,c)
# 5335
c=load(5335)
c['taps'][1]['phrase']="to applaud with her arms raised"
c['question']="What is the woman in denim doing?"
c['answer']=["She","is","applauding","with","her","arms","raised."]
c['notes']+=" | VERIFIER: phrase 2 / answer lifted to B level ('clap above her head' -> 'applaud with her arms raised'); question names the woman (crowd full of young women)."
save(5335,c)
