import json
def keys(n, d):
    out=[]
    for i in range(n):
        t=i*0.5; b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def w(d): json.dump(d,open("content/%d.json"%d["mediaId"],"w"),indent=1)

# ---------- 4249
hy={0:.78,.5:.79,1:.82,1.5:.82,2:.82,2.5:.86,3:.82,3.5:.84,4:.82,4.5:.80,5:.82,5.5:.82,6:.82,6.5:.82,7:.80,7.5:.78,8:.73,8.5:.81,9:.84,9.5:.82,10:.80,10.5:.73,11:.76,11.5:.80}
dx={0:(.20,.37),.5:(.25,.36),1:(0,.45),1.5:(0,.43),2:(.35,.42),2.5:(0,.52),3:(0,.63),3.5:(0,.68),4:(0,.53),4.5:(0,.50),5:(0,.51),5.5:(0,.50),6:(0,.47),6.5:(0,.48),7:(0,.50),7.5:(0,.50),8:(0,.38),8.5:(0,.33),9:(0,.37),9.5:(0,.33),10:(0,.33),10.5:(0,.40),11:(0,.48),11.5:(0,.50)}
hands={t:(0,y,1,round(1-y,2)) for t,y in hy.items()}
dragon={t:(x,y,round(1-x,2),round(hy[t]-.01-y,2)) for t,(x,y) in dx.items()}
wf={0:(0,.36,.19,.18),.5:(.03,.33,.21,.17),1:(.14,.29,.24,.15),1.5:(.20,.27,.22,.15),2:(.14,.34,.20,.15),2.5:(.16,0,.24,.14),
 4:(0,0,.22,.14),4.5:(0,0,.25,.16),5:(0,.02,.23,.22),5.5:(.07,.05,.28,.24),6:(.15,.04,.38,.30),6.5:(.33,.08,.42,.34),7:(.33,.04,.56,.44),7.5:(.24,0,.76,.49)}
w({"mediaId":4249,"level":"A","keyWord":"back","defaultVoice":"male",
"taps":[{"phrase":"to breathe fire","target":"the dragon","voice":"male","keys":keys(24,dragon)},
{"phrase":"to hold on tight","target":"the hands","voice":"male","keys":keys(24,hands)},
{"phrase":"to fall into the lake","target":"the waterfall","voice":"male","keys":keys(24,wf)}],
"stillS":11.0,
"nouns":[{"word":"the sun","x":.5,"y":.33,"voice":"male"},{"word":"a lake","x":.25,"y":.46,"voice":"male"},
{"word":"a back","x":.5,"y":.68,"voice":"male"},{"word":"hands","x":.27,"y":.82,"voice":"male"}],
"question":"What is the dragon doing?","answer":["It","is","flying","over","a","lake."],"answerVoice":"male",
"notes":"First-person ride: only the rider's two hands are seen, so target 2 is 'the hands' (they grip the saddle handle). Dragon box and hands box are split at the top of the hands; the dragon box is full width except at 0-0.5 s and 2.0 s where it starts right of the far waterfall, and at 1.0/1.5 s it starts below the waterfall (horn tips cut). Waterfall: small and far at 0-2 s, off at 3.0-3.5 s (only white streaks on the lake) and from 8.0 s (mist, then sunset). Key word 'back' as the pill 'a back' on the dragon's back; no 'a dragon' pill so the two do not compete. 'hands' pill sits on the left hand."})

