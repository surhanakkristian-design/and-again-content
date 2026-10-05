import json
T=[i*0.5 for i in range(19)]
W={0.0:(0,0,.70,1),0.5:(0,0,1,1),1.0:(.10,.20,.55,.70),1.5:(.08,.18,.55,.62),2.0:(.03,.15,.58,.58),
   2.5:(.03,.15,.60,.62),3.0:(.03,.12,.60,.60),3.5:(.03,.12,.60,.62),5.5:(.08,.10,.84,.47),
   6.0:(.06,.10,.62,.62),6.5:(.10,.08,.64,.80),8.5:(.08,.10,.62,.85),9.0:(.03,.10,.65,.85)}
M={1.0:(.66,.55,.34,.45),1.5:(.64,.55,.36,.45),2.0:(.64,.55,.36,.45),2.5:(.64,.48,.36,.52),3.0:(.64,.50,.36,.50),
   3.5:(.64,.50,.36,.50),4.0:(0,0,1,1),4.5:(0,0,1,1),5.0:(0,0,1,1),5.5:(.50,.60,.50,.40),6.0:(.70,.58,.30,.42),
   6.5:(.76,.50,.24,.50),7.0:(.02,.05,.95,.80),7.5:(.02,.05,.95,.80),8.0:(.02,.02,.95,.78),8.5:(.72,.58,.28,.42),9.0:(.70,.58,.30,.42)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4926,level="A",keyWord="dentist",defaultVoice="female",
 taps=[dict(phrase="to put on gloves",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to lie in the chair",target="the man",voice="male",keys=keys(M)),
       dict(phrase="to give a thumbs-up",target="the woman",voice="female",keys=keys(W))],
 stillS=9.0,
 nouns=[dict(word="a dentist",x=.45,y=.38,voice="female"),dict(word="a mirror",x=.20,y=.68,voice="female"),
        dict(word="a window",x=.22,y=.15,voice="female"),dict(word="a man",x=.85,y=.72,voice="male")],
 question="What is the dentist holding?",
 answer=["She","is","holding","a","mirror."],answerVoice="female",
 notes="Man set off at 0.0-0.5 s (only a shoulder at the bottom edge). 4.0-5.0 s is a close-up of his mouth (whole frame = man, woman off; the toothbrush is not a target). 7.0-8.0 s shows his face in the hand mirror (box on the reflection, woman off; the blurred fingers at the bottom are not clearly hers). Where both are in frame the boxes are split at x ~0.63-0.76 (woman left, man's head right); the man's body at the bottom left is not covered.")
json.dump(c,open('content/4926.json','w'),indent=1,ensure_ascii=False)
