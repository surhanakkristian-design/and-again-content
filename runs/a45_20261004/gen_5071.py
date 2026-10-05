import json
K = {0.0:(.43,.44,.41,.19),0.5:(.17,.43,.63,.23),1.0:(0,.41,.70,.34),1.5:(.28,.15,.72,.75),2.0:(.18,.17,.74,.62),
2.5:(.24,.18,.72,.60),3.0:(.28,.17,.68,.62),3.5:(0,.05,.68,.85),4.0:(0,.05,.65,.85),4.5:(0,.05,.58,.78),5.0:(0,.10,.60,.80),
5.5:(.52,.22,.48,.55),6.0:(.42,.20,.58,.50),6.5:(.38,.19,.62,.52),7.0:(.40,.19,.60,.52),7.5:(.28,.20,.72,.55),
8.0:(.04,.20,.96,.50),8.5:(0,.20,1.0,.50),9.0:(.06,.20,.94,.52)}
keys=[dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in sorted(K.items())]
tg="the mechanic"
c=dict(mediaId=5071,level="B",keyWord="service",defaultVoice="male",
 taps=[dict(phrase=p,target=tg,voice="male",keys=keys) for p in ["to lie on a creeper","to tighten the wheel nuts","to close the bonnet"]],
 stillS=6.0,
 nouns=[dict(word="a mechanic",x=.70,y=.42,voice="male"),dict(word="a bonnet",x=.35,y=.78,voice="male"),dict(word="shelves",x=.14,y=.33,voice="male")],
 question="What is the mechanic doing?",answer=["He","is","servicing","the","car."],answerVoice="male",
 notes="Only one person in the clip, so all three phrases target the mechanic. Shots 3.5-5.0 show only his arms/gloves at the wheel; box covers the visible arms and tool. 'creeper' is technical vocabulary.")
json.dump(c,open('content/5071.json','w'),indent=1)