# ---------- 4250
C={0:(0,.35,.74,.65),.5:(0,.33,.79,.67),1:(0,.34,.74,.66),1.5:(0,.34,.75,.66),2:(0,.34,.73,.66),2.5:(0,.34,.75,.66),3:(0,.35,.76,.65),3.5:(0,.35,.76,.65),
4:(0,.34,.77,.66),4.5:(0,.34,.77,.66),5:(0,.36,.80,.64),5.5:(0,.36,.80,.64),6:(0,.37,.75,.63),6.5:(0,.40,.68,.60),7:(0,.38,.62,.62),7.5:(0,.35,.64,.65),
8:(0,.37,.66,.63),8.5:(0,.37,.67,.63),9:(0,.37,.64,.63),9.5:(0,.39,.67,.61),10:(0,.40,.62,.60),10.5:(0,.34,.52,.66),11:(0,.35,.53,.65),11.5:(0,.36,.55,.64)}
R={0:(.27,.16,.26,.18),.5:(.28,.16,.26,.16),1:(.27,.16,.26,.17),1.5:(.27,.16,.26,.17),2:(.27,.16,.26,.17),2.5:(.28,.17,.26,.16),3:(.29,.18,.26,.16),3.5:(.30,.19,.26,.15),
4:(.32,.19,.26,.14),4.5:(.33,.19,.26,.14),5:(.34,.21,.26,.14),5.5:(.35,.21,.26,.14),6:(.36,.22,.26,.14),6.5:(.31,.25,.26,.14),7:(.31,.23,.26,.14),7.5:(.32,.20,.26,.14),
8:(.33,.20,.26,.14),8.5:(.34,.19,.26,.14),9:(.38,.23,.28,.13),9.5:(.43,.24,.29,.14),10:(.48,.24,.26,.15),10.5:(.53,.25,.26,.17),11:(.54,.26,.25,.17),11.5:(.56,.26,.25,.18)}
S={0:(.76,.50,.20,.17),.5:(.80,.50,.19,.17),1:(.77,.50,.20,.18),1.5:(.77,.50,.20,.18),2:(.76,.50,.20,.17),2.5:(.77,.50,.20,.17),3:(.78,.50,.20,.18),3.5:(.78,.50,.20,.18),
4:(.79,.49,.20,.17),4.5:(.79,.49,.20,.17),5:(.81,.49,.19,.17),5.5:(.81,.49,.19,.17),6:(.76,.48,.19,.16),6.5:(.69,.50,.18,.15),7:(.69,.48,.18,.15),7.5:(.72,.46,.18,.16),
8:(.74,.45,.18,.15),8.5:(.75,.45,.18,.15),9:(.75,.46,.18,.15),9.5:(.75,.46,.18,.15),10:(.75,.46,.18,.15),10.5:(.76,.46,.18,.15),11:(.76,.47,.18,.15),11.5:(.76,.47,.18,.15)}
w({"mediaId":4250,"level":"B","keyWord":"warehouse","defaultVoice":"female",
"taps":[{"phrase":"to operate a forklift","target":"the golden retriever","voice":"female","keys":keys(24,R)},
{"phrase":"to stare into the camera","target":"the dog in front","voice":"female","keys":keys(24,C)},
{"phrase":"to signal with its paw","target":"the small dog at the back","voice":"female","keys":keys(24,S)}],
"stillS":2.0,
"nouns":[{"word":"a warehouse","x":.70,"y":.07,"voice":"female"},{"word":"a forklift","x":.30,"y":.17,"voice":"female"},
{"word":"a hard hat","x":.22,"y":.41,"voice":"female"},{"word":"a vest","x":.40,"y":.86,"voice":"female"}],
"question":"What is the golden retriever doing?","answer":["It","is","operating","a","forklift","in","a","warehouse."],"answerVoice":"female",
"notes":"Three dogs, no people: defaultVoice from evenId. Retriever box is the dog in the forklift seat (it climbs out onto the spilled bottles from 9.0 s); its box ends just above the front dog's hard hat, and at 10.5-11.5 s the front dog's box is cut on the right (vest shoulder) so it does not overlap the retriever. 'to stare into the camera' is true at 0 s and 10.5-11.5 s; in between the front dog looks sideways. 'to signal with its paw': the far dog raises a paw towards the forklift at about 4-6.5 s - weakest phrase. Key word pill 'a warehouse' is placed on the racking/roof at the top right, as the place itself has no single spot."})

