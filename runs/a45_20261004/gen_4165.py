import json
times=[i*0.5 for i in range(24)]
carb={6.5:(.37,.42,.33,.14),7.0:(.53,.43,.31,.14),7.5:(.42,.42,.40,.17),8.0:(.24,.39,.56,.25)}
treeb={6.5:(.25,0,.75,.41),7.0:(.30,0,.70,.42),7.5:(.30,0,.70,.41),8.0:(.30,0,.70,.38)}
def keys(b):
    return [({"t":t,"x":float(b[t][0]),"y":float(b[t][1]),"w":float(b[t][2]),"h":float(b[t][3])} if t in b else {"t":t,"off":True}) for t in times]
man=[({"t":t,"off":True} if t in carb else {"t":t,"x":0.0,"y":0.26,"w":1.0,"h":0.74}) for t in times]
d={"mediaId":4165,"level":"A","keyWord":"speed","defaultVoice":"male",
"taps":[
 {"phrase":"to smile at the camera","target":"the man","voice":"male","keys":man},
 {"phrase":"to come around a corner","target":"the yellow car","voice":"male","keys":keys(carb)},
 {"phrase":"to be tall and green","target":"the trees","voice":"male","keys":keys(treeb)}],
"stillS":7.5,
"nouns":[{"word":"a car","x":0.62,"y":0.51,"voice":"male"},
 {"word":"trees","x":0.65,"y":0.20,"voice":"male"},
 {"word":"a road","x":0.50,"y":0.72,"voice":"male"},
 {"word":"rocks","x":0.15,"y":0.42,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","driving","at","high","speed."],
"answerVoice":"male",
"notes":"Key word 'speed' is abstract: not a noun on the still, used in the model answer (the speed shows in the blurred window behind the driver). Outside shot only 6.5-8.0 s (4 frames): the yellow car and the trees are tappable only there. The man smiles at the camera at 2.5, 5.0, 9.0, 11.0-11.5 s, otherwise he looks ahead and talks. Trees phrase is a state (nothing else to do for trees); the trees box leaves out the rock face on the left."}
json.dump(d,open("content/4165.json","w"),indent=1,ensure_ascii=False)
