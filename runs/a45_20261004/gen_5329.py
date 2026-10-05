import json
T=[i*0.5 for i in range(25)]
B=[(0,0,1,1),(0,0,1,1),(0,0,1,0.95),(0,0.05,1,0.9),(0,0,1,0.92),(0,0,1,0.72),(0,0,1,0.68),(0,0,1,0.68),
(0,0,1,0.63),(0,0,1,0.62),(0,0,1,0.65),(0,0,1,0.66),(0,0,1,0.68),(0,0,1,0.68),(0,0.05,1,0.63),(0,0,1,0.62),
(0.06,0.05,0.94,0.55),(0.18,0.12,0.78,0.46),(0.22,0.18,0.64,0.39),(0.28,0.11,0.48,0.46),(0.33,0.16,0.40,0.38),
(0.35,0.23,0.37,0.31),(0.37,0.28,0.32,0.26),(0.38,0.31,0.28,0.23),(0.40,0.33,0.24,0.21)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
d=dict(mediaId=5329,level="A",keyWord="a seed",defaultVoice="male",
taps=[dict(phrase=p,target="the man",voice="male",keys=keys) for p in ["to hold a tiny seed","to touch a small plant","to stand behind the plants"]],
stillS=10.0,
nouns=[dict(word="the sky",x=0.50,y=0.10,voice="male"),dict(word="a man",x=0.53,y=0.36,voice="male"),
dict(word="a field",x=0.15,y=0.50,voice="male"),dict(word="plants",x=0.55,y=0.75,voice="male")],
question="What is the man holding?",answer=["He","is","holding","a","tiny","seed."],answerVoice="male",
notes="Only one person (the man; at t 0-2.5 only his hands are visible), so all three phrases target him. The seed (key word) is only visible at t 0-2.5 in his hand, so it is not a noun on the still (t 10.0). The answer refers to the opening shot (t 0-2.5).")
json.dump(d,open("content/5329.json","w"),indent=1)
