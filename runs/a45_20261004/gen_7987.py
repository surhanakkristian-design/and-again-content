from gen_7986_7987_7988_7989_lib import *
car=keys([(.02,.39,.96,.12)]*8)
tor=keys([(.03,.52,.95,.29),(.03,.52,.96,.29),(.02,.52,.97,.29),(.02,.52,.97,.29),(.00,.52,.99,.30),(.00,.52,.99,.30),(.00,.52,.99,.30),(.01,.52,.98,.30)])
write(7987,{"mediaId":7987,"level":"A","keyWord":"slowly","defaultVoice":"male",
"taps":[
 {"phrase":"to cross the street","target":"the tortoise","voice":"male","keys":tor},
 {"phrase":"to wait behind the tortoise","target":"the car","voice":"male","keys":car},
 {"phrase":"to walk very slowly","target":"the tortoise","voice":"male","keys":tor}],
"stillS":0.2,
"nouns":[{"word":"a tortoise","x":0.40,"y":0.62,"voice":"male"},
 {"word":"a car","x":0.35,"y":0.44,"voice":"male"},
 {"word":"a leaf","x":0.33,"y":0.84,"voice":"male"},
 {"word":"a tree","x":0.88,"y":0.43,"voice":"male"}],
"question":"How is the tortoise walking?",
"answer":["The","tortoise","is","walking","very","slowly."],
"answerVoice":"male",
"notes":"The car sits right behind the tortoise; boxes split at y 0.51/0.52 (car = visible upper body above the shell, its lower front corner left of the tortoise is cut). 'a tree' = the small tree in the lit shop window."})
