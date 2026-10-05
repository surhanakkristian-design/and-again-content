import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,rows)]
win=K([(.29,.54,.45,.27),(.22,.41,.60,.39),(.21,.47,.62,.36),(.16,.47,.73,.40),(.28,.57,.72,.31),(.27,.56,.73,.33),(.19,.59,.77,.33),(.18,.50,.80,.43)])
lef=K([(0,.56,.28,.16),(0,.56,.21,.16),(0,.57,.20,.16),(0,.56,.15,.17),(0,.57,.26,.17),(0,.57,.25,.17),(0,.57,.18,.17),(0,.57,.17,.17)])
scr=K([(.15,0,.72,.21),(.15,0,.73,.20),(.14,0,.75,.19),(.12,0,.78,.18),(.09,0,.83,.15),(.09,0,.88,.14),(.07,0,.90,.14),(.06,0,.90,.14)])
c=dict(mediaId=6893,level="B",keyWord="break a record",defaultVoice="female",
taps=[dict(phrase="to punch the air",target="the swimmer in front",voice="female",keys=win),
      dict(phrase="to stare in disbelief",target="the swimmer on the left",voice="female",keys=lef),
      dict(phrase="to display the new record",target="the big screen",voice="female",keys=scr)],
stillS=3.2,
nouns=[dict(word="a scoreboard",x=.50,y=.05,voice="female"),dict(word="a crowd",x=.13,y=.40,voice="female"),
       dict(word="a swimming pool",x=.75,y=.58,voice="female"),dict(word="goggles",x=.83,y=.67,voice="female")],
question="What is the swimmer in front doing?",answer=["She","is","punching","the","air","with","joy."],answerVoice="female",
notes="Key word 'break a record' is a phrase, not a placeable noun. Left swimmer box is narrow (0.15-0.17 wide at 1.7/3.7 s) because the winner's arm comes close; split along the gap. Two officials stand on deck, so no official noun.")
json.dump(c,open('content/6893.json','w'),indent=1)
