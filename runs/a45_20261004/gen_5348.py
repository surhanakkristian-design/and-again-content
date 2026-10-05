import json
T=[i*0.5 for i in range(21)]
N=None
YM=[(0.08,0.46,0.72,0.54),(0,0.52,0.66,0.48),(0,0.51,0.84,0.49),(0,0.46,0.52,0.54),(0,0.43,0.33,0.57),(0,0.44,0.48,0.56)]+[N]*15
WO=[(0.55,0.28,0.25,0.18),(0.45,0.24,0.43,0.28),(0.42,0.36,0.36,0.15),(0.52,0.37,0.28,0.37),(0.33,0.35,0.39,0.39),(0.48,0.33,0.24,0.40),
(0.45,0.36,0.18,0.40),(0.44,0.36,0.18,0.40),(0.44,0.36,0.18,0.40),(0.44,0.33,0.18,0.43),(0.42,0.32,0.18,0.52),N,N,N,
(0.46,0.37,0.18,0.59),(0.35,0.36,0.33,0.63),(0.25,0.37,0.31,0.53),(0.15,0.34,0.30,0.51),(0.13,0.32,0.27,0.47),N,N]
OM=[N]*6+[(0.63,0.28,0.29,0.51),(0.62,0.28,0.26,0.50),(0.62,0.27,0.27,0.51),(0.62,0.24,0.29,0.56),(0.60,0.22,0.32,0.65),
(0.17,0.11,0.83,0.89),(0.18,0.09,0.82,0.91),(0.24,0.09,0.76,0.91),(0.64,0.07,0.36,0.93),(0.68,0.06,0.32,0.94),(0.60,0.05,0.40,0.95),
(0.58,0.05,0.42,0.95),(0.57,0.05,0.43,0.95),(0.19,0.05,0.81,0.95),(0.19,0.09,0.81,0.91)]
K=lambda L:[dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
c=dict(mediaId=5348,level="A",keyWord="thank",defaultVoice="female",
taps=[dict(phrase="to pick up the papers",target="the young man",voice="male",keys=K(YM)),
dict(phrase="to hold an umbrella",target="the older man",voice="male",keys=K(OM)),
dict(phrase="to get on the bus",target="the young woman",voice="female",keys=K(WO))],
stillS=2.0,
nouns=[dict(word="a phone box",x=0.42,y=0.12,voice="female"),dict(word="a taxi",x=0.78,y=0.22,voice="female"),
dict(word="a road",x=0.80,y=0.45,voice="female"),dict(word="papers",x=0.74,y=0.82,voice="female")],
question="What is the older man holding?",answer=["He","is","holding","a","black","umbrella."],answerVoice="male",
notes="Two shots. 0-2.5 s: the young man and the young woman kneel close together, so their boxes are split (his head is left out at 0.0-1.0 s where she is right behind it; her box is only her upper/right part). She holds a bundle of papers there too, but only he picks sheets up from the road. 3.0-10.0 s: older man with the umbrella; she stands right behind him at the bus stop, so her box is a narrow 0.18 strip at her visible left side (3.0-5.0 s) and OFF at 5.5-6.5 s (only her face peeks out behind his arm) and 9.5-10.0 s (inside the bus). His box leaves out the left half of the umbrella at 3.0-5.0 s and 7.0-9.0 s where she is under it. Key word thank (verb) is shown by her wave/smile, not a visible noun.")
json.dump(c,open('content/5348.json','w'),indent=1)
