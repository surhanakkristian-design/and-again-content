import json
W = {0.0:(0.46,0.55,0.36,0.45),0.5:(0.5,0.55,0.35,0.45),1.0:(0.47,0.54,0.34,0.46),1.5:(0.5,0.56,0.34,0.44),2.0:(0.56,0.56,0.34,0.44),
2.5:(0.54,0.58,0.36,0.42),3.0:(0.59,0.58,0.34,0.42),3.5:(0.57,0.58,0.36,0.42),4.0:(0.54,0.57,0.34,0.43),4.5:(0.54,0.58,0.34,0.42),
5.0:(0.48,0.59,0.34,0.41),5.5:(0.53,0.59,0.32,0.41),6.0:(0.51,0.54,0.29,0.38),6.5:(0.48,0.42,0.33,0.56),7.0:(0.46,0.48,0.24,0.42),
7.5:(0.46,0.58,0.2,0.32),8.0:(0.46,0.49,0.18,0.19),8.5:(0.5,0.49,0.18,0.21),9.0:(0.45,0.5,0.19,0.3),9.5:(0.52,0.49,0.18,0.19),10.0:None}
G = {0.0:(0.08,0.03,0.86,0.46),0.5:(0.1,0.03,0.86,0.45),1.0:(0.08,0.03,0.86,0.47),1.5:(0.08,0.03,0.88,0.47),2.0:(0.08,0.0,0.88,0.5),
2.5:(0.1,0.0,0.88,0.5),3.0:(0.08,0.0,0.88,0.5),3.5:(0.08,0.0,0.9,0.5),4.0:(0.02,0.0,0.96,0.52),4.5:(0.02,0.0,0.98,0.52),5.0:(0.0,0.0,1.0,0.55)}
times=[i/2 for i in range(21)]
def ks(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"t":t,"off":True}) for t in times]
wk, gk = ks(W), ks(G)
c={"mediaId":5119,"level":"A","keyWord":"entrance","defaultVoice":"female",
"taps":[{"phrase":"to smile at the camera","target":"the woman in red","voice":"female","keys":wk},
{"phrase":"to wave her arms","target":"the woman in red","voice":"female","keys":wk},
{"phrase":"to open slowly","target":"the big gates","voice":"female","keys":gk}],
"stillS":4.0,
"nouns":[{"word":"an entrance","x":0.52,"y":0.18,"voice":"female"},{"word":"a gate","x":0.8,"y":0.3,"voice":"female"},
{"word":"people","x":0.22,"y":0.6,"voice":"female"},{"word":"a red dress","x":0.66,"y":0.82,"voice":"female"}],
"question":"What is the woman in red doing?","answer":["She","is","smiling","at","the","camera."],"answerVoice":"female",
"notes":"Two staff members push the gates but there are two of them, so they are not a target; 'to open slowly' targets the gates (box covers both doors, from t=5.5 the doors are at the frame edges only -> off). Woman in red is tiny from t=8.0 and hidden in the crowd at t=10.0 (off). 'an entrance' pill is on the opening between the doors, 'a gate' on the right door leaf."}
json.dump(c,open('content/5119.json','w'),indent=1)
