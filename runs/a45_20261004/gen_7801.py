import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
W=[(0.12,0.32,0.46,0.32),(0.18,0.33,0.46,0.32),(0.20,0.32,0.50,0.32),(0.30,0.32,0.40,0.33),(0.23,0.33,0.37,0.33),(0.19,0.33,0.35,0.33),(0.18,0.33,0.32,0.35),(0.21,0.33,0.37,0.35)]
M=[(0.59,0.51,0.31,0.39),(0.65,0.51,0.26,0.39),(0.71,0.52,0.21,0.38),(0.71,0.52,0.21,0.38),(0.61,0.51,0.28,0.39),(0.55,0.52,0.33,0.38),(0.53,0.51,0.34,0.39),(0.60,0.51,0.29,0.39)]
k=lambda B:[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
d={"mediaId":7801,"level":"A","keyWord":"depend on","defaultVoice":"female",
"taps":[
 {"phrase":"to hang from a rope","target":"the woman","voice":"female","keys":k(W)},
 {"phrase":"to stand on the path","target":"the man","voice":"male","keys":k(M)},
 {"phrase":"to wear a blue T-shirt","target":"the man","voice":"male","keys":k(M)}],
"stillS":3.2,
"nouns":[{"word":"the sky","x":0.15,"y":0.20,"voice":"female"},{"word":"a rock","x":0.62,"y":0.12,"voice":"female"},
 {"word":"a bush","x":0.11,"y":0.72,"voice":"female"},{"word":"a bag","x":0.86,"y":0.91,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","hanging","from","a","rope."],"answerVoice":"female",
"notes":"Level A. Woman's feet come close to the man's head/hands at 0.7-2.2 s; boxes split along x, so the man's box loses his left leg/hands a little there. Third phrase is a state (blue T-shirt) because the woman also holds the rope and both smile/look up. 'a bag' = rope bag at bottom right."}
json.dump(d,open("content/7801.json","w"),indent=1)
