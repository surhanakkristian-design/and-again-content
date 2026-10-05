import json,sys
T=[i*0.5 for i in range(19)]
B=[(.24,.04,.66,.92),(.10,.03,.72,.96),(.22,.04,.78,.96),(.20,.04,.68,.96),(.13,.02,.87,.98),(.10,.02,.80,.98),
   (.06,.02,.94,.98),(.08,.02,.92,.98),(0,.02,1,.98),(0,.02,1,.98),(0,.03,.78,.97),(0,0,.85,1),(0,0,.90,1),(0,0,1,1),
   (0,.04,1,.96),(.22,.04,.78,.96),(.08,.06,.92,.94),(0,.06,.92,.94),(.03,.07,.94,.93)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
c=dict(mediaId=5084,level="A",keyWord="green",defaultVoice="female",
 taps=[dict(phrase=p,target="the woman",voice="female",keys=keys) for p in
   ["to walk towards the camera","to wear a long green dress","to look over her shoulder"]],
 stillS=0.5,
 nouns=[dict(word="earrings",x=.44,y=.15,voice="female"),dict(word="a dress",x=.45,y=.55,voice="female"),
        dict(word="phones",x=.15,y=.36,voice="female"),dict(word="the floor",x=.80,y=.90,voice="female")],
 question="What is the woman wearing?",answer="She is wearing a long green dress.".split(),answerVoice="female",
 notes="Only one clear target (the model); the guests are many small people on both sides, so all three phrases use the woman. She looks over her shoulder at 7.0-7.5 s. Still 0.5: phones = the group of phones held up by guests on the left (more phones on the right too).")
json.dump(c,open('content/5084.json','w'),indent=1)
