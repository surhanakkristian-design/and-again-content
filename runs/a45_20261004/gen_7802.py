import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
M=[(0.10,0.29,0.36,0.70),(0.10,0.29,0.45,0.70),(0.09,0.28,0.45,0.72),(0.07,0.25,0.46,0.75),(0.00,0.24,0.55,0.76),(0.00,0.23,0.57,0.77),(0.00,0.23,0.50,0.77),(0.00,0.23,0.54,0.77)]
W=[(0.47,0.29,0.47,0.71),(0.56,0.29,0.36,0.71),(0.55,0.28,0.44,0.72),(0.65,0.27,0.34,0.73),(0.64,0.28,0.36,0.72),(0.68,0.27,0.32,0.73),(0.51,0.29,0.49,0.71),(0.55,0.29,0.45,0.71)]
k=lambda B:[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":round(min(b[3],1-b[1]),2)} for t,b in zip(T,B)]
d={"mediaId":7802,"level":"B","keyWord":"deserve","defaultVoice":"male",
"taps":[
 {"phrase":"to present a medal","target":"the woman","voice":"female","keys":k(W)},
 {"phrase":"to bow his head","target":"the man","voice":"male","keys":k(M)},
 {"phrase":"to be covered in mud","target":"the man","voice":"male","keys":k(M)}],
"stillS":2.2,
"nouns":[{"word":"pine trees","x":0.18,"y":0.10,"voice":"male"},{"word":"a wooden wall","x":0.58,"y":0.32,"voice":"male"},
 {"word":"a medal","x":0.36,"y":0.57,"voice":"male"},{"word":"a hay bale","x":0.62,"y":0.80,"voice":"male"}],
"question":"What hangs around the man's neck?","answer":["A","medal","hangs","around","his","neck."],"answerVoice":"male",
"notes":"Woman presents the medal at 0.2-1.2 s; her reaching arms overlap the man's head/chest, so her boxes start right of the man's box (hands partly outside). 'to bow his head' is true at 0.2-0.7 s only, then he lifts his head."}
json.dump(d,open("content/7802.json","w"),indent=1)
