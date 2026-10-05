import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
man=K([(.00,.18,.36,.82),(.00,.19,.40,.81),(.00,.19,.39,.81),(.00,.19,.40,.81),(.00,.19,.41,.78),(.00,.19,.44,.79),(.00,.20,.50,.78),(.00,.20,.51,.78)])
woman=K([(.55,.20,.43,.76),(.58,.20,.41,.76),(.58,.21,.41,.76),(.59,.21,.40,.76),(.58,.21,.40,.74),(.58,.21,.41,.74),(.60,.22,.36,.74),(.62,.22,.37,.74)])
d={"mediaId":7083,"level":"B","keyWord":"encounter","defaultVoice":"male",
"taps":[{"phrase":"to gasp in disbelief","target":"the woman","voice":"female","keys":woman},
{"phrase":"to hold a retractable lead","target":"the woman","voice":"female","keys":woman},
{"phrase":"to tap his forehead","target":"the man","voice":"male","keys":man}],
"stillS":0.2,
"nouns":[{"word":"a scarf","x":0.20,"y":0.38,"voice":"male"},{"word":"a drainpipe","x":0.36,"y":0.15,"voice":"male"},
{"word":"tulips","x":0.50,"y":0.73,"voice":"male"},{"word":"corgis","x":0.45,"y":0.94,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","tapping","his","forehead."],"answerVoice":"male",
"notes":"Corgis sniff each other symmetrically, so no corgi phrase; both people laugh, so no laughing phrase. Woman's lead has a round retractable handle, the man's is a plain leather lead. Man taps his forehead only at ~3.0-3.7 s. 'a scarf' sits on the man's scarf (both wear one; the woman's is far right). Baker peeks from the doorway at 1.7-2.2 and 3.7 inside the man's box (not a target)."}
json.dump(d,open("content/7083.json","w"),indent=1)
