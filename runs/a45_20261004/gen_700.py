import json
T=[i*0.5 for i in range(21)]
S={0:(.03,.39,.94,.36),.5:(.02,.38,.93,.37),1:(0,.38,.92,.37),1.5:(.02,.38,.90,.37),2:(.06,.40,.90,.33),2.5:(.06,.40,.85,.33),
3:(.12,.40,.76,.33),3.5:(.12,.40,.74,.34),4:(.14,.40,.80,.32),4.5:(.12,.40,.78,.32),5:(.14,.40,.72,.30),5.5:(.20,.42,.68,.30),
6:(.27,.40,.44,.29),6.5:(.31,.40,.40,.27),7:(.34,.40,.38,.28),7.5:(.37,.31,.36,.37),8:(.36,.28,.37,.40),8.5:(.37,.27,.36,.41),
9:(.36,.26,.35,.52),9.5:(.34,.25,.36,.54),10:(.32,.26,.37,.43)}
L={1:(.72,.22,.28,.15),1.5:(.66,.22,.34,.15),2:(.60,.22,.40,.17),2.5:(.56,.18,.44,.21),3:(.50,.18,.50,.21),3.5:(.44,.18,.56,.21),
4:(.38,.19,.62,.20),4.5:(.28,.18,.72,.21),5:(.20,.21,.80,.18),5.5:(.16,.24,.84,.17),6:(.12,.26,.88,.13),6.5:(.10,.27,.90,.12),
7:(.03,.35,.30,.27),7.5:(.02,.36,.34,.28),8:(0,.38,.35,.28),8.5:(.02,.40,.34,.27),9:(0,.41,.35,.36),9.5:(.02,.41,.31,.36),10:(.02,.43,.29,.30)}
def keys(D): return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
sk=keys(S)
d={"mediaId":700,"level":"A","keyWord":"snail","defaultVoice":"female","taps":[
{"phrase":"to move very slowly","target":"the snail","voice":"female","keys":sk},
{"phrase":"to climb onto a leaf","target":"the snail","voice":"female","keys":sk},
{"phrase":"to lie on the wet path","target":"the big leaf","voice":"female","keys":keys(L)}],
"stillS":10.0,"nouns":[{"word":"a snail","x":.50,"y":.42,"voice":"female"},{"word":"a leaf","x":.78,"y":.55,"voice":"female"},
{"word":"grass","x":.65,"y":.11,"voice":"female"}],
"question":"What is the snail doing?","answer":["It","is","climbing","onto","a","leaf."],"answerVoice":"female",
"notes":"Only two targets (snail, leaf); the leaf phrase is a state because the leaf does nothing. The snail sits in front of / on the leaf from 4 s: up to 6.5 s the leaf box is the band above the snail, from 7.0 s it is only the LEFT part of the leaf (the right part is not covered). Leaf set off at 0-0.5 s (only a sliver at the edge; small blurred leaves in the background are not the target). 'grass' = the blurred green lawn at the top of the last frame; the green tufts on the path are moss (not used, not A level)."}
json.dump(d,open("content/700.json","w"),indent=1,ensure_ascii=False)
