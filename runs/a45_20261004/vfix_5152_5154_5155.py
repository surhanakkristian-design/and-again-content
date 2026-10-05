import json
def load(i): return json.load(open(f'content/{i}.json'))
def save(i,c): json.dump(c,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)
# 5152: widen late boxes (hair / legs outside)
c=load(5152)
new={10.5:(0.26,0.29,0.64,0.27),11.0:(0.22,0.36,0.66,0.22),11.5:(0.26,0.35,0.56,0.20),12.0:(0.28,0.34,0.46,0.19)}
for t in c['taps']:
  for k in t['keys']:
    if k['t'] in new and not k.get('off'):
      k['x'],k['y'],k['w'],k['h']=new[k['t']]
save(5152,c)
# 5154
c=load(5154)
c['taps'][1]['phrase']='to gaze at the plants'
for n in c['nouns']:
  if n['word']=='houseplants': n['x'],n['y']=0.28,0.86
save(5154,c)
# 5155
c=load(5155)
c['answer']=['She','is','putting','a','big','plate','on','the','table.']
save(5155,c)
