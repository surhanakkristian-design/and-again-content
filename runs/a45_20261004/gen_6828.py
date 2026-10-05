import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l):
    return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,l)]
woman=K([(0.68,0.66,0.32,0.34),(0.72,0.69,0.28,0.31),(0.76,0.71,0.24,0.29),(0.72,0.73,0.28,0.27),(0.55,0.55,0.45,0.45),(0,0.44,0.70,0.56),(0,0.38,0.59,0.62),(0,0.35,0.66,0.65)])
man=K([None,None,None,None,None,(0.70,0.42,0.22,0.48),(0.59,0.38,0.31,0.57),(0.66,0.36,0.30,0.56)])
c=dict(mediaId=6828,level="B",keyWord="alarm",defaultVoice="female",
 taps=[dict(phrase="to spread her arms wide",target="the woman",voice="female",keys=woman),
       dict(phrase="to lead a line of workers",target="the woman",voice="female",keys=woman),
       dict(phrase="to carry a clipboard",target="the man with the clipboard",voice="male",keys=man)],
 stillS=0.2,
 nouns=[dict(word="an alarm bell",x=0.35,y=0.28,voice="female"),dict(word="a warning light",x=0.64,y=0.50,voice="female"),
        dict(word="the ceiling",x=0.78,y=0.10,voice="female"),dict(word="a hard hat",x=0.88,y=0.71,voice="female")],
 question="What is the woman doing?",answer=["She","is","spreading","her","arms","wide."],answerVoice="female",
 notes="Clipboard man (black man in blue overalls) only from 2.7; the red clipboard is clearly visible only at 3.2-3.7 (at 2.7 he is the same man, clipboard not clear). At 2.7-3.7 the woman's outstretched right arm crosses in front of him: boxes split, her right arm is in his box. Still 0.2: hard hat pill on the woman's helmet; the bell is the key word 'alarm'.")
json.dump(c,open('content/6828.json','w'),indent=1)
