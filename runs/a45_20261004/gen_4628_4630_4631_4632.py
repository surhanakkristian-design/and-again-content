import json
OFF=None
def keys(times, boxes):
    assert len(times)==len(boxes), (len(times),len(boxes))
    out=[]
    for t,b in zip(times,boxes):
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=b
            w=min(w,round(1-x,2)); h=min(h,round(1-y,2))
            out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
    return out
T21=[i*0.5 for i in range(21)]
T25=[i*0.5 for i in range(25)]

# ---------- 4628
man=[(.27,.13,.71,.57),(.28,.13,.72,.57),(.21,.13,.79,.57),(.48,.13,.52,.57),(.29,.13,.71,.58),
(.16,.08,.84,.64),(0,.08,1,.70),(.29,.08,.71,.78),(.31,.08,.69,.70),(.24,.08,.76,.68),
(.21,.09,.76,.70),(.14,.09,.75,.70),(.05,.09,.95,.62),(.29,.14,.71,.84),(.26,.30,.74,.70),
(.21,.28,.79,.72),(.18,.26,.82,.66),(.11,.24,.89,.72),(.08,.24,.92,.76),(.08,.26,.92,.74),(.08,.26,.92,.74)]
k=keys(T21,man)
d={"mediaId":4628,"level":"A","keyWord":"sad","defaultVoice":"male",
"taps":[{"phrase":"to hug a blanket","target":"the man","voice":"male","keys":k},
{"phrase":"to sit by the window","target":"the man","voice":"male","keys":k},
{"phrase":"to look very sad","target":"the man","voice":"male","keys":k}],
"stillS":10.0,
"nouns":[{"word":"a window","x":0.20,"y":0.25,"voice":"male"},
{"word":"a man","x":0.62,"y":0.48,"voice":"male"},
{"word":"a blanket","x":0.55,"y":0.70,"voice":"male"},
{"word":"an armchair","x":0.30,"y":0.92,"voice":"male"}],
"question":"What is the sad man doing?",
"answer":["He","is","sitting","by","the","window."],
"answerVoice":"male",
"notes":"Only one possible target (the man); basket/blanket overlap him. Key word 'sad' is in a phrase and the question. Armchair pill sits on the front of the chair bottom left."}
json.dump(d,open("content/4628.json","w"),indent=1)

# ---------- 4630
barber=[(.30,0,.70,.33),(.35,0,.65,.36),(0,0,.60,.80),(0,0,.53,.84),(0,.03,.54,.80),(0,.06,.54,.78),
(.28,.66,.72,.34),(.10,.58,.90,.42),(.43,.05,.57,.95),(.43,.05,.57,.60),(.42,.44,.58,.52),
(.44,0,.56,1.0),(.37,0,.63,1.0),(.39,0,.61,1.0),(.80,0,.20,1.0),(.82,.05,.18,.55),
(.80,.38,.20,.20),OFF,OFF,OFF,OFF]
client=[OFF,OFF,(.25,.82,.75,.18),(.55,.16,.45,.84),(.56,.21,.44,.79),(.56,.24,.44,.76),
(0,.22,1.0,.43),(0,.20,1.0,.37),(0,.22,.42,.78),(0,.28,.42,.72),(0,.28,.41,.72),
(0,.16,.43,.84),(0,.13,.36,.87),(0,.12,.38,.88),(.12,.21,.66,.50),(0,.18,.81,.82),
(0,.18,.79,.82),(0,.18,.73,.82),(0,.16,.82,.84),(0,.14,.90,.86),(0,.18,1.0,.82)]
kb=keys(T21,barber); kc=keys(T21,client)
d={"mediaId":4630,"level":"A","keyWord":"haircut","defaultVoice":"male",
"taps":[{"phrase":"to hold a pencil","target":"the man with the beard","voice":"male","keys":kb},
{"phrase":"to cut a man's hair","target":"the man with the beard","voice":"male","keys":kb},
{"phrase":"to get a new haircut","target":"the young man","voice":"male","keys":kc}],
"stillS":10.0,
"nouns":[{"word":"a haircut","x":0.30,"y":0.30,"voice":"male"},
{"word":"an ear","x":0.20,"y":0.53,"voice":"male"},
{"word":"bottles","x":0.80,"y":0.42,"voice":"male"},
{"word":"a hand","x":0.80,"y":0.87,"voice":"male"}],
"question":"What is the young man getting?",
"answer":["He","is","getting","a","new","haircut."],
"answerVoice":"male",
"notes":"Close-ups 3.0-6.5: the two men overlap; split along a line between them: at 3.0-3.5 the barber's box is his hand with the clippers (his face above the hair is outside it), from 4.0 it is the right part of the picture (face + hand, with some of the young man's hair inside), the young man's box is the left part of his head. 0.0-0.5 the barber is only his hand with the pencil. 7.0-8.0 the barber is only a sliver/arm at the right edge."}
json.dump(d,open("content/4630.json","w"),indent=1)

