import json
def ed(i,f):
    p=f'content/{i}.json'; d=json.load(open(p)); f(d); json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
def a(d):
    n=[x for x in d['nouns'] if x['word']=='a lantern'][0]; n['word']='a lamp'
def b(d):
    t=d['taps'][1]; assert t['phrase']=='to clasp his hands together'; t['phrase']='to wear a khaki jacket'
def c(d):
    n=d['nouns'][0]; assert n['word']=='a jug'; n.update(word='a woman',x=0.44,y=0.22,voice='female')
ed(654,a); ed(656,b); ed(657,c)
