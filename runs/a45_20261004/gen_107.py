import json
T=[i*0.5 for i in range(15)]
boy=[(.27,.37,.73,.63),(.17,.16,.83,.84),(.04,.25,.96,.75),(.02,.14,.98,.86),(.03,.20,.97,.62),None,None,None,None,
(.79,.64,.21,.26),(0,.14,1.0,.69),(.07,.10,.93,.73),(.07,.07,.93,.73),(0,0,1.0,1.0),(0,.08,1.0,.73)]
sp=[None]*9+[(.38,.74,.40,.21),(.42,.84,.50,.13),(.42,.84,.50,.13),(.42,.82,.50,.13),None,(.42,.83,.50,.13)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
kb=[k(t,b) for t,b in zip(T,boy)]; ks=[k(t,b) for t,b in zip(T,sp)]
d={"mediaId":107,"level":"A","keyWord":"bowl","defaultVoice":"male",
"taps":[{"phrase":"to take a blue bowl","target":"the boy","voice":"male","keys":kb},
{"phrase":"to drink from the bowl","target":"the boy","voice":"male","keys":kb},
{"phrase":"to lie on the table","target":"the spoon","voice":"male","keys":ks}],
"stillS":7.0,
"nouns":[{"word":"glasses","x":0.47,"y":0.31,"voice":"male"},{"word":"a bowl","x":0.48,"y":0.70,"voice":"male"},
{"word":"a spoon","x":0.68,"y":0.87,"voice":"male"},{"word":"a table","x":0.20,"y":0.93,"voice":"male"}],
"question":"What is the boy doing?",
"answer":["He","is","drinking","milk","from","a","bowl."],
"answerVoice":"male",
"notes":"Cartoon. Only two usable targets: the boy and the spoon (the bowl is in the boy's hands or in front of his face whenever both are visible, and there is a stack of other blue bowls in the cupboard, so it is not a separate tap target). 1.0-2.0 s are close-ups of his hands with the bowl: the box covers hands + bowl. 2.5-4.0 s show only the bowl, the cereal box and the milk jug (at most a sliver of his hand at the top edge) -> boy off. 4.5 s: his hand puts the spoon down; boxes split at x 0.78. He drinks from the bowl at 5.5-6.0 s; the milk is seen at 3.5-4.5 s."}
json.dump(d,open("content/107.json","w"),indent=1)
