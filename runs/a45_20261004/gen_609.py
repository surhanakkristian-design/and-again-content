import json
times=[i*0.5 for i in range(19)]
man={0.0:(0,.44,.66,.30),0.5:(.02,.28,.66,.43),1.0:(.05,.20,.68,.65),1.5:(.28,.24,.62,.66),2.0:(.06,.24,.80,.53),
2.5:(0,.52,.47,.33),3.0:(0,.56,.60,.32),3.5:(0,.54,.59,.33),4.0:(0,.53,.47,.36),4.5:(0,.53,.47,.36),5.0:(0,.56,.47,.32),5.5:(0,.56,.44,.30),
6.0:(0,.53,.43,.33),6.5:(0,.53,.43,.33),7.0:(0,.57,.42,.28),7.5:(0,.57,.42,.28),8.0:(0,.53,.41,.30),8.5:(0,.53,.41,.30),9.0:(0,.54,.41,.28)}
wom={2.5:(.48,.38,.44,.27),3.0:(.61,.35,.39,.34),3.5:(.60,.37,.40,.32),4.0:(.48,.45,.52,.25),4.5:(.48,.45,.52,.25),5.0:(.48,.46,.52,.27),5.5:(.45,.47,.55,.25),
6.0:(.44,.45,.54,.24),6.5:(.44,.46,.54,.24),7.0:(.43,.47,.51,.25),7.5:(.43,.47,.51,.25),8.0:(.42,.45,.50,.25),8.5:(.42,.45,.50,.25),9.0:(.42,.46,.50,.25)}
def keys(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in times]
c={"mediaId":609,"level":"A","keyWord":"rest","defaultVoice":"male",
"taps":[{"phrase":"to carry a red backpack","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to take off his boots","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to wear a blue scarf","target":"the woman","voice":"female","keys":keys(wom)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":.50,"y":.12,"voice":"male"},{"word":"a lake","x":.42,"y":.38,"voice":"male"},{"word":"a rock","x":.80,"y":.64,"voice":"male"},{"word":"a backpack","x":.18,"y":.75,"voice":"male"}],
"question":"What are the man and woman doing?","answer":["They","are","resting","on","the","grass."],"answerVoice":"male",
"notes":"Cartoon. Only two possible targets, so the man has two phrases. The second hiker is read as a woman (hoop earring, red hair, blue headscarf): please check. Both wear orange shirts and both rest, so her phrase is a state (blue scarf). The man carries the red backpack only at 0.0-1.0 and kicks off a boot at 2.0 (his boots lie beside him afterwards). From 2.5 the two lie close together: the boxes are split along a vertical line between their heads, so the man's legs/feet right of that line are outside his box. Woman off at 2.0 (only her eyes peek over the hill behind the man's legs). A small butterfly appears at 4.0-4.5 (not used). 'a backpack' pill sits on the red one; the green one is almost hidden at 8.0."}
json.dump(c,open('content/609.json','w'),indent=1,ensure_ascii=False)
