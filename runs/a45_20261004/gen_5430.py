import json
B={0.0:(0.14,0.32,0.86,0.68),0.5:(0.1,0.33,0.9,0.67),1.0:(0.14,0.34,0.86,0.66),1.5:(0.12,0.32,0.88,0.68),
2.0:(0.12,0.32,0.88,0.68),2.5:(0.12,0.33,0.88,0.67),3.0:(0.14,0.35,0.86,0.65),3.5:(0.12,0.34,0.88,0.66),
4.0:(0.1,0.31,0.9,0.69),4.5:(0.1,0.29,0.9,0.71),5.0:(0.1,0.3,0.9,0.7),5.5:(0.14,0.34,0.86,0.66),
6.0:(0.14,0.35,0.86,0.65),6.5:(0.12,0.35,0.88,0.65),7.0:(0.14,0.36,0.86,0.64),7.5:(0.12,0.36,0.88,0.64),
8.0:(0.12,0.34,0.88,0.66),8.5:(0.08,0.36,0.92,0.64),9.0:(0.08,0.37,0.92,0.63)}
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in B.items()]
tap=lambda p:{"phrase":p,"target":"the woman","voice":"female","keys":keys}
c={"mediaId":5430,"level":"A","keyWord":"fast","defaultVoice":"female",
"taps":[tap("to ride a bike fast"),tap("to wear a helmet"),tap("to smile at the camera")],
"stillS":2.0,
"nouns":[{"word":"trees","x":0.5,"y":0.08,"voice":"female"},{"word":"a helmet","x":0.5,"y":0.38,"voice":"female"},
{"word":"a tunnel","x":0.8,"y":0.48,"voice":"female"},{"word":"a road","x":0.87,"y":0.68,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","riding","a","bike","fast."],"answerVoice":"female",
"notes":"Selfie POV: the woman is the only clear target (car passes only briefly at 6.0/8.5, partly behind her), so all three phrases use her. Key word 'fast' is an adjective/adverb, used in phrase 1 and the answer."}
json.dump(c,open('content/5430.json','w'),indent=1)
