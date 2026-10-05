import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [dict(t=t, **dict(zip("xywh", d[t]))) if t in d else dict(t=t, off=True) for t in T]
wom={0:(.52,0,.48,1),.5:(.47,0,.53,1),1:(.60,0,.40,1),1.5:(.47,0,.53,1),2:(.70,0,.30,.84),2.5:(.47,0,.53,.86),
3:(.42,0,.58,.90),3.5:(.48,0,.52,.70),4:(.42,0,.58,.68),4.5:(.50,0,.50,1),5:(.32,0,.68,1),5.5:(.30,0,.70,1),
6:(.30,0,.70,1),6.5:(.34,0,.66,1),7:(.42,0,.58,1),7.5:(.62,0,.38,1),8:(.66,.19,.34,.81),8.5:(.78,.26,.22,.74),
9:(.78,.33,.22,.67),9.5:(.68,.34,.32,.66),10:(.66,.32,.34,.68)}
man={0:(0,0,.20,.96),.5:(0,0,.20,.96)}
c={"mediaId":743,"level":"A","keyWord":"straight","defaultVoice":"female",
"taps":[
{"phrase":"to point at the road","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to wear a blue shirt","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to close one eye","target":"the woman","voice":"female","keys":keys(wom)}],
"stillS":7.0,
"nouns":[{"word":"the sky","x":.20,"y":.15,"voice":"female"},{"word":"a cap","x":.62,"y":.07,"voice":"female"},
{"word":"a road","x":.22,"y":.58,"voice":"female"},{"word":"a shoe","x":.78,"y":.88,"voice":"female"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","at","a","straight","road."],
"answerVoice":"female",
"notes":"The man is visible only at 0.0 and 0.5 s and only stands and watches, so his phrase is a state (blue shirt). 1.0-4.0 s show only the woman's hands/arms (grey rolled sleeves) laying bricks: boxed as the woman. She closes one eye at 4.5-6.5 s and points at 9.5-10.0 s. Key word 'straight' (adjective) is in the answer."}
json.dump(c,open("content/743.json","w"),indent=1)
