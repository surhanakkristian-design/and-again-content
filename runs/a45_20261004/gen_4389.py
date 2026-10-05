import json
O=None
# (woman, man on block, man in water)
K={
0.0:(O,O,O),0.5:(O,O,O),
1.0:((.0,.17,.12,.45),(.13,.14,.47,.27),O),
1.5:((.0,.17,.10,.42),(.10,.04,.50,.54),O),
2.0:((.0,.17,.12,.60),(.13,.02,.36,.44),O),
2.5:((.0,.17,.17,.65),(.18,.03,.27,.43),O),
3.0:((.0,.19,.20,.72),(.20,.02,.22,.54),O),
3.5:((.0,.15,.28,.72),(.28,.0,.16,.52),(.55,.74,.40,.20)),
4.0:((.0,.10,.29,.58),(.29,.0,.15,.34),(.42,.56,.56,.28)),
4.5:((.0,.03,.56,.42),O,(.38,.46,.60,.28)),
5.0:((.0,.01,.58,.44),O,(.32,.46,.62,.36)),
5.5:((.0,.0,.36,.40),O,(.28,.43,.68,.42)),
6.0:(O,O,(.26,.45,.74,.27)),
6.5:(O,O,(.27,.35,.71,.37)),
7.0:(O,O,(.24,.29,.60,.58)),
7.5:(O,O,(.20,.17,.69,.75)),
8.0:(O,O,(.24,.09,.68,.87)),
8.5:(O,O,(.26,.07,.66,.92)),
9.0:(O,O,(.23,.05,.74,.95)),
9.5:(O,O,(.28,.04,.63,.96)),
10.0:(O,O,(.14,.04,.86,.96)),
}
def keys(i):
    r=[]
    for t in sorted(K):
        b=K[t][i]
        r.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return r
d={"mediaId":4389,"level":"A","keyWord":"start","defaultVoice":"male",
"taps":[
 {"phrase":"to wave her arm","target":"the woman in white","voice":"female","keys":keys(0)},
 {"phrase":"to stand on the block","target":"the man on the block","voice":"male","keys":keys(1)},
 {"phrase":"to climb out of the pool","target":"the man in the water","voice":"male","keys":keys(2)}],
"stillS":5.0,
"nouns":[{"word":"a woman","x":0.17,"y":0.10,"voice":"female"},
 {"word":"a swimmer","x":0.62,"y":0.62,"voice":"male"},
 {"word":"water","x":0.68,"y":0.28,"voice":"male"},
 {"word":"the floor","x":0.50,"y":0.88,"voice":"male"}],
"question":"What is the woman in white doing?",
"answer":["She","is","waving","her","arm."],
"answerVoice":"female",
"notes":"0.0-0.5 s: four swimmers bent on the blocks, none identifiable as a target, all off. 'The man on the block' = the swimmer in black shorts who stays standing (a second swimmer in green stands right behind him, inside the same box); from 4.5 s only his legs are in the picture, set off. The man in the water (first seen at 3.5 s) wears different trunks than the standing man, so he is treated as a separate person. Woman and standing man overlap at 3.5-4.0 s: split at x 0.28. Woman off from 6.0 s (only her arm at the edge). The woman's arm is stretched out at 4.5-5.5 s (waving per description). At 5.0 s a second swimmer's head is small in the far lane; the 'a swimmer' pill sits on the near one."}
json.dump(d,open("content/4389.json","w"),indent=1)
