from lib_6816_6817_6818_6819 import *
adm=[(.30,.33,.62,.88),(.31,.33,.62,.88),(.30,.38,.62,.92),(.30,.47,.62,1.0),(.31,.53,.63,1.0),(.31,.57,.63,1.0),(.31,.60,.63,1.0),(.37,.60,.64,1.0)]
off=[(.62,.42,.78,.75),(.62,.42,.78,.76),(.62,.47,.79,.80),(.62,.55,.79,.90),(.63,.61,.80,.96),(.63,.65,.80,.99),(.63,.66,.79,1.0),(.64,.67,.80,1.0)]
flg=[(.31,.05,.52,.24),(.29,.04,.52,.22),(.25,.03,.57,.20),(.28,.06,.52,.24),(.27,.08,.52,.26),(.26,.12,.52,.29),(.25,.14,.52,.31),(.26,.15,.52,.32)]
A=keys(adm);O=keys(off);F=keys(flg)
write(6819,{"mediaId":6819,"level":"B","keyWord":"admiral","defaultVoice":"female",
"taps":[{"phrase":"to stand on a platform","target":"the admiral","voice":"female","keys":A},
{"phrase":"to hold a blue folder","target":"the officer in the raincoat","voice":"male","keys":O},
{"phrase":"to flap in the wind","target":"the flag","voice":"female","keys":F}],
"stillS":0.2,
"nouns":[{"word":"a flag","x":.42,"y":.15,"voice":"female"},
{"word":"a tugboat","x":.84,"y":.49,"voice":"female"},
{"word":"an admiral","x":.47,"y":.58,"voice":"female"},
{"word":"a platform","x":.50,"y":.92,"voice":"female"}],
"question":"Where is the admiral standing?",
"answer":["She","is","standing","on","a","wooden","platform."],
"answerVoice":"female",
"notes":"Admiral and a young sailor both salute, so the admiral's phrase is the platform instead. Camera tilts down: everything drifts lower; admiral/officer boxes split at x .62-.64."})
