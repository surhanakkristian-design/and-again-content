import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":round(v[2],2),"h":round(v[3],2)})
    return out
T12=[i*0.5 for i in range(25)]; T10=[i*0.5 for i in range(21)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4601
w={0.0:(0,.10,.88,.82),0.5:(0,.09,.90,.80),1.0:(0,.10,.88,.88),1.5:(0,.08,.90,.90),2.0:(0,.08,.88,.80),
2.5:(0,.20,.34,.63),3.0:(0,.18,.45,.77),3.5:(0,.18,.40,.77),4.0:(0,.19,.40,.63),4.5:(0,.19,.54,.63),
5.0:(0,.19,.74,.76),5.5:(.02,.19,.70,.76),6.0:(.03,.21,.50,.61),6.5:(0,.20,.33,.62),
7.0:(.23,.03,.70,.97),7.5:(.21,.02,.75,.98),8.0:(.18,.03,.80,.97),8.5:(.16,.18,.80,.82),
9.0:(.14,.38,.68,.62),9.5:(.03,.44,.86,.44)}
for t in (10.0,10.5,11.0,11.5,12.0): w[t]=(.03,.43,.90,.46)
k=K(T12,w)
save({"mediaId":4601,"level":"B","keyWord":"arrange","defaultVoice":"female",
"taps":[{"phrase":"to frown at the sofa","target":"the woman","voice":"female","keys":k},
{"phrase":"to arrange the cushions","target":"the woman","voice":"female","keys":k},
{"phrase":"to sprawl across the cushions","target":"the woman","voice":"female","keys":k}],
"stillS":6.5,
"nouns":[{"word":"a curtain","x":0.31,"y":0.22,"voice":"female"},
{"word":"cushions","x":0.65,"y":0.57,"voice":"female"},
{"word":"a coffee table","x":0.22,"y":0.74,"voice":"female"},
{"word":"a sofa","x":0.74,"y":0.80,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","arranging","the","cushions","on","the","sofa."],
"answerVoice":"female",
"notes":"Only one possible target (the woman), so all three phrases use her with the same keys. She frowns at the seat 0-2 s, brings and arranges the cushions 3-6.5 s, lies sprawled on them 9-12 s. Boxes at 4.5-5.5 s include the cushion she is holding. Key word 'arrange' is a verb: used in phrase and answer, not as a noun. 'a sofa' pill sits on the front armrest, away from the cushions; the answer has two lower-case 'the' chips (interchangeable)."})

# 4606
m={0.0:(.17,.39,.63,.61),0.5:(.17,.40,.58,.60),1.0:(.15,.42,.60,.58),1.5:(.19,.41,.60,.59),2.0:(.19,.39,.67,.61),
2.5:(.17,.43,.76,.57),3.0:(.17,.43,.83,.57),3.5:(.18,.52,.70,.48),4.0:(.17,.53,.53,.47),4.5:(.15,.53,.55,.47),
5.0:(.17,.60,.50,.40),5.5:(.17,.61,.52,.39),6.0:(.15,.55,.50,.45),6.5:(.12,.55,.56,.45),7.0:(.15,.55,.50,.45),
7.5:(.36,.22,.64,.78),8.0:(.40,.20,.60,.80),8.5:(.28,.18,.72,.82),9.0:(.22,.19,.78,.81),9.5:(.20,.19,.80,.81),
10.0:(.22,.20,.78,.80),10.5:(.20,.20,.80,.80),11.0:(.17,.20,.83,.80),11.5:(.10,.21,.90,.79),12.0:(0,.22,1.0,.78)}
c={3.5:(.30,.22,.40,.29),4.0:(.30,.22,.40,.30),4.5:(.30,.22,.40,.30),5.0:(.28,.23,.44,.36),5.5:(.28,.23,.44,.37),
6.0:(.28,.22,.44,.32),6.5:(.28,.21,.44,.33),7.0:(.24,.21,.44,.33)}
km=K(T12,m); kc=K(T12,c)
save({"mediaId":4606,"level":"A","keyWord":"a tower","defaultVoice":"male",
"taps":[{"phrase":"to carry a camera","target":"the young man","voice":"male","keys":km},
{"phrase":"to show the time","target":"the clock","voice":"male","keys":kc},
{"phrase":"to drink a big beer","target":"the young man","voice":"male","keys":km}],
"stillS":2.5,
"nouns":[{"word":"the sky","x":0.35,"y":0.12,"voice":"male"},
{"word":"a tower","x":0.60,"y":0.38,"voice":"male"},
{"word":"a river","x":0.20,"y":0.56,"voice":"male"},
{"word":"a jacket","x":0.45,"y":0.82,"voice":"male"}],
"question":"Where is the clock?",
"answer":["The","clock","is","on","a","tower."],
"answerVoice":"male",
"notes":"Three shots (bridge 0-3 s, clock tower 3.5-7 s, beer hall 7.5-12 s). The young man is in every shot; the camera hangs round his neck 0-7 s and he drinks at 8.5-10 s (the other men only hold their glasses). 'the clock' = the two big dials on the tower, only in the middle shot; its box is cut at the top of the man's head, so the lower dial is partly outside it. Pigeons and the men in the beer hall were not used (scattered / do the same as others). 'a tower' on the still is the dark bridge tower; the domed church beside it is not a tower. The answer is about the middle shot."})

# 4607
full=(.03,0,.97,1.0)
a={t:full for t in (0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5)}
a.update({5.0:(0,0,1.0,1.0),5.5:(.72,.42,.28,.36),6.0:(.70,.43,.30,.32),6.5:(.74,.45,.26,.30),
7.0:(0,.20,.50,.80),7.5:(0,0,.62,1.0),8.0:(.03,0,.92,1.0),8.5:(.08,.05,.51,.95),
9.0:(.03,.12,.66,.88),9.5:(0,.14,.69,.86),10.0:(0,.14,.69,.86),10.5:(0,.16,.66,.84),
11.0:(0,.20,.50,.80),11.5:(0,.22,.58,.78),12.0:(0,.21,.58,.79)})
g={8.5:(.61,.20,.32,.14),9.0:(.70,.22,.30,.55),9.5:(.70,.20,.30,.55),10.0:(.70,.20,.30,.45),10.5:(.70,.21,.30,.44),
11.0:(.70,.23,.30,.52),11.5:(.66,.23,.34,.54),12.0:(.66,.23,.34,.52)}
ka=K(T12,a); kg=K(T12,g)
save({"mediaId":4607,"level":"B","keyWord":"copper","defaultVoice":"female",
"taps":[{"phrase":"to pour a frothy beer","target":"the woman in the apron","voice":"female","keys":ka},
{"phrase":"to skim off the foam","target":"the woman in the apron","voice":"female","keys":ka},
{"phrase":"to wear a wristwatch","target":"the man in the green shirt","voice":"male","keys":kg}],
"stillS":10.5,
"nouns":[{"word":"copper","x":0.55,"y":0.14,"voice":"female"},
{"word":"tankards","x":0.62,"y":0.55,"voice":"female"},
{"word":"an apron","x":0.16,"y":0.75,"voice":"female"},
{"word":"a barrel","x":0.70,"y":0.82,"voice":"female"}],
"question":"What are the big tanks made of?",
"answer":["The","tanks","are","made","of","polished","copper."],
"answerVoice":"female",
"notes":"The woman in the apron pours 0-3.5 s and skims the foam off with a flat spatula at 4-5 s; at 5.5-6.5 s only her hand on the tankard is in the picture (box on the hand). The man in the green (olive) shirt: a state, because every action he does (laughing, clinking, standing at the barrel) the others do too; his wristwatch shows at 9-9.5 and 11.5-12 s, hidden at 8.5 s. At 8.5 s he stands behind her right shoulder, so his box is only his head and her box is cut at x 0.59 (it loses her right arm). Weak spot: the wristwatch is small. 'copper' pill sits on the tall copper vessel behind the group. The answer's subject is a thing -> default voice."})

# 4608
cap={0.0:(.29,.33,.32,.42),0.5:(.36,.38,.40,.31),1.0:(.34,.22,.38,.31),1.5:(.39,.43,.31,.26)}
sk={2.0:(.52,.30,.48,.58),2.5:(.24,.28,.76,.63),3.0:(.05,.31,.93,.67),3.5:(0,.32,.68,.63)}
cr={8.5:(0,.43,1.0,.37),9.0:(0,.47,1.0,.43),9.5:(0,.47,1.0,.43),10.0:(0,.44,1.0,.34)}
save({"mediaId":4608,"level":"A","keyWord":"a crowd","defaultVoice":"female",
"taps":[{"phrase":"to turn upside down","target":"the man in the cap","voice":"male","keys":K(T10,cap)},
{"phrase":"to dance in a skirt","target":"the woman in the skirt","voice":"female","keys":K(T10,sk)},
{"phrase":"to fill the whole square","target":"the crowd","voice":"female","keys":K(T10,cr)}],
"stillS":10.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.15,"voice":"female"},
{"word":"buildings","x":0.60,"y":0.42,"voice":"female"},
{"word":"a crowd","x":0.50,"y":0.58,"voice":"female"},
{"word":"the ground","x":0.50,"y":0.85,"voice":"female"}],
"question":"What is the crowd doing?",
"answer":["The","crowd","is","dancing","in","the","square."],
"answerVoice":"female",
"notes":"Four shots: breakdancer 0-1.5 s, couple in the street 2-3.5 s, group in a shopping centre 4-8 s, big square 8.5-10 s. The man in the cap is upside down only at 1.0 s. The woman in the skirt: her partner in white overlaps her box (he is not a target). 'the crowd' is boxed only in the last shot, where it fills the square; the onlookers in shots 1-3 are also crowds but do not fill a square and stand behind the dancers - verifier please judge. No target in the shopping-centre shot (all dancers do the same). No main person -> default voice female (evenId true)."})
