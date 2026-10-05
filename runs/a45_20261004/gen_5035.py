import json
T=[i*0.5 for i in range(19)]
J=[(0.17,0.11,0.50,0.89),(0.13,0.12,0.53,0.88),(0.21,0.51,0.64,0.49),(0.15,0.10,0.49,0.90),(0.17,0.10,0.53,0.90),
   (0.0,0.46,0.73,0.51),(0.20,0.43,0.61,0.51),(0.30,0.13,0.46,0.81),(0.16,0.12,0.48,0.81),(0.21,0.16,0.42,0.76),
   (0.20,0.20,0.42,0.75),(0.18,0.22,0.44,0.72),(0.18,0.23,0.43,0.72),(0.15,0.24,0.45,0.72),(0.22,0.27,0.41,0.70),
   (0.35,0.28,0.35,0.69),(0.38,0.29,0.35,0.69),(0.33,0.30,0.37,0.69),(0.29,0.31,0.39,0.69)]
G=[(0.67,0.32,0.32,0.14),(0.66,0.31,0.24,0.14),(0.59,0.30,0.41,0.14),(0.64,0.29,0.36,0.14),(0.70,0.31,0.25,0.14),
   (0.54,0.33,0.45,0.13),(0.70,0.30,0.30,0.12),(0.76,0.33,0.24,0.14),(0.64,0.33,0.35,0.14),(0.63,0.35,0.33,0.14),
   (0.62,0.38,0.35,0.14),(0.62,0.40,0.35,0.14),(0.61,0.40,0.36,0.14),(0.60,0.42,0.38,0.14),(0.63,0.43,0.37,0.14),
   (0.70,0.44,0.30,0.14),(0.73,0.44,0.27,0.14),(0.70,0.45,0.30,0.14),(0.68,0.46,0.32,0.14)]
k=lambda L:[dict(t=t,x=a,y=b,w=c,h=d) for t,(a,b,c,d) in zip(T,L)]
c=dict(mediaId=5035,level="A",keyWord="talent",defaultVoice="female",taps=[
 dict(phrase="to juggle three balls",target="the blond girl",voice="female",keys=k(J)),
 dict(phrase="to pick up a ball",target="the blond girl",voice="female",keys=k(J)),
 dict(phrase="to sit on the grass",target="the friends",voice="female",keys=k(G))],
 stillS=6.0,nouns=[dict(word="trees",x=0.50,y=0.12,voice="female"),dict(word="a T-shirt",x=0.42,y=0.50,voice="female"),
 dict(word="trousers",x=0.30,y=0.70,voice="female"),dict(word="grass",x=0.80,y=0.76,voice="female")],
 question="What is the blond girl doing?",answer=["She","is","juggling","three","balls."],answerVoice="female",
 notes="Juggler read as a young woman (hoop earrings), description says 'young person' - check gender/voice. Friends sit right behind the juggler's arm, so the boxes are split along a vertical line; the juggler's outstretched hand/ball on the right is cut at 0.0-0.5, 1.5-2.0, 3.5-5.0, 7.5-8.5; at 2.5 and 3.0 the split is horizontal (top of her hair cut). Balls in the air are not in the juggler box. Picking up a ball at 1.0 and 2.5-3.0. Key word 'talent' is abstract, not a noun slot.")
json.dump(c,open('content/5035.json','w'),indent=1)
