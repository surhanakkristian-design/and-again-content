import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
d=load(4529)
for t in d['taps']:
    if t['target']=='the woman':
        for k in t['keys']:
            if k['t']==7.0: k.update(y=0.36,h=0.64)
            if k['t']==7.5: k.update(y=0.37,h=0.63)
save(4529,d)
d=load(4531)
for n in d['nouns']:
    if n['word']=='a T-shirt': n['x']=0.33
save(4531,d)
d=load(4534)
assert d['answer'][-2:]==['the','woman.']
d['answer'][-2]='a'
save(4534,d)
