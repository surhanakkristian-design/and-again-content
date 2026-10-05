import json
def keys(d, times):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":round(v[2],2),"h":round(v[3],2)})
    return out
T25=[i*0.5 for i in range(25)]; T19=[i*0.5 for i in range(19)]

# ---------- 4276
W={0.0:(0,.29,.57,.71),0.5:(0,.29,.57,.71),1.0:(0,.29,.54,.71),1.5:(0,.29,.57,.71),2.0:(0,.29,.57,.71),2.5:(0,.29,.57,.71),
3.0:(.30,.53,.29,.42),3.5:(.30,.52,.28,.43),4.0:(.31,.38,.28,.47),4.5:(.30,.37,.29,.49),5.0:(.30,.36,.30,.64),5.5:(.26,.35,.35,.65),
6.0:(.28,.34,.36,.58),6.5:(.27,.33,.42,.60),7.0:(.37,.34,.33,.66),7.5:(.35,.35,.36,.65),8.0:(.38,.34,.33,.58),8.5:(.38,.34,.35,.55),
9.0:(.35,.33,.35,.62),9.5:(.35,.31,.35,.63),10.0:(.34,.30,.34,.52),10.5:(.31,.30,.32,.52),11.0:(.30,.30,.33,.64),11.5:(.30,.30,.33,.64),12.0:(.29,.29,.35,.53)}
M={0.0:(.58,.10,.42,.90),0.5:(.58,.10,.42,.90),1.0:(.55,.10,.45,.90),1.5:(.58,.10,.42,.90),2.0:(.58,.10,.42,.90),2.5:(.58,.10,.42,.90),
3.0:(.60,.47,.25,.50),3.5:(.59,.45,.32,.52),4.0:(.60,.31,.30,.54),4.5:(.60,.30,.34,.57),5.0:(.61,.28,.31,.72),5.5:(.62,.27,.33,.73),
6.0:(.65,.24,.35,.67),6.5:(.70,.22,.30,.71),7.0:(.05,.27,.31,.73),7.5:(.08,.28,.26,.72),8.0:(.10,.26,.27,.62),8.5:(.15,.24,.22,.63),
9.0:(.14,.24,.20,.68),9.5:(.14,.23,.20,.68),10.0:(.13,.22,.20,.58),10.5:(.11,.22,.19,.58),11.0:(.11,.22,.18,.70),11.5:(.11,.22,.18,.70),12.0:(.11,.22,.17,.58)}
c={"mediaId":4276,"level":"A","keyWord":"elderly","defaultVoice":"female",
"taps":[
 {"phrase":"to walk with a stick","target":"the old woman","voice":"female","keys":keys(W,T25)},
 {"phrase":"to wear an apron","target":"the young man","voice":"male","keys":keys(M,T25)},
 {"phrase":"to turn round at the door","target":"the old woman","voice":"female","keys":keys(W,T25)}],
"stillS":12.0,
"nouns":[{"word":"a door","x":.52,"y":.20,"voice":"female"},{"word":"a scarf","x":.44,"y":.44,"voice":"female"},
 {"word":"a stick","x":.45,"y":.70,"voice":"female"},{"word":"steps","x":.60,"y":.85,"voice":"female"}],
"question":"What is the elderly woman doing?",
"answer":["She","is","walking","with","a","stick."],"answerVoice":"female",
"notes":"Key word 'elderly' (adjective) used in the question. The nurse got no phrase: nothing she does is hers alone (both helpers hold an arm). Close shots 0-2.5 s: woman and young man overlap, boxes split at x 0.57. 'to wear an apron' is a state: his only action (holding her arm) is shared with the nurse."}
json.dump(c,open("content/4276.json","w"),indent=1,ensure_ascii=False)

