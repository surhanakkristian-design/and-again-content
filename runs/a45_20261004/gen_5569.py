import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def K(boxes): return [ {"t":t,"off":True} if b is None else {"t":t,"x":round(b[0],2),"y":round(b[1],2),"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,boxes)]
wom=[(0.23,0.0,0.88,0.71),(0.23,0.0,0.88,0.71),(0.23,0.0,0.88,0.72),(0.23,0.0,0.89,0.72),(0.23,0.0,0.89,0.74),(0.23,0.0,0.89,0.74)]
jar=[(0.0,0.52,0.23,0.93),(0.0,0.52,0.23,0.92),(0.0,0.53,0.23,0.93),(0.0,0.53,0.23,0.93),(0.0,0.55,0.23,0.96),(0.0,0.56,0.23,0.96)]
c={"mediaId":5569,"level":"A","keyWord":"artificial","defaultVoice":"female",
"taps":[{"phrase":"to hold two pink roses","target":"the woman","voice":"female","keys":K(wom)},
{"phrase":"to pull off a petal","target":"the woman","voice":"female","keys":K(wom)},
{"phrase":"to stand in a jar","target":"the roses in the jar","voice":"female","keys":K(jar)}],
"stillS":2.2,
"nouns":[{"word":"a kettle","x":0.80,"y":0.24,"voice":"female"},{"word":"a window","x":0.12,"y":0.32,"voice":"female"},
{"word":"an apron","x":0.52,"y":0.63,"voice":"female"},{"word":"a box","x":0.85,"y":0.88,"voice":"female"}],
"question":"What is the woman holding?","answer":["She","is","holding","two","pink","roses."],"answerVoice":"female",
"notes":"Only one clear person (workers behind are cut-off hands), so two phrases target the woman; 'pull off a petal' is visible only at the start (0.2 s). Woman's box starts at x 0.23 so it does not overlap the jar roses; her left elbow is slightly outside. 'a box' = the tray of handmade roses bottom right."}
json.dump(c,open('content/5569.json','w'),indent=1)
