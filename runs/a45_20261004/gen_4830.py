import json
M={0.0:(.47,.36,.18,.25),0.5:(.46,.35,.18,.24),1.0:(.45,.36,.18,.22),1.5:(.46,.36,.18,.22),2.0:(.44,.36,.18,.19),2.5:(.43,.37,.18,.18),
3.0:(.41,.41,.19,.16),3.5:(.41,.41,.18,.16),4.0:(.41,.39,.19,.21),4.5:(.40,.39,.23,.26),5.0:(.41,.38,.21,.31),5.5:(.41,.38,.23,.34),
6.0:(.39,.36,.25,.39),6.5:(.41,.36,.24,.42),7.0:(.38,.35,.27,.44),7.5:(.31,.35,.34,.51),8.0:(.35,.36,.24,.55),8.5:(.37,.35,.25,.59),
9.0:(.37,.47,.26,.53),9.5:(.36,.28,.26,.72),10.0:(.40,.56,.20,.14)}
O={0.0:(.58,0,.18,.14),6.0:(.53,0,.18,.14),6.5:(.55,0,.18,.22),7.0:(.54,.05,.19,.27),7.5:(.54,.16,.18,.19),8.0:(.59,.30,.19,.22),
8.5:(.62,.42,.21,.22),9.0:(.63,.54,.18,.36),9.5:(.62,.55,.18,.45),10.0:(.60,.52,.18,.14)}
def keys(D):
    out=[]
    for t in sorted(M):
        if t in D: x,y,w,h=D[t]; out.append(dict(t=t,x=x,y=y,w=w,h=h))
        else: out.append(dict(t=t,off=True))
    return out
mk=keys(M); ok=keys(O)
c=dict(mediaId=4830,level="A",keyWord="swim",defaultVoice="male",
 taps=[dict(phrase="to turn around in the water",target="the man below",voice="male",keys=mk),
       dict(phrase="to look up at the light",target="the man below",voice="male",keys=mk),
       dict(phrase="to reach the surface first",target="the man above",voice="male",keys=ok)],
 stillS=7.0,
 nouns=[dict(word="a mask",x=.53,y=.41,voice="male"),dict(word="water",x=.17,y=.60,voice="male"),
        dict(word="fins",x=.48,y=.73,voice="male"),dict(word="a rope",x=.53,y=.90,voice="male")],
 question="What is the man below doing?",
 answer=["He","is","swimming","up","to","the","surface."],answerVoice="male",
 notes="Two male freedivers. 'the man below' = the main diver in the centre (head down, turns at 2.5-3.5 s, rises). 'the man above' = the second diver, visible only at the top edge at 0.0 and 6.0-9.0 s and as the right head at 10.0 s; at 9.5 s the right pair of legs behind the main diver. At 10.0 s which head is which is a guess (nearer, lower head = man below). Rope pill on the thin line under the fins.")
json.dump(c,open('content/4830.json','w'),indent=1)
