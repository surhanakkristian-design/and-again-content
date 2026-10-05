import json
def ld(i): return json.load(open(f'content/{i}.json'))
def sv(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
d=ld(8038)
for k in d['taps'][1]['keys']: k['x']=0.22; k['w']=0.78
sv(8038,d)
d=ld(8042)
for n in d['nouns']:
    if n['word']=='a stained glass window': n['word']='a stained-glass window'
sv(8042,d)
d=ld(8043)
for k in d['taps'][1]['keys']:
    if k['t']==0.2: k['x']=0.51; k['w']=0.19
    if k['t']==0.7: k['x']=0.49; k['w']=0.19
sv(8043,d)
