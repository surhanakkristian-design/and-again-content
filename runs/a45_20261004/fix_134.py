import json
f='content/134.json'; c=json.load(open(f))
new={('the woman',4.5):(0,.38,.41,.45),('the woman',5.0):(0,.37,.29,.42),('the man',4.5):(.8,.33,.2,.37),('the man',5.0):(.68,.33,.32,.40)}
for t in c['taps']:
    for k in t['keys']:
        v=new.get((t['target'],k['t']))
        if v: k.update(dict(zip('xywh',v)))
json.dump(c,open(f,'w'),indent=1,ensure_ascii=False)
f='content/133.json'; c=json.load(open(f))
for n in c['nouns']:
    if n['word']=='sand': n['y']=0.52
json.dump(c,open(f,'w'),indent=1,ensure_ascii=False)
