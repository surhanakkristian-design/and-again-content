import json
T=[i*0.5 for i in range(19)]
W={0.0:(.17,0,.66,.70),1.0:(0,0,1,.50),1.5:(.20,0,.65,.22),2.0:(0,0,.55,.22),2.5:(0,0,.50,.60),
   3.0:(.12,0,.88,1),3.5:(.20,0,.80,1),4.0:(.08,.07,.87,.80),4.5:(.12,.07,.88,.80),5.0:(.15,.10,.83,.75),
   5.5:(.26,0,.62,.90),6.0:(.17,0,.62,.93),6.5:(0,.30,1,.70),7.0:(0,.32,1,.68),7.5:(.30,.08,.70,.38),
   8.0:(.18,.10,.82,.90),8.5:(.08,.12,.92,.88),9.0:(.08,.12,.88,.88)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in T]
c=dict(mediaId=4927,level="A",keyWord="lawyer",defaultVoice="female",
 taps=[dict(phrase="to walk up the steps",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to sign a paper",target="the woman",voice="female",keys=keys(W)),
       dict(phrase="to carry a briefcase",target="the woman",voice="female",keys=keys(W))],
 stillS=4.0,
 nouns=[dict(word="a lawyer",x=.52,y=.38,voice="female"),dict(word="books",x=.18,y=.15,voice="female"),
        dict(word="a briefcase",x=.45,y=.72,voice="female"),dict(word="a table",x=.30,y=.92,voice="female")],
 question="What is the lawyer carrying?",
 answer=["She","is","carrying","a","briefcase."],answerVoice="female",
 notes="Only one person is a real target (the man at 8.0-9.0 s is just a hand/sleeve at the left edge), so all three phrases use the woman. 0.0 s her body is behind the book stack (box on the person+stack), 0.5 s only books (off). 1.0-2.5 s and 6.5-7.5 s show only her hands (boxes on hands/arms); the signing and stamping hands are assumed hers (same manicure). The signing is a close-up only (6.5-7.0 s). Frames differ from the description (book/paper close-ups, no 'lifting the briefcase' moment clearly visible).")
json.dump(c,open('content/4927.json','w'),indent=1,ensure_ascii=False)
