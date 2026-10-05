import json
O=None
def keys(K,i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
def save(d):
    json.dump(d,open("content/%d.json"%d["mediaId"],"w"),indent=1,ensure_ascii=False)

# 4398 (woman, billboard)
K={0.0:((0,.08,1,.92),O),0.5:((0,.15,1,.85),O),1.0:((0,.52,1,.48),O),1.5:((.10,.72,.90,.28),O),2.0:((.20,.82,.65,.18),O),
2.5:(O,(.25,.24,.40,.24)),3.0:(O,(.28,.24,.42,.24)),3.5:(O,(.33,.23,.44,.24)),4.0:(O,(.37,.22,.46,.24)),4.5:(O,(.43,.20,.47,.25)),
5.0:((.25,.45,.60,.55),O),5.5:((.35,.45,.50,.55),O),6.0:((.33,.46,.47,.54),O),6.5:((.18,.46,.82,.54),O),7.0:((.20,.52,.58,.48),O),
7.5:((.05,.55,.95,.45),O),8.0:((.05,.50,.75,.50),O),8.5:((0,.48,.75,.52),O),9.0:((0,.50,.88,.50),O)}
save({"mediaId":4398,"level":"A","keyWord":"advertisement","defaultVoice":"female",
"taps":[
 {"phrase":"to open her mouth wide","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to look up at the screens","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to show a house","target":"the billboard","voice":"female","keys":keys(K,1)}],
"stillS":3.5,
"nouns":[{"word":"an advertisement","x":0.55,"y":0.33,"voice":"female"},
 {"word":"the sky","x":0.60,"y":0.12,"voice":"female"},
 {"word":"a road","x":0.60,"y":0.68,"voice":"female"}],
"question":"What is the woman looking at?",
"answer":["She","is","looking","at","a","big","advertisement."],
"answerVoice":"female",
"notes":"Three shots: bus stop (woman), train window (billboard with a house, woman not visible - only a faint reflection, set off), Times Square (woman). Two phrases share the woman; no third clear target (statue/crowd too small). 'to look up at the screens' is literally true only in the Times Square shot, but she looks up in every shot she is in. Nouns on the train-window shot: two small cars and green road signs left unlabelled on purpose."})

# 4399 (woman, billboard, screens)
T=(.34,.03,.33,.58)
K={0.0:((0,.30,.62,.70),O,O),0.5:((0,.30,.64,.70),O,O),1.0:((0,.32,.66,.68),O,O),1.5:((0,.33,.66,.67),O,O),2.0:((0,.37,.62,.63),O,O),
2.5:(O,(.04,.21,.80,.46),O),3.0:(O,(.20,.23,.78,.44),O),3.5:(O,(.45,.24,.55,.43),O),4.0:(O,(.72,.28,.28,.38),O),4.5:(O,O,O),5.0:(O,O,O),
5.5:((.38,.62,.26,.25),O,T),6.0:((.36,.62,.30,.24),O,T),6.5:((.38,.62,.28,.24),O,T),7.0:((.38,.63,.28,.24),O,T),7.5:((.39,.63,.32,.24),O,T),
8.0:((.40,.62,.26,.24),O,T),8.5:((.37,.62,.32,.24),O,T),9.0:((.37,.63,.28,.24),O,T),9.5:((.37,.63,.30,.24),O,T),10.0:((.37,.62,.30,.24),O,T)}
save({"mediaId":4399,"level":"A","keyWord":"dream","defaultVoice":"female",
"taps":[
 {"phrase":"to touch the glass","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to show a big house","target":"the billboard","voice":"female","keys":keys(K,1)},
 {"phrase":"to show a pink bottle","target":"the tall screens","voice":"female","keys":keys(K,2)}],
"stillS":0.5,
"nouns":[{"word":"a burger","x":0.75,"y":0.25,"voice":"female"},
 {"word":"hands","x":0.58,"y":0.60,"voice":"female"},
 {"word":"a jacket","x":0.25,"y":0.78,"voice":"female"},
 {"word":"the sky","x":0.22,"y":0.12,"voice":"female"}],
"question":"What is the woman dreaming of?",
"answer":["She","is","dreaming","of","a","big","burger."],
"answerVoice":"female",
"notes":"Key word 'dream' is not literally visible; the question reads her open-mouthed look at the giant burger picture as dreaming (weak spot - fallback: 'What is the woman looking at?' / 'She is looking at a big burger.'). The pink bottle is on the screens only 5.5-7.5 s, the tower itself stays visible to the end. Woman box in Times Square starts at y 0.62 right under the screens box (ends 0.61). 'glasses' not used as a noun because their reflection shows on the poster too."})

# 4401 (woman, viewer)
W=(0,.17,1,.83)
K={0.0:((.02,.18,.98,.82),O),0.5:(W,O),1.0:((0,.18,1,.82),O),1.5:((0,.18,1,.82),O),2.0:(W,O),2.5:((0,.15,1,.85),O),3.0:(W,O),3.5:(W,O),
4.0:((0,.15,1,.85),O),4.5:((.05,.15,.95,.85),O),5.0:((.10,.18,.90,.82),O),5.5:((.10,.18,.90,.82),O),
6.0:((0,.33,.24,.67),(.24,.13,.68,.87)),6.5:((0,.29,.25,.71),(.25,.13,.67,.87)),7.0:((0,.28,.30,.72),(.30,.16,.62,.84)),
7.5:((0,.28,.27,.72),(.27,.16,.67,.84)),8.0:((0,.27,.42,.73),(.42,.13,.52,.87)),8.5:((0,.26,.45,.74),(.45,.13,.50,.87)),
9.0:((0,.27,.48,.73),(.48,.14,.45,.86))}
save({"mediaId":4401,"level":"B","keyWord":"far","defaultVoice":"female",
"taps":[
 {"phrase":"to peer through binoculars","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to jot down a note","target":"the woman","voice":"female","keys":keys(K,0)},
 {"phrase":"to rest on a metal post","target":"the tower viewer","voice":"female","keys":keys(K,1)}],
"stillS":5.5,
"nouns":[{"word":"binoculars","x":0.48,"y":0.33,"voice":"female"},
 {"word":"a notebook","x":0.48,"y":0.57,"voice":"female"},
 {"word":"a lake","x":0.17,"y":0.20,"voice":"female"},
 {"word":"a forest","x":0.62,"y":0.05,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","peering","through","a","pair","of","binoculars."],
"answerVoice":"female",
"notes":"Only two targets (woman, coin-operated viewer). In the canyon shot the woman and the viewer overlap (her hand is on the viewer, at 6.0 her arm reaches across the post to the coin box): boxes are split along a vertical line, so her reaching arm / the viewer's left edge are cut. Key word 'far' (adjective) not used in a noun or the answer. She writes in the notebook only at about 5.0-5.5 s."})

# 4402 (man in cap, curly woman, bearded man)
K={0.0:((0,.08,1,.92),O,O),0.5:((0,.06,1,.94),O,O),1.0:((0,.08,1,.92),O,O),1.5:((0,.08,1,.92),O,O),2.0:((.14,.10,.86,.90),O,O),
2.5:((.36,.03,.64,.90),(0,.10,.34,.30),O),3.0:((.23,0,.77,.95),(0,.13,.23,.30),O),3.5:((.35,.05,.65,.95),(0,.17,.33,.30),O),
4.0:((.22,.04,.78,.92),(0,.14,.21,.30),O),4.5:((.20,.10,.80,.90),(0,.20,.17,.27),O),5.0:((.08,0,.92,.92),O,O),5.5:((0,.08,1,.92),O,O),
6.0:((0,0,1,1),O,O),6.5:((0,0,1,1),O,O),7.0:((.04,.10,.96,.90),O,O),
7.5:((.30,.17,.57,.60),(0,.25,.30,.37),O),
8.0:((.39,.26,.30,.38),(0,.25,.39,.42),(.69,.21,.31,.52)),
8.5:((.36,.29,.31,.33),(.11,.30,.24,.33),(.67,.29,.18,.38)),
9.0:((.42,.37,.21,.27),(.20,.39,.22,.24),(.63,.38,.18,.28))}
save({"mediaId":4402,"level":"B","keyWord":"appetite","defaultVoice":"male",
"taps":[
 {"phrase":"to bite into an apple","target":"the man in the cap","voice":"male","keys":keys(K,0)},
 {"phrase":"to have long curly hair","target":"the curly-haired woman","voice":"female","keys":keys(K,1)},
 {"phrase":"to grip a chicken drumstick","target":"the bearded man","voice":"male","keys":keys(K,2)}],
"stillS":5.0,
"nouns":[{"word":"a cap","x":0.52,"y":0.07,"voice":"male"},
 {"word":"a hoodie","x":0.72,"y":0.33,"voice":"male"},
 {"word":"a watermelon","x":0.58,"y":0.52,"voice":"male"},
 {"word":"a blanket","x":0.42,"y":0.90,"voice":"male"}],
"question":"Who has a huge appetite?",
"answer":["The","man","in","the","cap","has","a","huge","appetite."],
"answerVoice":"male",
"notes":"The curly-haired woman gets a state phrase: her actions (smiling, biting the burger tower, eating) are shared with others in the wide shot. The bearded man is fully visible only 8.0-9.0 s (at 7.5 only his hand with the drumstick and a blue sleeve at the right edge - set off). At 4.5 only the woman's hair is at the left edge. In the wide shot (8.0-9.0) the three targets sit shoulder to shoulder, boxes split between them; two more women (far left, blonde right) are not targets. 'a watermelon' at 5.0 is a big slice."})
