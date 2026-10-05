import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
# 4948: skyline pill onto the buildings
c=load(4948)
for n in c['nouns']:
    if n['word']=='a skyline': n['y']=0.43
save(4948,c)
# 4949: B-level phrase for the woman; widen her narrow boxes to 0.18
c=load(4949)
t=c['taps'][1]; t['phrase']='to follow the man uphill'
man={k['t']:k for k in c['taps'][0]['keys']}
for k in t['keys']:
    if k.get('off') or k['w']>=0.18: continue
    m=man[k['t']]; mx0=m['x']; mx1=m['x']+m['w']
    if k['x']>=mx1-0.001:  # woman right of man: grow right
        k['w']=0.18
    else:                  # woman left of man: grow left
        k['x']=round(k['x']+k['w']-0.18,2); k['w']=0.18
        if k['x']+k['w']>mx0: k['x']=round(mx0-0.18,2)
save(4949,c)
# 4950: drop the girl in black; second phrase on the woman in red; woman box to right edge 0-2.5
c=load(4950)
w=c['taps'][0]
for k in w['keys']:
    if not k.get('off') and k['t']<=2.5: k['w']=round(1.0-k['x'],2)
c['taps'][2]={'phrase':'to wear a ruffled red skirt','target':'the woman in red','voice':'female',
              'keys':json.loads(json.dumps(w['keys']))}
save(4950,c)
# 4952: older woman boxes at least 0.18 wide, 6.0 taller
c=load(4952)
for k in c['taps'][2]['keys']:
    if k['t']==5.5: k['x'],k['w']=0.11,0.18
    if k['t']==6.0: k['x'],k['w'],k['h']=0.19,0.18,0.55
    if k['t']==6.5: k['x'],k['w']=0.18,0.18
save(4952,c)
