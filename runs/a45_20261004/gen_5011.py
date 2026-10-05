import json
T=[i*0.5 for i in range(21)]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
HW=[(0,0.25,0.76,0.75),(0,0.26,0.86,0.74),(0,0.28,0.88,0.72),(0,0.29,0.90,0.71),(0,0.30,0.82,0.70),(0,0.26,0.78,0.74)]+[None]*15
OM=[None]*6+[(0,0.26,0.47,0.74),(0,0.23,0.72,0.77),(0,0.24,0.80,0.76),(0,0.24,0.82,0.76),(0,0.25,0.80,0.75),(0,0.24,0.80,0.76)]+[None]*9
YM=[None]*12+[(0.42,0.29,0.56,0.71),(0.20,0.35,0.75,0.65),(0.28,0.44,0.72,0.56),(0.28,0.49,0.72,0.51),(0.24,0.47,0.66,0.53),
    (0.25,0.48,0.71,0.52),(0.26,0.49,0.68,0.51),(0.26,0.49,0.70,0.51),(0.24,0.49,0.70,0.51)]
c=dict(mediaId=5011,level="A",keyWord="old",defaultVoice="male",
 taps=[dict(phrase="to wear a red hat",target="the woman in the red hat",voice="female",keys=K(HW)),
       dict(phrase="to kiss an old woman",target="the old man",voice="male",keys=K(OM)),
       dict(phrase="to kiss a young woman",target="the young man",voice="male",keys=K(YM))],
 stillS=4.0,
 nouns=[dict(word="a building",x=0.40,y=0.08,voice="male"),dict(word="a car",x=0.82,y=0.27,voice="male"),
        dict(word="a hand",x=0.70,y=0.50,voice="male"),dict(word="a jacket",x=0.15,y=0.75,voice="male")],
 question="What is the old man doing?",answer=["He","is","kissing","an","old","woman."],answerVoice="male",
 notes="Three separate shots, one target per shot. 'to wear a red hat' is a state: both women hug each other in shot 1, so no action fits only one of them. defaultVoice male (mixed people, evenId false). 'a hand' = the old man's hand on the woman's cheek at 4.0 s.")
json.dump(c,open('content/5011.json','w'),indent=1)
