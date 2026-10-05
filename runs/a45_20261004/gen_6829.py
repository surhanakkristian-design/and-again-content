import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(l):
    return [dict(t=t,off=True) if b is None else dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) for t,b in zip(T,l)]
woman=K([(0.29,0.35,0.39,0.64),(0.29,0.35,0.41,0.65),(0.29,0.35,0.43,0.65),(0.30,0.34,0.45,0.66),(0.29,0.32,0.50,0.68),(0.29,0.32,0.51,0.68),(0.30,0.31,0.52,0.69),(0.33,0.31,0.50,0.69)])
stall=K([None,None,None,None,(0,0.44,0.21,0.20),(0,0.45,0.29,0.21),(0,0.48,0.30,0.22),(0,0.48,0.33,0.21)])
c=dict(mediaId=6829,level="B",keyWord="alien",defaultVoice="female",
 taps=[dict(phrase="to study a guidebook",target="the blonde woman",voice="female",keys=woman),
       dict(phrase="to gaze up at the signs",target="the blonde woman",voice="female",keys=woman),
       dict(phrase="to hand over a paper bag",target="the stallholder",voice="female",keys=stall)],
 stillS=0.2,
 nouns=[dict(word="a lantern",x=0.23,y=0.40,voice="female"),dict(word="a guidebook",x=0.42,y=0.52,voice="female"),
        dict(word="a suitcase",x=0.78,y=0.83,voice="female"),dict(word="a shop sign",x=0.75,y=0.12,voice="female")],
 question="What is the blonde woman doing?",answer=["She","is","studying","a","guidebook."],answerVoice="female",
 notes="Key word 'alien' is not a visible noun. The stallholder is only an arm/hand holding out a paper bag at the left edge from 2.2 (gender not visible -> defaultVoice); box = arm + bag, split from the woman's box where the bag meets her book (3.2-3.7). She studies the book 0.2-1.7 and gazes up 1.7-3.7. The scooter rider passes behind her (blurred, mostly hidden) - not used.")
json.dump(c,open('content/6829.json','w'),indent=1)
