import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
pian=K([(.47,.53,.42,.34),(.47,.52,.48,.31),(.47,.51,.43,.33),(.46,.51,.42,.33),(.48,.47,.49,.38),(.48,.45,.48,.39),(.47,.43,.48,.42),(.46,.44,.50,.41)])
woman=K([(.70,.37,.18,.16),(.72,.37,.18,.15),(.73,.35,.18,.16),(.74,.33,.18,.18),(.72,.30,.19,.17),(.74,.28,.18,.17),(.75,.26,.18,.17),(.77,.24,.19,.19)])
fall=K([(.02,.04,.55,.32),(.05,.03,.60,.32),(.02,.02,.55,.30),(.05,.02,.55,.30),(.02,.01,.45,.30),(.05,.01,.55,.28),(.02,.01,.40,.28),(.02,.01,.40,.28)])
c={"mediaId":7099,"level":"B","keyWord":"falls","defaultVoice":"male",
"taps":[{"phrase":"to perform on a grand piano","target":"the pianist","voice":"male","keys":pian},
{"phrase":"to plunge into a deep gorge","target":"the waterfall","voice":"male","keys":fall},
{"phrase":"to wear a blue rain poncho","target":"the woman in blue","voice":"female","keys":woman}],
"stillS":0.2,
"nouns":[{"word":"the falls","x":0.25,"y":0.15,"voice":"male"},{"word":"a rainbow","x":0.66,"y":0.25,"voice":"male"},
{"word":"a railing","x":0.62,"y":0.47,"voice":"male"},{"word":"a grand piano","x":0.20,"y":0.60,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","performing","on","a","grand","piano."],"answerVoice":"male",
"notes":"Pianist box and the woman-in-blue box are split horizontally (her legs stand behind his head/coat tails), so her box covers only her upper body. Waterfall box = the top-left curtain of falling water only (spray right of it left out). Other spectators also hold phones, so the woman gets a state phrase (only blue poncho). 'the falls' pill on the main curtain; key word used with 'the'."}
json.dump(c,open('content/7099.json','w'),indent=1)
