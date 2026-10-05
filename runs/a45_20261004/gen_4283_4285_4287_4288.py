import json
def K(d,times):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(c): json.dump(c,open("content/%d.json"%c["mediaId"],"w"),indent=1,ensure_ascii=False)

# ---------- 4283
t=T(21)
C={0.0:(0,.25,.16,.75),0.5:(0,.25,.16,.75),1.0:(0,.25,.16,.75),1.5:(0,.25,.16,.75),
   2.0:(0,.33,.18,.57),2.5:(0,.33,.18,.57),3.0:(0,.33,.18,.57)}
for x in (3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5): C[x]=(0,.33,.25,.57)
S={0.0:(.17,.03,.83,.69),0.5:(.17,.03,.83,.69),1.0:(.17,.03,.83,.69),1.5:(.17,.03,.83,.69),
   2.0:(.19,.15,.81,.53),2.5:(.19,.15,.81,.53),3.0:(.19,.15,.81,.53),
   8.0:(0,.02,1.0,.72),8.5:(0,.02,1.0,.72),9.0:(0,.02,1.0,.76),9.5:(0,.02,1.0,.76),10.0:(0,.02,1.0,.78)}
for x in (3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5): S[x]=(.26,.15,.74,.53)
save({"mediaId":4283,"level":"A","keyWord":"cooking","defaultVoice":"female",
"taps":[
{"phrase":"to cook food in a pan","target":"the chef","voice":"female","keys":K(C,t)},
{"phrase":"to put food on a plate","target":"the chef","voice":"female","keys":K(C,t)},
{"phrase":"to clap their hands","target":"the students","voice":"female","keys":K(S,t)}],
"stillS":4.0,
"nouns":[{"word":"lights","x":.60,"y":.13,"voice":"female"},{"word":"a chef","x":.13,"y":.58,"voice":"female"},
{"word":"a plate","x":.50,"y":.72,"voice":"female"},{"word":"a pan","x":.27,"y":.87,"voice":"female"}],
"question":"What is the chef doing?",
"answer":["She","is","cooking","food","in","a","pan."],
"answerVoice":"female",
"notes":"Three shots (0-1.5 close, 2.0-7.5 wide, 8.0-10.0 close). The chef (woman in white, left edge) cooks in the wok only in the first shot and puts food on the plates in the second; she is out of the picture from 8.0 s (the clapping hands at the left edge at 8.0 s are not clearly hers). 'the students' = the whole group in aprons as one target; they clap only in the last shot. The chef overlaps the group in the picture, so the boxes are split along a vertical line: her outstretched arm and the students at the far left fall outside their boxes. The pan is a wok ('a pan' for level A)."})

# ---------- 4285
t=T(19)
M={0.0:(0,.08,.97,.92),0.5:(0,.08,1.0,.92),1.0:(0,.22,.90,.45),1.5:(0,0,.78,.75),2.0:(0,0,1.0,1.0),2.5:(0,0,1.0,1.0),
   3.0:(.17,.20,.80,.62),3.5:(0,.22,.80,.58),4.0:(0,.19,.84,.52),4.5:(0,.20,.84,.51),5.0:(0,.20,.85,.62),
   5.5:(.20,.26,.62,.74),6.0:(.29,.24,.71,.76),6.5:(.16,.25,.70,.75),7.0:(.11,.22,.82,.78),7.5:(0,.23,.93,.77),
   8.0:(0,.28,.80,.72),8.5:(0,.29,.85,.71),9.0:(0,.22,.82,.78)}
save({"mediaId":4285,"level":"A","keyWord":"adult","defaultVoice":"male",
"taps":[
{"phrase":"to put on a tie","target":"the man","voice":"male","keys":K(M,t)},
{"phrase":"to drink from a cup","target":"the man","voice":"male","keys":K(M,t)},
{"phrase":"to write with a pen","target":"the man","voice":"male","keys":K(M,t)}],
"stillS":4.0,
"nouns":[{"word":"a lamp","x":.53,"y":.14,"voice":"male"},{"word":"an adult","x":.40,"y":.40,"voice":"male"},
{"word":"a table","x":.86,"y":.68,"voice":"male"},{"word":"papers","x":.50,"y":.82,"voice":"male"}],
"question":"What is he doing at the table?",
"answer":["He","is","writing","with","a","pen."],
"answerVoice":"male",
"notes":"Only one possible target (the man in the blue shirt), used for all three phrases; the people in the street (8.0-9.0 s) are a blurred crowd and do none of the three things. At 1.0 s and 1.5 s only his hand / arm is in the picture (box on it). Key word 'an adult' is placed on the man, so no 'a tie' / 'a pen' noun on the same figure. 'a table': the pill sits on the dark table top right of the paper pile; 'a lamp' is the ceiling light."})

