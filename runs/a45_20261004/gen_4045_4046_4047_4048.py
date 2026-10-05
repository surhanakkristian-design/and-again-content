import json
T=[i*0.5 for i in range(31)]
def K(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def W(i,d): json.dump(d,open("content/%d.json"%i,"w"),indent=1)

# ---------- 4045
M={0.0:(.44,.13,.56,.87),0.5:(.42,.10,.58,.90),1.0:(0,.08,.92,.92),1.5:(.15,.10,.85,.90),2.0:(.31,.16,.69,.84),
2.5:(.50,.15,.50,.83),3.0:(.47,.26,.53,.74),3.5:(.48,.31,.52,.69),4.0:(.52,.19,.48,.80),4.5:(.40,.22,.60,.77),
5.0:(.35,.49,.65,.51),5.5:(.35,.48,.60,.52),6.0:(.38,.48,.54,.44),6.5:(.38,.24,.62,.68),7.0:(.45,.09,.55,.91),
7.5:(.40,.10,.60,.90),8.0:(.38,.09,.62,.91),8.5:(.38,.09,.62,.91),9.0:(.35,.09,.65,.91),9.5:(.35,.09,.65,.91),
11.0:(0,.42,.92,.48),11.5:(.40,.09,.60,.91),12.0:(.42,.08,.58,.92),12.5:(.43,.08,.57,.92),13.0:(.42,.08,.58,.92),
13.5:(.40,.08,.60,.92),14.0:(.40,.08,.60,.92),14.5:(.40,.08,.60,.92),15.0:(.40,.08,.60,.92)}
Wm={0.0:(0,.42,.40,.36),0.5:(.08,.48,.33,.32),2.0:(.05,.44,.25,.37),2.5:(.02,.38,.45,.42),3.0:(.02,.38,.44,.35),
3.5:(.06,.37,.41,.36),4.0:(.10,.40,.41,.32),4.5:(.08,.34,.31,.36),5.0:(.05,.35,.29,.36),5.5:(.03,.35,.31,.36),
6.0:(0,.33,.37,.36),6.5:(.03,.33,.34,.36),7.0:(0,.38,.44,.34),7.5:(.02,.39,.37,.34),8.0:(0,.38,.37,.34),
8.5:(0,.38,.37,.34),9.0:(0,.38,.34,.35),9.5:(0,.38,.34,.35),11.5:(.03,.38,.36,.36),12.0:(0,.39,.41,.38),
12.5:(0,.39,.42,.38),13.0:(0,.40,.41,.36),13.5:(0,.40,.39,.36),14.0:(0,.39,.39,.38),14.5:(0,.39,.39,.38),15.0:(0,.40,.39,.36)}
W(4045,{"mediaId":4045,"level":"A","keyWord":"find","defaultVoice":"male",
"taps":[{"phrase":"to find his phone","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to look under the table","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to sit on the sofa","target":"the woman","voice":"female","keys":K(Wm)}],
"stillS":10.0,
"nouns":[{"word":"grass","x":.50,"y":.17,"voice":"male"},{"word":"magazines","x":.40,"y":.37,"voice":"male"},
{"word":"keys","x":.42,"y":.55,"voice":"male"},{"word":"a phone","x":.65,"y":.68,"voice":"male"}],
"question":"What is the man looking for?",
"answer":["He","is","looking","for","his","phone."],"answerVoice":"male",
"notes":"Two targets only (man x2, woman x1). The man often stands in front of / next to the woman: boxes are split on a vertical line, so at 0.5 s his outstretched arm and at 4.5 s her legs fall outside their own box. 11.0 s shows only the man's hand taking the phone (box on the hand/arm). Woman is hidden at 1.0-1.5 s. 'to look under the table' = 5.0-6.0 s. The keys pill sits close to the lower magazine."})

# ---------- 4046
M={};Wm={}
for t in T:
    if t<=5.5: M[t]=(0,.07,.54,.93); Wm[t]=(.55,.15,.45,.67)
    elif t<=13.5: M[t]=(0,.07,.51,.93); Wm[t]=(.52,.14,.48,.70)
M[14.0]=(0,.08,.42,.92); Wm[14.0]=(.43,.18,.57,.62)
M[14.5]=(0,.06,.46,.94); Wm[14.5]=(.47,.16,.53,.66)
M[15.0]=(0,.09,.51,.91); Wm[15.0]=(.52,.20,.48,.64)
W(4046,{"mediaId":4046,"level":"B","keyWord":"refuse","defaultVoice":"male",
"taps":[{"phrase":"to raise his index finger","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to burst out laughing","target":"the woman","voice":"female","keys":K(Wm)},
{"phrase":"to grab his arm","target":"the woman","voice":"female","keys":K(Wm)}],
"stillS":6.5,
"nouns":[{"word":"an index finger","x":.40,"y":.46,"voice":"male"},{"word":"a pendant","x":.24,"y":.59,"voice":"male"},
{"word":"a blouse","x":.80,"y":.63,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","raising","his","finger","to","refuse."],"answerVoice":"male",
"notes":"Only two targets (close two-shot). Boxes split on a vertical line; the man's forearm/legs run under the woman at the bottom right and lie in her box. At 14.0-15.0 s they embrace: her hand on his shoulder is inside his box, his fist partly inside hers. 'to grab his arm' is clearest at 13.5-15.0 s (earlier her hand rests at his arm, low in the frame). 'refuse' in the answer is carried by the picture (shaking finger, frown), the spoken 'No' is not needed. Only 3 nouns: the background is blurred candle light."})

# ---------- 4047
M={};Wm={}
for t in [0.0,0.5,1.0,1.5,3.5,4.0]: M[t]=(0,.26,.53,.74); Wm[t]=(.54,.31,.46,.40)
for t in [2.0,2.5,3.0]: M[t]=(0,.23,.53,.77); Wm[t]=(.54,.31,.46,.40)
M[4.5]=(0,.26,.51,.74); Wm[4.5]=(.52,.28,.48,.43)
for t in [5.0,5.5,6.0,6.5,7.0,7.5]: M[t]=(0,.26,.52,.74); Wm[t]=(.53,.32,.47,.42)
M[8.0]=(0,.29,.53,.71); Wm[8.0]=(.54,.33,.46,.42)
M[8.5]=(0,.35,.54,.65); Wm[8.5]=(.55,.31,.45,.42)
M[9.0]=(0,.40,.40,.60); Wm[9.0]=(.41,.40,.59,.45)
M[9.5]=(0,.37,.44,.17); Wm[9.5]=(.20,.55,.80,.32)
for t in [10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5]: M[t]=(0,.33,.45,.15); Wm[t]=(.18,.49,.82,.34)
M[14.0]=(0,.34,.50,.16); Wm[14.0]=(.18,.51,.82,.31)
M[14.5]=(0,.34,.52,.17); Wm[14.5]=(.20,.52,.80,.30)
M[15.0]=(0,.36,.50,.16); Wm[15.0]=(.18,.53,.82,.32)
W(4047,{"mediaId":4047,"level":"A","keyWord":"holiday","defaultVoice":"male",
"taps":[{"phrase":"to hold a phone","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to put on sunglasses","target":"the woman","voice":"female","keys":K(Wm)},
{"phrase":"to lie on his chest","target":"the woman","voice":"female","keys":K(Wm)}],
"stillS":12.0,
"nouns":[{"word":"the sky","x":.35,"y":.18,"voice":"male"},{"word":"the sea","x":.72,"y":.385,"voice":"male"},
{"word":"sunglasses","x":.30,"y":.465,"voice":"male"},{"word":"a phone","x":.58,"y":.70,"voice":"male"}],
"question":"Where are the man and the woman?",
"answer":["They","are","on","holiday","by","the","sea."],"answerVoice":"male",
"notes":"Couple lies overlapping: boxes split on a vertical line. The phone (x .50-.65) lies right of the split in the first half and on top of the woman from 9.0 s, so a tap on the phone itself is not inside the man's box. From 9.5 s the woman lies across the man's chest: the boxes are split horizontally there (man = his head above her hair, woman = hair and white shirt), so his arm and legs are in no box. The man already wears sunglasses the whole clip; only the woman puts hers on (6.0-7.5 s). 'the sea' is a narrow strip of water behind the pool - pill may need a look. 'on holiday' = key word, shown by the resort; mixed couple -> defaultVoice male (evenId false)."})

# ---------- 4048
P={0.0:(.44,.39,.48,.52),0.5:(.40,.37,.44,.58),1.0:(.22,.41,.72,.59),1.5:(.36,.37,.32,.61),2.0:(.32,.30,.34,.37),
2.5:(.22,.23,.48,.62),3.0:(.42,.24,.32,.60),3.5:(.60,.29,.30,.59),4.0:(.65,.31,.28,.43),4.5:(.70,.31,.24,.41),
5.0:(.63,.30,.28,.56),7.0:(.06,.27,.24,.15),7.5:(.06,.35,.24,.15),8.0:(.04,.36,.24,.16),
12.5:(.12,.33,.27,.54),13.0:(.10,.30,.27,.63),13.5:(.08,.30,.29,.63)}
D={5.5:(.20,0,.56,.72),6.0:(.22,0,.52,.73),6.5:(.18,0,.62,.73),9.0:(.07,.33,.53,.27)}
H={11.0:(.17,.22,.83,.56),11.5:(.32,.39,.68,.45),12.0:(.63,.40,.37,.36)}
W(4048,{"mediaId":4048,"level":"B","keyWord":"install","defaultVoice":"male",
"taps":[{"phrase":"to climb into the van","target":"the man in white","voice":"male","keys":K(P)},
{"phrase":"to drive in a screw","target":"the drill","voice":"male","keys":K(D)},
{"phrase":"to wipe the white tiles","target":"the hand","voice":"male","keys":K(H)}],
"stillS":14.5,
"nouns":[{"word":"the sky","x":.40,"y":.10,"voice":"male"},{"word":"the horizon","x":.40,"y":.27,"voice":"male"},
{"word":"solar panels","x":.50,"y":.47,"voice":"male"},{"word":"a van","x":.40,"y":.60,"voice":"male"}],
"question":"What are the two men installing?",
"answer":["They","are","installing","solar","panels."],"answerVoice":"male",
"notes":"Time-lapse with many cuts; every target is off in most shots. 'the man in white' = white T-shirt: 0-5.0 s, small on the roof (left) at 7.0-8.0 s, front left in the group at 12.5-13.5 s; the tiny seated figure at 14-15 s is left off (not identifiable). 'the hand' = hand with the blue cloth and its arm, 11.0-12.0 s only; the hands holding the drill at 9.0 s are not boxed. Drill: 5.5-6.5 s and the yellow drill at the porthole at 9.0 s. Question refers to the roof shot 7.0-8.0 s; 'solar panels' is a noun on the still (panels on the van roof, small). Solar-panels and van pills are 0.13 apart in y."})
