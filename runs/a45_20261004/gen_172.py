import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def w(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 172
woman={0:(0,0,1,.14),.5:(0,0,1,.14),1:(0,0,1,.14),1.5:(0,0,1,.26),2:(0,0,1,.72),2.5:(.20,0,.62,.48),
3:(.17,0,.53,.40),3.5:(.50,0,.38,.41),4:(.20,0,.70,.52),4.5:(.14,0,.86,.54),5:(0,0,.90,.51),5.5:(0,0,1,.43),
6:(.17,0,.83,.35),6.5:(.42,0,.58,.46),7:(.33,.05,.44,.47),7.5:(.25,.07,.47,.55),8:(.19,.07,.62,.61),
8.5:(.15,0,.62,.68),9:(.16,.01,.58,.82),9.5:(.18,.01,.63,.82),10:(.21,.01,.57,.70)}
cleats={0:(.08,.15,.82,.85),.5:(.10,.15,.78,.85),1:(.12,.15,.78,.85),1.5:(.28,.27,.62,.73),2:(.27,.73,.68,.27),
2.5:(.16,.49,.56,.24),3:(.06,.41,.94,.32),3.5:(.17,.42,.63,.30),4:(.04,.53,.77,.17),4.5:(.30,.55,.46,.16),
5:(0,.52,.68,.18),5.5:(0,.44,.88,.21),6:(.05,.36,.95,.19),6.5:(.24,.47,.76,.15),7:(.44,.53,.38,.14),
7.5:(.36,.63,.36,.14),8:(.31,.69,.38,.15),8.5:(.28,.69,.40,.15),9:(.29,.84,.42,.15),9.5:(.31,.84,.42,.15),
10:(.30,.72,.43,.15)}
bench={3:(.71,.03,.27,.27),3.5:(.26,.07,.23,.30),4:(0,.11,.19,.29)}
w({"mediaId":172,"level":"B","keyWord":"cleats","defaultVoice":"female",
"taps":[{"phrase":"to sprint across the pitch","target":"the woman","voice":"female","keys":keys(woman)},
{"phrase":"to dig into the mud","target":"the cleats","voice":"female","keys":keys(cleats)},
{"phrase":"to clutch a football","target":"the player on the bench","voice":"female","keys":keys(bench)}],
"stillS":10.0,
"nouns":[{"word":"a rain jacket","x":.50,"y":.31,"voice":"female"},{"word":"a stone wall","x":.82,"y":.43,"voice":"female"},
{"word":"cleats","x":.52,"y":.77,"voice":"female"},{"word":"mud","x":.42,"y":.88,"voice":"female"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","at","her","muddy","cleats."],"answerVoice":"female",
"notes":"Woman and cleats overlap in the picture, so their boxes are split at the ankles (woman above, cleats below); at 0-1.5 s one cleat fills the frame and the woman only has the top strip. The player on the bench is small and visible only at 3.0-4.0 s (gender unclear, default voice). 'Sprint' happens at 5-6.5 s where only her legs are in frame."})

# ---------- 173
wo={0:(0,.47,.59,.53),.5:(0,.49,.59,.51),1:(0,.46,.53,.54),1.5:(0,.48,.45,.52),2:(0,.54,.30,.46),
4.5:(0,.44,.52,.56),5:(0,.42,.52,.58),5.5:(0,.41,.51,.59),6:(0,.49,.50,.51),6.5:(0,.52,.49,.48),7:(0,.54,.48,.46),
7.5:(0,.56,.49,.44),8:(0,.58,.49,.42),8.5:(0,.61,.49,.39),9:(0,.62,.50,.38),9.5:(0,.66,.52,.34),10:(0,.60,.50,.40)}
ma={0:(.60,.46,.40,.54),.5:(.60,.45,.40,.55),1:(.54,.42,.46,.58),1.5:(.63,.43,.37,.57),
4.5:(.55,.40,.45,.60),5:(.53,.40,.47,.60),5.5:(.52,.46,.48,.54),6:(.51,.52,.49,.48),6.5:(.50,.52,.50,.48),
7:(.49,.53,.51,.47),7.5:(.50,.56,.50,.44),8:(.50,.58,.50,.42),8.5:(.50,.62,.50,.38),9:(.51,.64,.49,.36),
9.5:(.55,.65,.45,.35),10:(.51,.60,.49,.40)}
wa={1.5:(0,.33,.27,.14),2:(0,.18,.32,.35),2.5:(0,.20,.40,.60),3:(0,.20,.45,.70),3.5:(0,.20,.50,.68),4:(0,.20,.45,.56),
4.5:(.02,.20,.46,.23),5:(0,.26,.47,.15),5.5:(0,.26,.47,.14),6:(0,.27,.46,.21),6.5:(0,.30,.43,.21),7:(0,.30,.44,.23),
7.5:(0,.30,.44,.25),8:(0,.28,.44,.29),8.5:(0,.25,.44,.35),9:(0,.28,.45,.33),9.5:(0,.30,.44,.35),10:(0,.22,.42,.37)}
w({"mediaId":173,"level":"A","keyWord":"cliff","defaultVoice":"male",
"taps":[{"phrase":"to wear an orange jacket","target":"the woman","voice":"female","keys":keys(wo)},
{"phrase":"to have a short beard","target":"the man","voice":"male","keys":keys(ma)},
{"phrase":"to hit the dark rocks","target":"the waves","voice":"male","keys":keys(wa)}],
"stillS":10.0,
"nouns":[{"word":"the sea","x":.20,"y":.30,"voice":"male"},{"word":"a cliff","x":.70,"y":.30,"voice":"male"},
{"word":"a woman","x":.20,"y":.82,"voice":"female"},{"word":"a man","x":.76,"y":.82,"voice":"male"}],
"question":"What are the two people doing?",
"answer":["They","are","lying","on","a","high","cliff."],"answerVoice":"male",
"notes":"Both people do the same actions (walk, lie down, look, laugh), so the two person phrases are states. The beard is seen only when the man's face is turned (0-1.5, 4.5-5, 9-10 s). The waves box is the sea with white foam left of the cliff; at 1.0 s only a sliver of sea shows behind the woman (off there); at 4.5-7.5 s the box is the sea strip above the people's heads. Mixed couple, odd id -> default voice male."})

# ---------- 174
boy={.5:(.13,.46,.28,.52),1:(.19,.48,.43,.52),1.5:(.30,.58,.70,.42),2:(.40,.70,.53,.30),2.5:(.16,.85,.54,.15),
3.5:(0,.46,.64,.54),4:(.06,.34,.62,.66),4.5:(.27,.29,.48,.69),5:(.37,.33,.50,.63),5.5:(.41,.34,.50,.55),
6:(.41,.36,.57,.56),6.5:(.42,.38,.44,.51),7:(.32,.40,.62,.55),7.5:(.22,.43,.47,.52),8:(.19,.44,.58,.56),
8.5:(.20,.42,.48,.58),9:(.37,.37,.49,.63),9.5:(.48,.35,.46,.60),10:(.54,.33,.36,.45)}
old={1:(0,.44,.18,.56),4.5:(0,.57,.26,.43),5:(0,.27,.36,.73),5.5:(0,.29,.40,.71),6:(0,.32,.40,.68),
6.5:(0,.34,.41,.66),7:(0,.36,.31,.64),7.5:(0,.42,.21,.58),8:(0,.66,.18,.34),8.5:(0,.66,.19,.34),
9:(0,.68,.18,.32),9.5:(0,.70,.18,.30)}
rec={1.5:(.50,.27,.30,.30),2:(.30,.22,.58,.40),2.5:(.27,.19,.73,.48),3:(.26,.16,.74,.50)}
w({"mediaId":174,"level":"B","keyWord":"clinic","defaultVoice":"female",
"taps":[{"phrase":"to fill in a form","target":"the receptionist","voice":"female","keys":keys(rec)},
{"phrase":"to grip a wooden cane","target":"the old man","voice":"male","keys":keys(old)},
{"phrase":"to carry a grey backpack","target":"the boy","voice":"male","keys":keys(boy)}],
"stillS":10.0,
"nouns":[{"word":"a lab coat","x":.62,"y":.35,"voice":"female"},{"word":"a houseplant","x":.40,"y":.47,"voice":"female"},
{"word":"a backpack","x":.70,"y":.56,"voice":"female"},{"word":"a chair","x":.16,"y":.83,"voice":"female"}],
"question":"What is the old man doing?",
"answer":["He","is","gripping","a","wooden","cane."],"answerVoice":"male",
"notes":"Receptionist is clearly visible only at 1.5-3.0 s (hidden behind the mother at 1.0, only a hand at 3.5). Old man: at 4.5 and 8.0-9.5 s only his arm/hand, cane and knee are in frame (box kept on them); off at 10.0. Boy and old man sit next to each other at 5-7.5 s: boxes split between them, the old man's knee reaches under the boy's box. Mother and doctor are not targets. The key word 'clinic' is not a placeable noun."})

# ---------- 175
man={0:(0,.36,.13,.50),.5:(0,.38,.13,.38),1:(0,.42,.13,.45),1.5:(0,.38,.13,.62),2:(0,.29,.25,.71),2.5:(0,.29,.28,.71),
3:(0,.34,.29,.66),3.5:(0,.36,.29,.64),4:(0,.36,.29,.64),4.5:(0,.33,.29,.67),5:(0,.31,.29,.69),5.5:(0,.31,.29,.69),
6:(0,.28,.28,.72),6.5:(0,.28,.28,.72),7:(0,.28,.30,.72),7.5:(0,.29,.32,.71),8:(0,.28,.33,.72),8.5:(0,.29,.30,.71),
9:(0,.27,.29,.73),9.5:(0,.28,.28,.72),10:(0,.28,.29,.72)}
wom={0:(.14,.77,.86,.23),.5:(.14,.68,.86,.32),1:(.14,.67,.86,.33),1.5:(.82,.40,.18,.60),2:(.77,.38,.23,.62),
2.5:(.74,.34,.26,.66),3:(.70,.38,.30,.62),3.5:(.67,.38,.33,.62),4:(.66,.38,.34,.62),4.5:(.65,.35,.35,.65),
5:(.67,.36,.33,.64),5.5:(.67,.34,.33,.66),6:(.66,.34,.34,.66),6.5:(.63,.35,.37,.65),7:(.66,.35,.34,.65),
7.5:(.65,.35,.35,.65),8:(.70,.35,.30,.65),8.5:(.72,.36,.28,.64),9:(.69,.34,.31,.66),9.5:(.67,.30,.33,.70),
10:(.68,.33,.32,.67)}
clk={0:(.14,.32,.69,.44),.5:(.14,.23,.72,.44),1:(.14,.22,.72,.44),1.5:(.14,.21,.67,.44),2:(.26,.25,.50,.37),
2.5:(.29,.25,.44,.30),3:(.30,.28,.39,.30),3.5:(.30,.28,.36,.30),4:(.30,.28,.35,.30),4.5:(.30,.27,.34,.30),
5:(.30,.27,.36,.30),5.5:(.30,.27,.36,.30),6:(.29,.25,.36,.32),6.5:(.29,.25,.33,.32),7:(.31,.24,.34,.33),
7.5:(.33,.24,.31,.33),8:(.34,.26,.35,.30),8.5:(.31,.25,.40,.29),9:(.30,.24,.38,.27),9.5:(.29,.25,.37,.26),
10:(.30,.26,.37,.23)}
w({"mediaId":175,"level":"A","keyWord":"clock","defaultVoice":"male",
"taps":[{"phrase":"to hang on the wall","target":"the clock","voice":"male","keys":keys(clk)},
{"phrase":"to set the clock","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to wear glasses","target":"the man","voice":"male","keys":keys(man)}],
"stillS":8.5,
"nouns":[{"word":"cups","x":.17,"y":.19,"voice":"male"},{"word":"a window","x":.86,"y":.19,"voice":"male"},
{"word":"a clock","x":.50,"y":.40,"voice":"male"},{"word":"a cat","x":.18,"y":.69,"voice":"male"}],
"question":"Where is the clock?",
"answer":["The","clock","is","hanging","on","the","wall."],"answerVoice":"male",
"notes":"At 0-1.0 s the woman's hands hold the clock: her box is only the strip with her arms below the clock, the man is a thin strip at the left edge (box narrower than 0.18 so it does not cut the clock). The woman sets the clock with the knob on its side at 2.5-5.0 s (the hands jump at 5.5 s). At 6.5-7.5 s her face is in front of the clock's right rim, the clock box is cut there. 'cups' = the group on the shelves (the couple also hold one cup each at the still). Mixed couple, odd id -> default voice male."})
