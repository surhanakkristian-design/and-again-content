from gen_7768_7769_7770_7771_k import *
a=keys([(.19,.54,.19,.23),(.18,.55,.20,.23),(.18,.57,.20,.24),(.18,.59,.20,.24),(.18,.61,.20,.26),(.18,.64,.20,.25),(.19,.69,.26,.20),(.43,.80,.20,.15)])
r=keys([(.38,.52,.62,.28),(.38,.54,.62,.26),(.38,.56,.62,.25),(.38,.57,.62,.25),(.38,.61,.62,.26),(.38,.62,.62,.26),(.45,.64,.55,.24),(.30,.65,.70,.15)])
write(7771,{"mediaId":7771,"level":"A","keyWord":"cap","defaultVoice":"male",
"taps":[{"phrase":"to stand on a big rock","target":"the animal","voice":"male","keys":a},
{"phrase":"to jump off the rock","target":"the animal","voice":"male","keys":a},
{"phrase":"to flow through the field","target":"the river","voice":"male","keys":r}],
"stillS":2.2,
"nouns":[{"word":"snow","x":0.45,"y":0.33,"voice":"male"},{"word":"a house","x":0.29,"y":0.58,"voice":"male"},
{"word":"a fence","x":0.80,"y":0.63,"voice":"male"},{"word":"a rock","x":0.25,"y":0.90,"voice":"male"}],
"question":"Where is the animal standing?",
"answer":["It","is","standing","on","a","big","rock."],"answerVoice":"male",
"notes":"only one animal (a marmot, called 'the animal' for level A); it jumps down at ~3.0 s. River box split from the animal box at 3.2 s (x) and 3.7 s (y), so a bit of water is outside it. Key word 'cap' is a verb (snow caps the peak), no noun slot; 'snow' sits on the peak."})
