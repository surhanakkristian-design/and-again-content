import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":round(r[2]-r[0],2),"h":round(r[3]-r[1],2)}) for t,r in zip(T,rows)]
cutter=K([(0,.15,.56,.78),(0,.14,.53,.77),(0,.14,.52,.80),(0,.13,.62,.80),(0,.05,.49,.66),(0,0,.48,.62),(0,0,.28,.66),(0,0,.28,.66)])
clutch=K([(.57,.13,.83,.39),(.54,.10,.84,.38),(.53,.10,.77,.37),(.63,.07,.81,.37),(.50,.01,.72,.31),(.49,.01,.72,.31),(.44,.01,.70,.30),(.42,.01,.68,.29)])
woman=K([None,None,None,(.82,.13,1,.58),(.73,.15,1,.62),(.73,.13,1,.62),(.71,.13,1,.64),(.69,.15,1,.62)])
c={"mediaId":7009,"level":"B","keyWord":"cut up","defaultVoice":"male",
"taps":[{"phrase":"to cut up a giant pizza","target":"the man with the pizza cutter","voice":"male","keys":cutter},
{"phrase":"to clutch his head","target":"the man in the black T-shirt","voice":"male","keys":clutch},
{"phrase":"to wear a yellow raincoat","target":"the woman in the raincoat","voice":"female","keys":woman}],
"stillS":0.7,
"nouns":[{"word":"bunting","x":0.30,"y":0.07,"voice":"male"},{"word":"a baking tray","x":0.70,"y":0.41,"voice":"male"},
{"word":"an apron","x":0.12,"y":0.56,"voice":"male"},{"word":"a pizza cutter","x":0.62,"y":0.61,"voice":"male"}],
"question":"What is happening to the pizza?",
"answer":["The","pizza","is","being","cut","into","squares."],"answerVoice":"male",
"notes":"Woman target is a state (raincoat): she reaches for slices, but the man in the blue cap also reaches/holds a plate, so no action is unique to her; she is off at 0.2-1.2 (only a yellow sliver at the right edge at 1.2). Cutter and clutching man rectangles split along a vertical line at 0.2-2.7, so the cutter's outstretched arm/cutter tip is partly outside his box. At 3.2/3.7 the cutter is only at the left edge (head/arm + hand with cutter). Woman/clutching man split vertically at 2.2-3.7 (her reaching hand partly cut). Question asks about the pizza (passive answer) because two men wear a white T-shirt and apron."}
json.dump(c,open('content/7009.json','w'),indent=1)
