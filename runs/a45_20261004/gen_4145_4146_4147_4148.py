import json
def mk(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def save(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1,ensure_ascii=False)
T24=[i*0.5 for i in range(24)]; T20=[i*0.5 for i in range(20)]; T25=[i*0.5 for i in range(25)]

# ---- 4145
W={0.0:(.80,.42,.20,.15),0.5:(.80,.54,.20,.15),1.0:(.76,.61,.22,.14),1.5:(.63,.73,.26,.18),2.0:(.53,.73,.32,.20),
2.5:(.35,.55,.60,.25),3.0:(.22,.60,.70,.25),3.5:(.20,.48,.67,.20),4.0:(.18,.46,.58,.19),4.5:(.18,.40,.66,.22),
9.5:(.48,.45,.26,.14),10.0:(.44,.37,.34,.21),10.5:(.46,.24,.43,.38),11.0:(.41,.28,.43,.37),11.5:(.33,.28,.43,.37)}
F={0.0:(0,.32,.38,.68),0.5:(.15,.30,.40,.70),1.0:(.16,.27,.42,.73),1.5:(0,.73,.40,.27),
6.5:(0,.78,.43,.22),7.0:(.15,.40,.64,.60),7.5:(.10,.39,.82,.55),8.0:(.06,.36,.80,.46),8.5:(.09,.45,.85,.31),9.0:(.11,.51,.80,.49),
9.5:(0,.70,.95,.30),10.0:(0,.75,.62,.25),10.5:(0,.82,.41,.18),11.0:(0,.74,.40,.26),11.5:(0,.70,.34,.30)}
save({"mediaId":4145,"level":"B","keyWord":"dive","defaultVoice":"male",
"taps":[{"phrase":"to dive for the ball","target":"the blond man","voice":"male","keys":mk(T24,W)},
{"phrase":"to attempt an overhead kick","target":"the dark-haired man","voice":"male","keys":mk(T24,F)},
{"phrase":"to celebrate with raised fists","target":"the blond man","voice":"male","keys":mk(T24,W)}],
"stillS":4.5,
"nouns":[{"word":"the sky","x":.60,"y":.08,"voice":"male"},{"word":"a volleyball","x":.33,"y":.22,"voice":"male"},
{"word":"a sailing boat","x":.78,"y":.36,"voice":"male"},{"word":"a splash","x":.50,"y":.52,"voice":"male"}],
"question":"What is the blond man doing?","answer":["He","is","diving","for","the","ball."],"answerVoice":"male",
"notes":"The packet description says one man does everything; the frames show two: the blond man in the sea dives (2.0-4.5) and raises his fists (10.5-11.5), the dark-haired man in the foreground serves (0-1.0) and does the overhead kick (6.5-9.0). Blond man off 5.0-6.0 (hidden in the splash) and 6.5-9.0 (other shot). At 4.5 only a bit of him shows inside the splash. Blond hair is clear only in the close frames (10.5-11.5)."})

# ---- 4146
M={0.0:(0,.08,1,.92),0.5:(0,.08,1,.92),1.0:(0,.08,1,.92),1.5:(0,.08,1,.92),2.0:(0,.02,1,.98),2.5:(0,0,1,1),3.0:(.14,0,.86,1),3.5:(0,.14,1,.86),
4.0:(.18,.41,.58,.59),4.5:(.32,.43,.36,.23),5.0:(.28,.43,.44,.23),5.5:(.25,.43,.50,.28),6.0:(.25,.43,.50,.31),6.5:(.18,.43,.60,.33),
7.0:(.25,.44,.50,.48),7.5:(.28,.46,.44,.50),8.0:(.15,.51,.65,.36),8.5:(.25,.56,.50,.40),9.0:(.25,.79,.52,.21),9.5:(.15,.86,.75,.14)}
k=mk(T20,M)
save({"mediaId":4146,"level":"B","keyWord":"exhausted","defaultVoice":"male",
"taps":[{"phrase":"to pull off his sweatshirt","target":"the man","voice":"male","keys":k},
{"phrase":"to collapse into the waves","target":"the man","voice":"male","keys":k},
{"phrase":"to lie motionless in the foam","target":"the man","voice":"male","keys":k}],
"stillS":6.0,
"nouns":[{"word":"the sky","x":.50,"y":.10,"voice":"male"},{"word":"foam","x":.84,"y":.57,"voice":"male"},
{"word":"trainers","x":.50,"y":.66,"voice":"male"},{"word":"sand","x":.30,"y":.88,"voice":"male"}],
"question":"What is the man doing?","answer":["The","exhausted","man","is","lying","in","the","foam."],"answerVoice":"male",
"notes":"Only one target (the man) for all three phrases: the sunset strip and the waves cannot be boxed apart from him. 'exhausted' in the answer is the key word, read from the way he drops and stays down. Foam lies all around him; the pill sits on the thick patch on the right."})

# ---- 4147
M={0.0:(.08,.13,.56,.66),0.5:(.18,.18,.48,.66),1.0:(.08,.18,.46,.56),2.0:(.26,.31,.45,.41),2.5:(.11,.24,.65,.48),3.0:(.18,.18,.48,.72),3.5:(.26,.21,.50,.74),
4.0:(.32,.26,.37,.50),4.5:(.29,.28,.33,.40),5.0:(.38,.13,.44,.52),5.5:(.34,.14,.62,.84),6.0:(.11,.18,.82,.82),6.5:(0,.22,.70,.78),
8.5:(.24,.26,.72,.32),9.0:(0,.14,.80,.52),9.5:(.20,.10,.80,.60),10.0:(.08,.10,.92,.58),10.5:(.16,.10,.84,.52),11.0:(0,.21,.55,.48)}
k=mk(T24,M)
save({"mediaId":4147,"level":"A","keyWord":"hurry","defaultVoice":"male",
"taps":[{"phrase":"to hurry to the car","target":"the man","voice":"male","keys":k},
{"phrase":"to carry a big sign","target":"the man","voice":"male","keys":k},
{"phrase":"to laugh in the car","target":"the man","voice":"male","keys":k}],
"stillS":5.0,
"nouns":[{"word":"a sign","x":.62,"y":.10,"voice":"male"},{"word":"a man","x":.62,"y":.37,"voice":"male"},{"word":"a car","x":.15,"y":.42,"voice":"male"}],
"question":"What is the man carrying?","answer":["He","is","carrying","a","big","yellow","sign."],"answerVoice":"male",
"notes":"One target (the man) for all three phrases: he carries the sign pressed against his body, so man and sign cannot get separate boxes. Man off at 1.5 (only a faint figure behind the sign), 7.0-8.0 (blurred shots of the sign; the face at 7.0 may be another person in the car) and 11.5 (road). At 8.5 he is a dark shape seen from behind; at 11.0 the picture is blurred and a second blurred shape with red lights is on the right. Only 3 nouns: nothing else is clear at one place."})

# ---- 4148
M={0.0:(0,0,.50,.56),0.5:(0,0,.47,.63),1.0:(0,0,.40,.79),1.5:(0,0,.35,.70),2.0:(0,0,.48,.60),2.5:(0,0,.67,.47),
3.0:(0,.20,.60,.74),3.5:(0,.24,1,.56),4.0:(0,.22,1,.60),4.5:(.68,.50,.32,.50),5.0:(.66,.50,.34,.50),5.5:(.68,.50,.32,.50),6.0:(.66,.54,.34,.46)}
C={0.0:(.50,.28,.50,.72),0.5:(.47,.28,.53,.72),1.0:(.40,.32,.60,.68),1.5:(.35,.32,.65,.68),2.0:(.48,.33,.52,.67),2.5:(0,.47,1,.53),
3.0:(.60,.10,.40,.90),3.5:(0,.80,1,.20),4.0:(0,.82,1,.18),4.5:(0,0,.68,1),5.0:(0,0,.66,1),5.5:(0,0,.68,1),6.0:(0,0,.66,1),
6.5:(.06,.36,.94,.31),7.0:(.11,.36,.83,.30),7.5:(.19,.38,.72,.28),8.0:(.28,.40,.66,.24),8.5:(.29,.42,.63,.23),9.0:(.26,.45,.61,.20),
9.5:(.46,.45,.54,.21),10.0:(.25,.44,.75,.23),10.5:(.13,.44,.87,.23),11.0:(.08,.45,.89,.22),11.5:(.07,.45,.90,.22),12.0:(.07,.44,.90,.23)}
km=mk(T25,M)
save({"mediaId":4148,"level":"B","keyWord":"luxury","defaultVoice":"male",
"taps":[{"phrase":"to stroke the bonnet","target":"the man","voice":"male","keys":km},
{"phrase":"to press the start button","target":"the man","voice":"male","keys":km},
{"phrase":"to emerge from the garage","target":"the red car","voice":"male","keys":mk(T25,C)}],
"stillS":4.0,
"nouns":[{"word":"a steering wheel","x":.22,"y":.42,"voice":"male"},{"word":"a suit","x":.72,"y":.50,"voice":"male"},{"word":"a seat","x":.78,"y":.72,"voice":"male"}],
"question":"What is the man pressing?","answer":["He","is","pressing","the","start","button."],"answerVoice":"male",
"notes":"Man and car overlap in 0-6.0, so the boxes are split along the line between them: 0-2.0 the man's arm on the left, the car on the right; 2.5 man above, car below; 3.0 the car is only the right part (seat, door); 3.5-4.0 the car is only the strip below the man (seat base, sill); 4.5-6.0 the man is his hand on the right, the car is the steering wheel and dials on the left (the start button lies under his finger, in the man's box). Key word 'luxury' is abstract, so it is not a noun here. Only 3 nouns."})
