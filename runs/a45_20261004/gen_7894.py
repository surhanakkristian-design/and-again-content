from gen_7891_7892_7893_7894_lib import *
wom=keys([(.39,.36,.66,.73),(.39,.36,.64,.73),(.39,.36,.71,.73),(.39,.36,.68,.73),(.39,.35,.68,.73),(.39,.35,.61,.73),(.38,.36,.57,.74),(.38,.36,.58,.74)])
dog=keys([(.43,.74,.73,.97),(.43,.74,.75,.98),(.42,.74,.78,.98),(.47,.74,.82,.98),(.52,.78,.83,.98),(.52,.79,.76,1),(.44,.76,.71,1),(.38,.75,.74,.98)])
cyc=keys([(.79,.49,.97,.63),(.80,.49,.98,.63),(.81,.49,.99,.64),(.82,.50,1,.64),(.82,.49,1,.65),(.81,.49,.99,.66),(.77,.50,.95,.66),None])
write({"mediaId":7894,"level":"A","keyWord":"live","defaultVoice":"female",
"taps":[{"phrase":"to drink from a cup","target":"the woman","voice":"female","keys":wom},
{"phrase":"to walk up the steps","target":"the dog","voice":"female","keys":dog},
{"phrase":"to ride a bike","target":"the cyclist","voice":"male","keys":cyc}],
"stillS":2.2,
"nouns":[{"word":"smoke","x":0.32,"y":0.22,"voice":"female"},{"word":"a plane","x":0.20,"y":0.42,"voice":"female"},
{"word":"a sheet","x":0.78,"y":0.50,"voice":"female"},{"word":"a dog","x":0.68,"y":0.88,"voice":"female"}],
"question":"Where does the woman live?","answer":["She","lives","in","an","old","plane."],"answerVoice":"female",
"notes":"Cyclist is small in the background (minimum-size box), looks male (voice male), hidden behind the sheet at 3.7 (off). Woman drinks from the cup at 3.2-3.7 (lifts it at 2.7). Dog moves around on the steps and climbs up at 3.7. Question uses the key word: the home (plants, doormat, boots, chimney smoke) is shown, but 'lives in' is an inference - check."})
