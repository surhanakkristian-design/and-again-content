import json
def B(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(d): return [B(t,d[t]) for t in sorted(d)]
def save(c): json.dump(c, open(f'content/{c["mediaId"]}.json','w'), indent=1, ensure_ascii=False)
T=lambda n:[i*0.5 for i in range(n)]
# ---------- 4336
man={0.0:(0,.13,.42,.87),0.5:(0,.13,.46,.87),1.0:(0,.14,.48,.86),1.5:(0,.14,.51,.86),2.0:(0,.15,.52,.85),2.5:(.09,.18,.38,.59),
3.0:(.09,.2,.37,.7),3.5:(.09,.2,.38,.7),4.0:(.1,.27,.38,.52),4.5:(.08,.21,.38,.56),5.0:(.01,.23,.37,.68),5.5:(0,.27,.52,.65),
6.0:(0,.21,.42,.6),6.5:(.06,.25,.32,.53),7.0:(.03,.21,.34,.69),7.5:(.04,.21,.33,.67),8.0:None,8.5:None,9.0:(0,.48,.25,.52),
9.5:(0,.22,.45,.78),10.0:(0,.22,.36,.78),10.5:(0,.23,.3,.77),11.0:(0,.25,.31,.75),11.5:(0,.25,.32,.75),12.0:(0,.16,.5,.84)}
wom={0.0:(.42,.15,.58,.8),0.5:(.46,.15,.54,.8),1.0:(.48,.18,.52,.8),1.5:(.52,.3,.48,.7),2.0:(.53,.28,.47,.72),2.5:(.52,.22,.43,.57),
3.0:(.5,.22,.43,.69),3.5:(.58,.23,.38,.69),4.0:(.5,.28,.48,.54),4.5:(.5,.21,.5,.6),5.0:(.68,.22,.32,.74),5.5:(.62,.21,.38,.78),
6.0:(.66,.2,.34,.66),6.5:(.64,.27,.36,.58),7.0:(.64,.21,.33,.77),7.5:(.6,.22,.38,.75),8.0:(.68,.32,.32,.68),8.5:(.66,.44,.34,.52),
9.0:(.42,.28,.58,.72),9.5:(.68,.28,.32,.72),10.0:(.7,.28,.3,.72),10.5:(.68,.28,.32,.72),11.0:(.7,.29,.3,.71),11.5:(.7,.29,.3,.71),12.0:(.51,.18,.49,.82)}
save({"mediaId":4336,"level":"B","keyWord":"instructions","defaultVoice":"female",
"taps":[{"phrase":"to read the instructions","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to attach a wooden leg","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to step on the stool","target":"the woman","voice":"female","keys":keys(wom)}],
"stillS":2.5,
"nouns":[{"word":"instructions","x":.36,"y":.42,"voice":"female"},{"word":"a stool","x":.5,"y":.74,"voice":"female"},
{"word":"a window","x":.24,"y":.18,"voice":"female"},{"word":"a parquet floor","x":.5,"y":.9,"voice":"female"}],
"question":"What is the man doing?","answer":["He","is","reading","the","assembly","instructions."],"answerVoice":"male",
"notes":"Two phrases share the woman (no third target: furniture overlaps both people). The man also uses a small tool on the shelf at 5.5-6.0 s, so the woman's phrase is 'attach a wooden leg', not 'tighten a screw'. 8.0-8.5 s: only the man's fingertips visible -> off; 8.5 s woman = arm only. 9.0 s man = forearm and leg at the left edge. 'step on the stool' = she puts one foot on it at 2.5-3.0 s."})
# ---------- 4339
w={0.0:(0,.25,.8,.75),0.5:(0,.1,.88,.9),1.0:(0,.5,.4,.5),1.5:(0,.03,.75,.97),2.0:(0,0,.65,1),2.5:(0,.14,.93,.86),3.0:(0,.13,1,.87),
3.5:(0,.1,1,.9),4.0:(0,.14,.9,.86),4.5:(0,.31,.63,.69),5.0:(.2,.29,.62,.71),5.5:(.24,.28,.54,.72),6.0:(.22,.29,.52,.71),6.5:None,7.0:None,
7.5:(.13,.17,.82,.83),8.0:(.14,.17,.84,.73),8.5:(.14,.19,.84,.71),9.0:(.1,.2,.88,.72)}
tg="the woman in the brown jacket"
save({"mediaId":4339,"level":"A","keyWord":"bank","defaultVoice":"female",
"taps":[{"phrase":"to use a bank card","target":tg,"voice":"female","keys":keys(w)},
{"phrase":"to press the buttons","target":tg,"voice":"female","keys":keys(w)},
{"phrase":"to count the money","target":tg,"voice":"female","keys":keys(w)}],
"stillS":9.0,
"nouns":[{"word":"money","x":.46,"y":.56,"voice":"female"},{"word":"a bag","x":.76,"y":.79,"voice":"female"},
{"word":"buttons","x":.46,"y":.94,"voice":"female"},{"word":"lights","x":.38,"y":.19,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","a lot of","money."],"answerVoice":"female",
"notes":"Only one clear target (the woman); all three phrases use her. 1.0 s: only her hands are in the picture. 6.5-7.0 s: she is not in the shot (the people with suitcases are others) -> off. Key word 'bank' is not a visible noun (only as logos), it appears in 'bank card'. 'a lot of' is one chip."})
# ---------- 4340
m={0.0:(.39,.08,.61,.92),0.5:(.41,.08,.59,.92),1.0:(.4,.08,.6,.92),1.5:(.41,.08,.59,.92),2.0:(.4,.08,.6,.92),2.5:(.41,.09,.59,.91),
3.0:(.39,.1,.61,.9),3.5:(.61,.1,.39,.9),4.0:(.28,.18,.72,.82),4.5:(.2,.24,.8,.76),5.0:(.18,.32,.82,.68),5.5:(.2,.42,.8,.58),
6.0:(.25,.46,.75,.54),6.5:(.26,.48,.74,.52),7.0:(.25,.48,.75,.52),7.5:(.25,.49,.75,.51),8.0:(.1,.48,.9,.52),8.5:(.1,.5,.9,.5),
9.0:(.39,.54,.61,.46),9.5:(.05,.45,.95,.55),10.0:(.15,.44,.8,.56),10.5:(.28,.51,.6,.49),11.0:(.36,.53,.42,.47),11.5:(.45,.52,.32,.48),12.0:(.34,.51,.22,.35)}
g={0.0:(0,.26,.38,.37),0.5:(0,.26,.4,.37),1.0:(0,.26,.39,.37),1.5:(0,.27,.4,.36),2.0:(0,.26,.39,.38),2.5:(0,.27,.4,.37),
3.0:(0,.27,.38,.38),3.5:(0,.1,.6,.6),4.0:(0,.1,.27,.52),4.5:None,5.0:(0,.05,1,.26),5.5:(.03,.01,.84,.4),
6.0:(0,.02,.85,.43),6.5:(0,.3,1,.17),7.0:(0,.13,1,.34),7.5:(0,.17,1,.31),8.0:(0,.13,1,.34),8.5:(0,.06,1,.43),
9.0:(0,.33,1,.2),9.5:(.45,0,.55,.44),10.0:(.52,.18,.48,.25),10.5:(.36,.3,.64,.2),11.0:(.25,.37,.55,.15),11.5:(.18,.29,.62,.22),12.0:(.34,.36,.36,.14)}
save({"mediaId":4340,"level":"B","keyWord":"chips","defaultVoice":"male",
"taps":[{"phrase":"to clutch a paper cone","target":"the young man","voice":"male","keys":keys(m)},
{"phrase":"to shield his chips","target":"the young man","voice":"male","keys":keys(m)},
{"phrase":"to snatch a chip","target":"the seagull","voice":"male","keys":keys(g)}],
"stillS":2.0,
"nouns":[{"word":"chips","x":.73,"y":.59,"voice":"male"},{"word":"a seagull","x":.18,"y":.47,"voice":"male"},
{"word":"a bench","x":.22,"y":.8,"voice":"male"},{"word":"the sky","x":.3,"y":.1,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","shielding","his","chips","from","the","seagulls."],"answerVoice":"male",
"notes":"WEAK SPOT: 'the seagull' is one bird until 4.0 s; from 5.0 s several gulls attack and each snatches chips, so the gull box is the band of gulls above/beside the man (not one bird). From 7.0 s gulls sit on or in front of the man, so parts of gulls fall inside the man's box (split along the top of his hood). 4.5 s: only a wing tip -> gull off."})
# ---------- 4341
m={0.0:(.38,.19,.62,.81),0.5:(.39,.18,.61,.82),1.0:(.4,.18,.6,.82),1.5:(.41,.18,.59,.82),2.0:(.42,.2,.58,.8),2.5:(.61,.2,.39,.8),
3.0:(.17,.3,.83,.7),3.5:(.06,.4,.94,.6),4.0:(.07,.42,.9,.58),4.5:(.1,.48,.9,.52),5.0:(.02,.4,.86,.6),5.5:(.02,.37,.98,.63),
6.0:(0,.29,.8,.71),6.5:(0,.28,.76,.72),7.0:(.16,.33,.42,.56),7.5:(.17,.35,.38,.42),8.0:(.24,.37,.3,.35),8.5:(.27,.38,.24,.3),
9.0:(.27,.39,.24,.25),9.5:(.27,.39,.2,.22),10.0:(.27,.4,.19,.2)}
g={t:None for t in m}
g.update({0.0:(0,.33,.37,.43),0.5:(0,.32,.38,.44),1.0:(0,.33,.39,.44),1.5:(0,.33,.4,.45),2.0:(0,.36,.41,.43),2.5:(0,.14,.6,.56)})
save({"mediaId":4341,"level":"B","keyWord":"flee","defaultVoice":"male",
"taps":[{"phrase":"to flee from the seagulls","target":"the young man","voice":"male","keys":keys(m)},
{"phrase":"to nibble a chip","target":"the young man","voice":"male","keys":keys(m)},
{"phrase":"to perch on the bench","target":"the seagull","voice":"male","keys":keys(g)}],
"stillS":1.5,
"nouns":[{"word":"a seagull","x":.2,"y":.52,"voice":"male"},{"word":"chips","x":.85,"y":.6,"voice":"male"},
{"word":"a bench","x":.2,"y":.9,"voice":"male"},{"word":"the sky","x":.4,"y":.12,"voice":"male"}],
"question":"What is the young man fleeing from?","answer":["He","is","fleeing","from","a","flock","of","seagulls."],"answerVoice":"male",
"notes":"'the seagull' = the bird perched on the bench (0-2.5 s, at 2.5 s it lunges at the cone); after that it cannot be told apart from the other gulls, which do not perch -> off from 3.0 s. From 8.0 s the running man is small and gulls fly across him; his box is kept tight."})
