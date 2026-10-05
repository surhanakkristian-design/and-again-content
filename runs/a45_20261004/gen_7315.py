import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
horse=[(0.09,0.61,0.18,0.14),(0.07,0.61,0.18,0.14),(0.05,0.62,0.18,0.14),(0.03,0.62,0.18,0.14),(0.01,0.63,0.19,0.14),(0.01,0.64,0.18,0.14),(0.01,0.65,0.18,0.14),(0.01,0.66,0.20,0.14)]
seal=[(0.12,0.76,0.22,0.14),(0.12,0.76,0.22,0.14),(0.13,0.77,0.22,0.14),(0.16,0.77,0.20,0.14),(0.21,0.77,0.20,0.14),(0.23,0.76,0.21,0.14),(0.28,0.75,0.20,0.14),(0.33,0.75,0.19,0.14)]
k=lambda L:[{"t":t,"x":a,"y":b,"w":c,"h":d} for t,(a,b,c,d) in zip(T,L)]
c={"mediaId":7315,"level":"B","keyWord":"mainland","defaultVoice":"male",
"taps":[{"phrase":"to lead the herd","target":"the first horse","voice":"male","keys":k(horse)},
{"phrase":"to reach the sandy shore","target":"the first horse","voice":"male","keys":k(horse)},
{"phrase":"to bask on the rocks","target":"the seal","voice":"male","keys":k(seal)}],
"stillS":2.2,
"nouns":[{"word":"mountains","x":0.60,"y":0.16,"voice":"male"},{"word":"the mainland","x":0.22,"y":0.26,"voice":"male"},
{"word":"horses","x":0.60,"y":0.52,"voice":"male"},{"word":"a seal","x":0.30,"y":0.82,"voice":"male"}],
"question":"What are the horses doing?","answer":["They","are","wading","towards","the","mainland."],"answerVoice":"male",
"notes":"Only the first horse and the seal are single clear targets; the other horses all wade, so no third target. 'to reach the sandy shore' holds only at the end (first horse at the waterline ~3.2-3.7 s). Lead horse is small: boxes at the 0.18 x 0.14 minimum."}
json.dump(c,open('content/7315.json','w'),indent=1)
