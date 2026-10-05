import json
T=[i*0.5 for i in range(19)]
N=None
E=[(.06,.28,.78,.34),(.06,.28,.78,.34),(.06,.28,.78,.48),(.06,.28,.78,.70),(.04,.28,.80,.72)]+[N]*14
BR=[N]*5+[(.28,0,.72,1),(.20,0,.80,1),(.24,.02,.76,.98),(.45,.05,.55,.65),(.48,.08,.52,.60),(.48,.10,.52,.55),(.50,.10,.50,.52),(.52,.12,.48,.50),(.52,.13,.48,.50),(.48,.14,.52,.50),(.41,.16,.59,.48),(.50,.16,.50,.46),(.51,.16,.49,.44),(.51,.16,.49,.42)]
GL=[N]*6+[(0,.27,.19,.45),(0,.24,.22,.40),(0,.22,.44,.58),(0,.22,.47,.55),(0,.22,.40,.45),(0,.22,.44,.48),(0,.22,.42,.45),(0,.22,.42,.42),(0,.24,.44,.42),(0,.26,.40,.40),(0,.28,.49,.38),(0,.28,.50,.38),(0,.28,.50,.40)]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
c=dict(mediaId=5387,level="B",keyWord="sorrow",defaultVoice="female",
 taps=[dict(phrase="to well up with tears",target="the eye",voice="female",keys=K(E)),
       dict(phrase="to pull out a tissue",target="the woman with braids",voice="female",keys=K(BR)),
       dict(phrase="to wear round glasses",target="the woman in glasses",voice="female",keys=K(GL))],
 stillS=6.0,
 nouns=[dict(word="a sofa",x=.40,y=.27,voice="female"),dict(word="glasses",x=.22,y=.43,voice="female"),
        dict(word="a tissue box",x=.68,y=.80,voice="female"),dict(word="a knitted blanket",x=.22,y=.92,voice="female")],
 question="What are the two friends doing?",answer=["They","are","crying","under","a","blanket."],answerVoice="female",
 notes="'the eye' = the extreme close-up 0-2.0 s only (off afterwards; whose eye is unclear). Both women dab their eyes, so the glasses woman gets a state phrase. 'sorrow' is abstract, not placed as a noun.")
json.dump(c,open('content/5387.json','w'),indent=1)
