import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
# 4071
c=load(4071)
for t in c['taps']:
    if t['target']=='the woman':
        for k in t['keys']:
            if k['t']==7.0: k.update(x=0,y=0.43,w=0.68,h=0.20)
for n in c['nouns']:
    if n['word']=='a boat': n.update(word='a woman',x=0.5,y=0.38,voice='female')
save(4071,c)
# 4072
c=load(4072)
for t in c['taps']:
    if t['target']=='the lagoon':
        t['phrase']='to glow bright turquoise'
        for k in t['keys']:
            if k['t']==1.5: k.pop('off',None); k.update(x=0,y=0.86,w=0.45,h=0.14)
            if k['t']==2.0: k.pop('off',None); k.update(x=0,y=0.78,w=1.0,h=0.22)
save(4072,c)
# 4073
c=load(4073)
c['answer']=["She","is","threatening","the","pigeon","with","a","stick."]
c['answerVoice']='female'
save(4073,c)
# 4074
c=load(4074)
for t in c['taps']:
    if t['target']=='the woman': t['phrase']='to wear a red swimsuit'
    if t['target']=='the sun': t['phrase']='to shine on the water'
save(4074,c)
