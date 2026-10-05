import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
chef=K([(0.42,0.0,0.83,1.0),(0.40,0.0,0.75,1.0),(0.41,0.03,0.69,1.0),(0.40,0.04,0.66,1.0),(0.40,0.07,0.62,1.0),(0.40,0.09,0.60,1.0),(0.37,0.12,0.58,0.96),(0.39,0.14,0.59,0.95)])
cow=K([None,(0.75,0.46,1.0,0.64),(0.69,0.45,1.0,0.68),(0.66,0.44,1.0,0.66),(0.62,0.36,1.0,0.80),(0.60,0.37,1.0,0.78),(0.58,0.40,1.0,0.76),(0.59,0.41,1.0,0.76)])
trol=K([(0.01,0.62,0.42,0.90),(0.08,0.59,0.40,0.86),(0.08,0.57,0.41,0.79),(0.13,0.57,0.40,0.78),(0.13,0.54,0.40,0.74),(0.15,0.54,0.40,0.71),(0.19,0.52,0.37,0.69),(0.21,0.51,0.39,0.68)])
c=dict(mediaId=6865,level="B",keyWord="bear",defaultVoice="female",
 taps=[dict(phrase="to balance a wedding cake",target="the chef",voice="female",keys=chef),
       dict(phrase="to sniff the chef's arm",target="the brown and white cow",voice="female",keys=cow),
       dict(phrase="to lie overturned in the mud",target="the shopping trolley",voice="female",keys=trol)],
 stillS=2.7,
 nouns=[dict(word="a wedding cake",x=0.42,y=0.21,voice="female"),dict(word="a marquee",x=0.85,y=0.13,voice="female"),
        dict(word="a shopping trolley",x=0.28,y=0.62,voice="female"),dict(word="mud",x=0.75,y=0.88,voice="female")],
 question="What is the chef doing?",answer=["She","is","carrying","a","wedding","cake","above","her","head."],answerVoice="female",
 notes="Key word 'bear' (verb, to carry/bear a weight) is not a noun, not among the nouns. Chef box starts at the trolley's right edge, so her raised left arm and the left part of the cake fall outside it (trolley lies behind her). Brown and white cow is only a sliver at the right edge at 0.2 (off); it nuzzles her arm/side at 2.2-3.2. Other black cows crowd nearby but do not sniff her. Chef box right edge cut to the cow's nose at 1.2-3.7, so part of her apron is outside.")
json.dump(c,open('content/6865.json','w'),indent=1)
