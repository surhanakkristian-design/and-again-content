import json
# t: (woman, machine, house)
D={0.0:((0,.20,.40,.80),(0,0,.40,.20),(.40,0,.60,.52)),
0.5:((0,.21,.40,.79),(0,0,.40,.21),(.40,0,.60,.52)),
1.0:((0,.23,.40,.77),(0,.02,.40,.21),(.40,0,.60,.53)),
1.5:((0,.23,.40,.77),(0,.02,.40,.21),(.40,0,.60,.53)),
2.0:((0,.25,.40,.75),(0,0,.40,.22),(.40,0,.60,.55)),
2.5:((0,.30,.39,.70),(0,.05,.40,.22),(.40,.05,.60,.53)),
3.0:((0,.33,.36,.67),(0,.10,.42,.22),(.42,.08,.58,.56)),
3.5:((0,.33,.36,.67),(0,.10,.42,.22),(.42,.08,.58,.56)),
4.0:((0,.33,.38,.67),(0,.12,.42,.20),(.42,.10,.58,.52)),
4.5:((0,.33,.38,.67),(0,.12,.42,.20),(.42,.10,.58,.52)),
5.0:((0,.38,.42,.62),(0,.13,.44,.24),(.44,.08,.56,.56)),
5.5:((0,.37,.42,.63),(0,.10,.44,.26),(.44,.08,.56,.56)),
6.0:((0,.36,.38,.64),(0,.04,.44,.28),(.44,.10,.56,.52)),
6.5:((0,.35,.36,.65),(0,.05,.46,.27),(.46,.10,.54,.52)),
7.0:((0,.36,.34,.64),(0,.08,.52,.26),(.52,.10,.48,.54)),
7.5:((0,.38,.34,.62),(0,.08,.52,.26),(.52,.10,.48,.54)),
8.0:((0,.35,.34,.65),(0,.08,.42,.24),(.42,.12,.58,.50)),
8.5:((0,.34,.38,.66),(0,.06,.46,.25),(.38,.32,.62,.29)),
9.0:((0,.32,.38,.68),(0,.06,.38,.24),(.45,.37,.55,.24)),
9.5:((0,.30,.38,.70),(0,.06,.32,.23),(.45,.37,.55,.22)),
10.0:((0,.27,.42,.73),(0,.03,.27,.23),(.45,.35,.55,.22)),
10.5:((0,.24,.57,.76),(0,.03,.24,.20),(.58,.33,.42,.22)),
11.0:((0,.23,.50,.77),(0,.03,.22,.19),(.50,.34,.50,.20)),
11.5:((0,.22,.56,.78),(0,0,.24,.21),(.56,.33,.44,.20)),
12.0:((0,.21,.58,.79),(0,0,.20,.20),(.58,.32,.42,.20))}
times=[i*0.5 for i in range(25)]
def keys(i):
    return [dict(t=t,x=D[t][i][0],y=D[t][i][1],w=D[t][i][2],h=D[t][i][3]) for t in times]
c={"mediaId":4637,"level":"A","keyWord":"destroy","defaultVoice":"female",
"taps":[
 {"phrase":"to hold up a phone","target":"the woman","voice":"female","keys":keys(0)},
 {"phrase":"to destroy a big house","target":"the yellow machine","voice":"female","keys":keys(1)},
 {"phrase":"to fall to the ground","target":"the house","voice":"female","keys":keys(2)}],
"stillS":12.0,
"nouns":[{"word":"the sky","x":.60,"y":.12,"voice":"female"},{"word":"a helmet","x":.20,"y":.29,"voice":"female"},
 {"word":"a phone","x":.49,"y":.57,"voice":"female"},{"word":"bricks","x":.76,"y":.68,"voice":"female"}],
"question":"What is the yellow machine doing?",
"answer":["It","is","destroying","a","big","house."],
"answerVoice":"female",
"notes":"Woman, machine arm and house touch in the picture; boxes are split along the lines between them, so the woman's box loses the right side of her jacket in 0-10 s (her head and most of her body are in), and the house box loses a strip at its left edge. From 9.0 s the house is only a low ruin in dust (box on the ruin). The phone is visible only from 10.5 s. 'the yellow machine' is used instead of 'excavator' (level A). Bricks already lie on the ground and do not fall visibly as a group, so 'to fall to the ground' is meant for the house only - worth a look."}
json.dump(c,open('content/4637.json','w'),indent=1)
