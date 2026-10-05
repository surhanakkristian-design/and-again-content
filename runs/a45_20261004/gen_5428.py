import json
T=[i*0.5 for i in range(19)]
O=None
W=[(.68,.40,.32,.60),(.47,.37,.53,.63),(.51,.40,.49,.60),(.47,.39,.53,.61),(.53,.38,.47,.62),(.80,.40,.20,.60),(.83,.42,.17,.58),(.84,.42,.16,.58),
(.81,.43,.19,.57),(.82,.44,.18,.56),(.85,.44,.15,.56),(.83,.44,.17,.56),(.73,.44,.27,.56),(.75,.45,.25,.55),(.77,.50,.23,.50),(.71,.52,.29,.48),
(.67,.52,.33,.48),(.61,.50,.39,.50),(.51,.45,.49,.55)]
K=[O,O,O,O,O,(.44,.29,.36,.31),(.34,.29,.48,.30),(.24,.29,.59,.32),(.15,.26,.65,.36),(.05,.22,.76,.42),(.00,.20,.84,.48),(.00,.16,.82,.56),
(.00,.10,.72,.65),(.00,.05,.74,.83),(.00,.08,.76,.80),(.00,.04,.70,.84),(.00,.06,.66,.82),(.00,.00,.60,.90),(.00,.00,.50,.90)]
P=[(.00,.00,.66,1.0),(.00,.00,.46,1.0),(.00,.00,.50,1.0),(.00,.00,.46,1.0),(.00,.04,.50,.92)]+[O]*14
def keys(L): return [dict(t=t,off=True) if k is None else dict(t=t,x=k[0],y=k[1],w=k[2],h=k[3]) for t,k in zip(T,L)]
c=dict(mediaId=5428,level="B",keyWord="freight",defaultVoice="male",
taps=[dict(phrase="to wave the truck forward",target="the worker",voice="male",keys=keys(W)),
dict(phrase="to tow a shipping container",target="the truck",voice="male",keys=keys(K)),
dict(phrase="to carry shrink-wrapped pallets",target="the pickup",voice="male",keys=keys(P))],
stillS=4.5,
nouns=[dict(word="a cloud",x=.40,y=.24,voice="male"),dict(word="a truck",x=.30,y=.45,voice="male"),
dict(word="a shipping container",x=.72,y=.42,voice="male"),dict(word="gravel",x=.40,y=.82,voice="male")],
question="What is the truck towing?",answer=["It","is","towing","a","shipping","container."],answerVoice="male",
notes="Pickup with the shrink-wrapped pallets only 0.0-2.0 (camera pans away). Truck enters at 2.5 and fills the frame from 6.0; the worker stands in front of it on the right, so boxes are split vertically (worker's waving arm/hands partly in the truck box at 2.5-5.5; truck box leaves out the container part behind the worker at 6.0-9.0). Driver waves from the cab at 6.0-7.0 but is tiny, not used. 'freight' is not used as a noun pill (the container stands for it). Answer subject 'It' -> defaultVoice male (main person is the worker).")
json.dump(c,open('content/5428.json','w'),indent=1)
