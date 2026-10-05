import json
T=[i*0.5 for i in range(21)]
M=[(0.02,0.23,0.98,0.77),(0,0.38,0.12,0.62),(0,0.24,1,0.76),(0,0.24,1,0.76),(0,0.24,1,0.76),(0,0.23,1,0.77),(0,0.24,1,0.76),
(0.26,0.27,0.58,0.58),(0,0.32,0.88,0.52),(0,0.31,0.90,0.51),(0.18,0.29,0.82,0.48),(0.22,0.22,0.62,0.55),(0.38,0.22,0.52,0.50),
(0,0.22,1,0.78),(0,0.22,1,0.78),(0,0.21,1,0.79),(0,0.20,0.74,0.80),(0,0.20,0.70,0.80),(0,0.27,1,0.73),(0,0.28,1,0.72),(0,0.30,1,0.70)]
W=[None,(0.12,0,0.88,1),None,None,None,None,None,(0.84,0.16,0.16,0.56),(0.60,0.11,0.26,0.20),(0.40,0.11,0.32,0.20),(0.53,0.13,0.24,0.16),
(0.62,0.04,0.22,0.17),(0.60,0.05,0.30,0.16),None,None,None,(0.74,0.09,0.26,0.28),(0.70,0.07,0.30,0.30),(0.40,0.06,0.38,0.20),(0.30,0.06,0.66,0.22),(0.40,0.08,0.58,0.22)]
def ks(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
mk,wk=ks(M),ks(W)
d=dict(mediaId=5330,level="A",keyWord="a spy",defaultVoice="male",
taps=[dict(phrase="to hold up a newspaper",target="the man in the hat",voice="male",keys=mk),
dict(phrase="to take a photo",target="the man in the hat",voice="male",keys=mk),
dict(phrase="to carry a tray",target="the waiter",voice="male",keys=wk)],
stillS=0.0,
nouns=[dict(word="a spy",x=0.45,y=0.50,voice="male"),dict(word="a newspaper",x=0.28,y=0.73,voice="male"),
dict(word="a cup",x=0.74,y=0.76,voice="male"),dict(word="a table",x=0.70,y=0.91,voice="male")],
question="What is the spy doing?",answer=["He","is","hiding","behind","a","newspaper."],answerVoice="male",
notes="Waiter boxes are cut where he stands behind the man in the hat (t 4.0-6.0, 8.0-10.0): waiter box above the man's hat / right of him, man box shrunk accordingly (t 8.0, 8.5 the man's box loses his right arm). Waiter set off at t 7.5 (only a sliver at the right edge). At t 3.5 the waiter box is 0.16 wide (right edge). 'a spy' pill sits on the man's coat.")
json.dump(d,open("content/5330.json","w"),indent=1)
