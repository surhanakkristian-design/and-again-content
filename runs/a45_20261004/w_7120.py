from gen_7120_7121_7125_7127_w import K,write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
roof=[(.08,.17,.22,.16),(.07,.17,.22,.16),(.07,.16,.22,.16),(.06,.15,.22,.16),(.04,.14,.22,.16),(.04,.12,.22,.16),(.01,.10,.21,.17),(.0,.09,.20,.18)]
board=[(.04,.61,.45,.20),(.04,.61,.45,.21),(.03,.61,.44,.21),(.0,.63,.43,.20),(.0,.65,.48,.20),(.0,.67,.54,.20),(.0,.69,.60,.19),(.0,.69,.61,.20)]
woman=[(.76,.40,.24,.33),(.76,.39,.24,.34),(.76,.39,.24,.36),(.76,.39,.24,.36),(.77,.38,.23,.37),(.77,.37,.23,.39),(.78,.37,.22,.39),(.78,.37,.22,.39)]
write(7120,{"mediaId":7120,"level":"A","keyWord":"fix something","defaultVoice":"female",
"taps":[
 {"phrase":"to stand on the roof","target":"the dog on the roof","voice":"female","keys":K(T,roof)},
 {"phrase":"to lie on a red board","target":"the dog on the board","voice":"female","keys":K(T,board)},
 {"phrase":"to hold an umbrella","target":"the woman","voice":"female","keys":K(T,woman)}],
"stillS":0.2,
"nouns":[{"word":"a bus","x":0.18,"y":0.48,"voice":"female"},{"word":"an umbrella","x":0.86,"y":0.46,"voice":"female"},
 {"word":"tools","x":0.62,"y":0.84,"voice":"female"},{"word":"the road","x":0.30,"y":0.93,"voice":"female"}],
"question":"What are the dogs doing?",
"answer":["The","dogs","are","fixing","an","old","bus."],
"answerVoice":"female",
"notes":"Dogs as workers; 'fixing' = key word. Board = mechanic's creeper (A-level wording). Woman box includes umbrella; lamp dog behind her not a target."})
