import json
p='content/4695.json'; c=json.load(open(p))
man=c['taps'][0]
upd={0.5:(0.38,0,0.62,0.88),1.0:(0.52,0,0.48,0.97),1.5:(0.60,0,0.40,1.0)}
for k in man['keys']:
    if k['t'] in upd: k['x'],k['y'],k['w'],k['h']=upd[k['t']]
c['taps'][1]['phrase']='to fill up with junk'
c['question']='What is the man emptying?'
c['answer']=['He','is','emptying','a','cabinet','full','of','toys.']
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
