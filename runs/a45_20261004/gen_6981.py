import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
woman=K([(0,0,.88,.77),(0,0,.87,.75),(0,0,.83,.72),(0,0,1.0,.68),(0,0,.92,.60),(0,0,.72,.56),(.06,0,.58,.52),(.14,.05,.60,.45)])
dog=K([(.20,.85,.35,.15),(.25,.85,.33,.15),(.20,.86,.30,.14),(.24,.86,.30,.14),(.24,.86,.30,.14),(.25,.86,.30,.14),(.24,.86,.28,.14),(.25,.85,.28,.14)])
man=K([None,None,None,None,(.34,.62,.18,.14),(.33,.59,.18,.16),(.35,.54,.18,.20),(.35,.54,.18,.20)])
taps=[dict(phrase="to tighten a bolt",target="the woman",voice="female",keys=woman),
      dict(phrase="to stand on the scaffolding",target="the man on the scaffold",voice="male",keys=man),
      dict(phrase="to stretch out on the grass",target="the dog",voice="female",keys=dog)]
c=dict(mediaId=6981,level="B",keyWord="construct",defaultVoice="female",taps=taps,stillS=3.2,
 nouns=[dict(word="a hard hat",x=.45,y=.06,voice="female"),dict(word="a tool belt",x=.20,y=.38,voice="female"),
        dict(word="a ladder",x=.62,y=.76,voice="female"),dict(word="a dog",x=.38,y=.95,voice="female")],
 question="What is the woman doing?",answer="She is constructing a wooden dome.".split(),answerVoice="female",
 notes="Opening close-up (0.2-1.7 s) shows only the woman's arms/overalls; dog is blurred at the bottom there. Scaffold man first visible (legs only) at 2.2 s. The two men holding the ladder are not used as a target.")
json.dump(c,open('content/6981.json','w'),indent=1)
