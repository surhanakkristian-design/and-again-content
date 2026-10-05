import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
woman=K([(.42,.18,.56,.80),(.42,.19,.56,.80),(.42,.23,.55,.77),(.42,.26,.56,.74),(.42,.31,.50,.69),(.42,.34,.52,.66),(.42,.36,.54,.64),(.42,.37,.56,.63)])
cloud=K([(.04,.0,.36,h) for h in (.43,.45,.47,.49,.52,.55,.57,.59)])
pers=K([(.23,y,.18,.14) for y in (.44,.46,.48,.50,.53,.56,.58,.60)])
d={"mediaId":5524,"level":"B","keyWord":"active","defaultVoice":"female",
"taps":[{"phrase":"to shield her eyes","target":"the woman","voice":"female","keys":woman},
{"phrase":"to billow into the sky","target":"the ash cloud","voice":"female","keys":cloud},
{"phrase":"to bend over the ground","target":"the person in the distance","voice":"female","keys":pers}],
"stillS":0.2,
"nouns":[{"word":"an ash cloud","x":0.25,"y":0.22,"voice":"female"},{"word":"a jacket","x":0.70,"y":0.50,"voice":"female"},
{"word":"a tripod","x":0.41,"y":0.65,"voice":"female"},{"word":"boots","x":0.53,"y":0.91,"voice":"female"}],
"question":"What is the woman watching?","answer":["She","is","watching","an","active","volcano."],"answerVoice":"female",
"notes":"ash cloud box covers only the left column (the cloud also spreads behind the woman, split at x .40). Person in the distance is small, bends over the ground from ~1.2 s; gender unclear."}
json.dump(d,open("content/5524.json","w"),indent=1)
