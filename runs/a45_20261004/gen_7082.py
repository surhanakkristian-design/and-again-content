import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
woman=K([(.17,.12,.43,.53),(.17,.12,.43,.53),(.16,.11,.44,.54),(.16,.11,.44,.55),(.15,.10,.45,.55),(.16,.10,.44,.55),(.28,.11,.37,.55),(.30,.10,.38,.57)])
dog=K([(.00,.65,.36,.20),(.00,.65,.36,.20),(.00,.65,.35,.20),(.00,.66,.29,.20),(.00,.65,.27,.22),(.00,.65,.27,.22),(.00,.66,.27,.23),(.00,.67,.27,.22)])
d={"mediaId":7082,"level":"B","keyWord":"employ","defaultVoice":"female",
"taps":[{"phrase":"to lean against the gate","target":"the woman","voice":"female","keys":woman},
{"phrase":"to stroke a sheep's head","target":"the woman","voice":"female","keys":woman},
{"phrase":"to watch the passing flock","target":"the dog","voice":"female","keys":dog}],
"stillS":2.7,
"nouns":[{"word":"a straw hat","x":0.45,"y":0.15,"voice":"female"},{"word":"a gate","x":0.12,"y":0.38,"voice":"female"},
{"word":"sheep","x":0.72,"y":0.63,"voice":"female"},{"word":"a dog","x":0.13,"y":0.73,"voice":"female"}],
"question":"What is the woman leaning against?","answer":["She","is","leaning","against","a","wooden","gate."],"answerVoice":"female",
"notes":"Woman's boots (y ~.66-.70) are cut from her box at 0.2-2.7 to keep it off the dog's box. She strokes the sheep only at ~3.0-3.4 s. Key word 'employ' is not visible as a noun. Dog looks towards the sheep - 'watch the passing flock' is a mild reading."}
json.dump(d,open("content/7082.json","w"),indent=1)