# ---------- 4277
W={0.0:(0,.10,.80,.60),0.5:(0,.09,.80,.61),1.0:(0,.09,.76,.67),1.5:(0,.08,.78,.69),2.0:(0,0,.81,.88),2.5:(0,0,.81,.88),3.0:(0,0,.81,.95),3.5:(0,0,.81,.97),
4.0:(0,0,.73,.84),4.5:(0,0,.75,.70),5.0:(0,0,.94,.52),5.5:(0,0,.95,.76),6.0:(0,0,1.0,.58),6.5:(0,.07,.76,.57),7.0:(.05,.08,.69,.66),7.5:(.05,.07,.71,.65),
8.0:(0,.06,.76,.58),8.5:(0,0,.81,.67),9.0:(0,0,.81,.76)}
L={0.0:(.82,.18,.18,.24),0.5:(.81,.19,.19,.23),1.0:(.78,.19,.22,.36),1.5:(.80,.19,.20,.35),2.0:(.82,.10,.18,.20),2.5:(.82,.08,.18,.22),3.0:(.82,.12,.18,.22),3.5:(.82,.10,.18,.24),
4.0:(.74,0,.26,.28),4.5:(.77,0,.23,.14),6.5:(.78,.17,.22,.24),7.0:(.75,.18,.25,.36),7.5:(.77,.18,.23,.36),8.0:(.78,.14,.22,.26),8.5:(.82,.16,.18,.24),9.0:(.82,.19,.18,.36)}
c={"mediaId":4277,"level":"B","keyWord":"accountant","defaultVoice":"female",
"taps":[
 {"phrase":"to examine a long receipt","target":"the woman","voice":"female","keys":keys(W,T19)},
 {"phrase":"to illuminate the cluttered desk","target":"the lamp","voice":"female","keys":keys(L,T19)},
 {"phrase":"to raise both fists triumphantly","target":"the woman","voice":"female","keys":keys(W,T19)}],
"stillS":7.0,
"nouns":[{"word":"an accountant","x":.38,"y":.38,"voice":"female"},{"word":"a desk lamp","x":.84,"y":.33,"voice":"female"},
 {"word":"a ledger","x":.66,"y":.59,"voice":"female"},{"word":"a calculator","x":.40,"y":.69,"voice":"female"}],
"question":"What is the accountant doing?",
"answer":["She","is","examining","a","long","receipt."],"answerVoice":"female",
"notes":"Only one person; the lamp is the second target (off 5.0-6.0 s, only a sliver at the right edge 2.0-3.5 s and 9.0 s). Where her receipt hand lies under the lamp the woman's box is cut at the lamp's left edge. 'a ledger' may be above B2. Fists go up only at 8.5-9.0 s."}
json.dump(c,open("content/4277.json","w"),indent=1,ensure_ascii=False)

# ---------- 4281
A={0.0:(0,.28,.75,.38),0.5:(0,.27,.72,.37),1.0:(0,.28,.67,.36),1.5:(0,.26,.64,.36),2.0:(0,.29,.62,.33),2.5:(0,.30,.66,.32),
3.0:(0,.32,.67,.30),3.5:(0,.30,.71,.32),4.0:(0,.32,.69,.30),4.5:(0,.31,.71,.30),5.0:(0,.32,.73,.29),5.5:(0,.32,.72,.30),
6.0:(0,.33,.74,.28),6.5:(0,.34,.79,.26),7.0:(0,.34,.83,.29),7.5:(0,.34,.84,.29),8.0:(0,.35,.84,.31),8.5:(0,.36,.84,.30),
9.0:(0,.37,.84,.30),9.5:(0,.37,.84,.30),10.0:(0,.37,.86,.27),10.5:(0,.38,.84,.26),11.0:(0,.39,.83,.26),11.5:(0,.39,.84,.26),12.0:(0,.39,.84,.25)}
M={0.0:(.76,0,.24,1.0),0.5:(.73,0,.27,1.0),1.0:(.68,0,.32,1.0),1.5:(.65,0,.35,1.0),2.0:(.63,0,.37,1.0),2.5:(.67,0,.33,1.0),
3.0:(.50,0,.50,.31),3.5:(.48,0,.52,.29),4.0:(.42,0,.58,.31),4.5:(.42,0,.58,.30),5.0:(.40,0,.60,.31),5.5:(.38,0,.62,.31),
6.0:(.36,0,.64,.32),6.5:(.36,0,.64,.33),7.0:(.35,0,.65,.33),7.5:(.35,0,.65,.33),8.0:(.33,0,.67,.34),8.5:(.33,0,.67,.35),
9.0:(.33,0,.67,.36),9.5:(.33,0,.67,.36),10.0:(.33,0,.67,.36),10.5:(.33,0,.67,.37),11.0:(.30,0,.70,.38),11.5:(.30,0,.70,.38),12.0:(.30,0,.70,.38)}
c={"mediaId":4281,"level":"A","keyWord":"change","defaultVoice":"male",
"taps":[
 {"phrase":"to change its colour","target":"the animal","voice":"male","keys":keys(A,T25)},
 {"phrase":"to hold a piece of wood","target":"the man","voice":"male","keys":keys(M,T25)},
 {"phrase":"to climb onto the wood","target":"the animal","voice":"male","keys":keys(A,T25)}],
"stillS":9.0,
"nouns":[{"word":"a man","x":.62,"y":.13,"voice":"male"},{"word":"an animal","x":.38,"y":.46,"voice":"male"},
 {"word":"wood","x":.65,"y":.66,"voice":"male"},{"word":"a leaf","x":.17,"y":.77,"voice":"male"}],
"question":"What is the animal doing?",
"answer":["It","is","changing","its","colour."],"answerVoice":"male",
"notes":"Key word 'change' is a noun in the packet; used as the verb in phrase and answer (no visible noun). 'animal' instead of 'chameleon' for level A. The animal sits in front of the man's face and hand: from 3.0 s the man's box is his face above the animal (his hand and shirt below are not in it); 0-2.5 s it is the strip right of the animal. 'a leaf' = the one big leaf in front (other leaves blurred behind)."}
json.dump(c,open("content/4281.json","w"),indent=1,ensure_ascii=False)

