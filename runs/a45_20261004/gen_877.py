import json
T=[i*0.5 for i in range(21)]
N=None
G=[(.06,.28,.30,.50),(.07,.29,.30,.52),(.07,.29,.29,.63),(.06,.28,.27,.63),(0,.28,.30,.58),N,N,N,N,(0,.10,.28,.42),(0,.10,.21,.84),(0,.08,.22,.88),(0,.20,.33,.66),(0,.15,.39,.70),(0,.20,.33,.75),(0,.18,.33,.77),(0,.20,.30,.66),(0,.40,.31,.48),(.02,.30,.31,.70),(.05,.46,.27,.54),(.05,.48,.27,.52)]
O=[(.36,.30,.25,.50),(.37,.30,.25,.50),(.36,.32,.26,.60),(.33,.31,.30,.63),(.30,.33,.35,.55),(.12,.15,.76,.85),(.05,.12,.90,.88),(.05,.12,.92,.88),(0,.08,1,.92),(.28,.26,.42,.70),(.22,.30,.49,.68),(.23,.31,.42,.67),(.33,.34,.31,.54),(.39,.33,.26,.56),(.33,.36,.34,.60),(.34,.42,.56,.53),(.31,.32,.36,.56),(.32,.10,.36,.76),(.33,.03,.31,.97),(.32,0,.34,.94),(.32,.03,.34,.85)]
P=[(.61,.30,.31,.48),(.62,.31,.33,.48),(.62,.33,.33,.57),(.63,.33,.34,.59),(.65,.34,.35,.52),N,N,N,N,(.70,.12,.30,.42),(.72,.17,.28,.76),(.66,.17,.34,.78),(.64,.20,.36,.66),(.66,.18,.34,.68),(.68,.18,.32,.76),(.68,.18,.32,.23),(.68,.20,.32,.66),(.69,.38,.31,.50),(.65,.33,.33,.67),(.66,.50,.31,.50),(.66,.53,.30,.47)]
def k(L): return [({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}) for t,b in zip(T,L)]
d={"mediaId":877,"level":"A","keyWord":"a winner","defaultVoice":"female",
"taps":[{"phrase":"to win the race","target":"the woman in orange","voice":"female","keys":k(O)},
{"phrase":"to wear a green top","target":"the man","voice":"male","keys":k(G)},
{"phrase":"to wear a purple top","target":"the woman in purple","voice":"female","keys":k(P)}],
"stillS":8.0,
"nouns":[{"word":"a man","x":.20,"y":.31,"voice":"male"},{"word":"a winner","x":.50,"y":.46,"voice":"female"},{"word":"a cup","x":.53,"y":.66,"voice":"female"},{"word":"mud","x":.50,"y":.90,"voice":"female"}],
"question":"What is the winner holding?","answer":["She","is","holding","a","gold","cup."],"answerVoice":"female",
"notes":"Animated clip. The man and the woman in purple do everything together (run, cheer, lift the winner), so their phrases are states (clothes). 'a cup' is used for the trophy to stay at level A. The three stand shoulder to shoulder or overlap: boxes are split along the lines between them, so arms are cut off in places (4.5-7.5 s, 9.5-10 s). At 2.5-4.0 s only the woman in orange is really in the picture (the others' hands on her shoulders / a sliver at the edge are set off). At 7.5 s the purple woman's box covers only her head and shoulders, the cup in front of her belongs to the winner's box. The 'a winner' pill is on her face, the 'a cup' pill on the cup she holds in front of her."}
json.dump(d,open("content/877.json","w"),indent=1)
