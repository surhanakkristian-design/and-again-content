import json
p='content/7763.json'; c=json.load(open(p))
c['stillS']=1.2
for n in c['nouns']:
    if n['word']=='seed pods': n['y']=0.94
c['taps'][1]['phrase']='to hold a tray of seedlings'
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