# ---------- 4282
D={0.0:(.50,.31,.50,.69),0.5:(.30,.25,.70,.75),1.0:(.50,.30,.50,.70),2.5:(.46,.50,.30,.22),3.0:(0,.36,.76,.40),3.5:(0,.32,.62,.30),4.0:(0,.29,.62,.46),
8.0:(0,.35,.76,.65),8.5:(.12,.36,.58,.52),9.0:(.24,.38,.45,.57),9.5:(.38,.36,.30,.54),10.0:(.40,.42,.34,.37),10.5:(.24,.45,.46,.35),11.0:(.26,.57,.40,.35),11.5:(.40,.58,.25,.34),12.0:(.40,.48,.32,.31)}
Y={0.0:(0,.21,.33,.79),0.5:(0,.20,.28,.80),1.0:(0,.21,.32,.79),1.5:(0,.30,.42,.70),2.0:(0,.28,.40,.72),2.5:(0,.30,.45,.70),3.0:(0,.77,.48,.23),3.5:(0,.63,.28,.37),4.0:(0,.76,.50,.24),
8.0:(0,0,.32,.34),8.5:(0,0,.42,.35),9.0:(0,0,.46,.37),9.5:(0,0,.37,.85),10.0:(.03,.02,.36,.73),10.5:(.03,.05,.42,.39),11.0:(0,.09,.43,.47),11.5:(0,.11,.39,.79),12.0:(.03,.12,.36,.66)}
S={1.5:(.18,.05,.36,.24),2.0:(.15,.04,.42,.23),2.5:(.02,.07,.46,.22),3.0:(.08,.13,.36,.18),3.5:(.20,.14,.26,.14),4.0:(.26,.11,.30,.17),
4.5:(0,0,.86,.32),5.0:(0,0,.86,.33),5.5:(0,0,.86,.33),6.0:(.08,.08,.92,.69),6.5:(0,.08,1.0,.60),7.0:(0,.09,1.0,.63),7.5:(0,.09,1.0,.63),
8.0:(.62,.21,.18,.14),8.5:(.58,.20,.18,.15),9.0:(.70,.27,.18,.14),9.5:(.75,.29,.18,.14),10.5:(.82,.30,.18,.14),11.0:(.82,.31,.18,.14)}
c={"mediaId":4282,"level":"B","keyWord":"shelter","defaultVoice":"female",
"taps":[
 {"phrase":"to wag its tail","target":"the dog","voice":"female","keys":keys(D,T25)},
 {"phrase":"to stamp the paperwork","target":"the woman in green","voice":"female","keys":keys(S,T25)},
 {"phrase":"to hold a red leash","target":"the young woman","voice":"female","keys":keys(Y,T25)}],
"stillS":10.0,
"nouns":[{"word":"a checked shirt","x":.72,"y":.14,"voice":"female"},{"word":"dungarees","x":.20,"y":.30,"voice":"female"},
 {"word":"a leash","x":.47,"y":.42,"voice":"female"},{"word":"a dog","x":.50,"y":.60,"voice":"female"}],
"question":"What is the dog doing?",
"answer":["It","is","wagging","its","tail."],"answerVoice":"female",
"notes":"Key word 'shelter' is the whole place, no label slot, not used. Mixed couple -> defaultVoice by evenId. Clip has 4 shots. The woman in green stamps only at 6.0 s (stamp in her hand to 7.5 s); from 8.0 s she is tiny at the desk in the background (small boxes; off where hidden). Hug shots 3.0-4.0 s: the young woman is mostly hidden behind the dog, her box is only her lower body. Walking shots: where dog and young woman overlap her box is the upper body with the leash hand (8.0-9.0, 10.5, 11.0 s). Signing hands at 4.5-5.5 s are the man's (no target). 'dungarees'/'checked' British, 'leash' as in the packet."}
json.dump(c,open("content/4282.json","w"),indent=1,ensure_ascii=False)
