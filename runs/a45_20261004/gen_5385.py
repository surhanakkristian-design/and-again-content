import json
T=[i*0.5 for i in range(21)]
B=[(0,.17,1,.83),(0,.19,1,.81),(0,.32,1,.68),(.05,.48,.76,.44),(0,.45,1,.30),(.10,.40,.90,.23),(.08,.42,.92,.30),(0,.46,.84,.23),(.07,.38,.72,.31),
   (0,.53,1,.24),(.02,.44,.96,.50),(0,.45,1,.50),(0,.17,.92,.83),(0,.33,1,.42),(0,.40,1,.42),(0,.40,1,.60),(0,.38,1,.62),(0,.35,1,.65),(0,.40,1,.60),(0,.38,1,.62),(0,.29,1,.71)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
W="the players"
c=dict(mediaId=5385,level="B",keyWord="a win",defaultVoice="male",
 taps=[dict(phrase=p,target=W,voice="male",keys=keys) for p in ["to huddle in a tight circle","to play volleyball under palm trees","to celebrate a win together"]],
 stillS=4.5,
 nouns=[dict(word="a volleyball",x=.59,y=.27,voice="male"),dict(word="palm trees",x=.22,y=.42,voice="male"),
        dict(word="a net",x=.84,y=.50,voice="male"),dict(word="a court",x=.40,y=.86,voice="male")],
 question="What are the players celebrating?",answer=["They","are","celebrating","their","win."],answerVoice="male",
 notes="Mixed group in identical yellow shirts, several cuts; no single player can be told apart across shots, so all three phrases target the group 'the players' (opposing blockers also wear yellow and are inside the box). The ball was not used as a target because it sits against the players' hands in several frames.")
json.dump(c,open('content/5385.json','w'),indent=1)
