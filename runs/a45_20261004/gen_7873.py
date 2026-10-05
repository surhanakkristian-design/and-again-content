import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) if r else dict(t=t,off=True) for t,r in zip(T,rows)]
off=K([(0.64,0.36,0.18,0.28)]*6+[(0.64,0.35,0.18,0.30),(0.65,0.35,0.18,0.30)])
car=K([(0.18,0.40,0.46,0.24)]*6+[(0.17,0.49,0.47,0.16),(0.22,0.42,0.43,0.23)])
man=K([None]*6+[(0.10,0.32,0.26,0.17),(0.03,0.31,0.19,0.32)])
c=dict(mediaId=7873,level="B",keyWord="illegally",defaultVoice="female",
taps=[dict(phrase="to issue a parking ticket",target="the police officer",voice="female",keys=off),
dict(phrase="to block the pavement",target="the yellow car",voice="female",keys=car),
dict(phrase="to protest with raised arms",target="the man in the linen shirt",voice="male",keys=man)],
stillS=3.2,
nouns=[dict(word="an awning",x=0.30,y=0.09,voice="female"),dict(word="trees",x=0.78,y=0.22,voice="female"),
dict(word="a sports car",x=0.36,y=0.54,voice="female"),dict(word="a pedestrian crossing",x=0.78,y=0.65,voice="female")],
question="What is the police officer doing?",answer="She is issuing a parking ticket.".split(),answerVoice="female",
notes="Officer read as a woman (blonde ponytail). Officer stands in front of the car: boxes split at x~0.64 (her arm with the ticket and the car's rear part fall outside). Man in linen shirt only visible from 3.2 (at 2.7 a sliver behind the group, off); at 3.2/3.7 his legs overlap the car front, split there. Another man in a white T-shirt sits at the cafe - target named by the linen shirt.")
json.dump(c,open('content/7873.json','w'),indent=1)
