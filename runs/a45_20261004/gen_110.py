import json
T=[i*0.5 for i in range(21)]
W=[(.15,.15,.74,.85),(.24,.13,.66,.87),(.21,.14,.70,.86),(.16,.26,.74,.74),(.25,.02,.53,.60),(.24,.09,.46,.53),(.28,.10,.44,.72),(.21,.08,.40,.78),
(.25,0,.55,.39),(.20,.03,.42,.66),(.20,.03,.41,.41),(0,.07,.80,.72),(.22,.02,.62,.64),(.10,.27,.78,.73),(.15,.24,.78,.74),(.13,.07,.87,.93),
(.02,.14,.90,.86),(.30,.16,.64,.84),(.48,.15,.50,.85),(.58,.16,.42,.84),(.53,.16,.45,.82)]
C=[(0,.68,.14,.30),(.02,.72,.21,.27),(0,.71,.20,.29),(0,.54,.15,.40),(0,.48,.24,.22),(0,.42,.23,.22),(0,.40,.27,.27),None,
(.58,.40,.23,.17),(.63,.41,.23,.18),(.30,.45,.47,.14),None,None,None,None,None,None,(0,.64,.18,.26),(.08,.25,.24,.45),(.05,.16,.50,.33),(.07,.12,.45,.28)]
M=[None]*4+[(.79,.28,.21,.64),(.71,0,.29,.90),(.73,0,.27,.98),(.62,.03,.38,.95),(.82,0,.18,.90),(.87,0,.13,.90),(.62,0,.38,.44)]+[None]*10
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
K=lambda L:[k(t,b) for t,b in zip(T,L)]
d={"mediaId":110,"level":"A","keyWord":"box","defaultVoice":"female",
"taps":[{"phrase":"to carry a big box","target":"the woman","voice":"female","keys":K(W)},
{"phrase":"to touch the cat","target":"the man","voice":"male","keys":K(M)},
{"phrase":"to sit on a box","target":"the cat","voice":"female","keys":K(C)}],
"stillS":10.0,
"nouns":[{"word":"a shelf","x":0.62,"y":0.15,"voice":"female"},{"word":"a cat","x":0.32,"y":0.26,"voice":"female"},
{"word":"a woman","x":0.74,"y":0.45,"voice":"female"},{"word":"boxes","x":0.35,"y":0.62,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","packing","a","big","box."],
"answerVoice":"female",
"notes":"Many cuts and three overlapping targets at 2.0-5.0 s (the man reaches across the woman, the cat stands between them): boxes are split along vertical / horizontal lines, so some are tighter than the usual padding and the man's reaching forearm is partly outside his box. The man is only partly in the picture: at 2.0 s just the top of his head behind the blanket and his shoe, at 4.0-4.5 s his arm, body edge and shoe; his hand touches the cat at 4.0-5.0 s. The cat sits on the top box only at 10.0 s (jumps up at 9.5 s). The woman carries the box at 7.5-8.0 s. Key word as the plural 'boxes' (pile of three)."}
json.dump(d,open("content/110.json","w"),indent=1)
