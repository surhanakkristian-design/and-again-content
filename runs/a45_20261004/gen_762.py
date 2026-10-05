import json
def mk(K,i):
    return [{"t":t,"x":K[t][i][0],"y":K[t][i][1],"w":K[t][i][2],"h":K[t][i][3]} for t in sorted(K)]
# woman, man
K={0.0:((.13,.05,.37,.49),(.51,0,.49,1)),
0.5:((.08,.04,.39,.49),(.48,0,.52,1)),
1.0:((.11,.06,.37,.52),(.49,0,.51,1)),
1.5:((.13,.08,.37,.50),(.51,0,.49,1)),
2.0:((.08,.08,.40,.50),(.49,0,.51,1)),
2.5:((.08,.13,.32,.50),(.41,0,.59,1)),
3.0:((.06,.18,.26,.57),(.33,0,.67,1)),
3.5:((.03,.28,.37,.60),(.42,0,.58,1)),
4.0:((0,.36,.37,.48),(.38,.03,.62,.97)),
4.5:((0,.38,.42,.50),(.43,.03,.57,.97)),
5.0:((0,.40,.24,.55),(.26,.08,.74,.92)),
5.5:((0,.48,.16,.52),(.17,0,.80,1)),
6.0:((0,.70,.13,.28),(.14,.15,.86,.85)),
6.5:((0,.62,.13,.36),(.14,.10,.86,.90)),
7.0:((0,.55,.16,.45),(.33,.08,.67,.92)),
7.5:((0,.55,.17,.45),(.33,.08,.67,.92)),
8.0:((0,.43,.13,.57),(.33,.06,.67,.94)),
8.5:((0,.43,.49,.57),(.50,.04,.50,.96)),
9.0:((0,.40,.44,.60),(.46,.06,.54,.94)),
9.5:((0,.43,.42,.57),(.43,.08,.57,.92)),
10.0:((0,.43,.35,.57),(.37,.10,.63,.90))}
d={"mediaId":762,"level":"A","keyWord":"t-shirt","defaultVoice":"male",
"taps":[{"phrase":"to put on a T-shirt","target":"the man","voice":"male","keys":mk(K,1)},
{"phrase":"to sit on the bed","target":"the woman","voice":"female","keys":mk(K,0)},
{"phrase":"to clap her hands","target":"the woman","voice":"female","keys":mk(K,0)}],
"stillS":4.0,
"nouns":[{"word":"a T-shirt","x":.64,"y":.56,"voice":"male"},{"word":"a woman","x":.17,"y":.62,"voice":"female"},
{"word":"a window","x":.27,"y":.25,"voice":"male"},{"word":"a drawer","x":.22,"y":.88,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","putting","on","a","T-shirt."],
"answerVoice":"male",
"notes":"Only two targets (man, woman); the woman has two phrases. From 7.0 s the man's reflection stands in the mirror between them: it has no box of its own; at 8.5-10.0 s the woman's box (head + clapping hands) and at 9.5-10.0 s the man's box cover parts of the mirror. 6.0-6.5 s the woman is only a strip at the left edge. 9.5-10.0 s the man's reaching hand lies inside the woman's box. 'a T-shirt' = the teal one in his hands at 4.0 s."}
json.dump(d,open("content/762.json","w"),indent=1,ensure_ascii=False)
