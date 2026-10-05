import json
T=[i*0.5 for i in range(25)]
W=[(0,0,.18,.58),(0,0,.18,.34),(0,0,.36,.48),None,(0,0,.30,.47),(0,0,.16,.48),(0,.06,.43,.51),(0,.11,.26,.46),(0,.16,.35,.45),
   (0,.22,.47,.36),(0,.16,.23,.41),(0,.23,.46,.36),(.07,.23,.49,.37),(.10,.21,.40,.39),(.11,.20,.34,.43),(.10,.20,.40,.42),
   (.10,.24,.29,.35),(.08,.27,.32,.30),(.04,.26,.23,.30),(.06,.26,.19,.28),(.12,.27,.18,.25),(.16,.28,.18,.24),(.18,.30,.19,.20),
   (.21,.32,.18,.20),(.23,.33,.18,.20)]
P=[(.19,.17,.45,.17),(.19,.10,.45,.20),(.37,.08,.20,.17),(0,.05,.62,.22),(.31,.07,.40,.19),(.17,.11,.73,.20),(.44,.21,.56,.24),
   (.27,.25,.73,.21),(.36,.27,.64,.22),(.48,.27,.52,.19),(.24,.25,.76,.22),(.47,.28,.53,.20),(.57,.29,.43,.22),(.51,.29,.49,.20),
   (.48,.32,.52,.20),(.51,.32,.49,.18),(.40,.31,.60,.17),(.41,.32,.59,.17),(.28,.34,.72,.16),(.26,.34,.74,.15),(.31,.34,.68,.14),
   (.35,.34,.63,.14),(.38,.35,.57,.14),(.40,.36,.55,.13),(.42,.37,.52,.13)]
FY=[.59,.36,.49,.32,.48,.49,.58,.58,.62,.59,.58,.60,.61,.61,.64,.63,.60,.58,.57,.55,.53,.53,.51,.53,.54]
F=[(0,y,1,round(1-y,2)) for y in FY]
def k(L):
    return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
c=dict(mediaId=5086,level="B",keyWord="shiny",defaultVoice="female",
 taps=[dict(phrase="to mop the polished floor",target="the cleaner",voice="female",keys=k(W)),
       dict(phrase="to hold a business meeting",target="the people in suits",voice="female",keys=k(P)),
       dict(phrase="to reflect the ceiling lights",target="the floor",voice="female",keys=k(F))],
 stillS=6.0,
 nouns=[dict(word="ceiling lights",x=.55,y=.13,voice="female"),dict(word="windows",x=.80,y=.24,voice="female"),
        dict(word="rubber gloves",x=.40,y=.41,voice="female"),dict(word="a mop",x=.78,y=.57,voice="female")],
 question="What is the cleaner doing?",answer="She is mopping the shiny office floor.".split(),answerVoice="female",
 notes="Cleaner only partly in frame 0.0-2.5 (arm, glove, feet), off at 1.5 (a sliver at the left edge). The meeting people sit behind a glass wall; their box is split from the cleaner where she stands in front of them (the leftmost seated person is sometimes left out of the people box). Floor box = the floor below the cleaner's feet (the floor reaches higher, cut to avoid overlap). Still 6.0: 'rubber gloves' sits on her left glove, the right glove is a bit lower.")
json.dump(c,open('content/5086.json','w'),indent=1)
