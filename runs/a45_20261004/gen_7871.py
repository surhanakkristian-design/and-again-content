import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
gs=K([(0.0,0.26,0.76,0.74),(0.06,0.27,0.76,0.73),(0.13,0.28,0.67,0.72),(0.19,0.36,0.57,0.64),(0.28,0.68,0.72,0.32),(0.33,0.76,0.67,0.24),(0.47,0.80,0.53,0.20),(0.49,0.85,0.51,0.15)])
bc=K([None,None,(0.0,0.60,0.13,0.37),(0.0,0.58,0.18,0.41),(0.02,0.60,0.26,0.37),(0.09,0.58,0.45,0.18),(0.19,0.52,0.50,0.28),(0.30,0.48,0.43,0.34)])
wo=K([None,None,None,None,(0.0,0.34,0.18,0.24),(0.0,0.34,0.18,0.24),(0.0,0.34,0.18,0.26),(0.0,0.34,0.18,0.26)])
c=dict(mediaId=7871,level="A",keyWord="hours",defaultVoice="male",
taps=[dict(phrase="to stand on two legs",target="the German shepherd",voice="male",keys=gs),
dict(phrase="to walk to the machine",target="the black-and-white dog",voice="male",keys=bc),
dict(phrase="to hold a clipboard",target="the woman",voice="female",keys=wo)],
stillS=3.2,
nouns=[dict(word="a clock",x=0.72,y=0.12,voice="male"),dict(word="the sky",x=0.14,y=0.24,voice="male"),
dict(word="a forklift",x=0.27,y=0.41,voice="male"),dict(word="a card",x=0.63,y=0.66,voice="male")],
question="What is the black-and-white dog carrying?",answer="It is carrying a card in its mouth.".split(),answerVoice="male",
notes="Woman is small in the background (left edge, 2.2-3.7 only; slivers before are off); 'clipboard' is small/dark - check. German shepherd leaves bottom-right from 2.2; its box shrinks to the visible back. Black-and-white dog box at 2.7 cut at y 0.76 to avoid the shepherd (legs lost). 'clipboard' may be A2+.")
json.dump(c,open('content/7871.json','w'),indent=1)
