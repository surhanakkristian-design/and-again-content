from gen_306 import keys,run
N=None
W=[(0,.40,.62,1),(.07,.40,.66,1),(0,.38,.60,1),(.06,.36,.58,1),(0,.36,.54,1),(0,.37,.49,1),(.03,.40,.45,1),(0,.39,.46,1),
   (0,.38,.47,1),(0,.37,.48,1),(0,.38,.68,1),(0,.38,.50,1),(0,.38,.43,1),(0,.39,.50,1),(0,.41,.46,1),(0,.42,.41,1),
   (0,.42,.33,1),(0,.42,.25,1),(0,.50,.33,1),(0,.42,.20,1),(.20,.41,.46,1)]
M=[(.63,.34,.94,.82),(.67,.35,.93,.80),(.60,.35,.88,.78),(.58,.36,.82,.74),(.54,.37,.74,.70),(.49,.38,.69,.67),(.45,.40,.65,.62),(.46,.40,.66,.60),
   (.47,.40,.67,.58),(.48,.40,.68,.56),N,N,(.50,.42,.70,.60),(.50,.41,.68,.63),(.46,.42,.66,.68),(.41,.37,.69,.73),
   (.33,.39,.64,.82),(.25,.37,.56,.95),(0,.36,.33,.50),N,(0,.33,.20,.75)]
S=[N]*17+[(.82,.56,1,.72),(.74,.56,.97,.74),(.70,.56,1,.74),N]
d=dict(mediaId=307,level="A",keyWord="fog",defaultVoice="male",
 taps=[dict(phrase="to wear a red hat",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to walk into the fog",target="the man",voice="male",keys=keys(M)),
       dict(phrase="to have white wool",target="the sheep",voice="male",keys=keys(S))],
 stillS=9.5,
 nouns=[dict(word="fog",x=0.50,y=0.20,voice="male"),
        dict(word="a sheep",x=0.85,y=0.62,voice="male"),
        dict(word="a hat",x=0.12,y=0.51,voice="male"),
        dict(word="grass",x=0.50,y=0.88,voice="male")],
 question="Where is the man walking?",
 answer=["He","is","walking","into","the","fog."],answerVoice="male",
 notes="The man walks into the fog 2.0-4.5 s, is hidden by it at 5.0 and 5.5 s (only a faint smudge, set off), and comes back from 6.0 s. Woman: only a state fits her alone (red hat); sheep: a state too (both people also stand on the grass). Where the two people are close the boxes are split on a vertical line, which cuts the woman's far arm in some frames; at 9.0 s the man is behind her, so the split is horizontal at y=0.50 (his head above, her below); at 10.0 s vertical at x=0.20. Sheep visible 8.5-9.5 s only. 'wool' is A2. defaultVoice: mixed pair, evenId false -> male.")
run(307,d)
