import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def box(a): return dict(x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2))
E=[(0.08,0.25,0.60,0.58),(0.08,0.25,0.57,0.58),(0.08,0.23,0.53,0.61),(0.07,0.23,0.55,0.60),
   (0.05,0.20,0.56,0.60),(0.05,0.19,0.57,0.60),(0.05,0.18,0.57,0.61),(0.05,0.17,0.57,0.63)]
W=[(0.60,0.34,0.88,0.62),(0.57,0.34,0.90,0.61),(0.53,0.34,0.90,0.61),(0.55,0.33,0.92,0.61),
   (0.56,0.33,0.92,0.60),(0.57,0.32,0.95,0.60),(0.57,0.31,0.95,0.61),(0.57,0.31,0.97,0.63)]
H=[(0.42,0.62,0.80,0.90),(0.42,0.61,0.82,0.88),(0.42,0.61,0.80,0.90),(0.42,0.61,0.82,0.88),
   (0.42,0.60,0.82,0.90),(0.42,0.60,0.85,0.90),(0.42,0.61,0.85,0.92),(0.50,0.63,0.90,0.92)]
def keys(b): return [dict(t=t,**box(a)) for t,a in zip(T,b)]
d=dict(mediaId=7782,level="B",keyWord="closer",defaultVoice="female",
 taps=[dict(phrase="to stretch out its trunk",target="the elephant",voice="female",keys=keys(E)),
       dict(phrase="to laugh with delight",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to hold out a banana",target="the hand with the banana",voice="female",keys=keys(H))],
 stillS=1.2,
 nouns=[dict(word="a chandelier",x=0.72,y=0.07,voice="female"),
        dict(word="a trunk",x=0.38,y=0.47,voice="female"),
        dict(word="croissants",x=0.66,y=0.60,voice="female"),
        dict(word="a tablecloth",x=0.42,y=0.86,voice="female")],
 question="What is the elephant doing?",
 answer=["It","is","stretching","its","trunk","closer","to","the","banana."],answerVoice="female",
 notes="The trunk tip crosses in front of the woman's arm and plate; elephant and woman boxes are split along a vertical line there, and the banana hand's box starts right under both. Third target is the viewer's own hand holding the banana (no face). The woman's plate is slightly cut at the bottom of her box where the banana begins.")
json.dump(d,open("content/7782.json","w"),indent=1)
