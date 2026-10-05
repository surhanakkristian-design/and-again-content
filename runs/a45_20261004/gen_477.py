import json
T=[i*0.5 for i in range(21)]
man=[(0,0,.21,.47),(0,.06,.33,.70),(0,.10,.38,.75),(0,.03,.31,.43),(0,0,.26,.80),(0,.10,.37,.80),(0,.17,.40,.80),(0,.17,.42,.80),(0,.10,.40,.70),(0,.08,.37,.72),(0,.08,.40,.75),(0,0,.34,.46),(0,0,.20,.46),(0,0,.38,.46),(0,.08,.42,.90),(0,.03,.42,.90),(0,.06,.42,.90),(0,.05,.38,.90),(0,.08,.24,.90),(0,.08,.28,.90),(0,.05,.32,.92)]
wom=[(.22,.15,.29,.31),(.34,.18,.18,.24),(.39,.26,.18,.25),(.32,.18,.22,.27),(.27,.15,.22,.40),(.38,.22,.18,.20),(.41,.27,.18,.24),(.43,.26,.18,.24),(.41,.22,.18,.22),(.38,.18,.20,.26),(.41,.22,.18,.24),(.35,.17,.27,.29),(.21,.17,.43,.29),(.39,.15,.36,.30),(.43,.17,.28,.34),(.43,.17,.30,.29),(.43,.12,.30,.31),(.39,.10,.33,.32),(.25,.13,.42,.32),(.29,.13,.41,.31),(.33,.12,.37,.32)]
mic=[(.03,.48,.97,.42),(.53,.43,.47,.46),(.53,.53,.47,.44),(.02,.47,.98,.42),(.50,.42,.50,.47),(.50,.44,.50,.45),(.50,.53,.50,.45),(.52,.51,.48,.46),(.52,.45,.48,.49),(.52,.45,.48,.47),(.52,.47,.48,.49),(.06,.47,.94,.49),(0,.47,1,.46),(.05,.47,.95,.44),(.43,.53,.57,.44),(.43,.47,.57,.43),(.43,.44,.57,.28),(.39,.44,.61,.28),(.25,.46,.75,.32),(.29,.46,.71,.30),(.33,.46,.67,.26)]
def k(b): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,b)]
d=dict(mediaId=477,level="A",keyWord="microwave",defaultVoice="male",
 taps=[dict(phrase="to take out the plate",target="the man",voice="male",keys=k(man)),
       dict(phrase="to stand behind the man",target="the woman",voice="female",keys=k(wom)),
       dict(phrase="to heat the food",target="the microwave",voice="male",keys=k(mic))],
 stillS=9.0,
 nouns=[dict(word="a microwave",x=.78,y=.55,voice="male"),dict(word="a plate",x=.50,y=.84,voice="male"),
        dict(word="a fork",x=.56,y=.70,voice="male"),dict(word="a lamp",x=.27,y=.06,voice="male")],
 question="What is the man taking out?",
 answer=["He","is","taking","a","plate","out","of","the","microwave."],answerVoice="male",
 notes="Man and woman overlap for most of the clip (her face is half hidden 2.5-5.0 s); boxes split along the line between their heads. The man's arm reaches over the microwave box. Man's box partly sits left of / above the microwave door.")
json.dump(d,open("content/477.json","w"),indent=1)
