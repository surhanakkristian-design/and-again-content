from gen_7768_7769_7770_7771_k import *
man=keys([(.02,.27,.64,.63),(.02,.30,.64,.61),(.03,.36,.63,.56),(.08,.47,.56,.50),(.04,.50,.59,.48),(.00,.38,.63,.59),(.00,.38,.62,.61),(.03,.39,.59,.61)])
crate=keys([(.80,.34,.19,.23),(.81,.34,.18,.23),(.81,.37,.18,.21),(.80,.36,.18,.22),(.80,.37,.18,.21),(.80,.36,.18,.23),(.79,.38,.18,.23),(.79,.38,.18,.24)])
cat=keys([(.66,.57,.18,.14),(.66,.58,.18,.14),(.66,.59,.18,.14),(.66,.59,.18,.14),(.66,.59,.18,.14),(.66,.61,.18,.14),(.66,.62,.18,.14),(.66,.63,.18,.14)])
write(7768,{"mediaId":7768,"level":"B","keyWord":"burden","defaultVoice":"male",
"taps":[{"phrase":"to stagger under heavy luggage","target":"the man with the bags","voice":"male","keys":man},
{"phrase":"to carry a crate of lemons","target":"the man with the lemons","voice":"male","keys":crate},
{"phrase":"to stretch out on a step","target":"the cat","voice":"male","keys":cat}],
"stillS":0.2,
"nouns":[{"word":"a guitar case","x":0.52,"y":0.40,"voice":"male"},{"word":"a cool box","x":0.56,"y":0.64,"voice":"male"},
{"word":"a crate","x":0.90,"y":0.44,"voice":"male"},{"word":"a dome","x":0.60,"y":0.23,"voice":"male"}],
"question":"What is the man in white doing?",
"answer":["He","is","staggering","under","heavy","luggage."],"answerVoice":"male",
"notes":"key word 'burden' is abstract, not used as a noun slot. Cat box kept right of the man's cool box (x>=.66); crate man box stops above the cat box. Other friends walk next to the man with the lemons (not targets)."})
