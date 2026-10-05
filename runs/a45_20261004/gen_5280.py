import json
W={0.0:(.48,.27,.34,.73),0.5:(.48,.26,.52,.74),1.0:(.46,.24,.54,.76),1.5:(.47,.25,.53,.75),2.0:(.45,.27,.55,.73),2.5:(.48,.33,.36,.67),3.0:(.48,.36,.27,.64),
3.5:(.00,.52,.52,.48),4.0:(.20,.47,.68,.53),4.5:(.25,.48,.75,.52),5.0:(.27,.61,.66,.39),5.5:(.36,.52,.52,.48),
6.0:(.82,.66,.18,.32),6.5:(.46,.43,.54,.57),7.0:(.15,.42,.72,.58),7.5:(.00,.41,1.0,.59),8.0:(.06,.38,.94,.62),8.5:(.08,.40,.86,.60),9.0:(.13,.41,.77,.59)}
S={0.0:(.00,.42,.47,.58),0.5:(.00,.42,.47,.58),1.0:(.00,.44,.45,.56),1.5:(.00,.44,.46,.56),2.0:(.00,.44,.44,.56),2.5:(.00,.46,.47,.54),3.0:(.00,.48,.47,.52),
3.5:(.20,.00,.80,.51),4.0:(.25,.00,.75,.46),4.5:(.15,.00,.85,.47),5.0:(.00,.00,.85,.60),5.5:(.00,.00,.80,.51),
6.0:(.00,.00,1.0,.64),6.5:(.08,.00,.86,.42),7.0:(.12,.05,.78,.36),7.5:(.15,.06,.72,.34),8.0:(.17,.10,.64,.27),8.5:(.19,.11,.60,.28),9.0:(.22,.17,.57,.23)}
def keys(d): return [dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in sorted(d.items())]
c=dict(mediaId=5280,level="B",keyWord="signpost",defaultVoice="female",taps=[
 dict(phrase="to throw both arms up",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to gaze up at the signs",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to point towards the harbour",target="the signpost",voice="female",keys=keys(S))],
 stillS=9.0,nouns=[dict(word="a signpost",x=.50,y=.24,voice="female"),dict(word="a water bottle",x=.80,y=.47,voice="female"),
 dict(word="the sea",x=.14,y=.58,voice="female"),dict(word="grass",x=.14,y=.86,voice="female")],
 question="What is the woman doing?",answer=["She","is","throwing","both","arms","up."],answerVoice="female",
 notes="Three shots, three different signposts (lane, town square, clifftop) all named 'the signpost'. Woman stands behind/under the post: boxes split along the line between them (shot 1 vertical split at x~0.46, shots 2-3 horizontal split under the sign arms); lower pole partly outside the signpost box. t=6.0 only her arm at the right edge. 'to point towards the harbour' is true of the town-square and clifftop posts (HARBOUR arms), not the lane post.")
json.dump(c,open('content/5280.json','w'),indent=1)
