import json
T=[i*0.5 for i in range(25)]
M=[None,None,None,(0,0,.72,1),(0,0,.88,1),(0,0,.90,1),(0,0,.56,.38),(0,0,.58,.22),(0,.10,.58,.24),(0,.18,.42,.33),
   (0,0,.50,.46),(0,.16,.44,.33),(0,0,.18,.47),(0,0,.28,.38),(0,0,.22,.42),(0,0,.18,.27),(0,0,.23,.26),(0,0,.18,.25),
   (0,.05,.18,.21),(0,.05,.18,.22),(0,0,.52,.30),(.15,.03,.32,.48),(.16,.06,.31,.48),(.16,.07,.30,.47),(.16,.08,.30,.46)]
D=[(0,.20,.18,.29),(0,.23,.55,.36),(.56,.34,.44,.49)]+[None]*22
def k(L):
    return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
c=dict(mediaId=5087,level="A",keyWord="dirty",defaultVoice="male",
 taps=[dict(phrase="to walk across the kitchen",target="the dog",voice="male",keys=k(D)),
       dict(phrase="to clean the dirty floor",target="the man",voice="male",keys=k(M)),
       dict(phrase="to wash the mop",target="the man",voice="male",keys=k(M))],
 stillS=6.0,
 nouns=[dict(word="a cupboard",x=.70,y=.08,voice="male"),dict(word="a bucket",x=.17,y=.25,voice="male"),
        dict(word="a mop",x=.35,y=.56,voice="male"),dict(word="footprints",x=.50,y=.86,voice="male")],
 question="What is the man doing?",answer="He is cleaning the dirty floor.".split(),answerVoice="male",
 notes="Dog only 0.0-1.0 (at 0.0 just a sliver at the left edge). Man mostly partly in frame: face 1.5-2.5, arm/hand washing and wringing the mop 3.0-5.5, only his leg/shoe at the left edge 6.0-9.5 (min-size boxes there, weak), full figure 10.5-12.0. Floor is clean at the end, so 'dirty floor' fits the start of the cleaning. 'footprints' = the muddy paw prints.")
json.dump(c,open('content/5087.json','w'),indent=1)