# ---------- 4631
man=[(.15,0,.85,.82),(.09,0,.91,.83),(.07,0,.93,.92),(.05,0,.95,.90),(0,0,1,.75),(0,0,1,.70),
(0,0,1,.85),(0,0,1,.85),(0,0,1,.75),(0,0,1,.57),(.17,0,.83,.76),(0,0,1,.78),
(.17,0,.83,.66),(.24,0,.76,.66),(.21,0,.79,.71),(.11,0,.89,.88),(.08,0,.92,.74),(.16,0,.84,.93),
(.08,0,.92,1),(.06,.01,.94,.99),(.04,.01,.96,.99)]
k=keys(T21,man)
d={"mediaId":4631,"level":"B","keyWord":"design","defaultVoice":"male",
"taps":[{"phrase":"to design a birdhouse","target":"the man","voice":"male","keys":k},
{"phrase":"to assemble wooden pieces","target":"the man","voice":"male","keys":k},
{"phrase":"to hold up his sketch","target":"the man","voice":"male","keys":k}],
"stillS":9.5,
"nouns":[{"word":"a potted plant","x":0.15,"y":0.37,"voice":"male"},
{"word":"a birdhouse","x":0.68,"y":0.52,"voice":"male"},
{"word":"a sketch","x":0.26,"y":0.66,"voice":"male"},
{"word":"an apron","x":0.62,"y":0.86,"voice":"male"}],
"question":"What did the man design?",
"answer":["He","designed","a","wooden","birdhouse."],
"answerVoice":"male",
"notes":"Only one possible target (the man; sketch and birdhouse are in his hands). Past simple because the finished birdhouse is shown next to the sketch at the end."}
json.dump(d,open("content/4631.json","w"),indent=1)

# ---------- 4632
woman=[(.17,.02,.75,.60),(.17,.02,.76,.66),(.17,.02,.76,.66),(.17,.02,.76,.66),(.17,.03,.74,.65),
(0,.05,.24,.55),(0,.28,.18,.30),(0,.28,.16,.28),(.62,.46,.38,.19),(.66,.50,.34,.22),
(.73,.50,.27,.20),(0,.35,.31,.14),OFF,(.82,.50,.18,.33),(.82,.44,.18,.16),(0,.44,.29,.14),
(0,.46,.30,.14),(.50,.17,.50,.24),(.53,.14,.47,.27),(.55,.14,.45,.28),(.48,.14,.52,.29),
(.48,.15,.52,.28),(.48,.15,.52,.28),(.48,.15,.52,.28),(.48,.15,.52,.28)]
lamp=[OFF]*5+[(.25,.17,.32,.42),(.19,.14,.33,.45),(.17,.13,.31,.44),(.11,.13,.27,.41),(.02,.13,.33,.41),
(0,.13,.29,.42),(0,.13,.28,.21),(0,.15,.27,.40),(0,.15,.22,.39),(0,.15,.24,.40),(0,.15,.29,.28),
(.03,.16,.29,.29),(.05,.18,.28,.38),(.05,.19,.27,.38),(.05,.20,.24,.37),(0,.20,.26,.38),
(0,.21,.26,.38),(0,.21,.26,.38),(0,.21,.26,.38),(0,.20,.26,.38)]
laptop=[OFF]*8+[(.39,.47,.22,.16),(.20,.55,.45,.14),(.30,.38,.42,.31),(.33,.38,.44,.32),
(.28,.37,.44,.30),(.23,.37,.45,.30),(.25,.37,.45,.30),(.30,.37,.45,.31),(.34,.38,.43,.30),
(.34,.42,.45,.26),(.33,.42,.45,.27),(.30,.43,.44,.27),(.27,.44,.46,.26),(.27,.44,.46,.27),
(.27,.44,.46,.27),(.27,.44,.46,.27),(.27,.44,.44,.27)]
d={"mediaId":4632,"level":"B","keyWord":"workspace","defaultVoice":"female",
"taps":[{"phrase":"to set up her workspace","target":"the woman","voice":"female","keys":keys(T25,woman)},
{"phrase":"to light up the desk","target":"the lamp","voice":"female","keys":keys(T25,lamp)},
{"phrase":"to display a document","target":"the laptop","voice":"female","keys":keys(T25,laptop)}],
"stillS":12.0,
"nouns":[{"word":"a desk lamp","x":0.17,"y":0.27,"voice":"female"},
{"word":"a potted plant","x":0.22,"y":0.44,"voice":"female"},
{"word":"a laptop","x":0.38,"y":0.61,"voice":"female"},
{"word":"a stack of books","x":0.70,"y":0.76,"voice":"female"}],
"question":"What is the woman setting up?",
"answer":["She","is","setting","up","her","workspace."],
"answerVoice":"female",
"notes":"2.5-8.0 the woman is only her hands/arms at the frame edge; where both hands are apart the box is on one hand. The lamp is switched on from 3.5, the laptop is open from 5.0 (closed at 4.0-4.5). Boxes of lamp/laptop are trimmed where plant, hands and laptop base meet."}
json.dump(d,open("content/4632.json","w"),indent=1)
