import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=ld(6993)
for n in d['nouns']:
    if n['word']=='an inkwell': n['word']='a bottle of ink'
sv(6993,d)
d=ld(6994)
for n in d['nouns']:
    if n['word']=='a sari': n['y']=0.42
d['question']='What is the man in white doing?'
sv(6994,d)
d=ld(6995)
for tp in d['taps']:
    for k in tp['keys']:
        if tp['target']=='the dark car' and k['t'] in (0.2,0.7): k['x']=0.82; k['w']=0.18
        if tp['target']=='the woman':
            if k['t']==2.2: k['y']=0.51; k['h']=0.37
            if k['t']==2.7: k['y']=0.57; k['h']=0.36
            if k['t']==3.2: k['y']=0.55; k['h']=0.42
            if k['t']==3.7: k['y']=0.57; k['h']=0.43
for n in d['nouns']:
    if n['word']=='a dirt road': n['x']=0.80
sv(6995,d)
