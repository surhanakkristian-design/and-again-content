import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l): return [dict(t=t,x=a,y=b,w=c,h=d) if a is not None else dict(t=t,off=True) for t,(a,b,c,d) in zip(T,l)]
mech=K([(.20,.15,.74,.66),(.24,.15,.64,.62),(.35,.18,.58,.55),(.38,.28,.54,.42),(.37,.36,.48,.40),(.38,.31,.48,.44),(.37,.26,.46,.47),(.35,.25,.48,.48)])
man=K([(.68,0,.19,.14),(.67,0,.19,.14),(.64,0,.19,.17),(.62,0,.18,.27),(.60,0,.19,.31),(.60,0,.19,.30),(.60,0,.19,.25),(.60,0,.19,.24)])
c=dict(mediaId=6894,level="B",keyWord="break apart",defaultVoice="female",
 taps=[dict(phrase="to lift out the engine",target="the mechanic",voice="female",keys=mech),
       dict(phrase="to clasp his hands",target="the man",voice="male",keys=man),
       dict(phrase="to wipe her oily hands",target="the mechanic",voice="female",keys=mech)],
 stillS=3.7,
 nouns=[dict(word="a tennis net",x=.25,y=.20,voice="female"),dict(word="a rag",x=.55,y=.46,voice="female"),
        dict(word="an engine",x=.66,y=.62,voice="female"),dict(word="springs",x=.64,y=.84,voice="female")],
 question="What is the mechanic doing?",answer="She is lifting the engine out of the frame.".split(),answerVoice="female",
 notes="Mechanic = the kneeling woman in the navy jumpsuit (the other woman wears denim overalls behind the net). The man stands behind her; his lower legs overlap her head at 0.7-1.2 and 3.2-3.7, so his box is cut above her head. He has folded arms until ~1.7 and clasps his hands from 2.2. Wiping with the rag only at 3.2-3.7.")
json.dump(c,open('content/6894.json','w'),indent=1)
