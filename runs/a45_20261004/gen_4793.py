import json
T=[i*0.5 for i in range(19)]
M={0.0:(.24,.13,.76,.6),0.5:(.3,.11,.7,.62),1.0:(.38,.1,.62,.62),1.5:(.4,.1,.6,.65),2.0:(.36,.1,.64,.52),
2.5:(.38,.11,.62,.54),3.0:(.32,.12,.68,.64),3.5:(.4,.09,.6,.64),4.0:(0,0,.7,.38),4.5:(0,0,.7,.38),5.0:(.02,0,.7,.4),
5.5:(.14,.16,.68,.56),6.0:(.13,.16,.8,.58),6.5:(.12,.16,.8,.58),7.0:(0,.16,1,.56),
7.5:(.55,.41,.42,.33),8.0:(.5,.46,.37,.27),8.5:(.48,.49,.3,.2),9.0:(.49,.51,.22,.19)}
F={1.5:(.1,.44,.29,.44),2.0:(.28,.63,.44,.15),2.5:(.13,.66,.5,.15)}
K={7.5:(0,0,.73,.32),8.0:(.28,0,.64,.36),8.5:(.12,0,.88,.42),9.0:(.17,.05,.75,.42)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4793,level="B",keyWord="sand",defaultVoice="male",taps=[
 dict(phrase="to gesture to the children",target="the bearded man",voice="male",keys=keys(M)),
 dict(phrase="to flap on the wooden dock",target="the fish",voice="male",keys=keys(F)),
 dict(phrase="to flutter above the park",target="the kites",voice="male",keys=keys(K))],
 stillS=6.0,nouns=[dict(word="a beard",x=.51,y=.36,voice="male"),dict(word="a birdhouse",x=.58,y=.74,voice="male"),
 dict(word="a screwdriver",x=.78,y=.83,voice="male"),dict(word="a workbench",x=.3,y=.93,voice="male")],
 question="What is on the workbench?",answer="There is a wooden birdhouse on the workbench.".split(),answerVoice="male",
 notes="Sanding is not used as a phrase: in the close-up (4.0-5.0) the hand holding the sandpaper seems to come from the child at the left edge, while the bearded man's hand rests on the roof, so who sands is unclear. The man's box in the close-up is his sleeve and hand at the top. In the park (7.5-9.0) the bearded man in the checked shirt with braces is the one at the right of the chess table; the other old man (denim shirt) is not boxed. The kites box covers all kites in the sky.")
json.dump(c,open('content/4793.json','w'),indent=1)
