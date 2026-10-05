import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) for t,r in zip(T,rows)]
# rows: x0,y0,x1,y1
blue=K([(0,.35,.35,.85),(0,.35,.33,.85),(0,.34,.33,.87),(0,.34,.33,.87),(0,.33,.33,.87),(0,.33,.33,.87),(0,.33,.36,.90),(0,.32,.36,.90)])
yel=K([(.37,.26,.60,.80),(.35,.25,.60,.81),(.35,.26,.62,.82),(.36,.26,.64,.82),(.34,.25,.64,.84),(.34,.23,.66,.84),(.37,.22,.70,.88),(.37,.21,.71,.89)])
man=K([(.60,.44,1,.91),(.60,.42,1,.91),(.62,.42,1,.91),(.64,.42,1,.92),(.64,.41,1,.92),(.66,.42,1,.90),(.70,.43,1,1),(.71,.41,1,1)])
d=dict(mediaId=7837,level="A",keyWord="for example",defaultVoice="female",
 taps=[dict(phrase="to show a round stone",target="the woman in yellow",voice="female",keys=yel),
       dict(phrase="to wear a blue jacket",target="the woman in blue",voice="female",keys=blue),
       dict(phrase="to pick up stones",target="the man",voice="male",keys=man)],
 stillS=0.2,
 nouns=[dict(word="the sky",x=.22,y=.12,voice="female"),dict(word="a cliff",x=.75,y=.25,voice="female"),
        dict(word="a bag",x=.22,y=.79,voice="female"),dict(word="a hammer",x=.42,y=.87,voice="female")],
 question="What is the man doing?",answer=["He","is","picking","up","stones."],answerVoice="male",
 notes="Woman in yellow and the man overlap (her legs / his hands), boxes split along a vertical line; her raised arm is cut at 0.2-1.2 s. Woman in blue has no unique action (only leans and looks), so a state phrase.")
json.dump(d,open("content/7837.json","w"),indent=1)
