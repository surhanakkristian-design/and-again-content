import json
def ed(i,f):
    p=f'content/{i}.json'; c=json.load(open(p)); f(c); json.dump(c,open(p,'w'),ensure_ascii=False,indent=1)
def a(c):
    n=[x for x in c['nouns'] if x['word']=='a ceiling fan'][0]; n['x'],n['y']=0.38,0.24
def b(c):
    n=[x for x in c['nouns'] if x['word']=='a blanket'][0]; n['x'],n['y']=0.30,0.90
def d(c):
    for t in c['taps']:
        if t['target']=='the woman': t['target']='the red-haired woman'
    c['question']='What is the red-haired woman doing?'
ed(4595,a); ed(4596,b); ed(4598,d)
