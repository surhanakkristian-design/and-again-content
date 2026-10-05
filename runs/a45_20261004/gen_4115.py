# writes content for 4115, 4116, 4117, 4118
import json
def K(t, b): return {"t": t, "off": True} if b is None else {"t": t, "x": round(b[0],2), "y": round(b[1],2), "w": round(b[2],2), "h": round(b[3],2)}
def keys(d, times): return [K(t, d.get(t)) for t in times]
def T(n): return [i*0.5 for i in range(n)]
def save(c): json.dump(c, open(f'content/{c["mediaId"]}.json','w'), ensure_ascii=False, indent=1)

# ---- 4115
t=T(16)
man={0.0:(.17,.17,.41,.80),0.5:(.17,.23,.36,.68),1.0:(.18,.26,.34,.70),1.5:(.18,.27,.34,.70),2.0:(.10,.28,.40,.60),2.5:(.16,.30,.34,.56),
3.0:(.19,.30,.33,.67),3.5:(.18,.31,.32,.65),4.0:(.26,.31,.25,.52),4.5:(.18,.28,.35,.51),5.0:(.14,.29,.37,.66),5.5:(.13,.31,.45,.66),
6.0:(.26,.30,.32,.53),6.5:(.29,.30,.30,.52),7.0:(.28,.31,.28,.63),7.5:(.26,.31,.28,.62)}
wom={0.0:(.58,.31,.38,.64),0.5:(.53,.36,.37,.59),1.0:(.52,.34,.34,.60),1.5:(.52,.34,.33,.60),2.0:(.50,.35,.35,.52),2.5:(.50,.37,.32,.47),
3.0:(.52,.38,.29,.58),3.5:(.50,.38,.33,.58),4.0:(.51,.37,.30,.45),4.5:(.53,.35,.35,.44),5.0:(.51,.40,.42,.50),5.5:(.58,.37,.28,.55),
6.0:(.58,.36,.28,.47),6.5:(.59,.36,.29,.46),7.0:(.56,.37,.26,.57),7.5:(.54,.37,.28,.56)}
save({"mediaId":4115,"level":"A","keyWord":"tourist","defaultVoice":"male",
"taps":[{"phrase":"to raise his arm","target":"the man","voice":"male","keys":keys(man,t)},
{"phrase":"to turn around and laugh","target":"the woman","voice":"female","keys":keys(wom,t)},
{"phrase":"to wear a white skirt","target":"the woman","voice":"female","keys":keys(wom,t)}],
"stillS":7.0,
"nouns":[{"word":"tourists","x":.56,"y":.42,"voice":"male"},{"word":"sunglasses","x":.14,"y":.47,"voice":"male"},
{"word":"hats","x":.27,"y":.56,"voice":"male"}],
"question":"Who is walking past the hats?",
"answer":["Two","tourists","are","walking","past","the","hats."],"answerVoice":"male",
"notes":"Night clip, couple seen from behind; they overlap (his arm around her), boxes split on the line between them. He raises his arm high only at 0.0-0.5 s. She spins round and laughs at 4.5-5.5 s. Key word used as plural 'tourists' on the couple."})

