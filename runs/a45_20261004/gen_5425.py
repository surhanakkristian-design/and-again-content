import json
T=[i*0.5 for i in range(25)]
W=[(.12,.37,.36,.27),(.11,.37,.36,.27),(.06,.36,.42,.27),(.02,.37,.45,.27),(.05,.34,.42,.28),(.03,.34,.44,.28),(.01,.34,.45,.28),(.01,.31,.45,.31),
(.00,.28,.46,.34),(.07,.28,.43,.34),(.02,.30,.48,.33),(.00,.30,.46,.32),(.01,.30,.46,.33),(.01,.30,.45,.33),(.01,.31,.46,.32),(.01,.30,.45,.33),
(.10,.30,.38,.33),(.01,.31,.46,.32),(.01,.31,.46,.32),(.07,.33,.41,.32),(.06,.22,.42,.42),(.07,.22,.41,.41),(.10,.24,.37,.40),(.12,.24,.35,.40),(.12,.25,.35,.38)]
M=[(.50,.34,.38,.29),(.49,.33,.40,.30),(.50,.33,.48,.30),(.48,.33,.48,.30),(.48,.30,.46,.32),(.48,.30,.47,.32),(.47,.28,.49,.34),(.47,.27,.50,.36),
(.48,.25,.52,.37),(.51,.25,.49,.36),(.51,.26,.49,.37),(.47,.25,.52,.37),(.48,.26,.51,.37),(.48,.27,.48,.36),(.48,.27,.46,.37),(.48,.27,.50,.36),
(.49,.27,.51,.36),(.48,.27,.52,.36),(.49,.27,.51,.36),(.49,.30,.51,.36),(.50,.18,.50,.48),(.48,.14,.52,.50),(.48,.17,.52,.48),(.48,.17,.50,.48),(.48,.18,.49,.47)]
def keys(L): return [dict(t=t,x=a,y=b,w=c,h=d) for t,(a,b,c,d) in zip(T,L)]
c=dict(mediaId=5425,level="A",keyWord="deal",defaultVoice="male",
taps=[dict(phrase="to wear a green jacket",target="the woman",voice="female",keys=keys(W)),
dict(phrase="to wear a grey suit",target="the man",voice="male",keys=keys(M)),
dict(phrase="to carry a blue folder",target="the man",voice="male",keys=keys(M))],
stillS=1.0,
nouns=[dict(word="trees",x=.50,y=.10,voice="male"),dict(word="a woman",x=.28,y=.53,voice="female"),
dict(word="a man",x=.70,y=.51,voice="male"),dict(word="a table",x=.80,y=.82,voice="male")],
question="What is the man carrying?",answer=["He","is","carrying","a","blue","folder."],answerVoice="male",
notes="Woman's jacket is teal (blue-green), called green. Man carries the folder under his arm only from 10.5 s (picks it up at 10.0); before that both signers sit and sign. Crowd of colleagues behind is not a target (men there wear dark suits, not grey). An extra colleague leans in with a stamp at 6.5-8.0 near the signers. Two people of different gender as main persons -> defaultVoice male (evenId false). Key word 'deal' is not a visible noun.")
json.dump(c,open('content/5425.json','w'),indent=1)
