import json
O=None
def keys(K,i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
def dump(d): json.dump(d,open("content/%d.json"%d["mediaId"],"w"),indent=1)

# ---- 4394 (woman, girl)
K={
0.0:((0,.08,1,.62),O),0.5:((0,.10,1,.62),O),1.0:((0,.22,1,.66),O),1.5:((0,.24,1,.63),O),
2.0:((0,.16,1,.66),O),2.5:((0,.15,1,.72),O),3.0:((0,.22,1,.76),O),3.5:((0,.48,1,.52),O),
4.0:((0,.45,1,.55),O),4.5:((0,.42,1,.58),O),5.0:((0,.53,1,.47),O),5.5:((0,.57,1,.43),O),
6.0:((.04,.15,.35,.52),(.39,.36,.56,.36)),
6.5:((.06,.17,.31,.50),(.37,.33,.58,.39)),
7.0:((.06,.27,.30,.40),(.36,.33,.53,.40)),
7.5:((.07,.29,.30,.40),(.37,.34,.52,.41)),
8.0:((.06,.32,.30,.40),(.36,.34,.53,.40)),
8.5:((.06,.30,.30,.42),(.36,.35,.54,.40)),
9.0:((.06,.30,.30,.42),(.36,.35,.53,.41)),
9.5:((.07,.31,.30,.40),(.37,.35,.52,.41)),
10.0:((.06,.31,.30,.40),(.36,.35,.53,.40)),
}
dump({"mediaId":4394,"level":"A","keyWord":"bend","defaultVoice":"female",
"taps":[
 {"phrase":"to bend a ruler","target":"the woman in yellow","voice":"female","keys":keys(K,0)},
 {"phrase":"to pull a branch down","target":"the woman in yellow","voice":"female","keys":keys(K,0)},
 {"phrase":"to bend backwards","target":"the girl in blue","voice":"female","keys":keys(K,1)}],
"stillS":9.0,
"nouns":[{"word":"a tree","x":0.28,"y":0.14,"voice":"female"},
 {"word":"a table","x":0.78,"y":0.43,"voice":"female"},
 {"word":"grass","x":0.50,"y":0.88,"voice":"female"}],
"question":"What is the girl in blue doing?",
"answer":["She","is","bending","backwards","on","the","grass."],
"answerVoice":"female",
"notes":"Three shots: ruler (0-3.0 s), branch (3.5-5.5 s), garden with the girl (6.0 s on). In the garden shot the girl's bent legs stand in front of the crouching woman, the two overlap in the picture: split with a vertical line at x 0.36-0.39, so the girl's box holds her body, head and arms but NOT her legs (they lie inside the woman's box). No person nouns, because the woman and the girl overlap. The table is partly hidden by the girl; the pill sits on its free right end."})

# ---- 4395 (woman, man)
K={
0.0:((.08,.17,.41,.33),(.49,.17,.51,.33)),
0.5:((.08,.17,.41,.33),(.49,.15,.51,.35)),
1.0:((.0,.18,.49,.34),(.49,.16,.51,.36)),
1.5:((.07,.19,.40,.33),(.47,.16,.53,.36)),
2.0:((.08,.18,.41,.34),(.49,.15,.51,.37)),
2.5:((0,.10,.47,.47),(.47,.11,.53,.42)),
3.0:((0,.11,.46,.46),(.46,.14,.54,.39)),
3.5:((0,.10,.44,.47),(.44,.18,.56,.35)),
4.0:((0,.09,.46,.47),(.46,.16,.54,.36)),
4.5:((0,.09,.47,.47),(.47,.15,.53,.37)),
5.0:((0,.08,.50,.61),(.50,.15,.50,.38)),
5.5:((0,.08,.57,.48),(.57,.15,.43,.38)),
6.0:((0,.10,.56,.50),(.56,.13,.44,.40)),
6.5:((0,.10,.55,.55),(.55,.12,.45,.41)),
7.0:((0,.10,.49,.48),(.49,.10,.51,.45)),
7.5:((0,.10,.48,.48),(.48,.09,.52,.46)),
8.0:((0,.10,.47,.47),(.47,.09,.53,.46)),
8.5:((0,.11,.46,.46),(.46,.09,.54,.46)),
9.0:((0,.12,.46,.46),(.46,.09,.54,.47)),
}
dump({"mediaId":4395,"level":"B","keyWord":"opponent","defaultVoice":"female",
"taps":[
 {"phrase":"to rearrange the game pieces","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to lean over the board","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to tilt his head back","target":"the man","voice":"male","keys":keys(K,1)}],
"stillS":8.0,
"nouns":[{"word":"glasses","x":0.68,"y":0.26,"voice":"female"},
 {"word":"a can","x":0.90,"y":0.45,"voice":"female"},
 {"word":"a tower","x":0.47,"y":0.62,"voice":"female"},
 {"word":"miniatures","x":0.82,"y":0.70,"voice":"female"}],
"question":"What is the woman rearranging?",
"answer":["She","is","rearranging","the","game","pieces."],
"answerVoice":"female",
"notes":"Wide shot 0-2.0 s (two more players only as hands / a slice of a face at the edges, not used), close shot from 2.5 s. The woman moves the figures at 5.0-5.5 s and the tower at 6.0-6.5 s; at 5.5-6.5 s her arm crosses the man's chest, split at x 0.55-0.57. The man tilts his head back to drink at 3.0-4.5 s. Key word 'opponent' is not in the texts: nothing in the picture alone shows who plays against whom. defaultVoice female = the woman as the acting person (only the nouns use it). 'miniatures' pill sits on the dense group on the right; single figures also stand elsewhere on the board."})

# ---- 4396 (woman, man)
K={
0.0:((0,.13,.43,.39),(.43,.09,.57,.43)),
0.5:((0,.13,.47,.39),(.47,.09,.53,.43)),
1.0:((0,.13,.39,.39),(.39,.13,.61,.42)),
1.5:((0,.12,.41,.40),(.41,.13,.59,.42)),
2.0:((0,.13,.42,.39),(.42,.11,.58,.41)),
2.5:((0,.13,.42,.39),(.42,.07,.58,.45)),
3.0:((0,.13,.42,.39),(.42,.06,.58,.46)),
3.5:((0,.16,.43,.36),(.43,.05,.57,.47)),
4.0:((0,.04,.42,.61),(.42,.04,.58,.48)),
4.5:((0,.01,.44,.62),(.44,.04,.56,.48)),
5.0:((0,.08,.43,.57),(.43,.05,.57,.44)),
5.5:((0,.13,.42,.50),(.42,.05,.58,.46)),
6.0:((0,.09,.43,.49),(.43,.08,.57,.44)),
6.5:((0,.07,.43,.46),(.43,.08,.57,.44)),
7.0:((0,.15,.42,.38),(.42,.07,.58,.45)),
7.5:((0,.15,.43,.38),(.43,.08,.57,.44)),
8.0:((0,.14,.43,.39),(.43,.08,.57,.44)),
8.5:((0,.14,.44,.39),(.44,.09,.56,.43)),
9.0:((0,.14,.43,.39),(.43,.08,.57,.44)),
9.5:((0,.14,.43,.39),(.43,.09,.57,.43)),
10.0:((0,.13,.44,.40),(.44,.09,.56,.43)),
}
dump({"mediaId":4396,"level":"B","keyWord":"shock","defaultVoice":"female",
"taps":[
 {"phrase":"to shift the red pieces","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to gulp down his drink","target":"the man","voice":"male","keys":keys(K,1)},
 {"phrase":"to stare in shock","target":"the man","voice":"male","keys":keys(K,1)}],
"stillS":8.0,
"nouns":[{"word":"glasses","x":0.65,"y":0.24,"voice":"female"},
 {"word":"a checked shirt","x":0.68,"y":0.35,"voice":"female"},
 {"word":"a cardigan","x":0.17,"y":0.44,"voice":"female"},
 {"word":"a game board","x":0.50,"y":0.72,"voice":"female"}],
"question":"What is the man doing?",
"answer":["He","is","staring","at","the","board","in","shock."],
"answerVoice":"male",
"notes":"The woman moves the red pieces at 4.0-5.5 s (her hand on the board; at 5.0 s her fingertips reach a little past her box under the man's box). The man drinks with his head back at 2.5-5.5 s; the woman only takes a small sip at 9.5-10.0 s ('gulp down his drink' is meant to fit only him - doubt for the verifier). He stares open-mouthed from 7.0 s. defaultVoice: no single main person, evenId true -> female. Question asks about the state at the end of the clip."})

# ---- 4397 (man)
K={
0.0:((0,.22,.86,.78),),0.5:((0,.24,.90,.76),),1.0:((0,.22,.80,.78),),1.5:((0,.23,1.0,.77),),
2.0:((0,.20,.56,.80),),2.5:((0,.22,.66,.78),),3.0:((0,.23,.78,.77),),3.5:((0,.25,.66,.75),),
4.0:((0,.26,.56,.74),),4.5:((0,.29,.50,.71),),5.0:((0,.32,.46,.68),),5.5:((0,.32,.44,.68),),
6.0:((0,.36,.37,.64),),6.5:((0,.37,.39,.63),),7.0:((0,.41,.54,.59),),7.5:((0,.42,.54,.58),),
8.0:((0,.41,.57,.59),),8.5:((0,.42,.58,.58),),9.0:((0,.41,.57,.59),),
}
dump({"mediaId":4397,"level":"A","keyWord":"bike","defaultVoice":"male",
"taps":[
 {"phrase":"to bike through the city","target":"the man","voice":"male","keys":keys(K,0)},
 {"phrase":"to wear a green jacket","target":"the man","voice":"male","keys":keys(K,0)},
 {"phrase":"to point at the bikes","target":"the man","voice":"male","keys":keys(K,0)}],
"stillS":2.5,
"nouns":[{"word":"the sky","x":0.62,"y":0.10,"voice":"male"},
 {"word":"a boat","x":0.80,"y":0.44,"voice":"male"},
 {"word":"a jacket","x":0.17,"y":0.55,"voice":"male"},
 {"word":"a basket","x":0.80,"y":0.79,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","biking","through","the","city."],
"answerVoice":"male",
"notes":"Selfie clip with one possible target (the man); the few walkers at 0-1.5 s are tiny. His box includes the arm that holds the camera. He points at the stacked bikes at 8.0-9.0 s. Still 2.5 s: several boats lie in the canal, the pill sits on the nearest white one on the right; 'a basket' = the wire basket on his bike."})
