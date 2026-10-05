import json
T=[i*0.5 for i in range(19)]
man=[(.09,.11,.85,.89),(.09,.12,.85,.88),(0,.15,.91,.85),(.06,.06,.93,.94),(0,.04,1,.96),(0,.14,.94,.86),(.08,.20,.90,.80),(.09,.21,.82,.79),(.08,.21,.81,.79),(.09,.26,.82,.74),(0,0,.92,1),(.04,0,.86,1),(.11,.04,.88,.96),(.08,.07,.85,.93),(.11,.07,.78,.93),(.11,.05,.81,.95),(.12,.04,.81,.96),(.07,.01,.85,.99),(.04,0,.88,1)]
k=lambda L:[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,L)]
c={"mediaId":4358,"level":"A","keyWord":"heavy","defaultVoice":"male",
"taps":[{"phrase":"to carry a heavy bag","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to hold a small bag","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to smile at the camera","target":"the man","voice":"male","keys":k(man)}],
"stillS":6.0,
"nouns":[{"word":"a bag","x":.60,"y":.33,"voice":"male"},{"word":"a pot","x":.26,"y":.49,"voice":"male"},{"word":"a man","x":.55,"y":.63,"voice":"male"},{"word":"grass","x":.82,"y":.84,"voice":"male"}],
"question":"What is the man carrying?",
"answer":["He","is","carrying","a","very","heavy","bag."],
"answerVoice":"male",
"notes":"One target only (the man) for all three phrases: the bags are on his body and cannot be split from him; the walkers far behind (from 7.5 s) are tiny and not targets. The man's box includes the pack he carries. Several pots hang on the pack; the 'a pot' slot sits on the big one at the left. 'to hold a small bag' is the first shot (0-1.5 s)."}
json.dump(c,open('content/4358.json','w'),indent=1)
