import json
T=[i*0.5 for i in range(21)]
W=[(0.18,0.14,0.70,0.84),(0.12,0.14,0.74,0.83),(0.18,0.14,0.70,0.83),(0.18,0.14,0.70,0.82),(0.20,0.14,0.60,0.80),
   (0.13,0.14,0.87,0.82),(0.13,0.23,0.80,0.75),(0.15,0.24,0.78,0.74),(0.28,0.22,0.46,0.73),(0.27,0.28,0.53,0.62),
   (0.28,0.36,0.47,0.52),(0.27,0.38,0.53,0.47),(0.30,0.39,0.46,0.43),(0.27,0.41,0.53,0.42),(0.35,0.41,0.33,0.43),
   (0.34,0.41,0.36,0.42),(0.36,0.44,0.29,0.39),(0.36,0.46,0.32,0.39),(0.36,0.48,0.29,0.38),(0.34,0.50,0.36,0.38),(0.34,0.54,0.33,0.36)]
F=[(0,0,1,0.14)]*6+[(0,0,1,0.22),(0,0,1,0.22),(0,0,1,0.21),(0,0,1,0.27),(0,0,1,0.32),(0,0,1,0.33),(0,0.06,1,0.30),
   (0,0,1,0.36),(0,0,1,0.38),(0,0.02,1,0.37),(0,0.04,1,0.38),(0,0.08,1,0.32),(0,0.08,1,0.32),(0,0.10,1,0.30),(0,0.13,1,0.25)]
k=lambda L:[dict(t=t,x=a,y=b,w=c,h=d) for t,(a,b,c,d) in zip(T,L)]
c=dict(mediaId=5033,level="A",keyWord="drum",defaultVoice="female",taps=[
 dict(phrase="to dance in the street",target="the woman",voice="female",keys=k(W)),
 dict(phrase="to open her arms wide",target="the woman",voice="female",keys=k(W)),
 dict(phrase="to hang over the road",target="the flags",voice="female",keys=k(F))],
 stillS=6.0,nouns=[dict(word="flags",x=0.50,y=0.17,voice="female"),dict(word="a woman",x=0.52,y=0.60,voice="female"),
 dict(word="a drum",x=0.10,y=0.61,voice="female"),dict(word="the street",x=0.50,y=0.86,voice="female")],
 question="What is the woman doing?",answer=["She","is","dancing","in","the","street."],answerVoice="female",
 notes="Drummers all do the same thing (many identical drummers), so no single drummer is a target; woman takes two phrases, the bunting flags the third. Woman box starts below the bunting at 0-2.5 s (thin feather tips above 0.14 cut off to keep boxes apart). Arms wide at 0-3.5 and 5.5-6.5 s. 'a drum' pill on the leftmost drum at 6.0.")
json.dump(c,open('content/5033.json','w'),indent=1)
