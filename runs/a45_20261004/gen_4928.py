import json
T=[i*0.5 for i in range(19)]
M={1.5:(.30,.38,.42,.42),2.0:(0,.33,1,.65),2.5:(0,.12,1,.88),3.0:(0,.12,1,.88),3.5:(0,.10,1,.90),4.0:(0,0,1,1),
   4.5:(.60,.45,.40,.55),5.0:(.55,.50,.45,.50),5.5:(.08,.12,.92,.88),6.0:(.18,.22,.82,.78),6.5:(0,.18,.65,.42),
   7.0:(0,.08,.70,.40),7.5:(.12,.25,.88,.52),8.0:(.13,.22,.87,.50),8.5:(.12,.22,.88,.50),9.0:(.12,.23,.88,.50)}
B={0.5:(.26,.48,.44,.33),1.0:(.27,.49,.45,.35)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4928,level="B",keyWord="to fix",defaultVoice="male",
 taps=[dict(phrase="to tighten the drain pipe",target="the young man",voice="male",keys=keys(M)),
       dict(phrase="to catch dripping water",target="the bucket",voice="male",keys=keys(B)),
       dict(phrase="to grin at the camera",target="the young man",voice="male",keys=keys(M))],
 stillS=8.5,
 nouns=[dict(word="a headlamp",x=.48,y=.30,voice="male"),dict(word="dungarees",x=.45,y=.50,voice="male"),
        dict(word="a mixer tap",x=.80,y=.56,voice="male"),dict(word="a kitchen sink",x=.40,y=.85,voice="male")],
 question="What is the man fixing?",
 answer=["He","is","fixing","a","leaking","pipe."],answerVoice="male",
 notes="Bucket is a target only 0.5-1.0 s (under the dripping pipe); at 4.5-5.0 s only a sliver of its rim shows at the bottom edge next to the man's arm, set off. 4.0 s is a close-up of his tool belt/torso (full-frame box). 4.5-5.0 s and 6.5-7.0 s show only his hands/arm. The wrench close-up shows him turning the nut on the drain (described as 'tightening the drain pipe'). Nouns: 'dungarees' pill on the bib, 'a headlamp' on his forehead - same figure but distinct parts, 0.23 apart in y.")
json.dump(c,open('content/4928.json','w'),indent=1,ensure_ascii=False)
