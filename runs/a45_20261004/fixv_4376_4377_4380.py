import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,d): json.dump(d,open(f'content/{i}.json','w'),ensure_ascii=False,indent=1)
def key(tap,t): return next(k for k in tap['keys'] if abs(k['t']-t)<1e-6)
def up(k,dy):
    k['y']=round(k['y']-dy,2); k['h']=round(k['h']+dy,2)
# 4376: woman 5.0 head top cut
d=load(4376); k=key(d['taps'][1],5.0); k['y']=0.38; k['h']=0.62; save(4376,d)
# 4377
d=load(4377)
h=d['taps'][0]; t=d['taps'][1]; door=d['taps'][2]
k=key(h,7.0); k['y']=0.35; k['h']=0.65
for tt in [9.0,9.5,10.0,10.5,11.0,11.5,12.0]: up(key(h,tt),0.03)
for tt in [11.0,11.5,12.0]: up(key(t,tt),0.03)
door['phrase']='to swing wide open'
d['notes']+=' VERIFIER: door phrase changed from "to swing open slowly" (it opens within a second); head padding added to late boxes.'
save(4377,d)
# 4380: 3.0 woman box ended below her hands and swallowed the top of the stream
d=load(4380)
for i in (0,1): key(d['taps'][i],3.0)['h']=0.47
k=key(d['taps'][2],3.0); k['y']=0.48; k['h']=0.52
save(4380,d)
