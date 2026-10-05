import json
B={0.0:(0.18,0.15,0.44,0.85),0.5:(0.15,0.14,0.49,0.86),1.0:(0.2,0.18,0.6,0.82),1.5:(0.0,0.27,0.9,0.53),
2.0:(0.31,0.06,0.43,0.72),2.5:(0.32,0.0,0.42,0.78),3.0:(0.3,0.02,0.42,0.78),3.5:(0.3,0.02,0.42,0.78),
4.0:(0.29,0.04,0.42,0.8),4.5:(0.3,0.1,0.4,0.76),5.0:(0.32,0.4,0.32,0.27),5.5:(0.18,0.26,0.66,0.62),
6.0:(0.14,0.18,0.68,0.72),6.5:(0.14,0.16,0.7,0.74),7.0:(0.14,0.18,0.68,0.72),7.5:(0.18,0.09,0.66,0.91),
8.0:(0.18,0.15,0.6,0.85),8.5:(0.2,0.36,0.56,0.64),9.0:(0.27,0.34,0.5,0.66),9.5:(0.3,0.33,0.5,0.67),10.0:(0.3,0.41,0.45,0.59)}
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in B.items()]
tap=lambda p:{"phrase":p,"target":"the woman","voice":"female","keys":keys}
c={"mediaId":5429,"level":"A","keyWord":"trust","defaultVoice":"female",
"taps":[tap("to close her eyes"),tap("to fall backwards"),tap("to stand on a box")],
"stillS":3.0,
"nouns":[{"word":"lights","x":0.2,"y":0.12,"voice":"female"},{"word":"a woman","x":0.5,"y":0.32,"voice":"female"},
{"word":"hands","x":0.5,"y":0.8,"voice":"female"},{"word":"a box","x":0.45,"y":0.92,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","falling","backwards."],"answerVoice":"female",
"notes":"Only one clear individual target (the woman); the group is too spread to box, so all three phrases use her. Cuts at 1.5/2.0/5.5/8.5 (angle changes). Key word 'trust' is a verb, not placed as a noun."}
json.dump(c,open('content/5429.json','w'),indent=1)
