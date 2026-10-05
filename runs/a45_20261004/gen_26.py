import json
def K(times, rows):
    out=[]
    for t,r in zip(times,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    assert len(rows)==len(times)
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---- 26
t=T(17)
man=[None,(.08,.24,.84,.35),(.02,.24,.96,.37),(.02,.24,.96,.37),(.02,.24,.96,.37),(.04,.24,.94,.37),(.04,.24,.94,.37),
 (0,0,1,.80),(0,0,1,.71),(0,0,1,.71),(0,0,1,.69),(0,0,1,.39),(0,0,1,.19),(0,0,1,.19),(0,.34,1,.66),(0,.34,1,.66),(0,.05,1,.95)]
gl=[None,(.36,.59,.28,.25),(.37,.61,.26,.23),(.37,.61,.26,.23),(.37,.61,.26,.23),(.37,.61,.26,.23),(.38,.61,.25,.23),
 (.08,.80,.86,.20),(.08,.71,.86,.29),(.08,.71,.86,.29),(.08,.69,.86,.31),(.08,.39,.86,.61),(.08,.19,.86,.81),(.08,.19,.86,.81),
 (.40,.04,.29,.30),(.44,.04,.31,.30),None]
save({"mediaId":26,"level":"A","keyWord":"straw","defaultVoice":"male",
 "taps":[{"phrase":"to stretch a long straw","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to drink orange juice","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to stand on the bar","target":"the glass","voice":"male","keys":K(t,gl)}],
 "stillS":2.5,
 "nouns":[{"word":"sunglasses","x":.50,"y":.30,"voice":"male"},{"word":"a straw","x":.50,"y":.51,"voice":"male"},
          {"word":"a glass","x":.50,"y":.74,"voice":"male"},{"word":"a shirt","x":.78,"y":.60,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","drinking","juice","through","a","straw."],"answerVoice":"male",
 "notes":"The glass stands in front of the man: boxes are split along the glass rim (man above, glass below), so his arms/hands beside the glass are outside his box. 7.0-7.5 s the glass is held upside down above his head (phrase 'to stand on the bar' is true 0.5-6.5 s). 'bar' is A2."})

# ---- 324
t=T(11)
girl=[(0,.27,.41,.46),(0,.27,.41,.46),(0,.27,.41,.46),(0,.27,.46,.46),(0,.27,.47,.46),(0,.27,.48,.46),(0,.28,.47,.46),
 (.02,.11,.50,.63),(.03,.07,.53,.67),(.03,.06,.59,.64),(.03,.06,.57,.64)]
boy=[(.41,.19,.59,.81),(.41,.19,.59,.81),(.41,.19,.59,.81),(.46,.17,.54,.83),(.47,.17,.53,.83),(.48,.17,.52,.83),(.47,.17,.53,.83),
 (.52,.19,.48,.81),(.56,.20,.44,.80),(.62,.42,.38,.58),(.60,.42,.40,.58)]
save({"mediaId":324,"level":"A","keyWord":"gaming","defaultVoice":"female",
 "taps":[{"phrase":"to put both hands up","target":"the girl","voice":"female","keys":K(t,girl)},
         {"phrase":"to win the game","target":"the girl","voice":"female","keys":K(t,girl)},
         {"phrase":"to wear a red jacket","target":"the boy","voice":"male","keys":K(t,boy)}],
 "stillS":4.0,
 "nouns":[{"word":"a girl","x":.36,"y":.36,"voice":"female"},{"word":"a jacket","x":.80,"y":.46,"voice":"female"},
          {"word":"boxes","x":.88,"y":.12,"voice":"female"},{"word":"a sofa","x":.60,"y":.90,"voice":"female"}],
 "question":"Who is winning the game?",
 "answer":["The","girl","is","winning","the","game."],"answerVoice":"female",
 "notes":"Both sit close; boxes split on a vertical line between them, his knee in front of her legs is in nobody's box. From 4.0 s her raised right arm/fist crosses over to his side and is cut by the split. 'to win the game' is read from her cheering while he panics (no score shown). Key word 'gaming' is not a visible noun."})

# ---- 612
t=T(19)
wom=[(.42,.27,.26,.31),(.45,.27,.24,.30),(.46,.31,.54,.28),(.47,.33,.53,.27),(.46,.30,.40,.28),(.47,.30,.53,.28),(.47,.31,.53,.27),(.47,.31,.53,.27),
 (.44,.29,.50,.29),(.13,.36,.42,.62),(.31,.35,.39,.65),(.45,.35,.26,.62),(.46,.30,.50,.28),(.47,.31,.49,.27),(.48,.31,.48,.25),(.30,.32,.25,.19),
 (.38,.28,.33,.30),(.37,.29,.40,.30),(.36,.31,.34,.30)]
man=[(0,.28,.42,.72),(0,.28,.45,.72),(0,.30,.46,.70),(0,.29,.47,.71),(0,.28,.46,.72),(0,.28,.47,.72),(0,.30,.47,.70),(0,.30,.47,.70),
 (0,.28,.34,.72),(0,.30,.13,.70),(0,.29,.31,.71),(.08,.28,.37,.72),(.06,.28,.40,.72),(.06,.28,.41,.72),(.04,.28,.44,.72),(.55,.28,.39,.72),
 (.72,.28,.28,.72),None,None]
save({"mediaId":612,"level":"A","keyWord":"right","defaultVoice":"female",
 "taps":[{"phrase":"to point to the right","target":"the woman","voice":"female","keys":K(t,wom)},
         {"phrase":"to carry a big backpack","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to wave goodbye","target":"the woman","voice":"female","keys":K(t,wom)}],
 "stillS":8.5,
 "nouns":[{"word":"lights","x":.50,"y":.13,"voice":"female"},{"word":"a woman","x":.56,"y":.40,"voice":"female"},
          {"word":"food","x":.62,"y":.585,"voice":"female"},{"word":"a wheel","x":.50,"y":.78,"voice":"female"}],
 "question":"Where is the woman pointing?",
 "answer":["She","is","pointing","to","the","right."],"answerVoice":"female",
 "notes":"4.5 s: only a sliver of the man at the left edge (box 0.13 wide). 7.5 s: the man walks in front of the woman; her box holds only her visible face/left arm, his box starts at his head and misses the left part of his backpack. She waves only at 8.5 s."})

# ---- 419
t=T(19)
wom=[(0,0,.50,1),(0,.08,.52,.92),(0,.56,.85,.25),(0,.49,.88,.27),None,None,None,(.59,.08,.41,.92),(0,.45,.68,.30),(.34,.02,.66,.47),(0,.08,.45,.92),
 None,None,(0,.31,.39,.68),(0,.32,.40,.68),(0,.31,.40,.66),(.04,.27,.36,.59),(0,.24,.38,.28),(0,.26,.42,.70)]
man=[None,None,None,None,(.03,.45,.97,.55),(0,.38,1,.60),(.62,.05,.38,.93),None,None,None,None,
 (.10,.40,.72,.60),None,(.40,.27,.60,.73),(.41,.32,.59,.68),(.58,.49,.42,.50),(.58,.50,.42,.40),(.60,.25,.40,.64),(.66,.26,.34,.72)]
ball=[(.50,.26,.36,.22),(.53,.19,.41,.26),(.09,.16,.83,.40),(.16,.07,.81,.42),(.25,.23,.36,.22),(.53,.19,.25,.19),(.23,.44,.33,.22),
 (.30,.44,.29,.18),(.32,.25,.29,.20),(.46,.49,.29,.18),(.45,.19,.28,.21),(.33,.07,.26,.18),(0,.40,.24,.31),(.80,0,.20,.14),
 (.59,.16,.29,.16),(.63,.35,.19,.14),(.67,.36,.20,.14),(.22,.52,.20,.14),(.48,.50,.18,.16)]
save({"mediaId":419,"level":"A","keyWord":"kick","defaultVoice":"male",
 "taps":[{"phrase":"to wear green trousers","target":"the woman","voice":"female","keys":K(t,wom)},
         {"phrase":"to wear a purple T-shirt","target":"the man","voice":"male","keys":K(t,man)},
         {"phrase":"to fly through the air","target":"the ball","voice":"male","keys":K(t,ball)}],
 "stillS":8.0,
 "nouns":[{"word":"the sky","x":.50,"y":.08,"voice":"male"},{"word":"buildings","x":.50,"y":.34,"voice":"male"},
          {"word":"a woman","x":.20,"y":.45,"voice":"female"},{"word":"a ball","x":.77,"y":.44,"voice":"male"}],
 "question":"What are they doing?",
 "answer":["They","are","kicking","a","ball."],"answerVoice":"male",
 "notes":"Both people kick, so the two person phrases are states (clothes). The ball often lies in front of a person: there the person's box is cut (2.0, 2.5, 7.5, 8.0 s: man's box starts below the ball, so his head is outside; 4.5, 8.5 s: woman's box ends above the ball; 0.0, 3.5, 4.0 s: her kicking leg is partly outside). 1.0-1.5 s: only her foot is visible (close-up). 6.0 s: only the ball and the water tank."})
