import json
B={0.0:(0,.32,.55,.68),0.5:(0,.33,.60,.67),1.0:(0,.31,.56,.69),1.5:(.12,.32,.45,.68),2.0:(0,.32,.46,.62),2.5:(.30,.28,.27,.70),3.0:(0,.24,.52,.76),3.5:(0,.24,.51,.76),
4.0:(0,.24,.52,.76),4.5:(0,.12,.50,.73),5.0:(0,.12,.48,.70),5.5:(.58,.28,.42,.62),6.0:(.47,.29,.40,.18)}
L={0.0:(.56,.35,.44,.65),0.5:(.61,.35,.39,.65),1.0:(.57,.33,.43,.67),1.5:(.58,.34,.42,.66),2.0:(.47,.33,.53,.64),2.5:(.58,.29,.32,.70),3.0:(.53,.21,.47,.79),3.5:(.52,.21,.48,.79),
4.0:(.53,.22,.47,.78),4.5:(.51,.30,.49,.70),5.0:(.49,.31,.51,.69),5.5:(.18,.52,.39,.48),6.0:(.27,.48,.50,.48)}
G={6.5:(0,.32,1,.68),7.0:(0,.40,1,.60),7.5:(0,.38,1,.62),8.0:(0,.30,1,.70),8.5:(0,.24,1,.76),9.0:(0,.41,1,.59)}
def keys(d):
    out=[]
    for t in [x/2 for x in range(19)]:
        v=d.get(t)
        out.append(dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) if v else dict(t=t,off=True))
    return out
c=dict(mediaId=5287,level="A",keyWord="silence",defaultVoice="female",taps=[
 dict(phrase="to do her friend's hair",target="the brown-haired girl",voice="female",keys=keys(B)),
 dict(phrase="to wear a sparkly top",target="the blonde girl",voice="female",keys=keys(L)),
 dict(phrase="to sit on the floor",target="the big group of girls",voice="female",keys=keys(G))],
 stillS=2.5,nouns=[dict(word="lights",x=.25,y=.12,voice="female"),dict(word="a lamp",x=.11,y=.45,voice="female"),
 dict(word="a window",x=.90,y=.40,voice="female"),dict(word="clothes",x=.18,y=.68,voice="female")],
 question="What is the brown-haired girl doing?",answer=["She","is","doing","her","friend's","hair."],answerVoice="female",
 notes="Key word 'silence' is not a visible noun (the clip shows the opposite: a loud crowd). Brown-haired girl and blonde girl are off from 6.5 (crowd wide shots; they may be among the girls but cannot be told apart). The group target is the whole crowd 6.5-9.0 (most sit on the floor, some on the sofa); off at 5.5-6.0 where only a few girls show around the pair. 'to wear a sparkly top' is a state: the blonde wears the sparkly top over her hoodie from 4.5; no action is hers alone (both pull the top, hug, pout). 6.0: brown-haired girl's box is only her head/shoulders above the blonde (horizontal split).")
json.dump(c,open('content/5287.json','w'),indent=1)
