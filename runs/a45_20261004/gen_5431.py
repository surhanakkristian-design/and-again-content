import json
B={0.0:(0.0,0.3,0.39,0.7),0.5:(0.0,0.28,0.4,0.72),1.0:(0.0,0.28,0.42,0.72),1.5:(0.0,0.28,0.42,0.72),
2.0:(0.0,0.27,0.44,0.73),2.5:(0.0,0.27,0.44,0.73),3.0:(0.0,0.27,0.44,0.73),3.5:(0.0,0.27,0.44,0.73),
4.0:(0.0,0.27,0.44,0.73),4.5:(0.0,0.27,0.42,0.73),5.0:(0.08,0.58,0.52,0.42),5.5:(0.0,0.58,0.42,0.42),
6.0:(0.0,0.57,0.44,0.43),6.5:(0.0,0.57,0.5,0.43),7.0:(0.0,0.58,0.52,0.42),7.5:(0.0,0.58,0.52,0.42),
8.0:(0.0,0.58,0.44,0.42),8.5:(0.0,0.2,0.74,0.8),9.0:(0.0,0.22,0.74,0.78),9.5:(0.0,0.22,0.78,0.78),
10.0:(0.0,0.22,0.78,0.78),10.5:(0.0,0.21,0.8,0.79),11.0:(0.0,0.2,0.82,0.8),11.5:(0.0,0.2,0.82,0.8),12.0:(0.0,0.19,0.84,0.81)}
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in B.items()]
tap=lambda p:{"phrase":p,"target":"the woman","voice":"female","keys":keys}
c={"mediaId":5431,"level":"A","keyWord":"balloon","defaultVoice":"female",
"taps":[tap("to look at the balloons"),tap("to point at the shelves"),tap("to drink a glass of tea")],
"stillS":2.0,
"nouns":[{"word":"the sky","x":0.6,"y":0.1,"voice":"female"},{"word":"a woman","x":0.2,"y":0.55,"voice":"female"},
{"word":"rocks","x":0.74,"y":0.7,"voice":"female"},{"word":"a balloon","x":0.78,"y":0.86,"voice":"female"}],
"question":"What is the woman drinking?","answer":["She","is","drinking","a","glass","of","tea."],"answerVoice":"female",
"notes":"Montage with cuts at 5.0 (bazaar, only her hand/arm visible, boxed as the woman) and 8.5 (ferry). Balloons and gulls are many and alike, so all three phrases use the woman. 'a balloon' pill is on the large close balloon; many small balloons elsewhere in the sky."}
json.dump(c,open('content/5431.json','w'),indent=1)
