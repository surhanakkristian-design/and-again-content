import json
p='content/7994.json'; d=json.load(open(p))
for n in d['nouns']:
    if n['word']=='snow': n.update(x=0.87,y=0.72)
d['notes']+=' VERIFIER: snow pill moved onto the clear snow patch between the women (the old spot was mostly wet pavement).'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/7995.json'; d=json.load(open(p))
d['taps'][0]['phrase']='to pop a wheelie'
d['taps'][1]['phrase']='to fling her arms up'
d['notes']+=' VERIFIER: phrase 1 had no B-level word -> "to pop a wheelie"; phrase 2 "recoil" also fits the waiter/guests who flatten themselves -> "to fling her arms up" (only she raises both arms).'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
