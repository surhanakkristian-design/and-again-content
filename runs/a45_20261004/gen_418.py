import json
def box(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(times,bs): return [box(t,b) for t,b in zip(times,bs)]
T21=[i*0.5 for i in range(21)]; T11=[i*0.5 for i in range(11)]
def dump(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 418
W=[(0,.41,.93,.59),(0,.40,.95,.60),(0,.48,1,.52),(0,.47,1,.53),(0,.41,.95,.59),(0,.41,1,.59),(0,.30,1,.70),(0,.25,1,.75),
(0,.34,.85,.66),(0,.31,.90,.69),(0,.38,.80,.62),(0,.37,1,.63),(0,.37,1,.63),(0,.20,.71,.80),(0,.30,.65,.70),(0,.28,.76,.72),
(0,.12,.65,.88),(0,.22,.65,.78),(0,.33,.68,.67),(0,.25,.73,.75),(0,.07,.77,.93)]
M=[(.40,0,.60,.40),(.40,0,.60,.39),(.35,0,.65,.47),(.35,0,.65,.46),(.38,0,.62,.40),(.45,0,.55,.40),(.42,0,.58,.29),(.44,0,.56,.24),
(.50,0,.50,.33),(.55,0,.45,.30),(.50,0,.50,.37),(.55,0,.45,.36),(.60,0,.40,.36),(.72,.05,.28,.40),(.66,.13,.34,.31),(.77,.26,.23,.52),
(.66,.34,.34,.40),(.66,.38,.34,.44),(.69,.48,.31,.44),(.74,.32,.26,.46),(.78,.18,.22,.70)]
dump({"mediaId":418,"level":"B","keyWord":"keychain","defaultVoice":"female",
"taps":[{"phrase":"to pry a ring open","target":"the woman","voice":"female","keys":keys(T21,W)},
{"phrase":"to applaud with a grin","target":"the man","voice":"male","keys":keys(T21,M)},
{"phrase":"to spin a keychain","target":"the woman","voice":"female","keys":keys(T21,W)}],
"stillS":7.0,
"nouns":[{"word":"a keychain","x":.52,"y":.60,"voice":"female"},{"word":"a vendor","x":.80,"y":.40,"voice":"male"},
{"word":"a bucket","x":.14,"y":.64,"voice":"female"},{"word":"a sleeve","x":.14,"y":.50,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","spinning","a","keychain","on","her","finger."],"answerVoice":"female",
"notes":"POV clip: until 7.0 s only the woman's hands/arms are visible (her face from 8.0 s); 'the woman' box = her hands and arms. Her hands are in front of the man, so the boxes are split along a horizontal line (man = head and chest above the hands); a strip of his lower torso falls into her box. Spinning visible 7.5-9.0 s, prying the ring 0-3 s, man applauds 8.0-10.0 s."})

# 422
W=[(0,.40,.31,.48),(0,.28,.40,.72),(0,.28,.41,.72),(0,.28,.47,.72),(0,.26,.46,.70),(0,.26,.50,.70),(0,.28,.43,.72),(0,.31,.48,.69),(0,.25,.52,.72),(0,.28,.65,.70),(0,.28,.66,.70)]
B=[(.32,0,.44,.82),(.48,0,.52,.80),(.42,0,.45,.90),(.50,0,.50,.90),(.48,0,.44,.80),(.51,0,.49,.78),(.44,0,.54,.90),(.49,0,.51,.92),(.53,0,.47,.80),(.66,0,.34,.76),(.67,0,.33,.74)]
dump({"mediaId":422,"level":"A","keyWord":"kicking","defaultVoice":"female",
"taps":[{"phrase":"to kick a big bag","target":"the woman","voice":"female","keys":keys(T11,W)},
{"phrase":"to hang from ropes","target":"the bag","voice":"female","keys":keys(T11,B)},
{"phrase":"to lift one leg high","target":"the woman","voice":"female","keys":keys(T11,W)}],
"stillS":2.0,
"nouns":[{"word":"a woman","x":.25,"y":.47,"voice":"female"},{"word":"a bag","x":.70,"y":.42,"voice":"female"},
{"word":"clouds","x":.22,"y":.16,"voice":"female"},{"word":"the floor","x":.62,"y":.90,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","kicking","a","big","bag."],"answerVoice":"female",
"notes":"When she kicks (0.0, 1.0, 4.0-5.0 s) her foot reaches into the bag; boxes split on a vertical line, so the foot tip lies in the bag's box. At 0.0 s only her leg is in the picture."})

# 423
W=[(0,.24,.55,.66),(0,.20,.69,.72),(0,.22,.48,.75),(0,.22,.40,.75),(0,.21,.39,.72),(0,.22,.43,.72),(0,.23,.42,.75),(0,.22,.40,.76),
(0,.22,.47,.70),(0,.23,.60,.68),(0,.22,.51,.73),(0,.24,.49,.72),(0,.21,.45,.70),(0,.22,.50,.70),(0,.25,.51,.72),(0,.26,.50,.72),
(0,.24,.50,.74),(0,.24,.54,.76),(0,.26,.51,.74),(0,.28,.48,.72),(0,.29,.43,.69)]
M=[(.58,.24,.42,.55),(.70,.20,.30,.55),(.50,.20,.50,.75),(.42,.20,.58,.75),(.40,.21,.60,.70),(.44,.22,.56,.68),(.43,.28,.57,.68),(.41,.28,.59,.68),
(.48,.22,.52,.65),(.61,.22,.39,.65),(.52,.22,.48,.72),(.51,.20,.49,.72),(.46,.20,.54,.68),(.51,.19,.49,.70),(.52,.19,.48,.76),(.51,.19,.49,.76),
(.51,.18,.49,.78),(.55,.18,.45,.80),(.52,.18,.48,.80),(.49,.18,.51,.80),(.44,.21,.56,.75)]
dump({"mediaId":423,"level":"A","keyWord":"kiss","defaultVoice":"male",
"taps":[{"phrase":"to blow a kiss","target":"the woman","voice":"female","keys":keys(T21,W)},
{"phrase":"to kiss her hand","target":"the man","voice":"male","keys":keys(T21,M)},
{"phrase":"to wear a big hat","target":"the woman","voice":"female","keys":keys(T21,W)}],
"stillS":5.5,
"nouns":[{"word":"a hat","x":.24,"y":.30,"voice":"male"},{"word":"a man","x":.78,"y":.48,"voice":"male"},
{"word":"a basket","x":.60,"y":.86,"voice":"male"},{"word":"a bottle","x":.82,"y":.74,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","kissing","her","hand."],"answerVoice":"male",
"notes":"The two sit close and overlap (his arm on her face 6.5-8.5 s, heads together from 7.0 s): boxes split on a vertical line between the faces. He kisses her hand at 3.0-3.5 s only; she blows the kiss at 0-1.5 s. Third phrase is a state (hat) because every other action is shared (both kiss, both smile). defaultVoice male: mixed couple, odd id."})

# 424
M=[(0,0,.85,.48),(0,0,.87,.48),(0,0,.85,.58),(0,0,.87,.58),(0,0,.87,.48),(0,0,.87,.48),(0,0,.78,.68),(0,0,.80,.66),(0,0,.78,.62),(0,0,.80,.62),(0,0,.78,.60),
(0,0,1,.63),(0,0,1,.62),(0,0,1,.60),(.48,.05,.52,.75),(.42,.08,.58,.62),(.37,.10,.60,.60),(.35,.09,.63,.62),(.37,.07,.56,.75),(.39,.10,.54,.72),(.43,.10,.50,.65)]
W=[None]*14+[(0,0,.47,.95),(0,.05,.41,.90),(0,.05,.36,.90),(0,.05,.34,.90),(0,.05,.36,.93),(0,.07,.38,.90),(0,.07,.42,.90)]
dump({"mediaId":424,"level":"A","keyWord":"knife","defaultVoice":"male",
"taps":[{"phrase":"to cut the bread","target":"the man","voice":"male","keys":keys(T21,M)},
{"phrase":"to dry her hands","target":"the woman","voice":"female","keys":keys(T21,W)},
{"phrase":"to eat a tomato sandwich","target":"the man","voice":"male","keys":keys(T21,M)}],
"stillS":10.0,
"nouns":[{"word":"a knife","x":.35,"y":.89,"voice":"male"},{"word":"a dog","x":.84,"y":.44,"voice":"male"},
{"word":"a tomato","x":.86,"y":.82,"voice":"male"},{"word":"a woman","x":.20,"y":.28,"voice":"female"}],
"question":"What is the man doing?","answer":["He","is","cutting","bread","with","a","knife."],"answerVoice":"male",
"notes":"0-6.5 s close-up: only the man's hands and shirt are visible (box = hands + torso); the woman appears from 7.0 s. At 7.0-7.5 s the woman moves the knife on the board (she does not cut bread). At 7.0 s her head is in front of his shoulder: his box holds only his right part there. He eats at 7.5-8.5 s; she dries her hands on a towel at 8.0-9.0 s. Noun 'a tomato' = the half tomato on the board (slices also lie on the sandwich)."})
