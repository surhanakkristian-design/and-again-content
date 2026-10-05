import json
def K(times, rows):
    out=[]
    for t,r in zip(times,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":round(r[2],2),"h":round(r[3],2)})
    return out
def B(x0,y0,x1,y1): return (x0,y0,x1-x0,y1-y0)
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 6824
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=K(T,[B(.30,.26,1,.60),B(.28,.23,1,.61),B(.48,.19,1,.86),B(.48,.18,1,.82),B(.48,.13,1,.85),B(.44,.09,1,1),B(.43,.07,1,1),B(.40,.07,1,1)])
gau=K(T,[B(.30,.61,.48,.75),B(.30,.62,.48,.76),B(.29,.64,.47,.80),B(.28,.60,.47,.80),B(.20,.61,.47,.83),B(.17,.61,.43,.86),B(.14,.66,.42,.92),B(.12,.68,.39,.93)])
buc=K(T,[B(.28,.76,.46,.95),B(.28,.77,.47,.97),B(.28,.81,.47,1),B(.24,.83,.60,1),B(.20,.86,.66,1),None,None,None])
save({"mediaId":6824,"level":"B","keyWord":"air conditioning","defaultVoice":"male",
 "taps":[{"phrase":"to wipe his sweaty forehead","target":"the man","voice":"male","keys":man},
         {"phrase":"to display the pressure","target":"the gauges","voice":"male","keys":gau},
         {"phrase":"to collect dripping water","target":"the bucket","voice":"male","keys":buc}],
 "stillS":0.2,
 "nouns":[{"word":"air conditioning","x":.72,"y":.76,"voice":"male"},{"word":"a bucket","x":.38,"y":.87,"voice":"male"},
          {"word":"a cap","x":.62,"y":.31,"voice":"male"},{"word":"the sky","x":.45,"y":.06,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","servicing","the","air","conditioning."],"answerVoice":"male",
 "notes":"Man and gauges touch (he holds them): man box is cut at the gauges, so his hands/forearms near the gauges fall outside his box. Bucket leaves the picture after 2.2 s (sliver at 2.7 marked off). Noun 'air conditioning' (key word, mass noun) sits on the front unit; three units are visible. 'servicing' is inferred from gauges/hoses."})

# 4858
T=[i*0.5 for i in range(19)]
man=K(T,[B(.08,0,.85,.50),B(.10,0,.90,.48),B(.08,0,.88,.46),B(.13,0,.92,.44),B(0,0,.30,.56),B(0,.57,.28,.78),None,B(.74,0,1,.72),B(.77,0,1,.53),B(.67,.42,1,.58),B(.60,.44,1,.63),None,None,None,B(.54,.03,.90,.33),B(.59,.02,.86,.27),B(.54,.10,.80,.32),B(.49,.10,.75,.34),B(.47,.12,.75,.34)])
dom=K(T,[B(.15,.51,1,.80),B(.15,.49,1,.76),B(.15,.47,1,.72),B(.10,.45,1,.74),B(.31,.27,1,.82),B(.30,.28,1,1),B(0,.35,1,1),B(0,.33,.73,1),B(0,.33,.76,1),B(0,.38,.66,1),B(0,.40,.59,1),B(0,.38,1,1),B(0,.34,1,1),B(0,.20,1,1),B(0,.34,1,1),B(0,.28,1,1),B(0,.33,1,1),B(0,.35,1,1),B(0,.35,1,1)])
save({"mediaId":4858,"level":"B","keyWord":"spiral","defaultVoice":"male",
 "taps":[{"phrase":"to topple the first domino","target":"the man","voice":"male","keys":man},
         {"phrase":"to clench his fists","target":"the man","voice":"male","keys":man},
         {"phrase":"to form a huge spiral","target":"the dominoes","voice":"male","keys":dom}],
 "stillS":8.5,
 "nouns":[{"word":"a spiral","x":.45,"y":.55,"voice":"male"},{"word":"a man","x":.62,"y":.22,"voice":"male"},{"word":"the floor","x":.30,"y":.90,"voice":"male"}],
 "question":"What has the man built?",
 "answer":["He","has","built","a","huge","spiral","of","dominoes."],"answerVoice":"male",
 "notes":"Only two targets (man, dominoes); they overlap in the picture, boxes split along a line (0-1.5 s: man above, front domino loop below; his fingertip reaches into the domino box). 2.5 and 4.0-5.0 s only his hand / hair is visible. Domino box at 7.0-9.0 s leaves out the squiggly lines behind the man. Question uses present perfect (result shown in the wide shot)."})

# 5566
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
run=K(T,[B(0,.20,.74,1),B(0,.13,.69,1),B(0,.20,.64,.97),B(0,.17,.65,.98),B(0,.17,.61,.95),B(.03,.18,.60,.93),B(.20,.18,.63,.95),B(.32,.24,.61,.94)])
spe=K(T,[B(.75,.46,1,.76),B(.70,.41,1,.74),B(.65,.40,1,.66),B(.66,.40,.86,.64),B(.62,.40,.80,.62),B(.61,.40,.75,.60),B(.64,.35,1,.49),B(.62,.37,1,.51)])
hoo=K(T,[None,None,None,B(.87,.33,1,1),B(.81,.32,1,.82),B(.76,.37,1,.80),B(.64,.50,.97,.73),B(.62,.52,.95,.73)])
save({"mediaId":5566,"level":"B","keyWord":"arrival","defaultVoice":"female",
 "taps":[{"phrase":"to cross the finish line","target":"the runner","voice":"female","keys":run},
         {"phrase":"to bend down for the tape","target":"the woman in the hoodie","voice":"female","keys":hoo},
         {"phrase":"to cheer behind the barriers","target":"the spectators","voice":"female","keys":spe}],
 "stillS":3.7,
 "nouns":[{"word":"a runner","x":.47,"y":.60,"voice":"female"},{"word":"spectators","x":.80,"y":.45,"voice":"female"},
          {"word":"bunting","x":.75,"y":.28,"voice":"female"},{"word":"paper cups","x":.15,"y":.76,"voice":"female"}],
 "question":"What is the runner doing?",
 "answer":["She","is","crossing","the","finish","line."],"answerVoice":"female",
 "notes":"Runner's outstretched right arm lies outside her box (it passes over the spectators / the woman in the hoodie). Spectators box is narrow at 2.2-2.7 s (squeezed between runner and hoodie woman) and at 3.2-3.7 s it is the strip above the bending woman. The man in the rust T-shirt is not a target (he applauds like the spectators). Key word 'arrival' is abstract and not used in the texts."})

# 4538
T=[i*0.5 for i in range(25)]
wom=K(T,[(.15,.05,.78,.70),(.20,.05,.80,.72),(.28,.05,.68,.95),(.22,.03,.78,.97),(.17,.03,.76,.94),(.17,.05,.80,.87),(.09,.22,.58,.68),(0,.24,.73,.72),(.34,.29,.52,.42),(.30,.22,.63,.62),(.38,.17,.62,.83),(.33,0,.67,.65),(.18,0,.82,.57),(.52,0,.48,.50),None,(0,.44,.24,.17),(0,.37,.45,.25),(0,.37,.55,.25),(.07,.38,.55,.25),(.08,.38,.52,.25),(.09,.38,.55,.24),(.08,.38,.55,.24),(.09,.38,.56,.25),(.08,.38,.55,.25),(.10,.37,.57,.26)])
save({"mediaId":4538,"level":"B","keyWord":"rest","defaultVoice":"female",
 "taps":[{"phrase":"to scrub the glass table","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to tie up a bin bag","target":"the woman","voice":"female","keys":wom},
         {"phrase":"to recline on the sofa","target":"the woman","voice":"female","keys":wom}],
 "stillS":12.0,
 "nouns":[{"word":"a sofa","x":.45,"y":.66,"voice":"female"},{"word":"a radiator","x":.85,"y":.53,"voice":"female"},
          {"word":"a light bulb","x":.80,"y":.11,"voice":"female"},{"word":"a bookcase","x":.55,"y":.38,"voice":"female"}],
 "question":"Where is the woman having a rest?",
 "answer":["She","is","having","a","rest","on","the","sofa."],"answerVoice":"female",
 "notes":"Only one target (the woman) for all three phrases; the mop is in the picture for one frame only. 5.5-6.5 s show only her hands / legs; 7.0 s she is out of the picture (off); 7.5 s only her legs on the sofa. 'a bookcase' = the open wooden shelf unit beside the window."})
