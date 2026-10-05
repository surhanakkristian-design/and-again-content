import json
p='content/5556.json'; d=json.load(open(p))
for k in d['taps'][2]['keys']:
    if k['t']==0.7: k.update(y=0.25,h=0.53)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
p='content/5558.json'; d=json.load(open(p))
d['taps'][1]['phrase']='to look through a folder'
d['answer']=["He","is","looking","through","a","folder."]
for n in d['nouns']:
    if n['word']=='croissants': n.update(x=0.88,y=0.72)
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
