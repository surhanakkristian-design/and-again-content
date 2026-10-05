import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
B=[(.49,.18,.37,.52),(.20,.08,.80,.78),(.18,.08,.82,.90),(.10,.18,.90,.78),(.06,.05,.70,.85),(.07,.12,.70,.82),
(.08,.08,.80,.90),(.16,.18,.70,.82),(.10,.29,.73,.63),(.15,.25,.68,.62),(.15,.20,.55,.63),(.14,.21,.62,.62),
(.08,.22,.62,.63),(.15,.10,.62,.74),(.03,.06,.80,.94),(.02,.05,.80,.95),(.02,.04,.84,.96),(.02,.03,.88,.94),
(.02,.08,.84,.92),(.04,.06,.86,.90),(.00,.08,.84,.90)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
tg="the man in white"
d=dict(mediaId=4982,level="A",keyWord="ankle",defaultVoice="male",
taps=[dict(phrase=p,target=tg,voice="male",keys=keys) for p in ["to kick the ball","to hold his ankle","to sit on a bench"]],
stillS=4.0,
nouns=[dict(word="a goal",x=.18,y=.12,voice="male"),dict(word="a headband",x=.30,y=.38,voice="male"),
dict(word="grass",x=.82,y=.62,voice="male"),dict(word="an ankle",x=.57,y=.77,voice="male")],
question="What is the man in white holding?",answer=["He","is","holding","his","ankle."],answerVoice="male",
notes="All three phrases on the man in white: the two helpers in blue do the same things, so no phrase fits only one of them. 'to kick the ball' only visible 0.0-1.5 s; 'to sit on a bench' from 9.0 s.")
json.dump(d,open("content/4982.json","w"),indent=1)
