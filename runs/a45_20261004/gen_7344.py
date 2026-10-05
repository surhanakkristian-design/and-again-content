import json
T=[0.2,0.7,1.2,1.7,2.2,2.7]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
W=[(0.10,0.37,0.48,0.51),(0.10,0.38,0.48,0.50),(0.16,0.38,0.45,0.52),(0.27,0.43,0.33,0.46),(0.36,0.40,0.36,0.46),(0.39,0.40,0.30,0.46)]
M=[(0.58,0.38,0.30,0.43),(0.59,0.38,0.30,0.44),(0.62,0.42,0.27,0.40),(0.78,0.46,0.20,0.32),(0.76,0.46,0.20,0.30),(0.70,0.46,0.20,0.24)]
wk=[k(t,b) for t,b in zip(T,W)]; mk=[k(t,b) for t,b in zip(T,M)]
d={"mediaId":7344,"level":"B","keyWord":"messenger","defaultVoice":"female",
"taps":[{"phrase":"to hand over an envelope","target":"the woman","voice":"female","keys":wk},
{"phrase":"to pedal along the pavement","target":"the woman","voice":"female","keys":wk},
{"phrase":"to enter the revolving door","target":"the man in the grey suit","voice":"male","keys":mk}],
"stillS":1.2,
"nouns":[{"word":"a messenger","x":0.35,"y":0.49,"voice":"female"},{"word":"a yellow taxi","x":0.12,"y":0.62,"voice":"female"},
{"word":"an envelope","x":0.75,"y":0.58,"voice":"female"},{"word":"a revolving door","x":0.88,"y":0.40,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","delivering","an","envelope","to","a","man."],"answerVoice":"female",
"notes":"Woman box includes her bicycle. At 1.7-2.7 the man in the grey suit is inside / behind the glass of the revolving door (2.7 only a faint shape) - box kept on him there. Other office workers in dark suits pass in the background; named the target 'the man in the grey suit'. Answer: she hands the envelope over (0.2-0.7), 'delivering' is a fair B-level reading."}
json.dump(d,open('content/7344.json','w'),indent=1)
