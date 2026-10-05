import json
M=[(0.0,.24,.11,.76,.65),(0.5,.47,.03,.53,.72),(1.0,.42,.09,.58,.48),(1.5,.57,.04,.43,.70),(2.0,0,.06,.68,.52),(2.5,0,.06,1.0,.61),
(3.0,0,0,1.0,.55),(3.5,0,0,.88,.59),(4.0,0,.02,.48,.72),(4.5,0,.03,.47,.72),(5.0,0,.07,.48,.68)]
F=[(0.0,.04,.60,.19,.14),(0.5,.18,.26,.28,.38),(1.0,.28,.58,.30,.27),(1.5,.28,.37,.28,.37),(2.0,.38,.59,.42,.19),(2.5,.34,.69,.50,.14),
(3.0,.17,.58,.76,.17),(3.5,.10,.60,.85,.14),(4.0,.49,.42,.22,.33),(4.5,.48,.39,.24,.32),(5.0,.49,.44,.24,.28)]
k=lambda L:[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,x,y,w,h in L]
d={"mediaId":220,"level":"B","keyWord":"defrost","defaultVoice":"male",
"taps":[{"phrase":"to defrost a frozen fish","target":"the man","voice":"male","keys":k(M)},
{"phrase":"to slam a fish down","target":"the man","voice":"male","keys":k(M)},
{"phrase":"to soak in a bowl","target":"the fish","voice":"male","keys":k(F)}],
"stillS":4.5,
"nouns":[{"word":"a fillet","x":.58,"y":.47,"voice":"male"},{"word":"a tap","x":.78,"y":.63,"voice":"male"},{"word":"a bowl","x":.62,"y":.84,"voice":"male"},{"word":"a cupboard","x":.65,"y":.15,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","defrosting","a","frozen","fish."],"answerVoice":"male",
"notes":"Two targets only (man, fish): the bowl and the tap overlap the fish / the water so a third box-clean target was not practical. The man holds the fish in most frames, so the boxes are split between hand and fish and the man's box loses his holding arm at 1.0, 4.0-5.0. 'to slam a fish down' is the moment at 1.0 s only. Fish at 0.0 is mostly hidden under his hand in the freezer drawer. 'a tap' pill sits close to the soap bottle."}
json.dump(d,open("content/220.json","w"),indent=1)
