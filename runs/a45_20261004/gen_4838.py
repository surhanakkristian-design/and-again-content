import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
W={0.0:(.31,.49,.42,.51),0.5:(.20,.57,.42,.43),1.0:(.23,.57,.42,.43),1.5:(.27,.47,.48,.53),3.5:(.29,.52,.34,.48),4.0:(.22,.69,.50,.31),
4.5:(.27,.37,.50,.47),5.0:(.25,.40,.38,.56),5.5:(0,.30,.18,.38),6.5:(.25,.40,.31,.60),7.0:(.06,.76,.30,.24),7.5:(.02,.66,.37,.34),
8.0:(.09,.53,.29,.47),8.5:(0,.38,.35,.62),9.0:(0,.37,.33,.63),9.5:(0,.43,.40,.57),10.0:(0,.52,.38,.48)}
M={6.5:(.68,.48,.18,.16),7.0:(.52,.69,.18,.16),7.5:(.48,.61,.18,.16),8.0:(.47,.53,.18,.17),8.5:(.40,.49,.29,.16),9.0:(.43,.46,.22,.16),
9.5:(.44,.37,.26,.25),10.0:(.43,.33,.25,.26)}
def keys(D):
    return [dict(t=t,x=D[t][0],y=D[t][1],w=D[t][2],h=D[t][3]) if t in D else dict(t=t,off=True) for t in T]
c=dict(mediaId=4838,level="A",keyWord="throw",defaultVoice="female",
 taps=[dict(phrase="to throw a watermelon",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to hold up a beach ball",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to fall in the sand",target="the man",voice="male",keys=keys(M))],
 stillS=10.0,
 nouns=[dict(word="the sky",x=.50,y=.14,voice="female"),dict(word="the sea",x=.13,y=.36,voice="female"),
        dict(word="a beach ball",x=.31,y=.44,voice="female"),dict(word="sand",x=.70,y=.75,voice="female")],
 question="What is the woman doing?",
 answer=["She","is","throwing","a","watermelon."],answerVoice="female",
 notes="Beach montage, one woman in a blue bikini throws a tennis ball, a frisbee, a beach ball and a watermelon. 'the man' = the young man in black shorts who runs in from 6.5 s and falls back into the sand at 8.5 s; the older man sitting on a towel at 2.0 s and tiny background people are not boxed. 2.0-3.0 s and 6.0 s show only the sky, the sea and thrown objects (a hand at the right edge at 2.0 s left unboxed). The question's answer fits 4.5-5.0 s.")
json.dump(c,open('content/4838.json','w'),indent=1)
