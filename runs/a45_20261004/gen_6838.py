import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,off=True) if r is None else dict(t=t,x=r[0],y=r[1],w=r[2],h=r[3]) for t,r in zip(T,rows)]
arch=K([(.37,.37,.34,.46),(.35,.30,.39,.54),(.34,.27,.35,.60),(.34,.26,.35,.61),(.34,.26,.37,.63),(.36,.25,.38,.65),(.33,.24,.40,.70),(.31,.23,.42,.72)])
serv=K([(.72,.46,.25,.34),(.75,.46,.23,.35),(.72,.46,.27,.36),(.71,.45,.29,.38),(.72,.44,.28,.40),(.76,.44,.24,.42),(.78,.46,.22,.42),(.78,.50,.22,.40)])
c=dict(mediaId=6838,level="B",keyWord="archbishop",defaultVoice="male",
 taps=[dict(phrase="to give a blessing",target="the archbishop",voice="male",keys=arch),
       dict(phrase="to raise a tall staff",target="the archbishop",voice="male",keys=arch),
       dict(phrase="to swing an incense burner",target="the young server",voice="male",keys=serv)],
 stillS=1.7,
 nouns=[dict(word="a rose window",x=.14,y=.10,voice="male"),dict(word="an archbishop",x=.58,y=.62,voice="male"),
        dict(word="pews",x=.15,y=.70,voice="male")],
 question="What is the young server doing?",
 answer=["He","is","swinging","an","incense","burner."],answerVoice="male",
 notes="Blessing hand visible mainly 0.2-1.7 s; later he lifts the staff high. Server partly out of frame on the right at 2.7-3.7 s. Description says chairs; frames show wooden pews.")
json.dump(c,open("content/6838.json","w"),indent=1)
