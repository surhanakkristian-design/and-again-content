import json
T=[0.2,0.7]
def K(boxes): return [{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,boxes)]
nurse=K([(.53,.36,.29,.44),(.51,.35,.32,.49)])
doc=K([(.00,.30,.23,.52),(.00,.29,.21,.54)])
para=K([(.32,.37,.19,.16),(.31,.36,.19,.17)])
d={"mediaId":7081,"level":"B","keyWord":"emergency room","defaultVoice":"female",
"taps":[{"phrase":"to rush alongside the stretcher","target":"the nurse","voice":"female","keys":nurse},
{"phrase":"to pull on his gloves","target":"the doctor","voice":"male","keys":doc},
{"phrase":"to squeeze a breathing bag","target":"the paramedic on the left","voice":"male","keys":para}],
"stillS":0.2,
"nouns":[{"word":"a stretcher","x":0.40,"y":0.56,"voice":"female"},{"word":"a nurse","x":0.70,"y":0.45,"voice":"female"},
{"word":"a doctor","x":0.12,"y":0.40,"voice":"male"},{"word":"a wheelchair","x":0.82,"y":0.80,"voice":"female"}],
"question":"What is the nurse doing?","answer":["She","is","rushing","alongside","the","stretcher."],"answerVoice":"female",
"notes":"Clip is only 0.88 s (2 frames). Paramedic squeezing the bag is small and partly behind the stretcher; second paramedic right of him is not a target. Doctor holds the gloves stretched - 'pull on' per description."}
json.dump(d,open("content/7081.json","w"),indent=1)
