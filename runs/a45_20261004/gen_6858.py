from gen_6855_6856_6858_6859_lib import K, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman=K(T,[(.27,.39,.69,.75),(.25,.38,.69,.71),(.27,.38,.69,.76),(.24,.37,.69,.71),(.25,.34,.69,.66),(.25,.33,.69,.64),(.22,.40,.69,.70),(.22,.40,.69,.70)])
suit=K(T,[(.46,.24,.83,.39),(.46,.23,.83,.38),(.46,.23,.83,.38),(.46,.22,.83,.37),(.46,.20,.85,.34),(.46,.18,.84,.33),(.45,.22,.84,.40),(.45,.16,.84,.40)])
cap=K(T,[(.69,.46,1,1),(.69,.46,1,1),(.69,.46,1,1),(.69,.46,1,1),(.69,.44,1,1),(.69,.42,1,1),(.69,.42,1,1),(.69,.41,1,1)])
write(6858,{"mediaId":6858,"level":"B","keyWord":"banker","defaultVoice":"female",
"taps":[{"phrase":"to slide the document forward","target":"the woman","voice":"female","keys":woman},
{"phrase":"to unfold the document","target":"the bearded man","voice":"male","keys":cap},
{"phrase":"to read a large ledger","target":"the man in the suit","voice":"male","keys":suit}],
"stillS":0.2,
"nouns":[{"word":"a banker","x":0.40,"y":0.62,"voice":"female"},{"word":"a ledger","x":0.72,"y":0.42,"voice":"female"},
{"word":"a desk lamp","x":0.74,"y":0.53,"voice":"female"},{"word":"banknotes","x":0.15,"y":0.33,"voice":"female"}],
"question":"What is the bearded man doing?","answer":["He","is","unfolding","the","document."],"answerVoice":"male",
"notes":"Man in the suit stands right behind the woman: split horizontally at her hairline, so his lower body is inside her box. From 2.2 s the bearded man reaches left under the woman for the paper; his arm/hand left of x .69 is outside his box (vertical split). 'a banker' pill on the woman = key word."})
