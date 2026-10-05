import json
T=[i*0.5 for i in range(25)]
B=[(0,0,1,.98),(0,0,1,.98),(0,0,1,.98),(0,0,1,.98),(0,0,1,.98),(0,0,1,.98),
(0,0,.72,.58),(0,.05,.72,.60),(0,.08,.72,.67),(0,.11,.84,.65),(.03,.14,.76,.62),(0,.13,.80,.63),(0,.12,.76,.62),
(.46,.18,.54,.82),(.50,.10,.50,.72),(.46,.05,.54,.72),(.70,.28,.30,.36),(.60,.41,.40,.22),(.36,.42,.64,.28),
(.28,.42,.72,.27),(.28,.40,.66,.28),(.10,.33,.78,.32),(.06,.21,.94,.58),(.04,.15,.96,.58),(.06,.17,.94,.55)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
tg="the officer"
d=dict(mediaId=4983,level="A",keyWord="officer",defaultVoice="male",
taps=[dict(phrase=p,target=tg,voice="male",keys=keys) for p in ["to look at a passport","to check a suitcase","to lie under a van"]],
stillS=11.0,
nouns=[dict(word="a van",x=.55,y=.12,voice="male"),dict(word="an officer",x=.45,y=.42,voice="male"),
dict(word="a torch",x=.22,y=.58,voice="male"),dict(word="a shoe",x=.15,y=.92,voice="male")],
question="What is the officer lying under?",answer=["He","is","lying","under","a","van."],answerVoice="male",
notes="All three phrases on the main officer; the bald second officer and the woman are small background figures with no clear own action. 0.0-2.5 s are close-ups (hands + face fill the frame), so the box is the whole picture. 'a shoe' = someone's dark shoe blurred in the bottom-left corner.")
json.dump(d,open("content/4983.json","w"),indent=1)
