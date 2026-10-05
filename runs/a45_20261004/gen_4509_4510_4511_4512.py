import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def tap(p,tg,v,keys): return {"phrase":p,"target":tg,"voice":v,"keys":keys}
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4509
t=T(19)
man={0.0:(.20,.22,.60,.66),0.5:(.27,.10,.73,.72),1.0:(.22,0,.78,.58),1.5:(.12,0,.86,.65),2.0:(.12,.13,.83,.80),
2.5:(.10,.13,.85,.80),3.0:(.10,.14,.82,.86),3.5:(.42,.12,.58,.88),4.0:(.44,.10,.56,.90),4.5:(.47,.10,.53,.90),
5.0:(.43,.20,.57,.80),5.5:(0,.08,.65,.92),6.0:(0,.04,.84,.90),6.5:(0,.64,.68,.26),7.0:(0,.66,.80,.34),
7.5:(0,.33,.32,.25),8.0:(0,.06,.78,.94),8.5:(0,.10,.92,.90),9.0:(0,.15,.92,.85)}
wom={3.5:(0,.14,.38,.52),4.0:(0,.13,.42,.56),4.5:(0,.13,.46,.58),5.0:(0,.14,.41,.52)}
mk=K(t,man)
save({"mediaId":4509,"level":"A","keyWord":"weigh","defaultVoice":"male",
"taps":[tap("to weigh a big bag","the man","male",mk),tap("to write with a pen","the man","male",mk),
tap("to stand behind the desk","the woman","female",K(t,wom))],
"stillS":4.0,
"nouns":[{"word":"a woman","x":.20,"y":.28,"voice":"female"},{"word":"a pen","x":.54,"y":.54,"voice":"male"},
{"word":"a watch","x":.86,"y":.65,"voice":"male"},{"word":"paper","x":.22,"y":.75,"voice":"male"}],
"question":"What is the man weighing?","answer":["He","is","weighing","a","big","bag."],"answerVoice":"male",
"notes":"Clip has cuts (airport scale 0-3.0, hotel desk 3.5-5.0, machine 5.5-7.5, hall 8.0-9.0). Two phrases share the man; the woman is only in the hotel shot. At 6.5-7.5 only the man's arm/hand is in the picture. The man carries two bags (big dark-brown holdall on the scale, lighter shoulder bag). 'paper' = the white sheet on the desk."})

# 4510
t=T(25)
B=(0,.07,1,.36)
wo={0.0:(.12,.46,.78,.54),0.5:(.17,.29,.83,.71),2.0:(.34,.36,.66,.64),2.5:(.19,.32,.77,.68),3.0:(.22,.46,.58,.54),
3.5:(.25,.45,.62,.55),4.0:(.26,.43,.58,.57),4.5:(.22,.43,.63,.57),5.0:(.20,.43,.62,.57),5.5:(.20,.44,.62,.56),
6.0:(.26,.43,.56,.57),6.5:(.26,.43,.56,.57),7.0:(.26,.43,.56,.57),7.5:(.23,.44,.59,.56),8.0:(.23,.43,.57,.57),
8.5:(.24,.44,.65,.56),9.0:(.29,.44,.55,.56),9.5:(.26,.44,.58,.56),10.0:(.26,.43,.56,.57),10.5:(.36,.48,.50,.52),
11.0:(.18,.45,.68,.55),11.5:(0,.44,.75,.56)}
bo={x:B for x in t}
bo.update({0.0:(0,.10,1,.35),0.5:(0,.09,1,.20),1.0:(0,.25,1,.33),1.5:(.08,.30,.80,.32),2.0:(.10,.15,.90,.21),2.5:(0,.10,1,.22),
3.0:(0,.09,1,.37),3.5:(0,.09,1,.36),12.0:(0,.08,1,.38)})
wk=K(t,wo)
save({"mediaId":4510,"level":"A","keyWord":"check","defaultVoice":"female",
"taps":[tap("to check her ticket","the woman","female",wk),tap("to look at her watch","the woman","female",wk),
tap("to show the flight times","the board","female",K(t,bo))],
"stillS":6.0,
"nouns":[{"word":"a board","x":.50,"y":.24,"voice":"female"},{"word":"a ticket","x":.55,"y":.66,"voice":"female"},
{"word":"a suitcase","x":.80,"y":.75,"voice":"female"},{"word":"a jacket","x":.40,"y":.84,"voice":"female"}],
"question":"What is the woman checking?","answer":["She","is","checking","her","ticket."],"answerVoice":"female",
"notes":"Only one clear person; third target is the big departures board. Where her raised hand is in front of the board (0.5, 2.0, 2.5) the board box is cut above her finger. 1.0-1.5 is a blurred pan (woman off, board blurred). 'a suitcase' pill is on the purple suitcase at the right; a trolley with luggage is also at the left. 'a jacket' and 'a ticket' are both on the woman but at clearly different places."})

