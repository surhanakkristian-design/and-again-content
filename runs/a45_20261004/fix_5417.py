import json
def setk(d,targets,t,**kw):
    for tap in d["taps"]:
        if tap["target"] in targets:
            for k in tap["keys"]:
                if k["t"]==t: k.update(kw)
p="content/5417.json"; d=json.load(open(p))
setk(d,["the old tram"],5.0,x=0.82,y=0.36,w=0.18,h=0.36)
setk(d,["the old tram"],7.0,x=0.75,y=0,w=0.25,h=0.44)
setk(d,["the woman"],7.0,x=0.82,y=0.44,w=0.18,h=0.56)
json.dump(d,open(p,"w"),indent=1,ensure_ascii=False)
p="content/5502.json"; d=json.load(open(p))
setk(d,["the pallet truck"],5.0,y=0.72,h=0.26)
setk(d,["the pallet truck"],5.5,y=0.72,h=0.26)
setk(d,["the pallet truck"],8.0,w=0.28)
setk(d,["the woman"],8.0,x=0.66,w=0.34)
json.dump(d,open(p,"w"),indent=1,ensure_ascii=False)
