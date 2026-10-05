import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
M=K([(0.14,0.26,0.33,0.74),(0.14,0.26,0.35,0.74),(0.13,0.28,0.35,0.72),(0.11,0.27,0.37,0.73),(0.11,0.28,0.37,0.72),(0.11,0.27,0.37,0.73),(0.09,0.26,0.39,0.74),(0.07,0.24,0.40,0.76)])
R=K([(0.48,0.44,0.36,0.29),(0.50,0.45,0.36,0.27),(0.48,0.39,0.42,0.27),(0.48,0.40,0.40,0.29),(0.48,0.39,0.42,0.31),(0.48,0.38,0.43,0.33),(0.48,0.39,0.44,0.35),(0.47,0.39,0.45,0.36)])
c=dict(mediaId=5707,level="B",keyWord="care for",defaultVoice="male",
 taps=[dict(phrase="to cradle a tortoise",target="the man",voice="male",keys=M),
       dict(phrase="to hold out a strawberry",target="the man",voice="male",keys=M),
       dict(phrase="to nibble a strawberry",target="the tortoise",voice="male",keys=R)],
 stillS=0.7,
 nouns=[dict(word="a lake",x=0.84,y=0.45,voice="male"),dict(word="a tortoise",x=0.66,y=0.55,voice="male"),
        dict(word="a flower bed",x=0.16,y=0.78,voice="male"),dict(word="a bowl of strawberries",x=0.66,y=0.92,voice="male")],
 question="What is the man doing?",answer=["He","is","feeding","the","tortoise","a","strawberry."],answerVoice="male",
 notes="Only two targets (man holds tortoise against his chest); boxes split vertically at the tortoise's left edge, so the man's box clips his right shoulder/arm around the tortoise.")
json.dump(c,open('content/5707.json','w'),indent=1)
