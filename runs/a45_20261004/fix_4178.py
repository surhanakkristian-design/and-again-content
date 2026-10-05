import json
p='content/4178.json'; c=json.load(open(p))
for k in c['taps'][1]['keys']:
    if k['t']==9.5:
        k.clear(); k.update({"t":9.5,"x":0.38,"y":0.54,"w":0.22,"h":0.14})
c['answer']=["She","is","sharing","the","corn","with","the","mice."]
json.dump(c,open(p,'w'),indent=1,ensure_ascii=False)
