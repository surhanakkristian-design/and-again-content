from gen_5648_5649_5650_5651_lib import *
man=K([(0.0,0.26,0.50,0.74),(0.0,0.25,0.50,0.75),(0.0,0.24,0.50,0.76),(0.0,0.23,0.50,0.77),
       (0.0,0.22,0.50,0.78),(0.0,0.21,0.51,0.79),(0.0,0.20,0.42,0.80),(0.0,0.20,0.47,0.80)])
wom=K([(0.50,0.31,0.50,0.69),(0.50,0.30,0.50,0.70),(0.50,0.29,0.50,0.71),(0.50,0.30,0.50,0.70),
       (0.50,0.28,0.50,0.72),(0.51,0.27,0.49,0.73),(0.42,0.27,0.58,0.73),(0.47,0.27,0.53,0.73)])
write(5650,{"mediaId":5650,"level":"B","keyWord":"bet","defaultVoice":"male",
 "taps":[{"phrase":"to point at the staircase","target":"the man","voice":"male","keys":man},
         {"phrase":"to wear baggy jeans","target":"the man","voice":"male","keys":man},
         {"phrase":"to wear a crop top","target":"the woman","voice":"female","keys":wom}],
 "stillS":0.2,
 "nouns":[{"word":"a handrail","x":0.50,"y":0.36,"voice":"male"},{"word":"banknotes","x":0.51,"y":0.78,"voice":"male"},
          {"word":"a skateboard","x":0.42,"y":0.92,"voice":"male"}],
 "question":"What is the man pointing at?",
 "answer":["He","is","pointing","at","the","staircase."],"answerVoice":"male",
 "notes":"Key word 'bet' (verb) not placed. Banknotes not a tap target: they sit between the two people's boxes and could not get a box of their own. Man and woman shake hands at x~0.5, boxes split there. At 3.2 her pointing finger sits under his pointing hand (split at 0.42, her fingertip cut); at 3.7 her arm reaches across to his chest, so her forearm lies inside his box. The woman wears baggy light-blue trousers, not jeans. Both laugh, so no laughing phrase."})
