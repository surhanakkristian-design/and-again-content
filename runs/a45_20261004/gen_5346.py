import json
T=[i*0.5 for i in range(19)]
M=[(0,0.03,0.67,0.97),(0,0.03,0.72,0.97),(0,0.04,0.69,0.96),(0,0,0.71,1),(0,0,0.74,0.95),(0,0,0.72,1),(0,0.08,0.66,0.92),
(0,0.05,1,0.88),(0,0,1,0.92),(0,0,1,0.92),(0,0.09,1,0.80),(0,0.06,1,0.84),(0,0.08,1,0.70),(0,0.07,1,0.70),(0,0.08,1,0.68),
(0.02,0.17,0.96,0.56),(0.07,0.22,0.92,0.48),(0.10,0.19,0.90,0.51),(0.02,0.15,0.96,0.57)]
G=[(0.67,0.30,0.33,0.70),(0.72,0.30,0.28,0.70),(0.69,0.30,0.31,0.70),(0.71,0.14,0.29,0.76),(0.74,0.06,0.26,0.70),(0.72,0.24,0.28,0.62),(0.66,0.33,0.34,0.67)]+[None]*12
K=lambda L:[dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
mk,gk=K(M),K(G)
c=dict(mediaId=5346,level="A",keyWord="stomach",defaultVoice="male",
taps=[dict(phrase="to hold his stomach",target="the young man",voice="male",keys=mk),
dict(phrase="to eat spaghetti",target="the young man",voice="male",keys=mk),
dict(phrase="to hold a bowl",target="the girl",voice="female",keys=gk)],
stillS=8.5,
nouns=[dict(word="a stomach",x=0.55,y=0.66,voice="male"),dict(word="a fork",x=0.14,y=0.70,voice="male"),
dict(word="spaghetti",x=0.64,y=0.77,voice="male"),dict(word="a bowl",x=0.50,y=0.88,voice="male")],
question="What is the young man eating?",answer=["He","is","eating","a","bowl","of","spaghetti."],answerVoice="male",
notes="The girl (dark hair, navy T-shirt) stands behind him in the queue 0-3.0 s holding a bowl/plate of food (her hands are less clear at 1.5-2.0 s); her box is split from his at his shirt edge. From 3.5 s she is gone; other blurry students sit in the background later. Stomach pill at 8.5 s sits between his hands just above the bowl rim (hands partly cover it).")
json.dump(c,open('content/5346.json','w'),indent=1)
