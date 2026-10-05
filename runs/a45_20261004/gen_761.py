import json
def mk(K,i):
    return [{"t":t,"x":K[t][i][0],"y":K[t][i][1],"w":K[t][i][2],"h":K[t][i][3]} for t in sorted(K)]
# man, woman, cushion
K={0.0:((0,.05,.25,.30),(.26,0,.74,.68),(0,.69,1,.17)),
0.5:((0,.05,.25,.36),(.26,0,.74,.71),(0,.72,1,.15)),
1.0:((0,.08,.22,.40),(.23,0,.77,.85),(0,.86,1,.12)),
1.5:((0,0,.20,.56),(.21,0,.79,.86),(0,.87,1,.11)),
2.0:((0,0,.22,.39),(.23,0,.77,.75),(0,.76,1,.14)),
2.5:((0,0,.30,.40),(.31,0,.69,.77),(0,.78,1,.14)),
3.0:((0,0,.44,.57),(.45,.05,.55,.84),(0,.90,1,.10)),
3.5:((0,0,.49,.57),(.50,.05,.50,.86),(0,.92,1,.08)),
4.0:((0,0,.52,.47),(.53,.07,.47,.72),(0,.80,1,.15)),
4.5:((0,0,.46,.46),(.47,.05,.53,.74),(0,.80,1,.15)),
5.0:((0,0,.43,.57),(.44,.07,.56,.83),(0,.91,1,.09)),
5.5:((0,0,.26,.56),(.27,.05,.73,.58),(0,.64,1,.28)),
6.0:((0,0,.38,.46),(.39,.06,.61,.68),(0,.75,1,.20)),
6.5:((0,0,.40,.42),(.41,.06,.59,.67),(0,.74,1,.20)),
7.0:((0,0,.47,.52),(.48,.08,.52,.78),(0,.87,1,.12)),
7.5:((0,0,.44,.51),(.45,.08,.55,.78),(0,.87,1,.12)),
8.0:((0,0,.42,.42),(.43,.06,.57,.67),(0,.74,1,.20)),
8.5:((0,0,.42,.48),(.43,.03,.57,.72),(0,.76,1,.18)),
9.0:((0,0,.42,.57),(.43,.07,.57,.79),(0,.87,1,.12)),
9.5:((0,0,.40,.57),(.41,.07,.59,.79),(0,.87,1,.12)),
10.0:((0,0,.42,.47),(.43,.07,.57,.69),(0,.77,1,.16))}
d={"mediaId":761,"level":"B","keyWord":"swelling","defaultVoice":"male",
"taps":[{"phrase":"to gasp in shock","target":"the man","voice":"male","keys":mk(K,0)},
{"phrase":"to wince in pain","target":"the woman","voice":"female","keys":mk(K,1)},
{"phrase":"to prop up her feet","target":"the cushion","voice":"male","keys":mk(K,2)}],
"stillS":6.5,
"nouns":[{"word":"an ice pack","x":.22,"y":.30,"voice":"male"},{"word":"glasses","x":.14,"y":.06,"voice":"male"},
{"word":"swelling","x":.72,"y":.62,"voice":"male"},{"word":"a cushion","x":.50,"y":.82,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","putting","an","ice","pack","on","the","swelling."],
"answerVoice":"male",
"notes":"The woman's feet lie in front of the man, so the three targets overlap in the picture: man box = upper left (his head, body, arm above the feet), woman box = from the man's right edge to the right, down to the soles (her left foot, viewer's left, is partly outside it), cushion box = strip below the feet. From 7.5 s the man's hand on the ice pack lies inside the woman's box; that is why his phrase is about his face (gasp), not the ice pack. defaultVoice male: mixed pair, odd id. 'swelling' = the redder, puffier foot/ankle (viewer's right); weakest noun."}
json.dump(d,open("content/761.json","w"),indent=1,ensure_ascii=False)
