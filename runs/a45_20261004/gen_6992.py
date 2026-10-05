import json
T=[0.2,0.7,1.2,1.7,2.2]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
woman=K([(.31,.39,.48,.56),(.32,.42,.51,.57),(.40,.47,.42,.53),(.38,.65,.44,.35),(.44,.65,.35,.35)])
dog=K([(.13,.25,.25,.14),(.14,.24,.25,.17),(.15,.25,.24,.18),(.42,.24,.18,.16),(.48,.21,.18,.15)])
bal=K([(.57,0,.20,.16),(.57,.02,.20,.15),(.57,.09,.20,.15),(.60,.19,.18,.14),(.66,.18,.18,.14)])
c={"mediaId":6992,"level":"B","keyWord":"cord","defaultVoice":"female",
"taps":[
 {"phrase":"to hoist a wicker basket","target":"the woman in the street","voice":"female","keys":woman},
 {"phrase":"to peek out of the basket","target":"the dog","voice":"female","keys":dog},
 {"phrase":"to lean over the balcony","target":"the woman on the balcony","voice":"female","keys":bal}],
"stillS":0.2,
"nouns":[{"word":"a pulley","x":0.25,"y":0.09,"voice":"female"},
 {"word":"a balcony","x":0.78,"y":0.22,"voice":"female"},
 {"word":"a wicker basket","x":0.25,"y":0.37,"voice":"female"},
 {"word":"a cord","x":0.52,"y":0.92,"voice":"female"}],
"question":"What is the woman below doing?",
"answer":["She","is","hoisting","a","wicker","basket."],
"answerVoice":"female",
"notes":"Hoisting is visible 0.2-1.2; at 1.7-2.2 she has let go and laughs. At 1.7 and 2.2 the dog/basket and the balcony woman are close: boxes split at the basket edge, her reaching hand is cut. Dog box covers dog + basket (dog head only peeks out). 'a cord' pill sits on the coils of rope on the cobbles (the key word; the rope is thick, cord is a slight stretch)."}
json.dump(c,open('content/6992.json','w'),indent=1)
