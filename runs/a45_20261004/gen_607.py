import json
times=[i*0.5 for i in range(21)]
dog={0.0:(.66,.72,.34,.25),8.5:(.80,.68,.20,.16),9.0:(.77,.68,.23,.16),9.5:(.80,.67,.20,.17),10.0:(.78,.66,.22,.19)}
wom={1.5:(.60,.24,.40,.76),2.0:(.47,.25,.42,.70),2.5:(.48,.25,.39,.65),3.0:(.75,.03,.25,.72),6.5:(.55,.12,.45,.88),7.0:(.56,.25,.44,.75),7.5:(.78,.27,.22,.73),8.0:(.80,.27,.20,.73),8.5:(.46,.25,.34,.75),9.0:(.46,.27,.31,.73),9.5:(.46,.27,.34,.73),10.0:(.46,.25,.32,.75)}
man={2.0:(.89,.14,.11,.27),2.5:(.87,.12,.13,.33),6.5:(0,.10,.24,.90),7.0:(0,.20,.37,.80),7.5:(0,.20,.33,.80),8.0:(0,.21,.33,.79),8.5:(0,.20,.38,.80),9.0:(0,.20,.39,.80),9.5:(0,.21,.42,.79),10.0:(0,.20,.42,.80)}
def keys(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in times]
c={"mediaId":607,"level":"A","keyWord":"refrigerator","defaultVoice":"male",
"taps":[{"phrase":"to lie on the floor","target":"the dog","voice":"male","keys":keys(dog)},
{"phrase":"to carry a basket","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to have a black beard","target":"the man","voice":"male","keys":keys(man)}],
"stillS":10.0,
"nouns":[{"word":"a refrigerator","x":.50,"y":.26,"voice":"male"},{"word":"a dog","x":.88,"y":.76,"voice":"male"},{"word":"a man","x":.20,"y":.50,"voice":"male"},{"word":"a woman","x":.68,"y":.57,"voice":"female"}],
"question":"Where are the man and woman standing?","answer":["They","are","standing","next","to","the","refrigerator."],"answerVoice":"male",
"notes":"Shots with only an arm/hands (0.0, 3.5-6.0) have the people off: the owner of the hand is not shown. Man at 2.0/2.5 is only a face at the right edge behind the woman, so his box is small and split from hers. Dog is off at 8.0 (almost hidden behind the door and the woman). The man's phrase is a state (beard): everything he does, the woman does too. Woman carries the basket only at 1.5-3.0."}
json.dump(c,open('content/607.json','w'),indent=1,ensure_ascii=False)
