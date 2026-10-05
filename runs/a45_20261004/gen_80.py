import json
T21=[i*0.5 for i in range(21)]; T17=[i*0.5 for i in range(17)]
def keys(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    assert len(out)==len(times)==len(boxes)
    return out
def w(c): json.dump(c,open(f'content/{c["mediaId"]}.json','w'),indent=1,ensure_ascii=False)
# ---- 80
B=[(0,.13,.60,.87),(0,.13,.60,.87),(0,.13,.60,.87),(0,.13,.60,.87),(0,.13,.70,.87),(0,.13,.62,.87),(0,.13,.68,.87),(0,.13,.63,.87),
   (0,.13,.53,.87),(0,.13,.50,.87),(0,.13,.46,.87),(0,.13,.42,.87),(0,.13,.50,.87),(0,.13,.42,.87),(0,.13,.42,.87),(0,.15,.45,.85),
   (0,.15,.48,.85),(0,.15,.48,.85),(0,.17,.52,.83),(0,.15,.52,.85),(0,.18,.50,.82)]
N=[(.62,.22,.38,.50),(.62,.22,.38,.50),(.62,.22,.38,.50),(.62,.22,.38,.50),(.72,.22,.28,.50),(.64,.22,.36,.40),(.70,.24,.30,.48),(.65,.24,.35,.48),
   (.55,.22,.45,.50),(.52,.22,.48,.50),(.48,.23,.52,.50),(.44,.23,.56,.52),(.52,.21,.48,.51),(.44,.22,.56,.51),(.44,.23,.56,.47),(.47,.24,.53,.46),
   (.50,.23,.50,.47),(.50,.23,.50,.47),(.54,.24,.46,.48),(.54,.24,.46,.48),(.52,.23,.48,.46)]
kb=keys(T21,B); kn=keys(T21,N)
w({"mediaId":80,"level":"A","keyWord":"beard","defaultVoice":"male",
 "taps":[{"phrase":"to comb his long beard","target":"the man with the beard","voice":"male","keys":kb},
         {"phrase":"to hold a phone","target":"the bald man","voice":"male","keys":kn},
         {"phrase":"to wear a white shirt","target":"the man with the beard","voice":"male","keys":kb}],
 "stillS":0.0,
 "nouns":[{"word":"a beard","x":.25,"y":.38,"voice":"male"},{"word":"a comb","x":.42,"y":.54,"voice":"male"},
          {"word":"tea","x":.75,"y":.76,"voice":"male"},{"word":"flowers","x":.50,"y":.07,"voice":"male"}],
 "question":"What is the man in white doing?","answer":["He","is","combing","his","long","beard."],"answerVoice":"male",
 "notes":"The two men sit close; the bearded man's hand (comb, oil, hand on the friend's shoulder at 6.5-8.5 s) reaches into the bald man's box, boxes are split on a vertical line. Third phrase is a state (white shirt) because the bald man's only other clear action (touching his chin) is too close to the bearded man stroking his beard. A second wooden comb-like piece lies on the table at 0.0 s; the 'a comb' pill is on the one in his hand."})
# ---- 81
O=None
W=[O,(.63,.50,.30,.50),(.11,.46,.35,.54),(.11,.43,.38,.57),(.13,.42,.38,.58),(.08,.41,.42,.59),(.02,.44,.49,.56),(0,.44,.52,.56),(0,.46,.44,.54),
   (0,.10,.65,.90),O,O,O,(0,.28,.66,.72),(0,.36,.67,.64),(.28,.26,.68,.74),(.08,.22,.76,.78),(.18,.27,.50,.73),(.16,.35,.45,.65),(.23,.34,.35,.66),(.09,.35,.46,.60)]
M=[O,O,(.47,.44,.31,.56),(.50,.41,.32,.59),(.52,.39,.36,.61),(.51,.37,.45,.63),(.52,.37,.48,.63),(.54,.37,.46,.63),(.50,.37,.50,.63),
   O,O,O,O,O,O,O,O,O,(.82,.40,.18,.60),(.77,.40,.23,.60),(.56,.42,.44,.58)]
S=[O,O,(.36,.23,.22,.16),(.39,.22,.22,.16),(.41,.21,.22,.16),(.42,.20,.22,.16),(.41,.21,.22,.15),(.42,.21,.22,.15),(.43,.21,.22,.15),
   O,O,O,O,(.56,.13,.22,.15),(.54,.14,.22,.16),O,(.85,.13,.15,.18),(.69,.22,.20,.16),(.62,.28,.19,.15),(.59,.30,.17,.14),(.59,.29,.22,.13)]
w({"mediaId":81,"level":"A","keyWord":"beauty","defaultVoice":"female",
 "taps":[{"phrase":"to dance in a white dress","target":"the woman","voice":"female","keys":keys(T21,W)},
         {"phrase":"to wear a blue shirt","target":"the man","voice":"male","keys":keys(T21,M)},
         {"phrase":"to shine over the sea","target":"the sun","voice":"female","keys":keys(T21,S)}],
 "stillS":1.5,
 "nouns":[{"word":"the sun","x":.50,"y":.30,"voice":"female"},{"word":"the sea","x":.22,"y":.44,"voice":"female"},
          {"word":"a woman","x":.28,"y":.78,"voice":"female"},{"word":"a man","x":.68,"y":.67,"voice":"male"}],
 "question":"What is the woman doing?","answer":["She","is","dancing","in","a","white","dress."],"answerVoice":"female",
 "notes":"Key word 'beauty' is abstract, so it is not a noun slot. Many cuts: 0.0 s empty lane, 5.0 s a cat, 5.5-6.0 s an empty lane (all targets off; the sun there is only a glare, no disc). Man's phrase is a state (blue shirt): he has no action of his own. 0.5 s: only the man's arm at the edge, set off. 8.5-10.0 s: the sun is right next to the woman, her box is cut short on the right (stretched arm / dress hem outside). 6.5-7.0 s: the woman is the arm with the mirror and her face in the mirror."})
# ---- 83
F=(0,0,1,1)
M=[F]*10+[(0,.07,.92,.78),(0,.14,.56,.66),(0,.18,.43,.57),(0,.21,.43,.50),(0,.26,.46,.43),(0,.27,.50,.41),(0,.28,.52,.40),(0,.28,.52,.40),(0,.30,.52,.45),(0,.30,.52,.45),(0,.30,.52,.34)]
W=[O]*11+[(.58,.20,.42,.60),(.44,.22,.56,.54),(.45,.25,.55,.47),(.50,.28,.50,.41),(.52,.30,.48,.38),(.54,.31,.46,.36),(.54,.31,.46,.36),(.55,.32,.45,.43),(.55,.32,.45,.43),(.54,.33,.42,.31)]
D=[O]*16+[(.25,.82,.75,.17),(.22,.80,.78,.17),(.23,.80,.77,.17),(.23,.80,.77,.17),(.23,.77,.77,.17)]
w({"mediaId":83,"level":"A","keyWord":"beer","defaultVoice":"male",
 "taps":[{"phrase":"to pour a beer","target":"the man","voice":"male","keys":keys(T21,M)},
         {"phrase":"to have long hair","target":"the woman","voice":"female","keys":keys(T21,W)},
         {"phrase":"to sleep under the table","target":"the dog","voice":"male","keys":keys(T21,D)}],
 "stillS":10.0,
 "nouns":[{"word":"beer","x":.41,"y":.50,"voice":"male"},{"word":"bread","x":.60,"y":.64,"voice":"male"},
          {"word":"a dog","x":.58,"y":.87,"voice":"male"},{"word":"lamps","x":.78,"y":.10,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","pouring","beer","into","a","glass."],"answerVoice":"male",
 "notes":"0.0-4.5 s is a close-up of the man only (box = whole picture). Woman's phrase is a state (long hair): both drink, laugh and hold a glass, so no action is hers alone. The dog lies under the table from about 8.0 s (dark shape only at 7.0-7.5 s, set off); the legs under the table are left out of the people's boxes so they do not meet the dog's box. 'beer' pill sits on the man's glass (the woman holds a second one); cheese lies next to the bread on the board."})
# ---- 84
M=[(.04,.09,.68,.91),(.08,.07,.84,.93),(.03,.06,.94,.94),(.06,.06,.93,.94),(.06,.04,.93,.96),O,F,F,F,F,F,F,(0,.05,1,.95),(0,.05,1,.95),(0,.03,1,.97),(.14,.10,.86,.90),(.16,.20,.75,.80)]
km=keys(T17,M)
w({"mediaId":84,"level":"A","keyWord":"belt","defaultVoice":"male",
 "taps":[{"phrase":"to hold up his trousers","target":"the man","voice":"male","keys":km},
         {"phrase":"to put on a belt","target":"the man","voice":"male","keys":km},
         {"phrase":"to dance happily","target":"the man","voice":"male","keys":km}],
 "stillS":6.0,
 "nouns":[{"word":"a shirt","x":.50,"y":.42,"voice":"male"},{"word":"a belt","x":.50,"y":.585,"voice":"male"},
          {"word":"trousers","x":.50,"y":.76,"voice":"male"},{"word":"a chair","x":.88,"y":.89,"voice":"male"}],
 "question":"What is the man wearing?","answer":["He","is","wearing","a","brown","belt."],"answerVoice":"male",
 "notes":"Cartoon clip. All three phrases use the man: the only other things are the belt and the chair; the belt is on the man from 3.0 s (its box would lie inside his), and the chair has no phrase that fits only it. 2.5 s shows only the chair with the belt (man off). 3.0-5.5 s is a close-up of his hands and waist (box = whole picture). Question asks what he is wearing because 'put on' / 'hold up' allow two word orders with chips; he also wears a shirt and trousers, the key word is the expected answer. 'to dance happily' is only 7.5-8.0 s."})
