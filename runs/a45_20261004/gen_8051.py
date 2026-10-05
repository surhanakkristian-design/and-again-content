import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def box(a): return dict(x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2))
def keys(b): return [dict(t=t,off=True) if a is None else dict(t=t,**box(a)) for t,a in zip(T,b)]
woman=[(0.0,0.0,0.75,1.0),(0.0,0.0,0.83,1.0),(0.18,0.07,0.86,1.0),(0.24,0.11,0.92,0.95),
       (0.34,0.11,0.72,0.86),(0.38,0.12,0.74,0.78),(0.43,0.13,0.89,0.73),(0.45,0.13,0.90,0.69)]
man=[None,None,(0.0,0.58,0.18,1.0),(0.0,0.45,0.24,1.0),
     (0.03,0.43,0.34,1.0),(0.14,0.40,0.38,0.98),(0.19,0.39,0.43,0.94),(0.24,0.38,0.45,0.88)]
d=dict(mediaId=8051,level="B",keyWord="computer science",defaultVoice="female",
 taps=[dict(phrase="to plug in a yellow cable",target="the woman",voice="female",keys=keys(woman)),
       dict(phrase="to balance on a stepladder",target="the woman",voice="female",keys=keys(woman)),
       dict(phrase="to clutch a bundle of cables",target="the man",voice="male",keys=keys(man))],
 stillS=3.2,
 nouns=[dict(word="a stepladder",x=0.62,y=0.84,voice="female"),
        dict(word="a server rack",x=0.85,y=0.55,voice="female"),
        dict(word="a beanie",x=0.30,y=0.42,voice="female")],
 question="What is the woman doing?",
 answer=["She","is","plugging","in","a","yellow","cable."],answerVoice="female",
 notes="Camera pulls back: the man is out of frame at 0.2-0.7 s and only his shoulder and cable bundle show at the left edge at 1.2 s (narrow box). Boxes split along the woman's trouser edge; her hair at the left is cut from 1.7 s. A third person (woman in lilac with a scooter) appears at 3.2-3.7 s, not a target. 'cables' left out of the nouns because cables are everywhere in the picture.")
json.dump(d,open("content/8051.json","w"),indent=1)
