import json
O={"off":True}
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
def keys(times,d): return [dict(t=t,**d[t]) for t in times]
T15=[i*0.5 for i in range(15)]
def dump(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1)
S={0.0:b(0.10,0.37,0.36,0.63),0.5:b(0.10,0.36,0.35,0.64),1.0:b(0.12,0.35,0.55,0.65),1.5:b(0.15,0.53,0.72,0.47),2.0:b(0.15,0.53,0.75,0.47),
2.5:b(0,0.24,1.0,0.76),3.0:b(0,0.27,1.0,0.73),3.5:b(0,0.60,0.47,0.40),4.0:b(0,0.54,0.39,0.46),4.5:b(0.04,0.40,0.38,0.48),
5.0:b(0.17,0.41,0.28,0.56),5.5:b(0.17,0.41,0.29,0.53),6.0:b(0,0.40,0.40,0.60),6.5:b(0.22,0.38,0.28,0.62),7.0:b(0.20,0.39,0.27,0.61)}
T={0.0:b(0.46,0.20,0.54,0.80),0.5:b(0.45,0.19,0.55,0.81),1.0:b(0.67,0.16,0.33,0.84),1.5:b(0,0,1.0,0.52),2.0:b(0,0.10,1.0,0.42),
2.5:O,3.0:O,3.5:b(0.15,0.05,0.85,0.54),4.0:b(0.40,0.15,0.60,0.85),4.5:b(0.43,0.20,0.55,0.66),
5.0:b(0.46,0.28,0.46,0.68),5.5:b(0.47,0.27,0.51,0.66),6.0:b(0.41,0.14,0.59,0.86),6.5:b(0.51,0.20,0.49,0.80),7.0:b(0.48,0.20,0.52,0.80)}
dump({"mediaId":580,"level":"A","keyWord":"protect","defaultVoice":"female",
"taps":[{"phrase":"to hold up a coat","target":"the tall woman","voice":"female","keys":keys(T15,T)},
{"phrase":"to carry a basket","target":"the small woman","voice":"female","keys":keys(T15,S)},
{"phrase":"to wear glasses","target":"the small woman","voice":"female","keys":keys(T15,S)}],
"stillS":0.0,
"nouns":[{"word":"a basket","x":0.32,"y":0.68,"voice":"female"},{"word":"a coat","x":0.72,"y":0.66,"voice":"female"},
{"word":"the sky","x":0.45,"y":0.10,"voice":"female"},{"word":"glasses","x":0.29,"y":0.47,"voice":"female"}],
"question":"What is the tall woman doing?","answer":["She","is","protecting","her","friend","from","the","rain."],"answerVoice":"female",
"notes":"Two women, close together most of the time: boxes split along the line between them (in the hug at 6.5-7.0 roughly between the two faces; the tall woman's box loses the left part of her head/sleeve). At 1.5-2.0 the tall woman's box includes the coat she holds up. At 2.5-3.0 (close-up of the small woman) only the coat and an arm of the tall woman are in the picture -> off. Third phrase is a state (glasses) because every other action is shared or hard to see; 'friend' in the answer is an inference."})