# ---------- 4287
G={0.5:(.48,.21,.24,.79),1.0:(0,.22,.73,.78),1.5:(0,.22,.72,.78),2.0:(.04,.17,.92,.83),2.5:(.18,.30,.72,.70),
   3.0:(.30,.32,.70,.68),3.5:(.37,.31,.63,.69),4.0:(.42,.30,.58,.70),4.5:(.29,.38,.71,.62),
   6.0:(.45,.32,.55,.68),6.5:(.45,.30,.55,.70),7.0:(.10,.25,.83,.75),7.5:(.17,.26,.78,.74),8.0:(.20,.21,.72,.79),8.5:(.28,.21,.52,.79)}
L={1.0:(.74,.34,.16,.66),1.5:(.73,.35,.20,.65),6.0:(0,.25,.25,.75),6.5:(0,.34,.44,.66),7.0:(0,.30,.09,.70),
   7.5:(0,.32,.16,.68),8.0:(0,.20,.19,.80),8.5:(0,.22,.27,.78),9.0:(.08,.20,.50,.75)}
GN="the woman in the green jacket"; LN="the woman with long hair"
save({"mediaId":4287,"level":"B","keyWord":"view","defaultVoice":"female",
"taps":[
{"phrase":"to draw back the curtains","target":GN,"voice":"female","keys":K(G,t)},
{"phrase":"to dangle the keys","target":GN,"voice":"female","keys":K(G,t)},
{"phrase":"to embrace the man tightly","target":LN,"voice":"female","keys":K(L,t)}],
"stillS":7.0,
"nouns":[{"word":"spotlights","x":.48,"y":.09,"voice":"female"},{"word":"keys","x":.33,"y":.47,"voice":"female"},
{"word":"a lanyard","x":.48,"y":.60,"voice":"female"},{"word":"a tablet","x":.80,"y":.69,"voice":"female"}],
"question":"What is the woman in green doing?",
"answer":["She","is","dangling","a","set","of","keys."],
"answerVoice":"female",
"notes":"Many cuts. The agent (green jacket) pulls the curtains aside at 3.0 s and dangles the keys at 7.0-7.5 s. The woman with long hair throws her arm round the man at 8.5 s and they hug at 9.0 s; the hug is mutual, the phrase names 'the man' as its object so it fits only her. At 9.0 s her box covers her head, shoulder and part of her arm and unavoidably part of the man (he is not a target); the agent is almost hidden there (off). 5.0 s: a hand on the worktop at the right edge, owner unclear, agent marked off. The man is not used as a target (no action that only he does). At 7.0 s the long-haired woman is only a sliver at the left edge (thin box). The key word 'view' (verb) is not in the answer: no single target views the flat alone. 'a tablet': the dark device under her arm (in other shots she carries it with a folder)."})

# ---------- 4288
t=T(17)
W={0.0:(.15,.08,.85,.92),0.5:(.12,.08,.88,.92),1.0:(0,.08,.41,.92),1.5:(0,.10,.65,.90),2.0:(0,.10,.57,.90),2.5:(0,.10,.62,.90),
   3.0:(0,.10,.58,.90),3.5:(0,.38,.18,.62),4.0:(0,.27,.20,.73),4.5:(0,.25,.22,.75),5.0:(0,.30,.20,.70),
   5.5:(0,.08,.68,.92),6.0:(0,.08,.68,.92),6.5:(0,.08,.58,.92)}
P={0.0:(0,.36,.14,.15),0.5:(0,.36,.11,.13),1.0:(.42,.37,.58,.33),1.5:(.66,.38,.34,.30),2.0:(.58,.39,.42,.28),2.5:(.63,.38,.37,.30),
   3.0:(.59,.40,.41,.30),5.5:(.69,.38,.31,.26),6.0:(.69,.37,.31,.28),6.5:(.59,.36,.41,.28)}
save({"mediaId":4288,"level":"A","keyWord":"target","defaultVoice":"female",
"taps":[
{"phrase":"to close one eye","target":"the woman","voice":"female","keys":K(W,t)},
{"phrase":"to hold an arrow","target":"the woman","voice":"female","keys":K(W,t)},
{"phrase":"to stand behind the woman","target":"the people","voice":"female","keys":K(P,t)}],
"stillS":4.0,
"nouns":[{"word":"the sky","x":.60,"y":.12,"voice":"female"},{"word":"a bow","x":.14,"y":.25,"voice":"female"},
{"word":"a target","x":.84,"y":.52,"voice":"female"},{"word":"grass","x":.55,"y":.80,"voice":"female"}],
"question":"What is the woman looking at?",
"answer":["She","is","looking","at","a","target."],
"answerVoice":"female",
"notes":"'the people' = the blurred group of watchers behind the archer, one target; where they stand on both sides of her head the box takes the larger group on the right (0.0-0.5 s only a small group at the left edge, small box). The archer fills the picture, so her box is cut along a vertical line next to the group and loses her far shoulder / elbow. 3.5-5.0 s: only her arm and shoulder at the left edge. 7.0-8.0 s: only parts of the bow, both targets off. Three targets stand apart at 4.0 s; the 'a target' pill is on the big right one and no other noun is on the other two. The answer joins the two shots (her aiming / the targets)."})
