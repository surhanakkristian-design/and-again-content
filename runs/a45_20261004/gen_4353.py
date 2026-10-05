import json
T=[i*0.5 for i in range(25)]
man=[(0,0,.92,.53),(0,0,1,.52),(0,0,.95,.51),(0,0,1,.49),(0,0,1,.45),(0,0,1,.42),(0,0,1,.43),(0,0,1,.45),(0,0,1,.43),(0,0,1,.43),(0,0,1,.43),(0,0,1,.42),(0,0,1,.39),(0,0,1,.38),(0,0,1,.38),(.33,0,.67,.32),(.30,0,.70,.29),(.03,0,.97,.33),(.08,0,.92,.29),(.15,0,.85,.47),(.05,0,.95,.41),(.15,0,.85,.48),(.05,.08,.95,.41),(.16,.08,.84,.42),(.15,.03,.85,.48)]
cake=[(.20,.54,.62,.24),(.20,.53,.64,.24),(.20,.52,.64,.25),(.20,.50,.67,.26),(.17,.46,.78,.30),(.06,.43,.90,.42),(.06,.44,.90,.50),(.06,.46,.90,.49),(.06,.44,.90,.41),(.06,.44,.90,.41),(.04,.44,.90,.52),(.03,.43,.94,.53),(.03,.40,.95,.45),(.03,.39,.97,.46),(0,.39,1,.54),(.08,.33,.92,.56),(.04,.30,.96,.48),(0,.34,1,.36),(0,.30,1,.58),(.20,.48,.42,.37),(.25,.42,.42,.31),(.23,.49,.52,.26),(.18,.50,.56,.26),(.18,.51,.56,.26),(.18,.52,.56,.25)]
k=lambda L:[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,L)]
c={"mediaId":4353,"level":"A","keyWord":"dessert","defaultVoice":"male",
"taps":[{"phrase":"to cut the cake","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to hold a white plate","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to be covered in chocolate","target":"the cake","voice":"male","keys":k(cake)}],
"stillS":12.0,
"nouns":[{"word":"a man","x":.50,"y":.22,"voice":"male"},{"word":"a dessert","x":.48,"y":.58,"voice":"male"},{"word":"cream","x":.20,"y":.68,"voice":"male"},{"word":"a plate","x":.78,"y":.74,"voice":"male"}],
"question":"What is the man holding?",
"answer":["He","is","holding","a","dessert","on","a","plate."],
"answerVoice":"male",
"notes":"Only two targets (the man, the cake); they overlap in the picture, split along the top edge of the cake, so his hands over the cake fall into the cake box. From 9.5 s the cake box follows the slice on the plate. 'to be covered in chocolate' is a state (no action fits only the cake). 'a dessert' sits on the slice; the cream beside it is arguably part of the dessert too. A waiter is visible in the background at 11.5 s (not a target)."}
json.dump(c,open('content/4353.json','w'),indent=1)
