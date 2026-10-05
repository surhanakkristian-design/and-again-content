import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(bs): return [({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)}) for t,b in zip(T,bs)]
chick=K([(.27,.40,.78,.67),(.29,.43,.78,.67),(.27,.40,.78,.67),(.45,.30,.71,.67),(.44,.29,.71,.67),(.44,.28,.71,.67),(.44,.27,.71,.67),(.44,.28,.71,.67)])
warb=K([(0,.19,.47,.39),(0,.16,.56,.42),(0,.22,.46,.39),(0,.23,.44,.44),(0,.22,.43,.45),(0,.20,.43,.47),(0,.23,.43,.50),(0,.29,.43,.54)])
fly=K([(.69,.25,.87,.39),(.70,.25,.88,.39),(.70,.25,.88,.39),(.72,.25,.90,.39),(.72,.25,.90,.39),(.72,.25,.90,.39),(.72,.26,.90,.40),(.72,.28,.90,.42)])
V="male"
d=dict(mediaId=7231,level="B",keyWord="host",defaultVoice=V,
 taps=[dict(phrase="to beg for more food",target="the big chick",voice=V,keys=chick),
       dict(phrase="to deliver a green caterpillar",target="the warbler on the left",voice=V,keys=warb),
       dict(phrase="to hover above the pond",target="the dragonfly",voice=V,keys=fly)],
 stillS=0.2,
 nouns=[dict(word="willow trees",x=.50,y=.10,voice=V),dict(word="a dragonfly",x=.78,y=.33,voice=V),
        dict(word="a caterpillar",x=.46,y=.44,voice=V),dict(word="a nest",x=.45,y=.80,voice=V)],
 question="What is the big chick doing?",
 answer=["It","is","begging","for","more","food."],answerVoice=V,
 notes="Key word 'host' is abstract here (the warbler is the cuckoo's host), not used as a noun pill. From 1.7 s the chick's raised head sits between the left warbler and the dragonfly, so its box is cut to x .44-.71 to avoid overlaps (left/right edge of its body outside). Second warbler on the right not used as a target.")
json.dump(d,open("content/7231.json","w"),indent=1)
