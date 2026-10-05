from gen_7891_7892_7893_7894_lib import *
man=keys([(.05,.24,.75,.72),(.05,.24,.75,.72),(.05,.25,.79,.72),(.05,.25,.80,.72),(.03,.24,.81,.72),(.04,.23,.83,.72),(.03,.22,.82,.72),(.03,.23,.83,.72)])
wai=keys([(.76,.05,1,1),(.76,.05,1,1),(.80,.02,1,1),(.81,.02,1,1),(.82,.02,1,1),(.84,.02,1,1),(.83,.02,1,1),(.84,.02,1,1)])
write({"mediaId":7891,"level":"A","keyWord":"little","defaultVoice":"male",
"taps":[{"phrase":"to add a little leaf","target":"the waitress","voice":"female","keys":wai},
{"phrase":"to look up at the waitress","target":"the man","voice":"male","keys":man},
{"phrase":"to cut the fish","target":"the man","voice":"male","keys":man}],
"stillS":2.2,
"nouns":[{"word":"a man","x":0.45,"y":0.47,"voice":"male"},{"word":"a waitress","x":0.90,"y":0.55,"voice":"female"},
{"word":"a plate","x":0.22,"y":0.67,"voice":"male"},{"word":"a table","x":0.30,"y":0.84,"voice":"male"}],
"question":"What is on the man's plate?","answer":["There","is","a","little","piece","of","fish."],"answerVoice":"male",
"notes":"Waitress adds the green leaf with tweezers at 0.2-0.7 only. Man and waitress boxes split vertically; her outstretched arm at 0.2-0.7 lies partly in the man's box. Man looks up at her at 2.7, cuts the fish at 3.2."})
