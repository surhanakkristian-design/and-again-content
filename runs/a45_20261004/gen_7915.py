import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
man=K([(.00,.32,.67,.68),(.00,.32,.68,.68),(.00,.36,.62,.64),(.00,.42,.60,.58),(.00,.52,.55,.48),(.00,.64,.60,.36),(.02,.80,.34,.20),None])
cook=K([(.72,.48,.28,.50),(.70,.52,.30,.46),(.80,.82,.20,.18),(.80,.85,.20,.15),None,None,None,None])
clock=K([None,None,None,None,None,(.34,.00,.30,.14),(.35,.02,.28,.18),(.37,.11,.27,.18)])
c={"mediaId":7915,"level":"A","keyWord":"noon","defaultVoice":"male",
"taps":[{"phrase":"to hold a box of noodles","target":"the man in front","voice":"male","keys":man},
{"phrase":"to cook the noodles","target":"the cook","voice":"male","keys":cook},
{"phrase":"to show twelve o'clock","target":"the clock","voice":"male","keys":clock}],
"stillS":3.2,
"nouns":[{"word":"a clock","x":0.50,"y":0.13,"voice":"male"},{"word":"the sky","x":0.88,"y":0.04,"voice":"male"},
{"word":"a building","x":0.13,"y":0.32,"voice":"male"},{"word":"people","x":0.20,"y":0.68,"voice":"male"}],
"question":"What is the man holding?","answer":["He","is","holding","a","box","of","noodles."],"answerVoice":"male",
"notes":"cook is only seen as a gloved arm/hand at the right edge (0.2-1.7 s), gender not visible -> voice = defaultVoice male; the two women both eat, so no woman phrase; clock only visible from 2.7 s (camera tilts up); many men in white shirts and ties in the crowd but the target man is the big foreground one"}
json.dump(c,open('content/7915.json','w'),indent=1)
