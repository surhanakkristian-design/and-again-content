import json
T=[i*0.5 for i in range(25)]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
N=None
W=[(0,.26,.66,.28),(0,.26,.72,.28),(0,.26,.70,.29),N,N,N,N,N,(0,.50,.40,.50),(0,.44,.34,.56),(0,.43,.40,.57),(0,.41,.42,.59),
(.06,.38,.38,.56),(.08,.35,.38,.56),(.07,.39,.38,.56),(.06,.40,.40,.55),(.02,.41,.42,.50),(.05,.41,.37,.52),(.01,.42,.27,.55),
(0,.44,.20,.52),(0,.45,.22,.50),(0,.48,.22,.44),(0,.51,.22,.47),(0,.52,.22,.44),(.02,.53,.22,.44)]
M=[(.30,.55,.52,.45),(.30,.55,.52,.45),(.30,.56,.52,.44),(.08,.27,.88,.73),(.06,.26,.86,.74),(.06,.26,.84,.74),(0,.40,.86,.60),(0,.40,.80,.60),
(.42,.50,.43,.50),(.38,.42,.52,.58),(.46,.40,.54,.60),(.50,.37,.50,.63),(.50,.35,.45,.65),(.53,.34,.46,.66),(.50,.38,.45,.62),(.50,.38,.42,.62),
(.54,.36,.42,.64),(.53,.36,.47,.64),(.60,.37,.40,.63),(.64,.38,.36,.62),(.76,.40,.24,.60),(.77,.43,.23,.57),(.77,.46,.23,.54),(.75,.49,.25,.51),(.64,.49,.36,.51)]
d=dict(mediaId=4985,level="B",keyWord="fix",defaultVoice="male",
taps=[dict(phrase="to use a cordless drill",target="the woman",voice="female",keys=K(W)),
dict(phrase="to stand on a stepladder",target="the woman",voice="female",keys=K(W)),
dict(phrase="to reach up to the ceiling",target="the man",voice="male",keys=K(M))],
stillS=12.0,
nouns=[dict(word="the ceiling",x=.35,y=.10,voice="male"),dict(word="screens",x=.55,y=.36,voice="male"),
dict(word="a lanyard",x=.77,y=.62,voice="male"),dict(word="a blouse",x=.13,y=.64,voice="male")],
question="What are the two workers doing?",answer=["They","are","fixing","a","screen","to","the","wall."],answerVoice="male",
notes="0.0-1.0 s: woman (on the stepladder, drilling) and man (below, arms up) overlap in the picture; split horizontally at y ~0.54: woman box = her head, arms and drill, man box = his head and body (his raised hands and her legs left out). A third worker in blue is partly hidden behind the woman 4.0-9.5 s (not a target). Key word 'fix' is a verb, used in the answer; defaultVoice male (mixed pair, evenId false), answer 'They' -> defaultVoice.")
json.dump(d,open("content/4985.json","w"),indent=1)
