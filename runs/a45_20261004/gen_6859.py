from gen_6855_6856_6858_6859_lib import K, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man=K(T,[(.37,.32,.81,.84),(.37,.31,.81,.83),(.38,.33,.81,.84),(.36,.33,.80,.84),(.38,.33,.80,.82),(.37,.32,.80,.82),(.37,.31,.81,.85),(.37,.32,.81,.84)])
woman=K(T,[(.40,.18,.68,.32),(.40,.17,.67,.31),(.41,.19,.68,.33),(.40,.18,.68,.33),(.41,.19,.68,.33),(.40,.16,.68,.32),(.39,.16,.68,.31),(.39,.16,.68,.32)])
cars=K(T,[(.30,0,1,.15)]*8)
write(6859,{"mediaId":6859,"level":"B","keyWord":"bar","defaultVoice":"male",
"taps":[{"phrase":"to block the open gate","target":"the young man","voice":"male","keys":man},
{"phrase":"to wave her arms frantically","target":"the young woman","voice":"female","keys":woman},
{"phrase":"to drive along the motorway","target":"the cars","voice":"male","keys":cars}],
"stillS":0.2,
"nouns":[{"word":"a hay bale","x":0.86,"y":0.30,"voice":"male"},{"word":"cattle","x":0.24,"y":0.36,"voice":"male"},
{"word":"a gate","x":0.90,"y":0.72,"voice":"male"},{"word":"a stone wall","x":0.13,"y":0.78,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","blocking","the","open","gate."],"answerVoice":"male",
"notes":"The woman stands right behind the man: boxes split horizontally at the man's head top, so her legs (y .32-.40) are inside his box. Cattle pass close to the man but are not a tap target. 'the cars' = the traffic on the motorway at the top."})
