import json
def ed(i, f):
    p=f'content/{i}.json'; c=json.load(open(p)); f(c); json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
def f02(c):
    for n in c['nouns']:
        if n['word']=='an apron': n['x'],n['y']=0.65,0.42
def f03(c):
    for n in c['nouns']:
        if n['word']=='a rowing boat': n['y']=0.69
        if n['word']=='a lamp post': n['y']=0.80
def f04(c):
    c['taps'][1]['phrase']='to wear an unbuttoned orange shirt'
    for n in c['nouns']:
        if n['word']=='a straw hat': n['x']=0.43
ed(7902,f02); ed(7903,f03); ed(7904,f04)
