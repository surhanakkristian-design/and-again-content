import json
p='content/4196.json';c=json.load(open(p))
man,bucket,clock=c['taps']
old={k['t']:k for k in man['keys']}
cell=[]
for k in man['keys']:
    t=k['t']
    if t>6.0: cell.append({'t':t,'off':True});continue
    k2=dict(k)
    if t<=0.5: k2['h']=round(0.84-k['y'],2)
    elif t==1.0: k2['h']=round(0.78-k['y'],2)
    elif t<=5.0: k2['h']=round(k['h']+0.03,2)
    else: k2['h']=round(0.95-k['y'],2)
    cell.append(k2)
bed=[({'t':k['t'],'off':True} if k['t']<=6.0 else k) for k in man['keys']]
c['taps']=[
 {'phrase':'to look at a candle','target':'the man with the candle','voice':'male','keys':cell},
 {'phrase':'to sleep in a bed','target':'the man in bed','voice':'male','keys':bed},
 clock]
c['notes']=(c.get('notes','')+' VERIFIER: the cellar man (moustache, no cap) and the sleeper (red cap, no moustache) look like two people, and nobody sleeps in a bed in the cellar: "to sleep in a bed" is now on only in the bedroom. "to hold a candle" (bucket) removed: the man\'s hand is on the candle at 0.0 s, so it did not fit only the bucket; replaced by "to look at a candle" on the cellar man.')
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
