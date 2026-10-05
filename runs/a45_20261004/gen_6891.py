import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def box(cx,cy,w=.18,h=.14): return dict(x=round(cx-w/2,2),y=round(cy-h/2,2),w=w,h=h)
sh=[(0.15,.36),(.18,.36),(.21,.37),(.24,.37),(.28,.38),(.32,.38),(.36,.38),(.40,.38)]
bt=[(.63,.86),(.64,.86),(.64,.87),(.64,.87),(.64,.88),(.64,.88),(.65,.90),(.64,.90)]
shk=[dict(t=t,**box(*p)) for t,p in zip(T,sh)]
btk=[dict(t=t,**box(*p)) for t,p in zip(T,bt)]
chk=[dict(t=t,x=.41,y=0.0,w=.22,h=.30) for t in T]
c=dict(mediaId=6891,level="B",keyWord="branch",defaultVoice="male",
taps=[dict(phrase="to glide across the mudflats",target="the plane's shadow",voice="male",keys=shk),
      dict(phrase="to branch into smaller streams",target="the main channel",voice="male",keys=chk),
      dict(phrase="to lie stranded",target="the rowing boat",voice="male",keys=btk)],
stillS=3.7,
nouns=[dict(word="a branch",x=.15,y=.47,voice="male"),dict(word="a shadow",x=.40,y=.38,voice="male"),
       dict(word="wooden posts",x=.72,y=.70,voice="male"),dict(word="a rowing boat",x=.64,y=.90,voice="male")],
question="What is the plane's shadow doing?",answer=["It","is","gliding","across","the","mudflats."],answerVoice="male",
notes="Aerial view, no people. Main channel box covers only the wide trunk (top) so it does not overlap the shadow box; smaller channels also fork, but the wide trunk is the clear one. 'to lie stranded' is a state (boat does not move). 'a branch' pill sits on the left fork of the channel.")
json.dump(c,open('content/6891.json','w'),indent=1)
