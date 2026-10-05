import json
p='content/7993.json'; d=json.load(open(p))
w,m,dog=d['taps']
for k in w['keys']:
    if k['t']==1.7: k.update(x=0.02,y=0.17,w=0.84,h=0.63)
for k in dog['keys']:
    if k['t']==1.7:
        k.clear(); k.update(t=1.7,x=0.86,y=0.38,w=0.14,h=0.14)
dog['phrase']='to lie next to the radio'
d['notes']+=' VERIFIER: dog is visible at the right edge at 1.7 -> boxed (narrow, woman box cut at .86); dog phrase made unique (bottles also lie on the ground).'
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
