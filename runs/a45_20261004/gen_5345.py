import json
T=[i*0.5 for i in range(19)]
W=[(0,0.26,0.58,0.74),(0,0.28,0.62,0.72),(0,0.26,0.63,0.74),(0,0.24,0.68,0.76),(0,0.36,0.64,0.64),(0,0.38,0.65,0.62),
(0,0.40,0.73,0.60),(0,0.38,0.74,0.62),(0.17,0.36,0.60,0.64),(0.20,0.31,0.66,0.69),(0.12,0.30,0.80,0.70),(0.12,0.29,0.84,0.71),
(0.12,0.26,0.86,0.74),(0.14,0.26,0.86,0.74),(0.13,0.26,0.87,0.74),(0.13,0.26,0.87,0.74),(0.10,0.24,0.90,0.76),(0.10,0.24,0.90,0.76),(0.06,0.23,0.94,0.77)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,W)]
tap=lambda p:dict(phrase=p,target="the woman",voice="female",keys=keys)
c=dict(mediaId=5345,level="B",keyWord="lean",defaultVoice="female",
taps=[tap("to lean on the railing"),tap("to clutch her side"),tap("to screw up her face")],
stillS=6.0,
nouns=[dict(word="the sky",x=0.35,y=0.08,voice="female"),dict(word="a ponytail",x=0.56,y=0.39,voice="female"),
dict(word="shorts",x=0.80,y=0.81,voice="female"),dict(word="a railing",x=0.17,y=0.70,voice="female")],
question="What is the woman doing?",answer=["She","is","leaning","on","the","railing."],answerVoice="female",
notes="All three phrases on the woman: her running partner is only a grey shoulder/arm at the right edge (0-3.5 s) and then a sliver of his face at the top, so he is no fair target. She clutches her side from 1.5 s and leans on the railing from 4.0 s; to lean is the key word (verb).")
json.dump(c,open('content/5345.json','w'),indent=1)
