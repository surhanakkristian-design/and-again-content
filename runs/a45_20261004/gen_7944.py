from gen_7943_7944_7945_7947_lib import *
L=[(.06,.38,.21,.85),(.06,.38,.20,.85),(.04,.38,.21,.87),(.02,.38,.30,.88),(0,.45,.33,.88),(0,.50,.33,.89),(0,.41,.34,.89),(0,.37,.30,.88)]
B=[(.36,.34,.60,.83),(.36,.34,.61,.85),(.37,.34,.61,.85),(.36,.34,.62,.86),(.36,.32,.60,.86),(.36,.32,.62,.87),(.36,.33,.63,.87),(.35,.32,.64,.87)]
C=[(.21,.35,.36,.72),(.20,.35,.36,.72),(.21,.35,.37,.72),None,(.60,.32,.99,.80),(.68,.38,1.0,.80),None,None]
write(7944,{"mediaId":7944,"level":"B","keyWord":"poll","defaultVoice":"female",
"taps":[{"phrase":"to reach into a bag","target":"the woman in lilac","voice":"female","keys":keys(L)},
 {"phrase":"to stand between the tubes","target":"the woman in denim","voice":"female","keys":keys(B)},
 {"phrase":"to cycle past the fountain","target":"the cyclist","voice":"male","keys":keys(C)}],
"stillS":3.7,
"nouns":[{"word":"a street lamp","x":0.24,"y":0.12,"voice":"female"},{"word":"a denim jacket","x":0.50,"y":0.50,"voice":"female"},{"word":"a fountain","x":0.86,"y":0.64,"voice":"female"},{"word":"tennis balls","x":0.31,"y":0.80,"voice":"female"}],
"question":"What is the cyclist doing?","answer":["He","is","cycling","past","the","fountain."],"answerVoice":"male",
"notes":"Cyclist (man in red T-shirt) sits on his bike behind the women at 0.2-1.2, hidden behind the woman in denim at 1.7 (off), rides past the fountain at 2.2-2.7, gone at 3.2-3.7; 'cycle past the fountain' is only true from 2.2. Woman in lilac reaches into the canvas bag only at 2.2-2.7 (holds up a ball at 3.7); her box is split from the cyclist's at x~0.21 early on (her reaching arm cut). Key word 'poll' is not a visible noun. Many background people (curly-haired skater, man in white jumper, woman in mustard dress)."})
