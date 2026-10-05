import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W=[(0.0,0.35,0.47,0.50),(0.0,0.33,0.48,0.52),(0.0,0.33,0.50,0.53),(0.0,0.33,0.52,0.53),
   (0.0,0.31,0.52,0.59),(0.0,0.30,0.53,0.66),(0.0,0.28,0.53,0.72),(0.0,0.27,0.55,0.73)]
M=[(0.47,0.31,0.25,0.42),(0.48,0.30,0.26,0.44),(0.50,0.29,0.23,0.45),(0.52,0.28,0.24,0.48),
   (0.52,0.26,0.28,0.48),(0.53,0.25,0.29,0.52),(0.53,0.23,0.29,0.55),(0.55,0.21,0.27,0.58)]
B=[(0.72,0.39,0.28,0.44),(0.74,0.39,0.26,0.45),(0.73,0.38,0.27,0.46),(0.76,0.37,0.24,0.47),
   (0.80,0.35,0.20,0.50),(0.82,0.34,0.18,0.42),(0.82,0.35,0.18,0.60),(0.82,0.35,0.18,0.60)]
k=lambda X:[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,X)]
c=dict(mediaId=5551,level="B",keyWord="analysis",defaultVoice="male",
 taps=[dict(phrase="to examine a brass fitting",target="the dark-haired woman",voice="female",keys=k(W)),
       dict(phrase="to crouch behind the machine",target="the man",voice="male",keys=k(M)),
       dict(phrase="to turn a metal cylinder",target="the blonde woman",voice="female",keys=k(B))],
 stillS=0.2,
 nouns=[dict(word="light bulbs",x=0.25,y=0.12,voice="male"),dict(word="an espresso machine",x=0.48,y=0.64,voice="male"),
        dict(word="a brass tank",x=0.62,y=0.80,voice="male"),dict(word="spanners",x=0.72,y=0.90,voice="male")],
 question="What are the three people doing?",answer=["They","are","examining","an","espresso","machine."],answerVoice="male",
 notes="Mixed group, evenId false -> defaultVoice male (answer subject 'They'). Three targets close together: boxes split along vertical lines (woman|man|blonde); the blonde woman's box is narrow (0.18) at 2.7-3.7 s as she is mostly cut off at the right edge, and the man's shoe region near her cylinder is given to her. 'to examine a brass fitting' = she holds up and looks at the small brass part at 0.2-0.7 s, then fits it in. Key word 'analysis' abstract.")
json.dump(c,open('content/5551.json','w'),indent=1)
