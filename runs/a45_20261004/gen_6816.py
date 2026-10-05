from lib_6816_6817_6818_6819 import *
act=[(.20,.33,.60,.68),(.18,.33,.62,.68),(.16,.33,.64,.68),(.14,.33,.64,.68),(.10,.31,.66,.72),(.38,.24,.68,.78),(.34,.23,.70,.82),(.32,.23,.66,.82)]
pia=[(.60,.33,.79,.49),(.63,.33,.84,.50),(.65,.32,.92,.53),(.65,.32,.93,.52),(.67,.31,.95,.55),(.69,.30,.98,.52),(.71,.29,1.0,.55),(.67,.29,.99,.56)]
lad=[(.80,.12,1.0,.62),(.85,.10,1.0,.62),(.79,.14,1.0,.30),None,None,None,None,None]
A=keys(act);P=keys(pia);L=keys(lad)
write(6816,{"mediaId":6816,"level":"B","keyWord":"act out","defaultVoice":"female",
"taps":[{"phrase":"to shade her eyes","target":"the actress","voice":"female","keys":A},
{"phrase":"to play an upright piano","target":"the pianist","voice":"male","keys":P},
{"phrase":"to tip a watering can","target":"the woman on the ladder","voice":"female","keys":L}],
"stillS":0.2,
"nouns":[{"word":"a watering can","x":.80,"y":.27,"voice":"female"},
{"word":"an electric fan","x":.14,"y":.40,"voice":"female"},
{"word":"an upright piano","x":.80,"y":.42,"voice":"female"},
{"word":"a wooden chair","x":.48,"y":.60,"voice":"female"}],
"question":"What is the actress doing?",
"answer":["She","is","acting","out","a","storm","on","stage."],
"answerVoice":"female",
"notes":"Woman on the ladder only partly visible (arm + can) at 1.2 s, off from 1.7 s. Actress/pianist boxes split where her arm/legs cross the piano."})
