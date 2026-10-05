from gen_7768_7769_7770_7771_k import *
woman=keys([(.08,.37,.44,.53),(.07,.37,.45,.53),(.06,.37,.46,.56),(.06,.36,.44,.57),(.07,.34,.38,.64),(.10,.33,.46,.64),(.04,.34,.41,.63),(.01,.35,.32,.58)])
man=keys([(.74,.42,.26,.58),(.75,.43,.25,.57),(.75,.42,.25,.58),(.76,.42,.24,.58),(.77,.41,.23,.59),(.78,.41,.22,.59),(.79,.40,.21,.60),(.79,.40,.21,.60)])
swan=keys([(.56,.46,.18,.16),(.57,.47,.18,.16),(.57,.46,.18,.17),(.58,.46,.18,.17),(.54,.46,.21,.19),(.56,.47,.21,.18),(.59,.47,.19,.19),(.60,.47,.18,.19)])
write(7769,{"mediaId":7769,"level":"A","keyWord":"by the way","defaultVoice":"female",
"taps":[{"phrase":"to point at the bathroom","target":"the woman","voice":"female","keys":woman},
{"phrase":"to tie his shoe","target":"the man","voice":"male","keys":man},
{"phrase":"to stand in the bath","target":"the white bird","voice":"female","keys":swan}],
"stillS":3.7,
"nouns":[{"word":"a lamp","x":0.30,"y":0.15,"voice":"female"},{"word":"coats","x":0.33,"y":0.45,"voice":"female"},
{"word":"a bath","x":0.66,"y":0.67,"voice":"female"},{"word":"boots","x":0.35,"y":0.80,"voice":"female"}],
"question":"What is the man doing?",
"answer":["He","is","tying","his","shoe."],"answerVoice":"male",
"notes":"key word 'by the way' is a phrase, no noun slot. Man's box starts right of the swan's box, so his foot on the left (x .60-.75, low) is outside it. The bird is called a swan in the packet but looks like a white goose (orange bill), so target is the white bird. Woman points only in the first ~2 s, then picks up her bag and leaves."})
