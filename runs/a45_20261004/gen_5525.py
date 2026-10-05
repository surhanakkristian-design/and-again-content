import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
man=K([(.47,.0,.52,.47),(.48,.06,.51,.46),(.48,.11,.52,.46),(.50,.18,.50,.42),(.51,.21,.49,.42),(.51,.21,.49,.41),(.51,.21,.49,.41),(.51,.21,.49,.41)])
hands=K([(.0,.56,1.0,.44),(.18,.56,.82,.44),(.0,.58,1.0,.42),(.0,.61,1.0,.39),(.0,.63,1.0,.37),(.0,.63,1.0,.37),(.0,.63,1.0,.37),(.0,.63,1.0,.37)])
d={"mediaId":5525,"level":"B","keyWord":"add together","defaultVoice":"male",
"taps":[{"phrase":"to lean on the counter","target":"the barista","voice":"male","keys":man},
{"phrase":"to count on his fingers","target":"the barista","voice":"male","keys":man},
{"phrase":"to sweep the coins together","target":"the customer's hands","voice":"male","keys":hands}],
"stillS":3.7,
"nouns":[{"word":"a coffee urn","x":0.27,"y":0.31,"voice":"male"},{"word":"a pendant lamp","x":0.60,"y":0.15,"voice":"male"},
{"word":"an apron","x":0.72,"y":0.49,"voice":"male"},{"word":"coins","x":0.52,"y":0.74,"voice":"male"}],
"question":"What is the barista doing?","answer":["He","is","counting","on","his","fingers."],"answerVoice":"male",
"notes":"POV clip, camera pulls back; customer's hands (gender not shown, default voice). Barista raises a finger from ~2.2 s (counting gesture); 'lean on the counter' visible throughout."}
json.dump(d,open("content/5525.json","w"),indent=1)
