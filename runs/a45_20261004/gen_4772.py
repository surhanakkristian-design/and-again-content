import json
def K(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def dump(c): json.dump(c, open(f'content/{c["mediaId"]}.json','w'), indent=1, ensure_ascii=False)

# ---- 4772
t=T(25)
flock={0.0:(0,.13,.68,.30),0.5:(0,.13,.68,.33),1.0:(0,.14,.70,.35),1.5:(0,.13,.75,.40),2.0:(0,.14,.80,.41),2.5:(0,.12,.90,.47),
3.0:(0,.10,.95,.53),3.5:(0,.08,1,.57),4.0:(0,.07,1,.62),4.5:(0,.07,1,.65),5.0:(0,.02,1,.70),5.5:(0,.02,1,.70),6.0:(0,.02,1,.70),
6.5:(0,.02,1,.68),7.0:(0,.02,1,.66),7.5:(0,.02,1,.62),8.0:(0,0,1,.63),8.5:(0,0,1,.60),9.0:(0,0,1,.58),9.5:(0,0,1,.54),
10.0:(0,0,1,.55),10.5:(0,0,1,.53),11.0:(0,0,1,.52),11.5:(0,0,1,.50),12.0:(0,0,1,.49)}
wom={0.0:(.10,.44,.62,.56),0.5:(.18,.47,.60,.53),1.0:(.25,.50,.58,.50),1.5:(.38,.55,.57,.45),2.0:(.52,.63,.48,.37),2.5:(.80,.68,.20,.32),
8.0:(.64,.73,.36,.27),8.5:(.52,.69,.36,.31),9.0:(.42,.65,.36,.35),9.5:(.30,.62,.42,.38),10.0:(.22,.58,.41,.42),10.5:(.19,.55,.42,.45),
11.0:(.15,.53,.43,.47),11.5:(.17,.51,.43,.49),12.0:(.16,.49,.43,.51)}
wk=K(t,wom)
dump({"mediaId":4772,"level":"B","keyWord":"flock","defaultVoice":"female",
"taps":[{"phrase":"to wheel across the sky","target":"the flock of birds","voice":"female","keys":K(t,flock)},
{"phrase":"to point at the flock","target":"the woman in the beret","voice":"female","keys":wk},
{"phrase":"to clutch his arm","target":"the woman in the beret","voice":"female","keys":wk}],
"stillS":2.0,
"nouns":[{"word":"a flock","x":.55,"y":.38,"voice":"female"},{"word":"a beret","x":.83,"y":.69,"voice":"female"},
{"word":"a marsh","x":.30,"y":.66,"voice":"female"},{"word":"a railing","x":.18,"y":.84,"voice":"female"}],
"question":"What is the woman pointing at?","answer":["She","is","pointing","at","a","flock","of","birds."],"answerVoice":"female",
"notes":"Two phrases share the woman: the man beside her does nothing she does not also do (both stare up open-mouthed, both wear scarves), so no phrase fits only him. She points only at 0-1.5 s and holds his arm from 8.5 s. Woman off 3.0-7.5 s (out of frame; only a sliver of beret at 7.5). Her box overlaps the man (not a target). 'wheel' is the B-level verb for the flock."})

# ---- 4773
t=T(21)
mus={0.0:(.40,.29,.27,.24),0.5:(.39,.30,.27,.22),1.0:(.37,.29,.26,.23),1.5:(.37,.29,.26,.24),2.0:(.37,.29,.26,.20),2.5:(.37,.30,.26,.21),
3.0:(.37,.32,.26,.25),3.5:(.39,.33,.26,.24),4.0:(.38,.33,.25,.24),4.5:(.38,.34,.24,.23),5.0:(.36,.36,.24,.20),5.5:(.37,.36,.23,.19),
6.0:(.41,.37,.19,.15),6.5:(.41,.38,.19,.15),7.0:(.42,.41,.18,.14),7.5:(.44,.42,.18,.14),8.0:(.43,.46,.18,.14),8.5:(.43,.47,.18,.14),
9.0:(.41,.50,.18,.14),9.5:(.41,.51,.18,.14),10.0:(.41,.53,.18,.14)}
wom={0.0:(.22,.53,.68,.47),0.5:(.42,.52,.55,.48),1.0:(.40,.52,.60,.48),1.5:(.47,.53,.53,.47),2.0:(.50,.49,.48,.51),2.5:(.50,.51,.48,.49),
3.0:(.48,.57,.50,.43),3.5:(.50,.57,.48,.43),4.0:(.48,.57,.45,.43),4.5:(.48,.57,.46,.43),5.0:(.48,.57,.44,.43),5.5:(.45,.56,.45,.44),
6.0:(.47,.56,.40,.44),6.5:(.47,.56,.38,.44),7.0:(.47,.57,.36,.43),7.5:(.48,.59,.36,.41),8.0:(.46,.62,.36,.38),8.5:(.50,.63,.34,.37),
9.0:(.40,.65,.40,.35),9.5:(.43,.66,.37,.34),10.0:(.50,.68,.36,.32)}
wk=K(t,wom)
dump({"mediaId":4773,"level":"B","keyWord":"gathering","defaultVoice":"male",
"taps":[{"phrase":"to play the accordion","target":"the musician","voice":"male","keys":K(t,mus)},
{"phrase":"to wave at the musician","target":"the woman with the plait","voice":"female","keys":wk},
{"phrase":"to grin at the camera","target":"the woman with the plait","voice":"female","keys":wk}],
"stillS":1.5,
"nouns":[{"word":"an accordion","x":.52,"y":.40,"voice":"male"},{"word":"an instrument case","x":.50,"y":.57,"voice":"male"},
{"word":"a plait","x":.80,"y":.76,"voice":"male"},{"word":"cobblestones","x":.22,"y":.70,"voice":"male"}],
"question":"What are the people doing?","answer":["They","are","gathering","around","a","musician."],"answerVoice":"male",
"notes":"Two phrases share the woman: the only other distinct figure, the cyclist (3.0-5.5 s), overlaps the musician's box, and the crowd surrounds him. She raises her hand towards the musician at 2.0-2.5 s (read as a wave) and turns to the camera grinning at 8.5-10 s. The black shape on the ground is read as his instrument case. From 6 s the musician is small (minimum-size box) with crowd members inside his box."})

# ---- 4775
t=T(19)
wom={0.0:(0,.04,.55,.41),0.5:(0,.04,.55,.41),1.0:(0,.04,.55,.41),1.5:(0,.04,.55,.41),2.0:(0,.08,.56,.38),2.5:(.02,.10,.54,.37),
3.0:(.05,.13,.50,.35),3.5:(.06,.16,.48,.33),4.0:(.08,.19,.44,.31),4.5:(.12,.20,.44,.31),5.0:(.12,.26,.42,.26),5.5:(.13,.28,.40,.24),
6.0:(.20,.28,.33,.24),6.5:(.20,.29,.33,.23),7.0:(.21,.33,.31,.19),7.5:(.22,.31,.30,.20),8.0:(.22,.31,.30,.20),8.5:(.22,.31,.30,.20),9.0:(.22,.31,.30,.20)}
baby={0.0:(.28,.45,.67,.35),0.5:(.28,.45,.67,.35),1.0:(.28,.45,.67,.35),1.5:(.28,.45,.67,.35),2.0:(.28,.46,.67,.34),2.5:(.28,.47,.62,.36),
3.0:(.30,.49,.56,.34),3.5:(.30,.50,.54,.33),4.0:(.30,.50,.52,.33),4.5:(.32,.51,.50,.32),5.0:(.30,.52,.48,.33),5.5:(.32,.52,.46,.33),
6.0:(.22,.52,.50,.35),6.5:(.22,.52,.50,.35),7.0:(.23,.53,.47,.34),7.5:(.24,.53,.46,.33),8.0:(.24,.53,.46,.33),8.5:(.24,.53,.46,.33),9.0:(.24,.53,.46,.33)}
boy={6.0:(0,.18,.20,.82),6.5:(0,.20,.20,.80),7.0:(0,.21,.21,.79),7.5:(0,.23,.22,.77),8.0:(0,.24,.22,.76),8.5:(0,.24,.22,.76),9.0:(0,.25,.22,.75)}
dump({"mediaId":4775,"level":"B","keyWord":"newborn","defaultVoice":"female",
"taps":[{"phrase":"to cradle a newborn baby","target":"the woman with the baby","voice":"female","keys":K(t,wom)},
{"phrase":"to sleep wrapped in a blanket","target":"the baby","voice":"female","keys":K(t,baby)},
{"phrase":"to wear a dark hoodie","target":"the boy","voice":"male","keys":K(t,boy)}],
"stillS":0.0,
"nouns":[{"word":"a newborn","x":.72,"y":.52,"voice":"female"},{"word":"a blanket","x":.40,"y":.78,"voice":"female"},
{"word":"a cushion","x":.75,"y":.32,"voice":"female"},{"word":"potted plants","x":.68,"y":.15,"voice":"female"}],
"question":"Who is sleeping in the blanket?","answer":["A","newborn","baby","is","sleeping","in","the","blanket."],"answerVoice":"female",
"notes":"The baby lies in the woman's arms, so the two boxes are split: her box = head and shoulders above the bundle, the baby's box = head and swaddled bundle (her hands lie on it). The boy's phrase is a state (he and the young woman both lean in and smile, no action fits only him); he is set off at 5.0-5.5 s where only hair and a sleeve show. 'a newborn' (noun) sits on the baby's head, 'a blanket' on the bundle below."})

# ---- 4777
man={0.0:(.32,.30,.38,.70),0.5:(.40,.29,.60,.71),1.0:(0,.28,1,.72),1.5:(.03,.22,.97,.78),2.0:(.26,.22,.46,.61),2.5:(.32,.33,.42,.52),
3.0:(.38,.40,.45,.46),3.5:(.36,.22,.60,.72),4.0:(.36,.19,.64,.81),4.5:(.50,.19,.50,.71),5.0:(.49,.20,.51,.73),5.5:(.55,.08,.45,.83),
6.0:(.54,.15,.42,.78),6.5:(.44,.30,.54,.70),7.0:(.28,.16,.72,.84),7.5:(.27,.15,.73,.85),8.0:(.25,.16,.75,.84),8.5:(.18,.16,.82,.84),9.0:(.27,.17,.73,.83)}
wom={4.5:(.07,.25,.42,.52),5.0:(.03,.26,.46,.55),5.5:(.03,.28,.52,.57),6.0:(.01,.30,.53,.58)}
mk=K(t,man)
dump({"mediaId":4777,"level":"A","keyWord":"helpful","defaultVoice":"male",
"taps":[{"phrase":"to pick up a scarf","target":"the man in the suit","voice":"male","keys":mk},
{"phrase":"to open an umbrella","target":"the man in the suit","voice":"male","keys":mk},
{"phrase":"to carry lots of bags","target":"the woman with the bags","voice":"female","keys":K(t,wom)}],
"stillS":5.5,
"nouns":[{"word":"an umbrella","x":.62,"y":.20,"voice":"male"},{"word":"a man","x":.76,"y":.55,"voice":"male"},
{"word":"a woman","x":.18,"y":.43,"voice":"female"},{"word":"shopping bags","x":.28,"y":.66,"voice":"male"}],
"question":"What is the man picking up?","answer":["He","is","picking","up","a","scarf."],"answerVoice":"male",
"notes":"Four shots (cuts at about 2.0, 4.5 and 6.5 s). Two phrases share the man: the other people are on screen for 1-2 s only and are hard to tell apart by a simple action (two old women, several bags). The woman with the bags is visible only 4.5-6.0 s; the other white-haired woman (scarf, 3.5-4.0 s) is not the target. At 5.5-6.0 s the man's umbrella reaches over the woman, so his box is cut at her right edge and does not hold the whole umbrella."})
