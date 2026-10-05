import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c, open(f'content/{i}.json','w'), indent=1, ensure_ascii=False)
def setk(tap, t, **kw):
    for n,k in enumerate(tap['keys']):
        if abs(k['t']-t)<0.01: tap['keys'][n] = {'t': k['t'], **kw}; return
    raise SystemExit('no key')
c = load(407)
setk(c['taps'][0], 4.5, x=0.28, y=0.32, w=0.28, h=0.10)
setk(c['taps'][1], 4.5, x=0.26, y=0.42, w=0.52, h=0.41)
save(407, c)
c = load(408)
setk(c['taps'][1], 2.5, x=0.86, y=0.35, w=0.14, h=0.65)
for n in c['nouns']:
    if n['word'] == 'a woman': n['x'], n['y'] = 0.60, 0.80
save(408, c)
c = load(410)
c['taps'][0]['phrase'] = 'to open a jam jar'
setk(c['taps'][0], 3.0, x=0.57, y=0, w=0.43, h=0.65)
setk(c['taps'][2], 3.0, x=0.37, y=0.08, w=0.20, h=0.15)
setk(c['taps'][2], 7.0, x=0.45, y=0.08, w=0.35, h=0.16)
setk(c['taps'][2], 10.0, x=0.47, y=0.32, w=0.15, h=0.14)
save(410, c)
