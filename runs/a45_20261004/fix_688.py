import json
def ed(i,f):
    p=f'content/{i}.json'; c=json.load(open(p)); f(c); json.dump(c,open(p,'w'),ensure_ascii=False,indent=1)
def a(c):
    assert c['taps'][0]['phrase']=='to put cream on her face'; c['taps'][0]['phrase']='to put on face cream'
def b(c):
    for t in c['taps']:
        for k in t['keys']:
            if k['t']==9.5: k.update(x=0.34,y=0.0,w=0.60,h=0.92)
def d(c):
    assert c['taps'][2]['phrase']=='to be parked beside a wall'; c['taps'][2]['phrase']='to be parked outside'
def e(c):
    assert c['taps'][0]['phrase']=='to stretch his arms'; c['taps'][0]['phrase']='to put his arms up'
ed(688,a); ed(689,b); ed(691,d); ed(692,e)
