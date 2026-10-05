import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
woman=K([(0,.41,.44,.48),(0,.42,.46,.48),(0,.41,.44,.47),(0,.40,.43,.47),(0,.38,.42,.47),(0,.40,.42,.46),(0,.41,.46,.47),(0,.43,.47,.47)])
seal=K([(.76,.53,.18,.14),(.76,.53,.18,.14),(.75,.52,.19,.14),(.74,.52,.19,.14),(.74,.53,.19,.14),(.73,.53,.19,.14),(.71,.55,.19,.14),None])
c={"mediaId":7100,"level":"B","keyWord":"fashion","defaultVoice":"female",
"taps":[{"phrase":"to fashion a makeshift sail","target":"the woman","voice":"female","keys":woman},
{"phrase":"to punch the air","target":"the woman","voice":"female","keys":woman},
{"phrase":"to poke its head out","target":"the seal","voice":"female","keys":seal}],
"stillS":1.2,
"nouns":[{"word":"a sail","x":0.70,"y":0.30,"voice":"female"},{"word":"an iceberg","x":0.20,"y":0.35,"voice":"female"},
{"word":"a seal","x":0.82,"y":0.58,"voice":"female"},{"word":"a sea kayak","x":0.27,"y":0.93,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","fashioning","a","makeshift","sail."],"answerVoice":"female",
"notes":"Only two living targets: the woman (2 phrases) and the seal. 'to punch the air' = she raises her fist at ~3.2 s while looking at the seal (2.2-2.7 she bounces with a fist, a bit weaker). Seal dives at 3.7 (only a splash) -> off. 'to fashion' = key word as verb: she ties the cord/sail at 0.2-1.7."}
json.dump(c,open('content/7100.json','w'),indent=1)
