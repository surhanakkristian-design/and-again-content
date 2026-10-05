import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def box(a): return dict(x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2))
def keys(b): return [dict(t=t,**box(a)) for t,a in zip(T,b)]
man=[(0.18,0.28,0.74,0.79),(0.15,0.28,0.70,0.79),(0.07,0.28,0.68,0.80),(0.11,0.29,0.67,0.79),
     (0.09,0.29,0.60,0.80),(0.04,0.27,0.57,0.82),(0.02,0.27,0.52,0.83),(0.09,0.27,0.53,0.84)]
woman=[(0.74,0.36,1.0,0.92),(0.70,0.36,1.0,0.91),(0.68,0.36,1.0,0.90),(0.67,0.36,1.0,0.88),
       (0.60,0.36,1.0,0.85),(0.57,0.36,0.99,0.83),(0.52,0.36,0.92,0.82),(0.53,0.37,0.92,0.82)]
d=dict(mediaId=8050,level="A",keyWord="at first",defaultVoice="male",
 taps=[dict(phrase="to hold the rail",target="the man",voice="male",keys=keys(man)),
       dict(phrase="to skate with no hands",target="the man",voice="male",keys=keys(man)),
       dict(phrase="to wear a red jacket",target="the woman",voice="female",keys=keys(woman))],
 stillS=2.2,
 nouns=[dict(word="a hat",x=0.48,y=0.32,voice="male"),
        dict(word="a Christmas tree",x=0.89,y=0.27,voice="male"),
        dict(word="lights",x=0.29,y=0.22,voice="male"),
        dict(word="ice",x=0.45,y=0.84,voice="male")],
 question="What is the man doing?",
 answer=["He","is","skating","with","no","hands."],answerVoice="male",
 notes="Only two people, so the man takes two phrases. 'to hold the rail' is true only at the start (0.2 s), which fits the key word 'at first'. The woman also holds out her hands, so she gets a state phrase (red jacket) instead. The man's outstretched hand reaches the woman's head; boxes split at the woman's hands.")
json.dump(d,open("content/8050.json","w"),indent=1)
