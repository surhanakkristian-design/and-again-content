import json
W={0.0:(.38,.32,.62,.68),0.5:(.31,.31,.69,.69),1.0:(.36,.32,.64,.68),1.5:(.50,.33,.50,.67),2.0:(.50,.37,.50,.63),2.5:(.58,.38,.42,.62),3.0:(.56,.39,.44,.61),
3.5:(0,.50,.47,.50),4.0:(0,.51,.48,.49),4.5:(0,.52,.47,.48),5.0:(0,.52,.47,.48),5.5:(0,.52,.47,.48),6.0:(0,.52,.47,.48),6.5:(0,.52,.48,.48),
7.0:(.20,.35,.55,.46),7.5:(.28,.37,.41,.39),8.0:(.38,.40,.28,.27),8.5:(.39,.42,.30,.22),9.0:(.38,.35,.30,.22),9.5:(.42,.33,.30,.25),
10.0:(.33,.34,.37,.20),10.5:(.26,.30,.53,.25),11.0:(.20,.30,.68,.28),11.5:(.10,.29,.70,.29),12.0:(0,.27,.72,.33)}
K={3.5:(.36,.36,.50,.14),4.0:(.28,.37,.62,.14),4.5:(.37,.38,.61,.14),5.0:(.38,.38,.62,.14),5.5:(.32,.38,.68,.14),6.0:(.40,.38,.60,.14),6.5:(.38,.38,.57,.14)}
T=[i/2 for i in range(25)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4347,level="B",keyWord="ferry",defaultVoice="female",taps=[
 dict(phrase="to film the wildlife",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to ride through the surf",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to hop across the plain",target="the kangaroos",voice="female",keys=keys(K))],
 stillS=0.0,nouns=[dict(word="the sky",x=.60,y=.15,voice="female"),dict(word="a bridge",x=.15,y=.41,voice="female"),
 dict(word="a visor",x=.57,y=.38,voice="female"),dict(word="foam",x=.22,y=.88,voice="female")],
 question="What is the woman filming?",answer=["She","is","filming","kangaroos","hopping","across","the","plain."],answerVoice="female",
 notes="Key word 'ferry' is a verb and the boat itself is hardly visible (roof and rail only), so it is not used in the texts. In the grass shot the kangaroos run right above the woman's head: boxes are split along a horizontal line, the woman's box starts just under the kangaroos and loses the crown of her hair. Bridge was rejected as a tap target (visible only 0-1.0 s).")
json.dump(c,open('content/4347.json','w'),indent=1,ensure_ascii=False)
