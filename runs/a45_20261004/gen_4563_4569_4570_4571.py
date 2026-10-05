import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def write(c):
    json.dump(c,open(f"content/{c['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4563
W={0.0:(0,.63,.65,.28),0.5:(0,.63,.65,.28),1.0:(0,.63,.65,.28),1.5:(0,.62,.68,.27),
   2.0:(0,0,.54,.72),2.5:(0,0,.34,.76),3.0:(0,.05,.34,.75),3.5:(0,.07,.38,.73),
   4.0:(0,.08,.34,.70),4.5:(0,.08,.33,.70),5.0:(0,.09,.27,.76),5.5:(0,.09,.27,.75),
   6.0:(0,.08,.30,.72),6.5:(0,.08,.30,.70),7.0:(0,.08,.28,.72),7.5:(0,.08,.28,.72),
   8.0:(0,.20,.30,.72),8.5:(0,.20,.30,.72),9.0:(0,.22,.30,.70),9.5:(0,.22,.30,.70),
   10.0:(0,.21,.30,.71),10.5:(0,.23,.40,.67)}
C={0.0:(0,0,1,.25),0.5:(0,0,1,.25),1.0:(0,0,1,.22),1.5:(0,0,1,.14),
   2.0:(.56,0,.44,.30),2.5:(.35,0,.33,.28),3.0:(.35,.05,.40,.29),3.5:(.39,.05,.55,.32),
   4.0:(.35,.02,.65,.34),4.5:(.34,.02,.66,.36),5.0:(.28,.02,.72,.42),5.5:(.28,.02,.72,.41),
   6.0:(.31,.02,.69,.34),6.5:(.31,.02,.69,.36),7.0:(.29,.02,.71,.38),7.5:(.29,.02,.71,.38),
   8.0:(.31,.43,.18,.19),8.5:(.31,.43,.18,.19),9.0:(.31,.44,.18,.20),9.5:(.31,.44,.18,.20),
   10.0:(.31,.41,.18,.20)}
F={8.0:(.36,.02,.24,.40),8.5:(.36,.02,.24,.40),9.0:(.36,.03,.24,.40),9.5:(.36,.03,.24,.40),
   10.0:(.36,.04,.22,.36),10.5:(.40,.04,.20,.30),11.0:(.38,.04,.24,.34),11.5:(.38,.04,.24,.34),
   12.0:(.36,.03,.26,.35)}
write({"mediaId":4563,"level":"B","keyWord":"law","defaultVoice":"female",
 "taps":[{"phrase":"to leaf through the pages","target":"the woman","voice":"female","keys":keys(W)},
         {"phrase":"to pack the entire hall","target":"the crowd","voice":"female","keys":keys(C)},
         {"phrase":"to hang from a flagpole","target":"the flag","voice":"female","keys":keys(F)}],
 "stillS":9.5,
 "nouns":[{"word":"a flag","x":.47,"y":.28,"voice":"female"},
          {"word":"an emblem","x":.66,"y":.46,"voice":"female"},
          {"word":"a wax seal","x":.62,"y":.83,"voice":"female"},
          {"word":"a blazer","x":.20,"y":.66,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","leafing","through","a","huge","law","book."],
 "answerVoice":"female",
 "notes":"Key word 'law' is not a visible noun; it is used in the answer ('law book': the book is taken as a law book from the key word/description, the picture only shows a ceremonial handwritten book). Woman and crowd overlap in the picture from 2.5 s on: the woman's box is cut to head+torso, her outstretched gloved hand lies outside. 0.0-1.5 s only her gloved hand and sleeve are visible (boxed). In the last shot (8.0-10.0 s) the crowd is only a small group between her and the book (small box right of her face). Crowd at 10.5 s almost hidden behind her -> off. Flag: only a red tip at the top edge in 3.0-7.5 s -> off there, boxed from 8.0 s. Crowd mouths are open (singing per description), so the crowd phrase avoids 'gasp'/'sing'."})

# ---------- 4569
M={0.0:(0,.02,.44,.98),0.5:(0,.02,.44,.98),1.0:(0,.02,.44,.98),1.5:(0,.02,.42,.98),
   2.0:(0,.02,.44,.98),2.5:(0,.02,.44,.98),3.0:(0,.07,.40,.93),3.5:(0,.07,.40,.93),
   4.0:(0,.07,.51,.93),4.5:(0,.07,.51,.93),5.0:(0,.08,.40,.92),5.5:(0,.07,.49,.93),
   6.0:(0,.04,.49,.96),6.5:(0,.04,.49,.96),7.0:(0,.04,.46,.96),7.5:(0,.04,.49,.96),
   8.0:(0,.02,.48,.98),8.5:(0,.02,.49,.98),9.0:(0,.07,.56,.93),9.5:(0,.07,.50,.93),
   10.0:(0,.06,.45,.94),10.5:(0,.04,.45,.96),11.0:(0,.06,.44,.94),11.5:(0,.08,.43,.92),
   12.0:(0,.08,.34,.92)}
S={0.0:(.45,.33,.42,.24),0.5:(.45,.33,.42,.24),1.0:(.45,.36,.42,.23),1.5:(.44,.35,.43,.25),
   2.0:(.45,.33,.42,.24),2.5:(.45,.32,.42,.24),3.0:(.41,.33,.46,.15),3.5:(.41,.33,.47,.14),
   4.0:(.52,.34,.34,.14),4.5:(.52,.32,.34,.14),5.0:(.41,.33,.45,.15),5.5:(.50,.33,.37,.18),
   6.0:(.50,.31,.33,.15),6.5:(.50,.29,.36,.20),7.0:(.47,.31,.35,.20),7.5:(.50,.30,.36,.20),
   8.0:(.49,.29,.32,.21),8.5:(.50,.29,.36,.20),9.0:(.57,.38,.19,.17),9.5:(.51,.40,.29,.20),
   10.0:(.50,.36,.28,.20),10.5:(.50,.35,.28,.20),11.0:(.45,.37,.33,.25),11.5:(.44,.35,.36,.27),
   12.0:(.35,.34,.44,.26)}
P={0.0:(.48,.65,.47,.19),0.5:(.48,.65,.47,.19),1.0:(.46,.60,.46,.25),1.5:(.44,.65,.46,.19),
   2.0:(.47,.64,.45,.20),2.5:(.47,.63,.50,.20),3.0:(.45,.69,.47,.17),3.5:(.47,.69,.45,.17),
   4.0:(.52,.69,.40,.16),4.5:(.52,.69,.40,.16),5.0:(.45,.69,.45,.17),5.5:(.50,.67,.38,.17),
   6.0:(.50,.68,.36,.14),6.5:(.50,.68,.34,.14),7.0:(.47,.69,.34,.14),7.5:(.50,.68,.34,.14),
   8.0:(.49,.68,.33,.14),8.5:(.50,.68,.34,.14),9.0:(.58,.56,.24,.14),9.5:(.51,.64,.24,.15),
   10.0:(.46,.68,.26,.14),10.5:(.46,.68,.27,.14),11.0:(.45,.82,.27,.14),11.5:(.44,.82,.30,.14),
   12.0:(.44,.67,.28,.14)}
write({"mediaId":4569,"level":"A","keyWord":"to fry","defaultVoice":"male",
 "taps":[{"phrase":"to fry some fish","target":"the man","voice":"male","keys":keys(M)},
         {"phrase":"to be red and yellow","target":"the peppers","voice":"male","keys":keys(P)},
         {"phrase":"to have white waves","target":"the sea","voice":"male","keys":keys(S)}],
 "stillS":12.0,
 "nouns":[{"word":"a man","x":.17,"y":.48,"voice":"male"},
          {"word":"the sky","x":.55,"y":.20,"voice":"male"},
          {"word":"the sea","x":.58,"y":.42,"voice":"male"},
          {"word":"a plate","x":.55,"y":.76,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","frying","fish","in","a","pan."],
 "answerVoice":"male",
 "notes":"Only one person; the peppers and the sea are things, so two phrases are states. Peppers box = the pepper strips in the pan (0-8.5 s) and on the plate (9.0-12.0 s); small from 6.0 s where the fish lies over them. The man's hand reaches into the pan / holds the plate, his box is cut at the split line. The sea box is the part of the sea right of the man. There are also some green pepper strips, red and yellow dominate."})

# ---------- 4570
B={0.0:(0,0,.52,.82),0.5:(0,0,.52,.82),1.0:(0,0,.56,.84),1.5:(0,0,.61,.84),2.0:(0,0,.61,.82),2.5:(0,0,.63,.82)}
Wm={3.0:(.06,.03,.66,.80),3.5:(.08,.03,.66,.80),4.0:(.08,.03,.66,.66),4.5:(.10,.04,.67,.60),
    5.0:(.18,.08,.60,.68),5.5:(.50,.22,.38,.50),6.0:(.20,.15,.62,.52),6.5:(.18,.17,.60,.52)}
Ch={7.0:(0,0,1,.58),7.5:(0,0,1,.58),8.0:(0,0,1,.60),8.5:(0,0,1,.59),9.0:(0,0,1,.61),9.5:(0,0,1,.63),
    10.0:(0,0,1,.60),10.5:(.05,0,.95,.71),11.0:(0,.04,1,.70),11.5:(0,.04,1,.86),12.0:(0,0,.88,.92)}
write({"mediaId":4570,"level":"A","keyWord":"chef","defaultVoice":"female",
 "taps":[{"phrase":"to cook by the sea","target":"the man with the beard","voice":"male","keys":keys(B)},
         {"phrase":"to laugh behind the fire","target":"the woman","voice":"female","keys":keys(Wm)},
         {"phrase":"to wear a white jacket","target":"the man in white","voice":"male","keys":keys(Ch)}],
 "stillS":11.5,
 "nouns":[{"word":"a chef","x":.50,"y":.45,"voice":"male"},
          {"word":"a plate","x":.50,"y":.90,"voice":"female"},
          {"word":"a knife","x":.84,"y":.73,"voice":"female"}],
 "question":"Where is the woman cooking?",
 "answer":["She","is","cooking","on","the","street."],
 "answerVoice":"female",
 "notes":"Three shots, one cook each: 0-2.5 s man with the beard, 3.0-6.5 s woman, 7.0-12.0 s man in white (7.0-9.5 s only his jacket and hands). Third phrase is a state (white jacket) because cooking fits all three. At 5.5 s the woman is almost hidden by the flame (box on her visible body). People walking in the street behind the woman are not targets. defaultVoice female by evenId (mixed group)."})

# ---------- 4571
Bo={0.0:(0,0,1,.27),0.5:(0,0,1,.27),1.0:(0,0,1,.27),1.5:(0,0,1,.27),2.0:(0,0,1,.26),2.5:(0,0,1,.25),
    3.0:(0,0,1,.29),3.5:(.05,0,.95,.23),4.0:(0,0,1,.23),4.5:(.05,0,.95,.24),5.0:(0,0,1,.30),
    5.5:(.20,0,.78,.19),6.0:(.12,0,.86,.16),6.5:(.12,0,.86,.21),7.0:(.05,0,.95,.36),7.5:(0,0,1,.37),
    8.0:(0,0,1,.37),8.5:(0,0,1,.39),9.0:(0,0,1,.43),9.5:(0,0,1,.44),10.0:(0,0,.74,.56),
    10.5:(0,.02,.75,.35),11.0:(0,.08,.33,.46),11.5:(0,.07,.19,.26)}
Pe={0.0:(0,.28,1,.72),0.5:(0,.28,1,.72),1.0:(0,.28,1,.72),1.5:(0,.28,1,.72),2.0:(0,.27,1,.73),2.5:(0,.26,1,.74),
    3.0:(0,.30,1,.70),3.5:(0,.24,1,.72),4.0:(0,.24,1,.66),4.5:(0,.25,1,.72),5.0:(0,.31,1,.69),
    5.5:(.12,.20,.88,.80),6.0:(.08,.17,.92,.83),6.5:(.08,.22,.92,.78),7.0:(.04,.37,.92,.27),7.5:(0,.38,.92,.27),
    8.0:(0,.38,.90,.32),8.5:(0,.40,.80,.32),9.0:(0,.44,.34,.26),9.5:(.02,.45,.30,.25),10.0:(.75,.42,.25,.40),
    10.5:(.55,.38,.45,.46),11.0:(.34,.34,.66,.50),11.5:(.18,.36,.82,.45),12.0:(.05,.33,.92,.47)}
Se={8.5:(.81,.47,.19,.33),9.0:(.62,.60,.38,.16),9.5:(.34,.58,.66,.15),10.0:(.75,.26,.25,.15),
    10.5:(.76,.10,.24,.27),11.0:(.34,.09,.66,.24),11.5:(.20,.09,.80,.26),12.0:(0,.09,1,.23)}
write({"mediaId":4571,"level":"A","keyWord":"push","defaultVoice":"male",
 "taps":[{"phrase":"to push a big boat","target":"the people","voice":"male","keys":keys(Pe)},
         {"phrase":"to go into the water","target":"the boat","voice":"male","keys":keys(Bo)},
         {"phrase":"to shine in the sun","target":"the sea","voice":"male","keys":keys(Se)}],
 "stillS":11.0,
 "nouns":[{"word":"a boat","x":.15,"y":.25,"voice":"male"},
          {"word":"the sea","x":.68,"y":.22,"voice":"male"},
          {"word":"people","x":.65,"y":.50,"voice":"male"},
          {"word":"sand","x":.50,"y":.90,"voice":"male"}],
 "question":"What are the people doing?",
 "answer":["They","are","pushing","a","big","boat."],
 "answerVoice":"male",
 "notes":"The old man with the whistle stands inside the crowd in the picture, so he is not a separate target: 'the people' box holds the whole group including him. Boat and people overlap in the pushing shots (3.5-5.0, 7.0-9.5 s): boat box = hull above the heads, people box below. The sea is visible only from 8.5 s (off before); it shines clearly from 10.5 s. At the end the people stand at the water's edge; 'to go into the water' is meant for the boat (splash at 9.5-10.0 s). Boat at 12.0 s out of frame -> off. defaultVoice male by evenId (mixed group)."})
