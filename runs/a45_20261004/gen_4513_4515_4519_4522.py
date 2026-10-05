import json
def K(times, rows):
    out=[]
    assert len(times)==len(rows),(len(times),len(rows))
    for t,r in zip(times,rows):
        if r is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def W(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4513
t=T(21)
w=[(.08,.14,.92,.86),(.02,.13,.98,.87),(0,.20,1,.80),(0,.24,1,.76),(.08,.32,.92,.68),(.03,.28,.97,.72),(.02,.27,.98,.73),(.02,.26,.98,.74),
(0,.26,1,.74),(0,.26,1,.74),(.02,.27,.98,.73),(.03,.26,.97,.74),(.03,.25,.97,.75),(.03,.25,.97,.75),(0,.25,1,.75),(.05,.26,.95,.74),
(.08,.24,.92,.76),(.22,.25,.78,.75),(.09,.26,.91,.74),(.06,.26,.94,.74),(0,.20,.34,.80)]
k=K(t,w)
W({"mediaId":4513,"level":"A","keyWord":"suitcase","defaultVoice":"female",
"taps":[{"phrase":"to point at the board","target":"the woman","voice":"female","keys":k},
{"phrase":"to look at her watch","target":"the woman","voice":"female","keys":k},
{"phrase":"to open her passport","target":"the woman","voice":"female","keys":k}],
"stillS":4.5,
"nouns":[{"word":"a passport","x":.22,"y":.60,"voice":"female"},{"word":"a watch","x":.45,"y":.73,"voice":"female"},
{"word":"a suitcase","x":.22,"y":.89,"voice":"female"},{"word":"a jacket","x":.75,"y":.88,"voice":"female"}],
"question":"What is the woman holding?",
"answer":["She","is","holding","her","passport."],"answerVoice":"female",
"notes":"Only one clear target (background people are blurred), so all three phrases are on the woman. Of the suitcase only the handle is visible (bottom left); the pill sits on the handle. She holds passport plus tickets; the answer names only the passport."})

# 4515
t=T(19)
w=[(.03,.10,.97,.90),(0,0,1,1),(0,.02,1,.98),(.04,.03,.96,.97),(.03,.03,.97,.97),(.10,.07,.90,.93),(.10,.06,.90,.94),(.05,.02,.95,.98),
(.02,.03,.98,.97),(0,.04,1,.96),(0,.04,1,.96),(0,.04,1,.96),(0,.06,1,.94),(0,.06,1,.94),(0,.07,1,.93),(0,.08,1,.92),(0,.09,1,.91),(0,.10,1,.90),(0,.09,.98,.91)]
k=K(t,w)
W({"mediaId":4515,"level":"A","keyWord":"to win","defaultVoice":"male",
"taps":[{"phrase":"to get a medal","target":"the young man","voice":"male","keys":k},
{"phrase":"to look at his medal","target":"the young man","voice":"male","keys":k},
{"phrase":"to smile at the camera","target":"the young man","voice":"male","keys":k}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":.40,"y":.05,"voice":"male"},{"word":"trees","x":.80,"y":.28,"voice":"male"},
{"word":"a T-shirt","x":.72,"y":.60,"voice":"male"},{"word":"a medal","x":.50,"y":.79,"voice":"male"}],
"question":"What is the young man looking at?",
"answer":["He","is","looking","at","his","new","medal."],"answerVoice":"male",
"notes":"One target only: the volunteer is just arms that cross the runner's body (2.0-4.0 s), no clean separate box possible. The key word 'to win' is not in the texts (a past-tense 'He won a medal' would break the present-continuous rule). The race number changes 299/295 in the clip (generation artefact), so no noun on it."})

# 4519
t=T(25)
man=[(.37,.21,.63,.79),(.36,.22,.64,.78),(.30,.24,.70,.76),(.32,.23,.68,.77),(.44,.18,.56,.82),(.52,.17,.48,.83),(.48,.17,.52,.83),
(.59,.15,.41,.44),(.59,.15,.41,.46),(.59,.14,.41,.47),(.59,.16,.41,.47),(.59,.16,.41,.47),(.60,.13,.40,.49),(.60,.16,.40,.46),(.60,.18,.40,.50)]+[None]*10
logs=[(0,.58,.36,.24),(0,.58,.35,.24),(.04,.58,.25,.24),(.06,.58,.25,.24),(.05,.58,.38,.22),(.03,.59,.47,.22),(0,.59,.46,.24),
(0,.40,.58,.40),(0,.39,.58,.41),(0,.33,.58,.47),(0,.20,.58,.60),(0,0,.58,.80),(0,.08,.59,.72),(0,.03,.59,.77),(0,.20,.59,.63)]+[None]*10
smoke=[None]*15+[(.28,0,.40,.32),(.33,.04,.36,.36),(.28,.05,.40,.43),(.25,.08,.43,.50),(.25,.12,.43,.51),(.25,.10,.45,.59),(.25,.13,.45,.59),(.23,.15,.47,.58),(.23,.15,.47,.59),(.23,.15,.47,.60)]
W({"mediaId":4519,"level":"B","keyWord":"ash","defaultVoice":"male",
"taps":[{"phrase":"to kneel by the fireplace","target":"the man","voice":"male","keys":K(t,man)},
{"phrase":"to catch fire","target":"the logs","voice":"male","keys":K(t,logs)},
{"phrase":"to rise from the chimney","target":"the smoke","voice":"male","keys":K(t,smoke)}],
"stillS":5.0,
"nouns":[{"word":"flames","x":.45,"y":.33,"voice":"male"},{"word":"a jumper","x":.80,"y":.46,"voice":"male"},
{"word":"logs","x":.33,"y":.63,"voice":"male"},{"word":"ash","x":.40,"y":.88,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","lighting","a","fire","in","the","fireplace."],"answerVoice":"male",
"notes":"From 3.5 s the log pile and the man overlap in the picture (right log reaches under his arm): boxes split on a vertical line at x 0.59, so the right end of the pile is outside the logs box. The logs box includes the flames. 'to catch fire' has 3 words. Smoke box = the plume above the chimney only. The man is not seen striking a match; 'lighting a fire' rests on him arranging the logs and the fire catching."})

# 4522
t=T(25)
woman=[(.14,.40,.84,.60),(.16,.40,.70,.60),(.11,.43,.89,.57),(.09,.41,.70,.59),(.02,.46,.70,.54),(0,.46,.64,.54),(.06,.46,.66,.54),(.24,.45,.76,.55),(.20,.46,.69,.54),
(0,.39,.65,.42),(0,.50,1,.32),(0,.50,1,.36),(0,.49,1,.51),(.26,.50,.74,.50),(.24,.50,.76,.50),(.24,.50,.76,.50),
(0,.34,.80,.50),(0,.23,.82,.55),(0,.24,.88,.50),(0,.18,.95,.50),(0,.19,.95,.52),(0,.26,.86,.44),(0,.24,.82,.46),(0,.23,.89,.47),(0,.23,.89,.50)]
man=[None]*9+[(.66,.34,.24,.15),(.64,.35,.24,.14),(.62,.35,.26,.14),(.57,.34,.27,.14),(.55,.35,.28,.14),(.52,.35,.28,.14),(.49,.35,.28,.14)]+[None]*9
kw=K(t,woman)
W({"mediaId":4522,"level":"A","keyWord":"tour","defaultVoice":"female",
"taps":[{"phrase":"to lie in a boat","target":"the woman","voice":"female","keys":kw},
{"phrase":"to hold chopsticks","target":"the woman","voice":"female","keys":kw},
{"phrase":"to hold a long stick","target":"the man","voice":"male","keys":K(t,man)}],
"stillS":5.0,
"nouns":[{"word":"the sky","x":.60,"y":.08,"voice":"female"},{"word":"mountains","x":.32,"y":.31,"voice":"female"},
{"word":"water","x":.20,"y":.56,"voice":"female"},{"word":"a boat","x":.50,"y":.90,"voice":"female"}],
"question":"Where is the woman lying?",
"answer":["She","is","lying","in","a","boat."],"answerVoice":"female",
"notes":"Three shots (wall 0-4.0, river 4.5-7.5, market 8.0-12.0). The man on the raft is small and sits just above the woman's head: in the river shot her box starts at y 0.50 (cap tip cut off) and at 4.5 s it is cut at x 0.65 instead. 'chopsticks' may be above A level; 'a long stick' = his pole. The key word 'tour' is not a visible noun and is not used. The second 'a boat' could also be read as the far raft, but the pill is on the wooden boat in front."})
