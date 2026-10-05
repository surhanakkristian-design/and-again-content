import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
jay=[(0.17,0.31,0.48,0.30),(0.17,0.31,0.48,0.30),(0.18,0.30,0.53,0.31),(0.15,0.30,0.59,0.31),(0.15,0.28,0.60,0.33),(0.15,0.28,0.60,0.33),(0.16,0.26,0.58,0.35),(0.16,0.24,0.58,0.37)]
sq=[(0.02,0.65,0.96,0.33)]*8
k=lambda b:[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,(x,y,w,h) in zip(T,b)]
d={"mediaId":7259,"level":"B","keyWord":"jay","defaultVoice":"male",
"taps":[{"phrase":"to open its beak wide","target":"the jay on the doughnut","voice":"male","keys":k(jay)},
{"phrase":"to perch on a doughnut","target":"the jay on the doughnut","voice":"male","keys":k(jay)},
{"phrase":"to sit in a row","target":"the squirrels on the bench","voice":"male","keys":k(sq)}],
"stillS":3.7,
"nouns":[{"word":"a jay","x":0.60,"y":0.42,"voice":"male"},{"word":"a glazed doughnut","x":0.50,"y":0.61,"voice":"male"},
{"word":"a layer cake","x":0.88,"y":0.53,"voice":"male"},{"word":"squirrels","x":0.50,"y":0.80,"voice":"male"}],
"question":"What is the jay standing on?","answer":["It","is","standing","on","a","glazed","doughnut."],"answerVoice":"male",
"notes":"Second jay flies in the sky (small, upper left) and is not a target; the squirrel climbing onto the table (0.2-1.2 s, right) is inside neither box's phrase: it is on the table, not sitting in a row on the bench. Only two targets: the blanket overlaps the jay."}
json.dump(d,open("content/7259.json","w"),indent=1)
