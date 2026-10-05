import json
T=[i*0.5 for i in range(19)]
def K(L): return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,L)]
B=[(0,0.03,1,0.97),(0,0.12,1,0.88),(0,0.10,1,0.90),(0,0.05,1,0.95),(0,0,1,1),(0.62,0.29,0.32,0.33),(0.42,0.28,0.28,0.33),
   (0.40,0.27,0.47,0.35),(0.58,0.23,0.30,0.38),(0.63,0.23,0.27,0.38),(0.05,0.29,0.65,0.71),(0,0.27,0.85,0.73),(0,0.28,0.40,0.72)]+[None]*6
L=[None]*5+[(0.22,0.49,0.20,0.15),(0.22,0.50,0.20,0.15),(0.21,0.16,0.18,0.14),(0.31,0.18,0.18,0.14),(0.38,0.27,0.18,0.14)]+[None]*6+[(0.01,0.62,0.18,0.14),(0.18,0.57,0.18,0.14),(0.12,0.54,0.18,0.14)]
b=K(B); l=K(L)
c=dict(mediaId=5009,level="A",keyWord="child",defaultVoice="male",
 taps=[dict(phrase="to go down a slide",target="the boy",voice="male",keys=b),
       dict(phrase="to kick a ball",target="the boy",voice="male",keys=b),
       dict(phrase="to fly into the air",target="the ball",voice="male",keys=l)],
 stillS=3.0,
 nouns=[dict(word="the sky",x=0.50,y=0.15,voice="male"),dict(word="a child",x=0.57,y=0.40,voice="male"),
        dict(word="a ball",x=0.33,y=0.57,voice="male"),dict(word="grass",x=0.50,y=0.85,voice="male")],
 question="What is the boy kicking?",answer=["He","is","kicking","a","ball."],answerVoice="male",
 notes="Small children play in the background of the park shots; one rides a scooter at 6.5-7.0 s, so no scooter phrase. The ball at 8.0-9.0 s is a tiny blur on the lawn (boxed at minimum size). 'a child' sits on the red-haired boy; the background kids are tiny and unlabelled.")
json.dump(c,open('content/5009.json','w'),indent=1)
