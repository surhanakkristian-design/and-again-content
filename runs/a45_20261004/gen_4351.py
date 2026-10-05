import json
W={0.0:(.16,.29,.84,.71),0.5:(.11,.31,.77,.69),1.0:(.24,.30,.70,.70),1.5:(.07,.30,.93,.70),2.0:(.18,.30,.64,.70),
2.5:(.46,.17,.54,.52),3.0:(.43,.19,.57,.48),3.5:(.43,.22,.57,.45),4.0:(.43,.21,.57,.45),4.5:(.44,.20,.56,.46),5.0:(.45,.19,.55,.48),
5.5:(.46,.18,.54,.48),6.0:(.46,.18,.54,.48),6.5:(.46,.18,.54,.48),7.0:(.47,.18,.53,.48),
8.0:(0,.78,.18,.22),8.5:(0,.77,.18,.23),9.0:(0,.58,.37,.42),9.5:(0,.37,.37,.63),
10.0:(0,.34,1.0,.66),10.5:(0,.34,1.0,.66),11.0:(0,.35,1.0,.65),11.5:(0,.35,1.0,.65),12.0:(0,.37,1.0,.63)}
M={t/2:(0,.61,.43,.25) for t in range(5,15)}
C={7.5:(.45,.46,.19,.15),8.0:(.44,.47,.19,.15),8.5:(.43,.47,.19,.15),9.0:(.41,.46,.19,.15),9.5:(.38,.47,.19,.15)}
T=[i/2 for i in range(25)]
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4351,level="B",keyWord="marble",defaultVoice="female",taps=[
 dict(phrase="to lean on the balustrade",target="the woman",voice="female",keys=keys(W)),
 dict(phrase="to play string instruments",target="the musicians",voice="female",keys=keys(M)),
 dict(phrase="to hang from a cable",target="the cable cars",voice="female",keys=keys(C))],
 stillS=4.0,nouns=[dict(word="a chandelier",x=.52,y=.22,voice="female"),dict(word="a trench coat",x=.74,y=.44,voice="female"),
 dict(word="marble",x=.87,y=.63,voice="female"),dict(word="musicians",x=.20,y=.72,voice="female")],
 question="What is the woman leaning on?",answer=["She","is","leaning","on","a","marble","balustrade."],answerVoice="female",
 notes="'balustrade' is above B2 for some learners (alternative: 'railing'), kept because it is the exact word for the wide stone rail. The stone statue at the bottom was left out as a noun because 'marble' could label it too. Several chandeliers are in the hall; the slot is on the nearest, largest one. Cable cars are small and visible 7.5-9.5 s only. At 8.0-8.5 s only a sliver of the woman's coat is in the corner (small box); at 9.5 s her box is cut at x 0.37 so it does not overlap the cable cars (loses her right shoulder). 7.0 s is a cross-fade: woman and musicians still visible.")
json.dump(c,open('content/4351.json','w'),indent=1,ensure_ascii=False)