# 4511
t=T(21)
man={0.0:(0,.25,.45,.75),0.5:(0,.25,.55,.75),1.0:(0,.27,.72,.73),1.5:(0,.26,.60,.74),2.0:(0,.23,.41,.77),2.5:(0,.24,.42,.76),
3.0:(0,.24,.64,.76),3.5:(0,.26,.76,.74),4.0:(0,.22,.69,.78),4.5:(0,.26,.72,.74),5.0:(0,.27,.73,.73),5.5:(0,.28,.73,.72),
6.0:(0,.27,.73,.73),6.5:(0,.26,.61,.74),7.0:(0,.25,.63,.75),7.5:(0,.26,.67,.74),8.0:(0,.25,.76,.75),8.5:(0,.19,.55,.81),
9.0:(0,.23,.80,.77),9.5:(0,.25,.52,.75),10.0:(0,.28,.60,.72)}
wom={1.0:(.82,.46,.18,.30),1.5:(.82,.47,.18,.28),3.5:(.78,.47,.22,.20),4.0:(.70,.40,.30,.30),4.5:(.73,.40,.27,.30),
5.0:(.74,.40,.26,.30),5.5:(.76,.40,.24,.28),6.0:(.74,.39,.26,.30),6.5:(.62,.38,.38,.30),7.0:(.64,.40,.36,.30),
7.5:(.68,.41,.32,.30),8.0:(.77,.40,.23,.30)}
mk=K(t,man)
save({"mediaId":4511,"level":"B","keyWord":"service","defaultVoice":"male",
"taps":[tap("to sign a document","the man","male",mk),tap("to lift a leather holdall","the man","male",mk),
tap("to hand back a passport","the woman","female",K(t,wom))],
"stillS":7.5,
"nouns":[{"word":"a monitor","x":.42,"y":.13,"voice":"male"},{"word":"a luggage tag","x":.62,"y":.50,"voice":"male"},
{"word":"a passport","x":.74,"y":.61,"voice":"male"},{"word":"a pen","x":.60,"y":.71,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","signing","a","document","at","the","check-in","desk."],"answerVoice":"male",
"notes":"Key word 'service' is abstract and not a visible noun, so it is not among the nouns. Two targets only (man, woman): the man's box is wide so that his hands on the counter are inside it and it also covers the bag; it is cut where the woman's hands begin. The woman is at the right edge only (1.0-1.5, 3.5-8.0); off where only a sliver shows. At 6.5-7.0 her arm reaches over the bag to the tag. 'a luggage tag' pill is on the white tag at the bag's right end. 'check-in' is one chip."})

# 4512
t=T(19)
man={0.0:(0,0,.75,1),0.5:(0,0,.92,1),1.0:(0,0,.76,1),1.5:(0,.05,.92,.95),2.0:(0,.02,.82,.98),2.5:(0,.07,.92,.93),
3.0:(0,.19,.78,.81),3.5:(.04,.24,.76,.76),4.0:(.05,.27,.74,.73),4.5:(.06,.33,.58,.67),5.0:(.04,.37,.50,.63),
5.5:(.11,.44,.58,.54),6.0:(.13,.47,.42,.43),6.5:(.18,.50,.34,.33),7.0:(.23,.55,.35,.35),7.5:(.23,.56,.35,.34),
8.0:(.26,.50,.25,.38),8.5:(.26,.56,.27,.33),9.0:(.26,.56,.27,.33)}
mk=K(t,man)
save({"mediaId":4512,"level":"A","keyWord":"list","defaultVoice":"male",
"taps":[tap("to write on a list","the man","male",mk),tap("to hold a red pen","the man","male",mk),
tap("to touch a brown box","the man","male",mk)],
"stillS":2.0,
"nouns":[{"word":"a pencil","x":.40,"y":.17,"voice":"male"},{"word":"a list","x":.74,"y":.61,"voice":"male"},
{"word":"boxes","x":.72,"y":.86,"voice":"male"}],
"question":"What is the man writing on?","answer":["He","is","writing","on","a","list."],"answerVoice":"male",
"notes":"Only one clear target (the worker), so all three phrases are his. Forklift drivers in the background are tiny. Boxes are everywhere in the hall; the 'boxes' pill is on the stack right below the clipboard."})
