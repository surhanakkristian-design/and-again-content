import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) for t,r in zip(T,rows)]
split=[.38,.37,.37,.40,.39,.39,.35,.37]
mtop=[.16,.27,.27,.24,.21,.19,.17,.17]
wtop=[.37,.37,.37,.34,.33,.32,.31,.31]
wr=[.79,.81,.81,.83,.84,.88,.89,.90]
man=K([(.02,mtop[i],split[i],1.0) for i in range(8)])
wom=K([(split[i],wtop[i],wr[i],1.0) for i in range(8)])
d=dict(mediaId=7839,level="A",keyWord="forever",defaultVoice="male",
 taps=[dict(phrase="to throw a small key",target="the man",voice="male",keys=man),
       dict(phrase="to hold a lock",target="the woman",voice="female",keys=wom),
       dict(phrase="to wear a purple dress",target="the woman",voice="female",keys=wom)],
 stillS=1.2,
 nouns=[dict(word="the sky",x=.25,y=.12,voice="male"),dict(word="a lamp",x=.77,y=.17,voice="male"),
        dict(word="a church",x=.67,y=.36,voice="male"),dict(word="locks",x=.72,y=.86,voice="male")],
 question="What is the woman holding?",answer=["She","is","holding","a","lock."],answerVoice="female",
 notes="Key throw only at 0.2 s (key in the air top right); the man's raised arm and hand overlap the woman's head area, so his box is cut at the split line (arm not inside at 0.2/0.7). Seagull too small and next to the man, so only two targets. defaultVoice male: couple = mixed, evenId false.")
json.dump(d,open("content/7839.json","w"),indent=1)
