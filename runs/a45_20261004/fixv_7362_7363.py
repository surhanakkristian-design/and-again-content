import json
p='content/7362.json'; d=json.load(open(p))
d['taps'][0]['phrase']='to catch a splash of cream'
d['answer']=["It","is","catching","a","splash","of","cream."]
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/7363.json'; d=json.load(open(p))
W={0.2:dict(x=0.2,y=0.12,w=0.52,h=0.47),0.7:dict(x=0.25,y=0.08,w=0.58,h=0.55),1.7:dict(x=0.38,y=0.01,w=0.55,h=0.68),2.2:dict(x=0.37,y=0,w=0.57,h=0.7),2.7:dict(x=0.38,y=0.02,w=0.56,h=0.7)}
M={0.2:dict(x=0.08,y=0.59,w=0.38,h=0.14),0.7:dict(x=0.06,y=0.45,w=0.19,h=0.3),1.7:dict(x=0.07,y=0.47,w=0.31,h=0.3),2.2:dict(x=0.06,y=0.49,w=0.31,h=0.32),2.7:dict(x=0.07,y=0.51,w=0.31,h=0.31)}
for tap in d['taps']:
  src = M if tap['target']=='the man' else W
  new=[]
  for k in tap['keys']:
    new.append(dict(t=k['t'],**src[k['t']]) if k['t'] in src else k)
  tap['keys']=new
d['notes']+=" VERIFIER: man is partly visible behind her legs at 0.2/0.7 s -> boxes on his visible legs/side; woman/man split moved to x 0.37-0.38 at 1.7-2.7 s so her raised arm is mostly inside."
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
