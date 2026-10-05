import json
OFF=None
# t: (woman, man, bird)
K={
0.0:(OFF,OFF,(.66,.02,.26,.16)),
0.5:((.24,0,.20,.14),(.45,0,.20,.14),(.72,.05,.28,.18)),
1.0:((.12,0,.24,.14),(.37,0,.20,.14),OFF),
1.5:((.06,0,.25,.15),(.32,0,.20,.15),OFF),
2.0:((.06,0,.25,.24),(.32,0,.24,.21),(.62,.22,.18,.14)),
2.5:((0,0,.41,.40),(.42,0,.26,.22),(.63,.29,.18,.14)),
3.0:((0,0,.47,.64),(.48,0,.22,.42),(.71,.35,.18,.14)),
3.5:((0,.03,.55,.57),(.56,0,.18,.47),(.75,.36,.18,.14)),
4.0:((0,.09,.56,.46),(.57,.04,.22,.46),(.80,.37,.18,.14)),
4.5:((0,0,.52,.60),(.53,.10,.20,.24),(.82,.38,.18,.14)),
5.0:((0,.08,.38,.66),(.39,.29,.30,.36),(.74,.39,.18,.14)),
5.5:((0,.13,.33,.64),(.34,.28,.28,.42),OFF),
6.0:((.27,.22,.28,.42),(.07,.25,.19,.17),OFF),
6.5:((.50,.19,.30,.36),(.09,.26,.40,.34),OFF),
7.0:((.63,.31,.32,.38),(.34,.25,.28,.43),OFF),
7.5:((.62,.25,.29,.43),(.22,.31,.39,.37),OFF),
8.0:((.62,.22,.28,.35),(0,.29,.32,.31),OFF),
8.5:((.62,.24,.26,.33),(0,.26,.36,.34),OFF),
9.0:((.56,.22,.28,.47),(.08,.21,.36,.48),OFF),
9.5:((.57,.31,.26,.37),(.14,.31,.30,.38),OFF),
10.0:((.57,.27,.25,.30),(.15,.28,.26,.30),OFF),
}
def keys(i):
    out=[]
    for t in sorted(K):
        b=K[t][i]
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
d={"mediaId":746,"level":"A","keyWord":"stream","defaultVoice":"female",
"taps":[
 {"phrase":"to splash the water","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to hold a small boat","target":"the man","voice":"male","keys":keys(1)},
 {"phrase":"to stand on a rock","target":"the bird","voice":"female","keys":keys(2)}],
"stillS":10.0,
"nouns":[{"word":"the sky","x":.50,"y":.07,"voice":"female"},
 {"word":"a woman","x":.72,"y":.40,"voice":"female"},
 {"word":"a stream","x":.50,"y":.68,"voice":"female"},
 {"word":"grass","x":.16,"y":.85,"voice":"female"}],
"question":"What are they jumping over?",
"answer":["They","are","jumping","over","a","stream."],
"answerVoice":"female",
"notes":"Bird: stands on a rock at 0.0-0.5 s; a small bird sits in the water at 2.0-5.0 s (boxed as the same bird, small). People: only feet / legs at 0.5-2.0 s (left dark trousers = woman, right bare legs = man), nothing usable at 0.0 s. 2.5-5.5 s the two crouch behind each other: boxes split on a vertical line, the woman's hands reach past it. 6.0 s the man is mostly hidden behind the woman (small box on his visible back). 'a small boat' = the little leaf / bark boat he puts on the water (3.0-5.0 s); it could be read as a small basket. Both jump, so jumping is only in the question."}
json.dump(d,open("content/746.json","w"),indent=1,ensure_ascii=False)
