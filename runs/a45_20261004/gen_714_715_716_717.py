import json
def keys(K,i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
O=None
# ---- 714: (soldier, bag)
K={0.0:((.12,.13,.56,.87),(.69,.52,.31,.36)),
0.5:((.14,.13,.55,.87),(.70,.57,.30,.33)),
1.0:((.05,.14,.60,.86),(.66,.66,.34,.32)),
1.5:((.06,.15,.61,.85),(.68,.65,.32,.35)),
2.0:((.10,.13,.57,.87),(.68,.55,.32,.33)),
2.5:((.17,.10,.52,.90),(.70,.49,.30,.30)),
3.0:((.19,.10,.45,.90),(.65,.43,.29,.28)),
3.5:((.23,.10,.43,.90),(.67,.41,.27,.26)),
4.0:((.25,.10,.41,.90),(.67,.41,.28,.25)),
4.5:((.27,.10,.42,.90),(.70,.42,.30,.26)),
5.0:((.20,.12,.49,.88),(.70,.63,.30,.37)),
5.5:((.12,.17,.60,.83),(.73,.73,.27,.27)),
6.0:((.05,.08,.95,.92),O),
6.5:((.07,.08,.93,.92),O),
7.0:((.20,.15,.75,.85),O),
7.5:((.08,.30,.70,.70),O),
8.0:((.18,.18,.64,.82),O),
8.5:((.30,.17,.55,.60),O),
9.0:((.02,.08,.68,.45),O),
9.5:((.03,0,.87,.56),O),
10.0:((.05,0,.87,.58),O)}
d={"mediaId":714,"level":"A","keyWord":"soldier","defaultVoice":"male",
"taps":[
 {"phrase":"to walk through a door","target":"the soldier","voice":"male","keys":keys(K,0)},
 {"phrase":"to run to his family","target":"the soldier","voice":"male","keys":keys(K,0)},
 {"phrase":"to hang from his shoulder","target":"the bag","voice":"male","keys":keys(K,1)}],
"stillS":3.5,
"nouns":[{"word":"a hat","x":.50,"y":.16,"voice":"male"},
 {"word":"a soldier","x":.45,"y":.36,"voice":"male"},
 {"word":"a bag","x":.78,"y":.55,"voice":"male"},
 {"word":"shoes","x":.52,"y":.93,"voice":"male"}],
"question":"What is the soldier doing?",
"answer":["He","is","running","to","his","family."],
"answerVoice":"male",
"notes":"Two phrases share the soldier (the family members appear only from 7.0 s, all laughing and hugging alike, so no phrase fits just one of them). The bag hangs on the soldier's side: boxes are split along the vertical line between body and bag, so the soldier's bag-side arm lies outside his box at 0.0-5.5 s. At 5.0-5.5 s the bag is in his hand / dropped (no longer on the shoulder) but still boxed. Bag gone from 6.0 s. From 8.0 s the soldier is partly hidden in the group hug; box on his cap, face and back. 'a soldier' pill on the chest, 'a hat' on the cap of the same (large) figure."}
json.dump(d,open("content/714.json","w"),indent=1,ensure_ascii=False)

# ---- 715: (woman, man)
K={0.0:((.02,.02,.58,.62),O),
0.5:((.05,.05,.72,.64),O),
1.0:((.05,.08,.80,.67),O),
1.5:((.05,0,.92,.70),O),
2.0:((0,0,1,.64),O),
2.5:((0,0,1,.66),O),
3.0:((0,0,1,.80),O),
3.5:((0,0,1,.80),O),
4.0:((0,.09,.95,.72),O),
4.5:((.02,.18,.86,.68),O),
5.0:((.18,.30,.70,.62),O),
5.5:((.61,.26,.39,.74),(.12,.30,.48,.66)),
6.0:((.40,.20,.60,.68),(0,.36,.33,.52)),
6.5:((.58,.27,.42,.73),O),
7.0:((.12,.31,.74,.66),O),
7.5:((.08,.18,.82,.68),O),
8.0:((.10,.13,.82,.62),O),
8.5:((.02,.13,.95,.66),O),
9.0:((.03,.17,.92,.68),O),
9.5:((.03,.17,.92,.72),O),
10.0:((0,.13,.97,.66),O)}
d={"mediaId":715,"level":"A","keyWord":"someone","defaultVoice":"female",
"taps":[
 {"phrase":"to hold a yellow note","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to drink her coffee","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to type on a keyboard","target":"the man","voice":"male","keys":keys(K,1)}],
"stillS":8.0,
"nouns":[{"word":"a note","x":.67,"y":.38,"voice":"female"},
 {"word":"a cup","x":.24,"y":.66,"voice":"female"},
 {"word":"a bun","x":.74,"y":.77,"voice":"female"},
 {"word":"a keyboard","x":.62,"y":.93,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","a","yellow","note."],
"answerVoice":"female",
"notes":"Key word 'someone' is a pronoun and nobody is shown leaving the things, so it is not in the texts. The man in the black hat is visible only at 5.5-6.0 s (at 6.0 s cut by the left edge); he is the only one seen typing. Co-workers in the background are blurred and not used. At 5.5 s the woman's hand with the note reaches slightly into the man's box (split at x 0.60). 'a bun' may be a little above A level ('a roll' would be the alternative). The drinking happens only at 9.5-10.0 s."}
json.dump(d,open("content/715.json","w"),indent=1,ensure_ascii=False)

# ---- 716: (man, cat, candle)
K={0.0:(O,O,O),
0.5:((.35,.48,.65,.50),O,(0,.17,.20,.16)),
1.0:((.22,.68,.58,.32),O,(.03,.15,.20,.15)),
1.5:((.35,.68,.55,.32),O,(0,.15,.18,.15)),
2.0:((.42,.63,.58,.35),O,O),
2.5:((.10,.23,.90,.40),(0,.03,.46,.19),(0,.76,.26,.20)),
3.0:((0,0,1,.63),O,O),
3.5:((.30,0,.70,.66),(0,.12,.29,.19),O),
4.0:((.22,0,.78,.60),(0,.07,.21,.18),O),
4.5:((.22,0,.78,.62),(0,.09,.21,.17),O),
5.0:((.24,0,.76,.63),(0,.13,.23,.18),O),
5.5:((0,0,1,.42),O,O),
6.0:((0,0,1,.50),O,O),
6.5:((.22,0,.78,.58),(0,.05,.21,.16),O),
7.0:((.27,0,.73,.62),(0,.12,.26,.18),O),
7.5:((.22,0,.78,.62),(0,.09,.21,.17),O),
8.0:((.20,0,.80,.58),(0,0,.19,.16),O),
8.5:((0,0,1,.58),O,O),
9.0:((.30,0,.70,.64),(.03,.04,.26,.18),O),
9.5:((.31,0,.69,.62),(.05,.05,.25,.17),O),
10.0:((0,0,1,.56),O,(.04,.67,.25,.18))}
d={"mediaId":716,"level":"A","keyWord":"soup spoon","defaultVoice":"male",
"taps":[
 {"phrase":"to eat vegetable soup","target":"the man","voice":"male","keys":keys(K,0)},
 {"phrase":"to sit behind the man","target":"the cat","voice":"male","keys":keys(K,1)},
 {"phrase":"to burn on the table","target":"the candle","voice":"male","keys":keys(K,2)}],
"stillS":1.5,
"nouns":[{"word":"soup","x":.45,"y":.13,"voice":"male"},
 {"word":"a candle","x":.10,"y":.25,"voice":"male"},
 {"word":"bread","x":.88,"y":.19,"voice":"male"},
 {"word":"a soup spoon","x":.38,"y":.51,"voice":"male"}],
"question":"What is the man eating?",
"answer":["He","is","eating","vegetable","soup."],
"answerVoice":"male",
"notes":"0.5-2.0 s show only the man's hand; boxed as the man. Where the cat sits beside the man's head/shoulder the boxes are split: the man's box starts right of the cat (3.5-5.0, 6.5-8.0, 9.0-9.5 s), so his spoon hand at the left edge lies outside it; at 2.5 s the split is horizontal (cat above y 0.22, man below 0.23, his forehead outside). The cat is small and in the background (yawns at 9.0-9.5 s). The candle is visible only at 0.5-1.5, 2.5 and 10.0 s. Still at 1.5 s shows three spoons (teaspoon, soup spoon, ladle): the 'a soup spoon' pill is on the middle one, and no other noun names a spoon. The bread is cut by the right edge."}
json.dump(d,open("content/716.json","w"),indent=1,ensure_ascii=False)

# ---- 717: (woman, man, cat)
K={0.0:((.48,.44,.52,.22),O,O),
0.5:((.58,.44,.42,.22),O,O),
1.0:((.63,.48,.37,.20),O,O),
1.5:((.05,.05,.95,.72),O,O),
2.0:((.05,.05,.95,.58),O,O),
2.5:(O,O,O),3.0:(O,O,O),3.5:(O,O,O),4.0:(O,O,O),4.5:(O,O,O),
5.0:((.44,.46,.56,.50),(.34,0,.46,.44),O),
5.5:((.50,.56,.50,.44),(.13,.18,.66,.37),(.05,.67,.30,.30)),
6.0:((.68,.50,.32,.47),(.08,.16,.59,.53),(0,.70,.29,.30)),
6.5:(O,(.03,.14,.97,.56),(0,.71,.31,.29)),
7.0:(O,(.03,.17,.97,.57),(0,.75,.28,.25)),
7.5:(O,(.03,.17,.97,.57),(0,.75,.28,.25)),
8.0:(O,(.02,.15,.98,.61),(0,.77,.28,.23)),
8.5:(O,(.02,.15,.98,.61),(0,.77,.28,.23)),
9.0:(O,(.02,.17,.98,.60),(0,.78,.28,.22)),
9.5:(O,(.02,.17,.98,.60),(0,.78,.28,.22)),
10.0:(O,(.02,.15,.98,.62),(0,.78,.28,.22))}
d={"mediaId":717,"level":"A","keyWord":"soup","defaultVoice":"male",
"taps":[
 {"phrase":"to cook soup in a pot","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to eat from a bowl","target":"the man","voice":"male","keys":keys(K,1)},
 {"phrase":"to sleep next to the man","target":"the cat","voice":"male","keys":keys(K,2)}],
"stillS":8.0,
"nouns":[{"word":"a window","x":.72,"y":.10,"voice":"male"},
 {"word":"soup","x":.50,"y":.52,"voice":"male"},
 {"word":"a blanket","x":.62,"y":.74,"voice":"male"},
 {"word":"a cat","x":.14,"y":.88,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","eating","soup","from","a","bowl."],
"answerVoice":"male",
"notes":"Mixed pair (woman cooks, man eats): defaultVoice by evenId false = male. Woman: only her hand/arm at 0.0-1.0 and 5.0-6.0 s, whole at 1.5-2.0 s; the close-ups of pot, ladle and bowl (2.5-4.5 s) show no target. Both blow on the hot soup, so blowing is not used. The man's box covers head, hands and bowl and ends above the cat (the lower blanket is outside). The cat sits and looks up at 5.5-6.5 s and sleeps from about 8.0 s. The man in the background at 5.0 s is blurred. 'tomato' is avoided because the kind of soup cannot be seen for sure."}
json.dump(d,open("content/717.json","w"),indent=1,ensure_ascii=False)
