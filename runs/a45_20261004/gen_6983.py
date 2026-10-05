import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
man=K([(.31,.34,.66,.35),(.26,.32,.72,.37),(.25,.27,.74,.43),(.23,.26,.76,.45),(.21,.25,.78,.45),(.14,.21,.86,.49),(.04,.18,.96,.50),(.02,.17,.98,.50)])
woman=K([(0,.10,.30,.48),(0,.08,.25,.52),(0,.03,.24,.59),(0,.01,.22,.63),(0,0,.20,.64),None,None,None])
lamp=K([(.34,0,.22,.14),(.33,0,.23,.14),(.32,0,.24,.14),(.32,0,.24,.14),None,None,None,None])
taps=[dict(phrase="to wolf down his food",target="the man in front",voice="male",keys=man),
      dict(phrase="to ladle out beans",target="the woman",voice="female",keys=woman),
      dict(phrase="to glow above the table",target="the lantern",voice="male",keys=lamp)]
c=dict(mediaId=6983,level="B",keyWord="consume",defaultVoice="male",taps=taps,stillS=0.7,
 nouns=[dict(word="a lantern",x=.44,y=.06,voice="male"),dict(word="a pot",x=.13,y=.54,voice="male"),
        dict(word="bread",x=.62,y=.63,voice="male"),dict(word="a stack of plates",x=.80,y=.76,voice="male")],
 question="What is the man in front doing?",answer="He is wolfing down his food.".split(),answerVoice="male",
 notes="Woman's ladle reaches into the man's area at 1.7-2.2 s; boxes split at her side, ladle tip falls in the man's box. Woman only hair at the edge from 2.7 s -> off. Lantern leaves the frame from 2.2 s -> off. Other workers in the background also eat, but only the front man wolfs his food.")
json.dump(c,open('content/6983.json','w'),indent=1)
