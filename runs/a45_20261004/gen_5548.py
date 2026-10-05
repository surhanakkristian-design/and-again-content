import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
B=[(0.25,0.22,0.60,0.58),(0.32,0.22,0.64,0.62),(0.26,0.19,0.74,0.66),(0.33,0.18,0.56,0.69),
   (0.18,0.14,0.72,0.77),(0.15,0.13,0.63,0.80),(0.13,0.13,0.58,0.81),(0.13,0.13,0.58,0.81)]
keys=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,B)]
tap=lambda p:dict(phrase=p,target="the man",voice="male",keys=keys)
c=dict(mediaId=5548,level="A",keyWord="ambition",defaultVoice="male",
 taps=[tap("to dance with a broom"),tap("to turn around"),tap("to close his eyes")],
 stillS=1.2,
 nouns=[dict(word="a lamp",x=0.27,y=0.12,voice="male"),dict(word="a broom",x=0.80,y=0.42,voice="male"),
        dict(word="a man",x=0.55,y=0.62,voice="male"),dict(word="the floor",x=0.30,y=0.90,voice="male")],
 question="What is the man doing?",answer=["He","is","dancing","with","a","broom."],answerVoice="male",
 notes="Single person clip: all three phrases on the man. 'to turn around' = the spin at 1.7 s; 'to close his eyes' = end (2.7-3.7 s). Box includes the broom he holds. Key word 'ambition' is abstract, not a noun slot.")
json.dump(c,open('content/5548.json','w'),indent=1)