# ---- 4116
t=T(31)
man={0.0:(.20,.12,.52,.30),0.5:(.20,.12,.52,.30),1.0:(.22,.12,.56,.30),1.5:(.24,.12,.58,.25),2.0:(.26,.12,.58,.21),2.5:(.13,.11,.63,.32),
3.0:(.11,.12,.65,.32),3.5:(.16,.27,.68,.18),4.0:(.14,.31,.70,.14),4.5:(.18,.37,.64,.20),5.0:(.18,.37,.64,.20),5.5:(.18,.37,.64,.20),
8.5:(.54,.42,.34,.42),9.0:(.53,.45,.33,.41),9.5:(.54,.45,.34,.41),10.0:(.53,.41,.35,.43),10.5:(.54,.40,.36,.44),
11.0:(.10,.42,.80,.25),11.5:(.10,.42,.80,.25),12.0:(.10,.40,.80,.27),12.5:(.10,.40,.80,.27)}
car={0.0:(.10,.42,.76,.48),0.5:(.10,.42,.76,.48),1.0:(.10,.42,.76,.48),1.5:(.10,.37,.76,.53),2.0:(.10,.33,.76,.57),2.5:(.10,.43,.76,.47),
3.0:(.10,.44,.76,.46),3.5:(.10,.45,.78,.45),4.0:(.10,.45,.76,.45),4.5:(.10,.57,.76,.33),5.0:(.10,.57,.76,.33),5.5:(.10,.57,.76,.33),
6.0:(.26,.36,.52,.31),6.5:(.26,.36,.53,.31),7.0:(.26,.37,.54,.31),7.5:(.26,.39,.55,.31),8.0:(.28,.40,.56,.32),
8.5:(.03,.50,.51,.36),9.0:(.02,.49,.51,.38),9.5:(.03,.50,.51,.37),10.0:(.02,.50,.51,.37),10.5:(.03,.50,.51,.37),
11.0:(0,.67,1,.33),11.5:(0,.67,1,.33),12.0:(0,.67,1,.33),12.5:(0,.67,1,.33),
13.0:(.26,.40,.74,.56),13.5:(.18,.41,.56,.42),14.0:(.14,.42,.46,.34),14.5:(.10,.44,.38,.28),15.0:(.10,.46,.34,.23)}
save({"mediaId":4116,"level":"A","keyWord":"small","defaultVoice":"male",
"taps":[{"phrase":"to get into the car","target":"the man","voice":"male","keys":keys(man,t)},
{"phrase":"to sit on a bench","target":"the man","voice":"male","keys":keys(man,t)},
{"phrase":"to be small and red","target":"the red car","voice":"male","keys":keys(car,t)}],
"stillS":10.0,
"nouns":[{"word":"a car","x":.28,"y":.72,"voice":"male"},{"word":"a bench","x":.87,"y":.63,"voice":"male"},
{"word":"a tree","x":.25,"y":.25,"voice":"male"},{"word":"grass","x":.50,"y":.92,"voice":"male"}],
"question":"What is the man driving?",
"answer":["He","is","driving","a","small","red","car."],"answerVoice":"male",
"notes":"The man does not push the car (packet description): he opens the lid, climbs in (2.5-5 s), drives, sits on a bench (8.5-10.5 s). While he sits inside the car, his box = the windscreen area and the car box = the body below it; in the far driving shots (6-8 s, 13-15 s) he is only a silhouette, so he is off there. The car phrase is a state (the big dark cars beside it make it unique)."})

