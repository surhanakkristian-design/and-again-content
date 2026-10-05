import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
dog=K([(0,.40,.46,.29),(0,.40,.50,.30),(0,.41,.47,.29),(0,.42,.47,.32),(0,.42,.40,.33),(0,.44,.36,.33),(0,.48,.40,.31),(0,.47,.41,.35)])
woman=K([(.47,.47,.40,.53),(.51,.47,.42,.53),(.48,.47,.50,.53),(.53,.49,.47,.51),(.56,.40,.44,.60),(.58,.38,.42,.62),(.60,.38,.40,.62),(.63,.38,.37,.62)])
c={"mediaId":7101,"level":"A","keyWord":"fast food","defaultVoice":"female",
"taps":[{"phrase":"to give her the food","target":"the dog at the window","voice":"female","keys":dog},
{"phrase":"to lift the bag high","target":"the woman","voice":"female","keys":woman},
{"phrase":"to sit on a scooter","target":"the woman","voice":"female","keys":woman}],
"stillS":2.2,
"nouns":[{"word":"fast food","x":0.65,"y":0.45,"voice":"female"},{"word":"a helmet","x":0.85,"y":0.56,"voice":"female"},
{"word":"a dog","x":0.18,"y":0.62,"voice":"female"},{"word":"a scooter","x":0.76,"y":0.90,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","a","bag","of","fast","food."],"answerVoice":"female",
"notes":"Two more dogs in cook's hats stand in the kitchen behind, so the window dog is named 'the dog at the window' (all wear hats). Dog and woman boxes split at the bag hand-over (0.2-1.2): the bag is between them. Woman box includes the raised bag. Window dog's hand-over only 0.2-1.2 s."}
json.dump(c,open('content/7101.json','w'),indent=1)
