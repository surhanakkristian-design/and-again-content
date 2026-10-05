from gen_7986_7987_7988_7989_lib import *
wom=keys([(.33,.21,.66,.58),(.31,.21,.65,.59),(.31,.19,.65,.63),(.35,.18,.58,.65),(.37,.17,.56,.66),(.37,.17,.56,.66),(.37,.17,.55,.68),(.36,.16,.58,.70)])
man=keys([(.02,.42,.28,.20),(.02,.42,.27,.20),(.02,.42,.28,.21),(.04,.42,.30,.21),(.05,.42,.31,.21),(.05,.42,.31,.21),(.03,.42,.33,.21),(.02,.42,.33,.21)])
dog=keys([(.02,.62,.28,.14),(.02,.62,.27,.14),(.02,.63,.28,.13),(.04,.63,.30,.13),(.05,.63,.31,.13),(.05,.63,.31,.13),(.03,.63,.33,.13),(.02,.63,.33,.14)])
write(7989,{"mediaId":7989,"level":"A","keyWord":"softly","defaultVoice":"female",
"taps":[
 {"phrase":"to carry her shoes","target":"the woman","voice":"female","keys":wom},
 {"phrase":"to sleep on the sofa","target":"the man","voice":"male","keys":man},
 {"phrase":"to lie on the floor","target":"the dog","voice":"female","keys":dog}],
"stillS":1.2,
"nouns":[{"word":"a man","x":0.18,"y":0.52,"voice":"male"},
 {"word":"a dog","x":0.18,"y":0.66,"voice":"female"},
 {"word":"a window","x":0.76,"y":0.30,"voice":"female"},
 {"word":"shoes","x":0.85,"y":0.53,"voice":"female"}],
"question":"How is the woman walking?",
"answer":["She","is","walking","softly."],
"answerVoice":"female",
"notes":"Man and dog are seen through the doorway, stacked (man on the sofa above, dog on the floor below); their boxes split at y 0.62/0.63. Woman's reaching left hand (x ~0.25-0.30) is cut from her box at 1.2-2.7 so it does not overlap the man's box. Answer is only 4 words."})
