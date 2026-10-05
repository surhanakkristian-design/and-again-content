import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
B={0.2:(0.05,0.24,0.95,0.70),0.7:(0.05,0.23,0.95,0.72),1.2:(0.04,0.24,0.96,0.72),1.7:(0.03,0.23,0.97,0.74),
   2.2:(0.02,0.23,0.97,0.75),2.7:(0.02,0.23,0.98,0.75),3.2:(0.05,0.24,0.95,0.72),3.7:(0.05,0.24,0.95,0.72)}
keys=[dict(t=t,x=B[t][0],y=B[t][1],w=B[t][2],h=B[t][3]) for t in T]
taps=[dict(phrase=p,target="the woman",voice="female",keys=keys) for p in
 ["to catch falling snowflakes","to tilt her head back","to squeeze her eyes shut"]]
c=dict(mediaId=7107,level="B",keyWord="feel",defaultVoice="female",taps=taps,stillS=2.2,
 nouns=[dict(word="a hillside",x=0.50,y=0.12,voice="female"),
        dict(word="lava rocks",x=0.80,y=0.36,voice="female"),
        dict(word="a hot spring",x=0.78,y=0.62,voice="female"),
        dict(word="a swimsuit",x=0.45,y=0.74,voice="female")],
 question="What is the woman doing?",
 answer="She is catching falling snowflakes with her hands.".split(),
 answerVoice="female",
 notes="Only one person, so all three taps share the woman. Key word 'feel' is a verb and not placeable; 'lava rocks' = the snow-covered black rocks on the right.")
json.dump(c,open('content/7107.json','w'),indent=1)