# ---- 4117
man={0.0:(0,.03,.88,.97),0.5:(0,.03,1,.97),1.0:(.02,.03,.98,.97),1.5:(.15,.02,.85,.98),2.0:(.08,.10,.92,.90),2.5:(.11,.05,.89,.95),
3.0:(.28,.09,.72,.86),3.5:(0,.17,.90,.78),4.0:(.27,.20,.73,.70),4.5:(.25,.15,.75,.75),5.0:(.26,.38,.74,.58),5.5:(.30,.38,.70,.57),
9.0:(0,.08,1,.48),9.5:(0,.02,1,.48),10.0:(0,.02,1,.44),10.5:(0,.02,1,.44),11.0:(0,.02,1,.46),11.5:(0,.02,.72,.70),
12.0:(0,.02,1,.70),12.5:(0,.02,1,.70),13.0:(.04,.35,.44,.37),13.5:(.04,.35,.44,.37),14.0:(0,.33,.60,.39),14.5:(0,.33,.56,.39),15.0:(0,.33,.56,.39)}
wom={3.0:(0,.40,.28,.34),4.0:(0,.39,.27,.20),4.5:(0,.42,.25,.18),5.0:(0,.39,.26,.28),5.5:(.03,.39,.27,.37),
6.0:(0,0,1,1),6.5:(0,0,1,1),7.0:(0,0,1,1),7.5:(0,0,1,1),8.0:(0,0,1,1),
9.0:(.45,.56,.55,.24),9.5:(.55,.50,.45,.24),10.0:(.55,.46,.45,.24),10.5:(.55,.46,.45,.24),11.0:(.55,.48,.45,.25),11.5:(.72,.50,.28,.23),
13.0:(.58,.37,.42,.36),13.5:(.58,.37,.42,.36),14.0:(.64,.36,.36,.36),14.5:(.64,.37,.36,.35),15.0:(.64,.37,.36,.35)}
save({"mediaId":4117,"level":"A","keyWord":"search","defaultVoice":"male",
"taps":[{"phrase":"to look under the sofa","target":"the man","voice":"male","keys":keys(man,t)},
{"phrase":"to hold a phone","target":"the man","voice":"male","keys":keys(man,t)},
{"phrase":"to point at the table","target":"the woman","voice":"female","keys":keys(wom,t)}],
"stillS":10.0,
"nouns":[{"word":"a phone","x":.47,"y":.735,"voice":"male"},{"word":"keys","x":.75,"y":.84,"voice":"male"},
{"word":"a hand","x":.82,"y":.65,"voice":"male"},{"word":"a table","x":.35,"y":.93,"voice":"male"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","at","the","table."],"answerVoice":"female",
"notes":"At 9.0-11.5 s only the woman's pointing hand is in the picture: her box is the hand, the man's box is the part above it. 8.5 s is a blurred transition (both off). Key word 'search' is not used as a word (noun, abstract); 'to look under the sofa' shows it. He crouches by the sofa at 4-5.5 s."})

# ---- 4118
t=T(26)
# time: (player centre x, feet y, net bottom y, mountain top y)
D={0.0:(.52,.51,.575,.21),0.5:(.50,.51,.56,.19),1.0:(.455,.495,.54,.17),1.5:(.455,.495,.54,.16),2.0:(.445,.51,.56,.17),2.5:(.45,.515,.57,.19),
3.0:(.56,.51,.57,.19),3.5:(.645,.495,.58,.18),4.0:(.68,.51,.57,.18),4.5:(.61,.525,.59,.19),5.0:(.585,.545,.60,.22),5.5:(.575,.56,.615,.25),
6.0:(.575,.58,.63,.30),6.5:(.58,.68,.735,.40),7.0:(.555,.81,.88,.535),7.5:(.61,.82,.89,.52),8.0:(.60,.64,.70,.30),8.5:(.41,.56,.625,.18),
9.0:(.33,.54,.61,.16),9.5:(.36,.50,.58,.14),10.0:(.46,.465,.55,.11),10.5:(.54,.455,.55,.10),11.0:(.56,.495,.605,.12),11.5:(.51,.51,.64,.145),
12.0:(.49,.525,.65,.16),12.5:(.505,.535,.65,.16)}
pl={};net={};mt={}
for k,(px,f,nb,mtop) in D.items():
    pl[k]=(px-.10,f-.13,.20,.14)
    y0=f+.01; y1=max(nb+.03,y0+.10); net[k]=(0,y0,1,y1-y0)
    m0=max(0,mtop-.03); mt[k]=(0,m0,1,(f-.14)-m0)
save({"mediaId":4118,"level":"B","keyWord":"court","defaultVoice":"female",
"taps":[{"phrase":"to sprint across the court","target":"the player","voice":"female","keys":keys(pl,t)},
{"phrase":"to hang between two posts","target":"the net","voice":"female","keys":keys(net,t)},
{"phrase":"to tower over the valley","target":"the mountain","voice":"female","keys":keys(mt,t)}],
"stillS":12.5,
"nouns":[{"word":"a court","x":.55,"y":.82,"voice":"female"},{"word":"a net","x":.60,"y":.585,"voice":"female"},
{"word":"a peak","x":.47,"y":.20,"voice":"female"},{"word":"a meadow","x":.78,"y":.485,"voice":"female"}],
"question":"What is the player doing?",
"answer":["The","player","is","sprinting","across","the","court."],"answerVoice":"female",
"notes":"POV clip; the far player is tiny (box at minimum size) and of unclear gender, so 'the player' and the default voice. The yellow blob on the mountain is lens flare, not the ball. The player's box sits directly above the net box and cuts the bottom of the mountain box. Player runs at 2-3 s, 8.5 s, 11 s. Camera player's arm/racket appear at 1.0, 1.5, 6.5-7.5, 9.5 s (not a target)."})
