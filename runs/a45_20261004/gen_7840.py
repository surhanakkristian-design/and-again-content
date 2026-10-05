import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,x=r[0],y=r[1],w=round(r[2]-r[0],2),h=round(r[3]-r[1],2)) for t,r in zip(T,rows)]
man=K([(.22,.27,.67,.92),(.24,.27,.68,.92),(.23,.27,.67,.92),(.20,.27,.69,.92),(.27,.26,.68,.91),(.27,.26,.68,.92),(.15,.27,.66,.94),(.16,.27,.67,.93)])
wom=K([(.67,.37,.81,.61),(.68,.37,.82,.61),(.67,.36,.80,.60),(.69,.37,.81,.61),(.68,.37,.80,.61),(.68,.37,.81,.61),(.66,.37,.79,.61),(.67,.37,.79,.60)])
d=dict(mediaId=7840,level="A",keyWord="forward",defaultVoice="male",
 taps=[dict(phrase="to drink his coffee",target="the man in the coat",voice="male",keys=man),
       dict(phrase="to walk towards the camera",target="the man in the coat",voice="male",keys=man),
       dict(phrase="to hold a lamp post",target="the woman",voice="female",keys=wom)],
 stillS=2.2,
 nouns=[dict(word="a flamingo",x=.24,y=.50,voice="male"),dict(word="a cup",x=.49,y=.41,voice="male"),
        dict(word="a lamp",x=.76,y=.26,voice="male"),dict(word="a chair",x=.80,y=.58,voice="male")],
 question="What is the man in brown doing?",answer=["He","is","drinking","his","coffee."],answerVoice="male",
 notes="Umbrella flying rejected as a target because the hat also flies at 0.2 s; flamingo men overlap the main man's coat, so the main man carries two phrases. Woman box is narrow (about 0.13 wide) to stay clear of the man's flapping coat; coat tip cut at 1.2/1.7 s. He sips the coffee from 2.7 s.")
json.dump(d,open("content/7840.json","w"),indent=1)
