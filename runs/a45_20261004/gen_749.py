import json
OFF=None
# t: (woman, man, duck)
K={
0.0:((.02,.12,.48,.88),(.52,.08,.48,.92),OFF),
0.5:((.02,.15,.48,.85),(.52,.10,.48,.90),OFF),
1.0:((0,.20,.50,.80),(.52,.18,.48,.82),OFF),
1.5:((0,.25,.48,.75),(.50,.23,.50,.77),OFF),
2.0:((0,.05,.50,.95),(.52,0,.48,1),OFF),
2.5:((0,.30,.50,.70),(.52,.25,.48,.75),OFF),
3.0:((0,.30,.48,.70),(.50,.28,.50,.72),OFF),
3.5:((0,.20,.49,.78),(.50,.20,.50,.75),OFF),
4.0:((.05,.20,.44,.66),(.50,.20,.50,.65),OFF),
4.5:((.19,.24,.33,.58),(.53,.22,.47,.62),(0,.45,.18,.14)),
5.0:((.20,.26,.33,.66),(.54,.26,.46,.68),(0,.47,.19,.14)),
5.5:((.22,.28,.31,.66),(.54,.28,.46,.68),(.02,.48,.19,.14)),
6.0:((.22,.20,.34,.70),(.57,.26,.43,.64),(.02,.52,.19,.14)),
6.5:((.22,.13,.30,.85),(.53,.11,.47,.87),(.02,.55,.19,.14)),
7.0:((.26,.20,.24,.80),(.51,.18,.32,.82),(.06,.57,.19,.14)),
7.5:((.20,.34,.24,.23),(.45,.24,.35,.76),(.12,.58,.20,.14)),
8.0:((.17,.39,.27,.24),(.45,.25,.33,.75),(.12,.64,.22,.14)),
8.5:((.03,.24,.47,.76),(.51,.23,.49,.77),OFF),
9.0:((.02,.28,.43,.72),(.52,.26,.48,.74),OFF),
9.5:((0,.32,.44,.68),(.57,.30,.43,.70),OFF),
10.0:((0,.35,.30,.65),(.56,.30,.44,.70),(.31,.66,.18,.14)),
}
def keys(i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
d={"mediaId":749,"level":"A","keyWord":"stretch","defaultVoice":"male",
"taps":[
 {"phrase":"to touch his leg","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to wear a green T-shirt","target":"the man","voice":"male","keys":keys(1)},
 {"phrase":"to walk by the water","target":"the duck","voice":"male","keys":keys(2)}],
"stillS":7.0,
"nouns":[{"word":"trees","x":.75,"y":.20,"voice":"male"},
 {"word":"a duck","x":.21,"y":.65,"voice":"male"},
 {"word":"water","x":.82,"y":.70,"voice":"male"},
 {"word":"grass","x":.78,"y":.90,"voice":"male"}],
"question":"What are they doing?",
"answer":["They","are","stretching","under","the","trees."],
"answerVoice":"male",
"notes":"Both runners do the same stretches, so the man gets a state (green T-shirt) and the woman the one action only she does (hand on his leg, 5.0-6.0 s). The duck walks along the puddle behind them (4.5-8.0 s, 10.0 s); it is only a sliver at the left edge at 0.0, 2.0, 2.5 and 4.0 s and an unclear dark spot at 9.5 s (off there). Where the duck is next to the woman (4.5-6.5 s) her box is cut on the left to keep the two apart. 7.5-8.0 s back-to-back stretch: the two bodies overlap, woman box = head and upper body on the left, man box = the right part. 'water' = the puddle on the path."}
json.dump(d,open("content/749.json","w"),indent=1,ensure_ascii=False)
