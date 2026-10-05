import json
times=[i*0.5 for i in range(25)]
W={0.0:(.02,.13,.85,.87),0.5:(.02,.12,.80,.88),1.0:(.02,.11,.80,.89),1.5:(.02,.10,.82,.90),2.0:(.02,.08,.78,.92),
2.5:(.02,.09,.98,.91),3.0:(0,.14,.92,.86),3.5:(0,.12,1.0,.88),4.0:(.13,.17,.87,.83),4.5:(.27,.18,.73,.82),5.0:(.36,.24,.64,.76),
5.5:(.30,.21,.70,.79),6.0:(.30,.17,.70,.83),6.5:(0,.12,.70,.88),7.0:(0,.20,.52,.80),7.5:(0,.19,.44,.81),8.0:(0,.19,.52,.81),
8.5:(0,.22,.67,.78),9.0:(0,.20,.40,.80),9.5:(.12,.21,.50,.79),10.0:(0,.20,.55,.80),10.5:(0,.20,.62,.80),11.0:(0,.22,.52,.78),
11.5:(0,.22,.55,.78),12.0:(.06,.15,.72,.85)}
T={9.0:(.40,.20,.60,.40),9.5:(.62,.22,.38,.50),10.0:(.55,.24,.45,.40),10.5:(.62,.22,.38,.40),11.0:(.52,.20,.48,.38),
11.5:(.55,.20,.45,.38),12.0:(.78,.22,.22,.36)}
def ks(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) if t in d else dict(t=t,off=True) for t in times]
w="the woman in the orange jacket"
c=dict(mediaId=5074,level="A",keyWord="introduce",defaultVoice="female",
 taps=[dict(phrase="to carry a big box",target=w,voice="female",keys=ks(W)),
       dict(phrase="to shake many hands",target=w,voice="female",keys=ks(W)),
       dict(phrase="to stand behind her",target="the team",voice="female",keys=ks(T))],
 stillS=2.0,
 nouns=[dict(word="a jacket",x=.15,y=.58,voice="female"),dict(word="a box",x=.65,y=.66,voice="female"),
        dict(word="a chair",x=.78,y=.48,voice="female"),dict(word="a computer",x=.72,y=.36,voice="female")],
 question="What is the woman carrying?",answer=["She","is","carrying","a","big","box."],answerVoice="female",
 notes="Many people shake her hand, so the handshake phrase is 'to shake many hands' (only she does). 'the team' = the group of colleagues standing behind her, only from 9.0 s; boxes split at the woman's shoulder, so her outstretched hand at 9.0-11.5 s is outside her box. Bearded man and grey-shirt woman not used as targets.")
json.dump(c,open('content/5074.json','w'),indent=1)
