import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
M=[(0.0,0.26,1.0,0.74),(0.0,0.16,1.0,0.84),(0.0,0.17,1.0,0.81),(0.0,0.27,1.0,0.52),
   (0.08,0.27,0.84,0.52),(0.21,0.26,0.78,0.53),(0.11,0.23,0.73,0.55),(0.07,0.24,0.88,0.56)]
k=[dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,M)]
tap=lambda p:dict(phrase=p,target="the man",voice="male",keys=k)
c=dict(mediaId=5550,level="B",keyWord="ample",defaultVoice="male",
 taps=[tap("to stretch his arms wide"),tap("to roll over on the seat"),tap("to burst out laughing")],
 stillS=3.2,
 nouns=[dict(word="windows",x=0.75,y=0.33,voice="male"),dict(word="a jumper",x=0.38,y=0.42,voice="male"),
        dict(word="a carpet",x=0.12,y=0.68,voice="male"),dict(word="a blanket",x=0.40,y=0.80,voice="male")],
 question="How much room does the man have?",answer=["He","has","ample","room","to","stretch","out."],answerVoice="male",
 notes="Single person clip: all three phrases on the man. Arms flung wide 0.2-1.2 s, rolls onto his front at 1.7-2.2 s and back. Box covers him incl. legs; at 0.2-1.2 s it spans the full width because his arms reach the edges. Answer uses the key word 'ample' (adjective); check that the question reads naturally.")
json.dump(c,open('content/5550.json','w'),indent=1)
