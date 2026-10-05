import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def box(a): return dict(x=a[0],y=a[1],w=round(a[2]-a[0],2),h=round(a[3]-a[1],2))
def keys(b): return [dict(t=t,**box(a)) for t,a in zip(T,b)]
man=[(0.30,0.43,0.68,0.60),(0.30,0.42,0.68,0.60),(0.29,0.42,0.68,0.60),(0.28,0.41,0.69,0.59),
     (0.27,0.40,0.72,0.59),(0.27,0.39,0.72,0.58),(0.27,0.39,0.72,0.58),(0.25,0.39,0.72,0.59)]
left=[(0.21,0.60,0.49,0.87),(0.21,0.60,0.49,0.87),(0.20,0.60,0.49,0.88),(0.20,0.59,0.49,0.88),
      (0.19,0.59,0.48,0.88),(0.18,0.58,0.47,0.88),(0.18,0.58,0.48,0.89),(0.18,0.59,0.47,0.90)]
mid=[(0.49,0.60,0.74,0.84),(0.49,0.60,0.74,0.85),(0.49,0.60,0.75,0.85),(0.49,0.59,0.75,0.85),
     (0.48,0.59,0.76,0.87),(0.47,0.58,0.76,0.87),(0.48,0.58,0.77,0.88),(0.47,0.59,0.79,0.89)]
d=dict(mediaId=8052,level="A",keyWord="have a shower",defaultVoice="male",
 taps=[dict(phrase="to have a shower",target="the man",voice="male",keys=keys(man)),
       dict(phrase="to hold a white bottle",target="the monkey in the middle",voice="male",keys=keys(mid)),
       dict(phrase="to copy the man",target="the monkey on the left",voice="male",keys=keys(left))],
 stillS=2.2,
 nouns=[dict(word="a waterfall",x=0.25,y=0.20,voice="male"),
        dict(word="a rainbow",x=0.80,y=0.20,voice="male"),
        dict(word="a bag",x=0.82,y=0.57,voice="male"),
        dict(word="a bottle",x=0.55,y=0.70,voice="male")],
 question="What is the man doing?",
 answer=["He","is","having","a","shower."],answerVoice="male",
 notes="The man's body below the chest is hidden behind the monkeys, so his box covers head, arms and chest only and stops at the monkeys' heads. 'to copy the man' = the left monkey holds its hands on its head like him (0.2-3.2 s); at 3.7 s it reaches for the bottle. Middle/left monkey boxes split at the bottle hand.")
json.dump(d,open("content/8052.json","w"),indent=1)
