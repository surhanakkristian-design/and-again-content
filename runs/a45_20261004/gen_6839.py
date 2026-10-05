import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,off=True) if r is None else dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
woman=K([(.08,.38,.76,.62),(.08,.38,.82,.62),(.06,.38,.88,.62),(.06,.38,.90,.62),(.05,.37,.95,.63),(.05,.35,.88,.65),(.05,.35,.65,.65),(.05,.34,.67,.66)])
fw=K([None,None,(.50,.06,.26,.20),(.43,.02,.53,.24),(.40,.00,.57,.29),(.38,.00,.58,.30),(.38,.00,.60,.33),(.38,.00,.62,.32)])
c=dict(mediaId=6839,level="A",keyWord="architecture",defaultVoice="female",
 taps=[dict(phrase="to hold a paper model",target="the woman",voice="female",keys=woman),
       dict(phrase="to look at the fireworks",target="the woman",voice="female",keys=woman),
       dict(phrase="to light up the sky",target="the fireworks",voice="female",keys=fw)],
 stillS=2.2,
 nouns=[dict(word="fireworks",x=.62,y=.10,voice="female"),dict(word="a building",x=.80,y=.31,voice="female"),
        dict(word="a model",x=.72,y=.50,voice="female"),dict(word="a woman",x=.24,y=.72,voice="female")],
 question="What is the woman holding?",
 answer=["She","is","holding","a","paper","model."],answerVoice="female",
 notes="Fireworks only a rising spark at 0.2/0.7 s (off). She looks up at the fireworks from about 2.7 s. Key word 'architecture' abstract, not placed.")
json.dump(c,open("content/6839.json","w"),indent=1)
