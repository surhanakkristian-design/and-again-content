import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l):
    return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,l)]
woman=K([(0,0.30,0.66,0.23),(0,0.30,0.66,0.23),(0,0.30,0.66,0.23),(0,0.24,0.66,0.30),(0,0.06,0.65,0.48),(0,0.06,0.68,0.49),(0,0.04,0.64,0.52),(0,0.30,0.70,0.26)])
clock=K([(0.33,0.53,0.30,0.22),(0.32,0.53,0.31,0.22),(0.32,0.53,0.31,0.23),(0.33,0.54,0.33,0.24),(0.37,0.54,0.31,0.21),(0.36,0.55,0.34,0.25),(0.37,0.56,0.33,0.25),(0.37,0.56,0.35,0.26)])
c=dict(mediaId=6827,level="A",keyWord="alarm clock",defaultVoice="female",
 taps=[dict(phrase="to sleep on a white pillow",target="the woman",voice="female",keys=woman),
       dict(phrase="to lift her head",target="the woman",voice="female",keys=woman),
       dict(phrase="to stand on a newspaper",target="the alarm clock",voice="female",keys=clock)],
 stillS=0.2,
 nouns=[dict(word="a woman",x=0.22,y=0.40,voice="female"),dict(word="a pillow",x=0.70,y=0.45,voice="female"),
        dict(word="an alarm clock",x=0.47,y=0.63,voice="female"),dict(word="a glass",x=0.88,y=0.70,voice="female")],
 question="What is the woman doing?",answer=["She","is","sleeping","on","a","white","pillow."],answerVoice="female",
 notes="Only two targets (woman, alarm clock); the glass is cut by the edge. At 2.2 her arm reaches over the clock onto the book: woman box stops above the clock, her hand on the book is outside both boxes. 'to lift her head' = 2.2-3.2 when she sits up; she sleeps at the start and end.")
json.dump(c,open('content/6827.json','w'),indent=1)
