import json
T=[i*0.5 for i in range(25)]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
N=None
W=[(0,0,.72,.74),(0,0,.82,.70),(.05,0,.72,.70),N,N,(0,.06,1.0,.66),(0,.21,.56,.74),(0,.16,.75,.80),(0,.15,.55,.74),
(0,.17,.44,.72),(0,.21,.36,.79),(0,.18,.32,.82),(0,.17,.30,.80),(0,.18,.30,.78),(0,.18,.28,.82),(0,.19,.22,.81),
(0,.30,.20,.46),(0,.30,.19,.44),(0,.30,.18,.42),(0,.30,.18,.42),(0,.30,.18,.40),(0,.30,.18,.40),(0,.31,.18,.43),(0,.31,.18,.43),(0,.31,.18,.41)]
J=[N,N,N,(.12,.17,.88,.83),(.08,.17,.92,.83),N,N,(.82,.12,.18,.70),(.64,.24,.36,.58),(.68,.38,.32,.44),(.53,.24,.47,.56),
(.42,.23,.45,.59),(.38,.22,.43,.58),(.44,.21,.46,.60),(.33,.24,.55,.58),(.31,.23,.56,.60),(.30,.31,.38,.45),(.29,.28,.40,.46),
(.30,.31,.36,.40),(.29,.31,.40,.40),(.32,.31,.33,.40),(.31,.29,.30,.42),(.33,.29,.28,.42),(.34,.28,.26,.43),(.35,.29,.26,.42)]
S=[N]*18+[(.82,.33,.18,.36),(.72,.31,.28,.37),(.69,.29,.31,.39),(.62,.29,.38,.38),(.63,.29,.37,.42),(.61,.29,.39,.42),(.62,.29,.38,.38)]
d=dict(mediaId=4984,level="B",keyWord="briefcase",defaultVoice="female",
taps=[dict(phrase="to wear knee pads",target="the older woman",voice="female",keys=K(W)),
dict(phrase="to clutch a skateboard",target="the man in the jacket",voice="male",keys=K(J)),
dict(phrase="to carry a black briefcase",target="the businessman",voice="male",keys=K(S))],
stillS=10.0,
nouns=[dict(word="the sky",x=.25,y=.08,voice="female"),dict(word="palm trees",x=.70,y=.12,voice="female"),
dict(word="a briefcase",x=.74,y=.46,voice="female"),dict(word="a promenade",x=.45,y=.85,voice="female")],
question="What is the businessman carrying?",answer=["He","is","carrying","a","black","briefcase."],answerVoice="male",
notes="'to wear knee pads' is a state: every rider skates, so no action fits only the woman. Businessman marked off before 9.0 s: a suited figure with a briefcase passes in the background at 6.0-8.5 s (possibly another man, blond at 6.0). 'to clutch a skateboard' = the man in the jacket holding his board on the bench 1.5-4.5 s.")
json.dump(d,open("content/4984.json","w"),indent=1)
