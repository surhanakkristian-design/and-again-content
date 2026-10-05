import json
T=[round(i*0.5,1) for i in range(21)]
B={0.0:(.12,.15,.78,.85),0.5:(.02,.32,.97,.68),1.0:(0,.27,1,.73),1.5:(0,.23,1,.77),2.0:(0,.13,1,.87),
2.5:(.05,.18,.82,.81),3.0:(0,.17,.72,.83),3.5:(0,0,1,1),4.0:(0,0,1,1),4.5:(.02,.2,.68,.78),5.0:(.28,.2,.56,.76),
5.5:(.09,.19,.84,.76),6.0:(0,.09,1,.91),6.5:(0,.08,1,.92),7.0:(0,.07,1,.93),7.5:(0,.07,1,.93),8.0:(0,.09,1,.91),
9.5:(.25,.12,.56,.87),10.0:(.25,.14,.57,.85)}
def keys(b):
    return [dict(t=t,x=b[t][0],y=b[t][1],w=b[t][2],h=b[t][3]) if t in b else dict(t=t,off=True) for t in T]
k=keys(B)
c=dict(mediaId=4912,level="B",keyWord="instructor",defaultVoice="female",
taps=[dict(phrase="to hold out a wooden board",target="the instructor",voice="female",keys=k),
      dict(phrase="to snap the board in half",target="the instructor",voice="female",keys=k),
      dict(phrase="to wear a black belt",target="the instructor",voice="female",keys=k)],
stillS=6.0,
nouns=[dict(word="an instructor",x=.5,y=.19,voice="female"),dict(word="students",x=.15,y=.31,voice="female"),
       dict(word="a wooden board",x=.5,y=.52,voice="female"),dict(word="a black belt",x=.5,y=.70,voice="female")],
question="What is the instructor doing?",
answer=["She","is","holding out","a","wooden","board."],answerVoice="female",
notes="All three phrases on the instructor: students copy her kicks and bows, and the board sits inside her box. 'holding out' kept as one chip so the particle cannot move. 8.5-9.0 show only students (off). Pill 'an instructor' on her face, 'a black belt' on the belt of the same large figure.")
json.dump(c,open('content/4912.json','w'),indent=1)
