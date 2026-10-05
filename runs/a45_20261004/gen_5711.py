import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
M=K([(0,0.16,0.64,0.30),(0,0.15,0.68,0.34),(0,0.18,0.80,0.38),(0,0.26,0.98,0.28),(0,0.34,0.94,0.21),(0,0.31,0.92,0.19),(0,0.26,0.95,0.19),(0,0.22,0.97,0.19)])
E=K([(0.36,0.47,0.64,0.53),(0.31,0.50,0.69,0.50),(0.34,0.57,0.66,0.43),(0.14,0.55,0.86,0.45),(0,0.56,1.0,0.44),(0.10,0.51,0.90,0.49),(0.24,0.46,0.76,0.54),(0.23,0.42,0.77,0.58)])
c=dict(mediaId=5711,level="B",keyWord="caring",defaultVoice="male",
 taps=[dict(phrase="to stroke the elephant's head",target="the man",voice="male",keys=M),
       dict(phrase="to drink milk from a bottle",target="the baby elephant",voice="male",keys=E),
       dict(phrase="to curl its trunk upwards",target="the baby elephant",voice="male",keys=E)],
 stillS=0.2,
 nouns=[dict(word="acacia trees",x=0.40,y=0.11,voice="male"),dict(word="a fence",x=0.80,y=0.36,voice="male"),
        dict(word="a milk bottle",x=0.25,y=0.58,voice="male"),dict(word="a blanket",x=0.90,y=0.79,voice="male")],
 question="What is the man doing?",answer=["He","is","bottle-feeding","a","baby","elephant."],answerVoice="male",
 notes="Man and elephant overlap heavily; split horizontally: man box = head/torso above the elephant's head, elephant box below (man's legs inside the elephant box at 2.2 s). Elephant's raised trunk falls partly in the man's box at 0.2-0.7 and 2.7-3.7 s.")
json.dump(c,open('content/5711.json','w'),indent=1)
