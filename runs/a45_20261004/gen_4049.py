import json
T=[i*0.5 for i in range(31)]
man=[(.36,.39,.31,.24),(.36,.39,.30,.24),(.38,.38,.27,.25),(.40,.38,.27,.25),(.38,.34,.29,.31),(.39,.30,.27,.36),(.38,.30,.29,.40),(.37,.34,.28,.38),(.33,.37,.36,.38),(.32,.38,.30,.39),(.24,.40,.38,.36),(.25,.40,.37,.35),(.36,.38,.30,.32),(.35,.38,.28,.32),(.42,.39,.26,.29),(.35,.39,.31,.27),(.41,.38,.33,.25),(.44,.39,.23,.25),(.46,.39,.21,.25),(.39,.35,.24,.26),(.39,.34,.23,.27),(.41,.36,.23,.27),(.39,.36,.21,.26),(.37,.36,.21,.26),(.40,.36,.24,.26),(.41,.38,.23,.24),(.36,.38,.25,.24),(.32,.39,.26,.23),(.32,.34,.26,.28),(.31,.33,.27,.30),(.30,.32,.29,.30)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,man)]
d={"mediaId":4049,"level":"A","keyWord":"load","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to carry a heavy load","to lift the beach chairs","to walk across the sand"]],
"stillS":10.0,
"nouns":[{"word":"a load","x":.42,"y":.28,"voice":"male"},{"word":"a building","x":.76,"y":.18,"voice":"male"},{"word":"an umbrella","x":.74,"y":.38,"voice":"male"},{"word":"sand","x":.50,"y":.80,"voice":"male"}],
"question":"What is the man carrying?","answer":["He","is","carrying","a","heavy","load."],"answerVoice":"male",
"notes":"Only one possible target (the man); he is mostly hidden under the chairs while he carries them, the box covers his visible body and the lower edge of the load. 'a load' pill sits on the stack of chairs he carries."}
json.dump(d,open("content/4049.json","w"),indent=1)
