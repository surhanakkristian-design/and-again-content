import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [dict(t=t,**dict(zip('xywh',r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(.20,.12,.52,.49),(.24,.08,.59,.55),(.32,.04,.55,.61),(.40,.01,.53,.68),(.41,0,.53,.70),(.41,.02,.53,.70),(.40,.05,.33,.67),(.40,.07,.30,.67)])
man=K([None,None,(.05,.45,.26,.31),(.07,.47,.32,.30),(.06,.49,.34,.32),(.07,.51,.33,.31),(.05,.52,.34,.30),(.07,.52,.32,.30)])
c={"mediaId":7363,"level":"A","keyWord":"mobile phone","defaultVoice":"female",
"taps":[{"phrase":"to hold her phone up","target":"the woman","voice":"female","keys":woman},
{"phrase":"to stand on a big rock","target":"the woman","voice":"female","keys":woman},
{"phrase":"to eat a sandwich","target":"the man","voice":"male","keys":man}],
"stillS":2.7,
"nouns":[{"word":"a mobile phone","x":.45,"y":.07,"voice":"female"},{"word":"the sky","x":.18,"y":.22,"voice":"female"},
{"word":"a backpack","x":.38,"y":.90,"voice":"female"},{"word":"a map","x":.80,"y":.86,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","holding","her","phone","above","her","head."],"answerVoice":"female",
"notes":"The man is hidden behind the woman's legs at 0.2 and 0.7 s (off). From 1.2 s the boxes are split at x 0.31-0.40 where her legs stand in front of his shoulder, so his right shoulder and her raised left arm/hair edge are cut a little. He laughs with the sandwich 1.2-2.2 s and bites it 2.7-3.7 s. Two black birds fly past only at 3.2-3.7 s, too small to use."}
json.dump(c,open('content/7363.json','w'),indent=1)