# ---------- 4251
W={0:(.15,.19,.68,.81),.5:(.34,.24,.66,.76),1:(.60,.46,.40,.24),1.5:(0,.21,1,.79),2:(0,.21,.63,.79),2.5:(0,.22,.64,.78),3:(0,.23,.50,.77),3.5:(0,.55,.42,.20),
9.5:(0,.23,.44,.77),10:(0,.17,.67,.83),11.5:(0,.34,.26,.62)}
M={2:(.65,.04,.35,.96),2.5:(.66,.04,.34,.96),3:(.51,.09,.49,.91),3.5:(.43,.53,.57,.24),6:(.33,.31,.33,.36),6.5:(.30,.29,.40,.47),7:(.26,.26,.50,.74),7.5:(.31,.23,.51,.77),
8:(.26,.16,.60,.84),8.5:(.08,.09,.92,.91),9:(.09,.11,.88,.89),10.5:(0,0,1,1),11:(0,0,1,1),11.5:(.27,0,.73,1)}
w({"mediaId":4251,"level":"B","keyWord":"space","defaultVoice":"female",
"taps":[{"phrase":"to point at bare shelves","target":"the woman","voice":"female","keys":keys(24,W)},
{"phrase":"to grin at the man","target":"the woman","voice":"female","keys":keys(24,W)},
{"phrase":"to stare in disbelief","target":"the man","voice":"male","keys":keys(24,M)}],
"stillS":10.0,
"nouns":[{"word":"a shelf","x":.35,"y":.14,"voice":"female"},{"word":"a bun","x":.16,"y":.25,"voice":"female"},
{"word":"socks","x":.65,"y":.49,"voice":"female"},{"word":"sweaters","x":.52,"y":.87,"voice":"female"}],
"question":"What is the woman pointing at?","answer":["She","is","pointing","at","the","bare","shelves."],"answerVoice":"female",
"notes":"The clip shows a woman as well as the man (the packet description mentions only the man): she points along bare shelves (0.5-1.0 s), they shake hands (3.0-3.5 s), cut to the full wardrobe (4.0-5.5 s, nobody visible, both off), the man stands in the heap of clothes (6-9 s), she points at one shelf with a pair of socks (9.5-10 s), his shocked face (10.5-11.5 s). Only two clean targets, so the woman has two phrases; the heap of clothes was not used as a target because the man stands in the middle of it and the boxes cannot be separated. Key word 'space' is abstract: not used as a pill, nor in the answer. At 1.0 and 3.5 s only arms are visible; at 3.0-3.5 s the boxes are split at the handshake. 'sweaters' pill is on the lower stack; another stack lies at the top edge above the 'a shelf' pill."})

# ---------- 4252
U={0:(0,.13,1,.87),.5:(0,.13,1,.87),1:(0,.18,.91,.82),1.5:(0,.39,.80,.61),2:(0,.38,.63,.44),2.5:(0,.42,.45,.36),3:(0,.44,.40,.32),3.5:(0,.44,.33,.28),
4:(0,.42,.29,.24),4.5:(0,.42,.29,.24),5:(0,.43,.25,.23),5.5:(0,.43,.24,.22),6:(0,.42,.21,.22),6.5:(0,.42,.21,.22),7:(0,.43,.24,.23),7.5:(0,.42,.24,.23)}
B={2.5:(.82,.06,.18,.32),3:(.76,.09,.24,.34),3.5:(.71,.11,.29,.32),4:(.70,.13,.30,.30),4.5:(.70,.14,.30,.30),5:(.71,.16,.29,.31),5.5:(.71,.17,.29,.31),
6:(.73,.18,.27,.30),6.5:(.74,.18,.26,.30),7:(.73,.18,.27,.30),7.5:(.72,.18,.28,.31)}
F={1.5:(.82,.55,.18,.45),2:(.64,.36,.36,.64),2.5:(.46,.50,.54,.50),3:(.42,.58,.58,.42),3.5:(.36,.55,.64,.45),4:(.30,.50,.70,.50),4.5:(.30,.52,.70,.48),
5:(.26,.54,.74,.46),5.5:(.25,.53,.75,.47),6:(.22,.51,.78,.47),6.5:(.22,.51,.78,.47),7:(.25,.52,.75,.46),7.5:(.25,.52,.75,.46)}
w({"mediaId":4252,"level":"B","keyWord":"concrete","defaultVoice":"male",
"taps":[{"phrase":"to sip an orange drink","target":"the man in sunglasses","voice":"male","keys":keys(16,U)},
{"phrase":"to scrub with a brush","target":"the man in white","voice":"male","keys":keys(16,B)},
{"phrase":"to spread across the concrete","target":"the foam","voice":"male","keys":keys(16,F)}],
"stillS":6.0,
"nouns":[{"word":"a pool","x":.20,"y":.30,"voice":"male"},{"word":"a rug","x":.50,"y":.45,"voice":"male"},
{"word":"foam","x":.72,"y":.58,"voice":"male"},{"word":"concrete","x":.72,"y":.87,"voice":"male"}],
"question":"What is spreading across the concrete?","answer":["Soapy","foam","is","spreading","across","the","concrete."],"answerVoice":"male",
"notes":"The man in white only enters at 2.5 s (off before). 'to scrub with a brush' rather than naming what he scrubs: his brush is on the concrete next to the rug at 3-5 s and on the rug's edge from 5.5 s. Foam box = the main area of suds to the right of / below the lying man; foam left of it under his rug's corner and the thin foam round the far rug are outside the box; foam is off at 0-1.0 s (not in the picture). 'a rug' pill is on the far rug in the middle; a second rug lies under the man at the left edge (no pill there)."})
