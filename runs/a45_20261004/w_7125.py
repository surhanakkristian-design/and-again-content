from gen_7120_7121_7125_7127_w import K,write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
woman=[(.16,.30,.40,.63),(.14,.29,.40,.68),(.15,.27,.44,.73),(.14,.27,.42,.73),(.17,.27,.37,.73),(.17,.26,.39,.74),(.14,.24,.43,.76),(.12,.23,.44,.77)]
man=[(.56,.38,.29,.45),(.55,.37,.32,.47),(.59,.37,.32,.49),(.58,.38,.35,.51),(.57,.38,.42,.53),(.58,.37,.42,.57),(.60,.36,.40,.60),(.60,.38,.40,.61)]
old=[(.0,.41,.16,.30),(.0,.41,.14,.31),(.0,.41,.15,.31),(.0,.41,.14,.31),(.0,.44,.17,.28),(.0,.44,.17,.29),(.0,.48,.14,.27),(.0,.48,.12,.27)]
write(7125,{"mediaId":7125,"level":"B","keyWord":"flip","defaultVoice":"female",
"taps":[
 {"phrase":"to catch a coin in mid-air","target":"the young woman","voice":"female","keys":K(T,woman)},
 {"phrase":"to lean against the piano","target":"the bearded man","voice":"male","keys":K(T,man)},
 {"phrase":"to wave from a doorway","target":"the old man","voice":"male","keys":K(T,old)}],
"stillS":0.2,
"nouns":[{"word":"a coin","x":0.47,"y":0.18,"voice":"female"},{"word":"a balcony","x":0.82,"y":0.27,"voice":"female"},
 {"word":"a piano","x":0.47,"y":0.68,"voice":"female"},{"word":"straps","x":0.64,"y":0.88,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","flipping","a","coin."],
"answerVoice":"female",
"notes":"Old man in the left doorway waves only 0.2-1.7, then stands; from 2.2 the woman's ponytail overlaps him, boxes split (old-man box narrow, 0.11-0.17 wide). Piano is wrapped in a moving blanket; 'a piano' pill sits on its visible black body. Upper-left balcony man also leans on a railing, so no balcony phrase."})
