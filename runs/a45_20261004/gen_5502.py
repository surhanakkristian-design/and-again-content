import json
T=[i*0.5 for i in range(19)]
Wm={0.0:(0,.16,.64,.6),0.5:(.25,.17,.52,.57),1.0:(.12,.18,.6,.56),1.5:(.28,.18,.56,.5),2.0:(.3,.21,.48,.35),2.5:(.3,.22,.33,.22),3.0:(.38,.25,.25,.14),
    4.5:(.6,.2,.38,.5),5.0:(.66,.37,.28,.6),5.5:(.69,.36,.3,.6),6.0:(.68,.36,.28,.58),6.5:(.7,.36,.26,.57),7.0:(.7,.36,.27,.6),7.5:(.67,.36,.31,.6),8.0:(.69,.36,.31,.6),8.5:(.57,.36,.43,.64),9.0:(.28,.34,.59,.66)}
P={0.0:(.8,.65,.2,.32),0.5:(.8,.65,.2,.33),1.0:(.82,.65,.18,.32),1.5:(.82,.69,.18,.28),2.0:(.79,.38,.21,.52),2.5:(.8,.4,.2,.5),3.0:(.79,.42,.21,.52),3.5:(.78,.66,.22,.28),4.0:(.79,.44,.21,.5),
   4.5:(.42,.71,.32,.27),5.0:(.4,.76,.26,.22),5.5:(.42,.75,.27,.23),6.0:(.4,.72,.28,.25),6.5:(.4,.72,.3,.24),7.0:(.4,.72,.29,.26),7.5:(.38,.7,.28,.27),8.0:(.38,.71,.3,.25),8.5:(.22,.6,.34,.37),9.0:(0,.63,.28,.35)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=5502,level="B",keyWord="storage",defaultVoice="female",
 taps=[dict(phrase="to stack cardboard boxes",target="the woman",voice="female",keys=keys(Wm)),
       dict(phrase="to carry a loaded pallet",target="the pallet truck",voice="female",keys=keys(P)),
       dict(phrase="to wrap boxes in film",target="the woman",voice="female",keys=keys(Wm))],
 stillS=7.5,
 nouns=[dict(word="cardboard boxes",x=.3,y=.68,voice="female"),dict(word="a pallet truck",x=.55,y=.84,voice="female"),
        dict(word="a hi-vis vest",x=.83,y=.52,voice="female"),dict(word="shelves",x=.7,y=.12,voice="female")],
 question="What is the woman doing?",
 answer=["She","is","stacking","cardboard","boxes","on","a","pallet."],answerVoice="female",
 notes="Key word 'storage' is abstract (no thing to label), so it is not in the nouns or the answer. Woman is hidden behind the stack at 3.5-4.0 s (off). Pallet truck and woman overlap from 4.5 s (her hands on the handle): truck box = orange body and wheels, the handle falls in her box. 'to wrap boxes in film': she holds the film roll at 5.5-6.0 s and the load is wrapped from 4.5 s. The shelves also hold boxes; the 'cardboard boxes' pill is on the big stack.")
json.dump(c,open('content/5502.json','w'),indent=1,ensure_ascii=False)
