import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def box(a): return dict(x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2))
grey=[(0.18,0.27,0.70,0.86),(0.27,0.49,0.73,0.95),(0.15,0.12,0.77,0.87),(0.0,0.04,1.0,0.52),
      (0.0,0.02,1.0,0.46),(0.0,0.03,1.0,0.48),(0.12,0.07,0.80,0.83),(0.10,0.46,0.80,1.0)]
lilac=[(0.0,0.43,0.18,0.82),(0.0,0.43,0.19,0.82),(0.0,0.44,0.15,0.85),(0.0,0.52,0.15,0.85),
       (0.0,0.46,0.16,0.85),(0.0,0.48,0.15,0.85),(0.0,0.44,0.12,0.98),(0.0,0.43,0.10,0.95)]
green=[(0.80,0.43,1.0,0.86),(0.81,0.42,1.0,0.87),(0.77,0.46,1.0,0.88),(0.74,0.52,1.0,0.88),
       (0.74,0.52,1.0,0.90),(0.76,0.53,1.0,0.90),(0.80,0.56,1.0,1.0),(0.80,0.60,1.0,1.0)]
def keys(b): return [dict(t=t,**box(a)) for t,a in zip(T,b)]
d=dict(mediaId=8044,level="B",keyWord="wildly",defaultVoice="male",
 taps=[dict(phrase="to leap into the air",target="the man in grey",voice="male",keys=keys(grey)),
       dict(phrase="to cover her mouth",target="the woman in lilac",voice="female",keys=keys(lilac)),
       dict(phrase="to double over with laughter",target="the man in green",voice="male",keys=keys(green))],
 stillS=0.7,
 nouns=[dict(word="fairy lights",x=0.55,y=0.11,voice="male"),
        dict(word="a bride",x=0.78,y=0.72,voice="female"),
        dict(word="a hay bale",x=0.24,y=0.70,voice="male"),
        dict(word="a tie",x=0.49,y=0.62,voice="male")],
 question="What is the man in grey doing?",
 answer=["He","is","leaping","wildly","into","the","air."],answerVoice="male",
 notes="The leaping man's limbs span the full width in mid-air, so his box is split from the lilac woman (below his leg, left) and the man in green (right) along horizontal/vertical lines; his hands/feet are partly cut at 0.2, 1.2, 3.2, 3.7. The woman in lilac covers her mouth only from 2.2 s on. At 0.7 s the bride partly overlaps the man in green; pill sits on her white dress.")
json.dump(d,open("content/8044.json","w"),indent=1)
