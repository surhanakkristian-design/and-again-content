import json
def ed(i,f):
    p=f'content/{i}.json'; c=json.load(open(p)); f(c); json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
def a(c):
    assert c['taps'][1]['phrase']=='to turn very fast'; c['taps'][1]['phrase']='to turn round and round'
def b(c):
    for k in c['taps'][2]['keys']:
        if k['t']==5.0:
            k.pop('off'); k.update(x=0,y=0,w=0.55,h=0.07)
def d(c):
    assert c['taps'][0]['phrase']=='to clutch his calf'; c['taps'][0]['phrase']='to clutch his own calf'
ed(4579,a); ed(4582,b); ed(4583,d)
