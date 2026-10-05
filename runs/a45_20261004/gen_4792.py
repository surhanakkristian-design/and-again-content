import json
T=[i*0.5 for i in range(19)]
G={0.0:(.38,.23,.4,.76),0.5:(.3,.13,.68,.87),1.0:(.28,.18,.68,.82),1.5:(.31,.18,.69,.82),
2.0:(0,.33,.42,.5),2.5:(0,.36,.4,.5),3.0:(0,.35,.38,.5),3.5:(0,.34,.36,.5),4.0:(0,.34,.32,.5),
4.5:(0,0,.63,.73),5.0:(0,0,.68,.87),5.5:(0,0,.7,.8),
6.0:(.28,.37,.28,.27),6.5:(.33,.42,.22,.19),7.0:(.42,.45,.16,.22),7.5:(.44,.45,.13,.17),
8.0:(.41,.44,.11,.17),8.5:(.41,.46,.11,.16),9.0:(.42,.47,.1,.16)}
N={0.0:(0,.35,.37,.58),0.5:(0,.34,.29,.58),1.0:(0,.34,.27,.6),1.5:(0,.35,.3,.6),
6.0:(.02,.24,.26,.34),6.5:(.13,.32,.2,.27),7.0:(.19,.36,.23,.25),7.5:(.24,.4,.2,.21),
8.0:(.28,.41,.13,.18),8.5:(.29,.42,.12,.17),9.0:(.32,.44,.1,.17)}
M={2.0:(.54,.17,.46,.6),2.5:(.5,.19,.5,.6),3.0:(.48,.16,.52,.62),3.5:(.41,.13,.59,.62),4.0:(.36,.14,.64,.62),
6.0:(.66,.22,.34,.37),6.5:(.66,.3,.33,.27),7.0:(.62,.36,.3,.23),7.5:(.58,.4,.25,.2),8.0:(.56,.42,.22,.18),8.5:(.56,.43,.22,.17),9.0:(.58,.45,.18,.16)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4792,level="B",keyWord="to plant",defaultVoice="female",taps=[
 dict(phrase="to twirl on the spot",target="the little girl",voice="female",keys=keys(G)),
 dict(phrase="to clap her hands with delight",target="the white-haired woman",voice="female",keys=keys(N)),
 dict(phrase="to cradle a teacup",target="the old man",voice="male",keys=keys(M))],
 stillS=5.0,nouns=[dict(word="a girl",x=.3,y=.1,voice="female"),dict(word="a seedling",x=.52,y=.5,voice="female"),
 dict(word="a trowel",x=.22,y=.78,voice="female"),dict(word="soil",x=.68,y=.9,voice="female")],
 question="What is the girl planting?",answer="She is planting a seedling in the soil.".split(),answerVoice="female",
 notes="Clip has 4 shots. The girl beside the white-haired woman in the garden shots (6.0-9.0) is assumed to be the same girl; there boxes are tiny and split vertically from the woman's box. The old man's arm/hands in the close-up (4.5-5.5) are set off because they overlap the girl's hands. Other white-haired women (watering, sitting) appear at 7.0+ and are not boxed. The girl also holds a cup at 3.0-4.0 but with one hand, so cradling a teacup in both hands fits only the man.")
json.dump(c,open('content/4792.json','w'),indent=1)
