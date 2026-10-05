import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
blue={0.0:(0.02,0.22,0.73,0.75),0.5:(0.02,0.21,0.72,0.76),1.0:(0.02,0.24,0.73,0.74),1.5:(0.03,0.28,0.74,0.70),
2.0:(0.03,0.23,0.70,0.74),2.5:(0.03,0.26,0.67,0.72),3.0:(0,0.30,0.64,0.68),3.5:(0,0.33,0.56,0.62),4.0:(0,0.39,0.48,0.42),
4.5:(0,0.42,0.22,0.40),8.5:(0.34,0.31,0.18,0.14),9.0:(0.25,0.34,0.18,0.14),9.5:(0.17,0.31,0.18,0.14),10.0:(0.23,0.27,0.18,0.14),
10.5:(0.29,0.22,0.18,0.14),11.0:(0.32,0.21,0.18,0.14),11.5:(0.33,0.19,0.18,0.14),12.0:(0.31,0.18,0.18,0.14)}
teach={8.5:(0.53,0.27,0.18,0.24),9.0:(0.44,0.26,0.18,0.24),9.5:(0.36,0.24,0.18,0.26),10.0:(0.42,0.23,0.18,0.24),
10.5:(0.48,0.18,0.18,0.25),11.0:(0.51,0.16,0.18,0.25),11.5:(0.53,0.14,0.18,0.26),12.0:(0.51,0.13,0.18,0.25)}
floor={9.5:(0.28,0.52,0.34,0.26),10.0:(0.30,0.48,0.40,0.38),10.5:(0.30,0.50,0.50,0.38),11.0:(0.39,0.51,0.42,0.40),
11.5:(0.42,0.54,0.46,0.36),12.0:(0.38,0.51,0.50,0.44)}
d={"mediaId":5025,"level":"A","keyWord":"joke","defaultVoice":"male",
"taps":[{"phrase":"to look at his phone","target":"the man with blue hair","voice":"male","keys":keys(blue)},
{"phrase":"to stand at the whiteboard","target":"the teacher","voice":"male","keys":keys(teach)},
{"phrase":"to lie on the floor","target":"the man on the floor","voice":"male","keys":keys(floor)}],
"stillS":11.5,
"nouns":[{"word":"a teacher","x":0.62,"y":0.26,"voice":"male"},{"word":"a whiteboard","x":0.80,"y":0.17,"voice":"male"},
{"word":"a laptop","x":0.22,"y":0.46,"voice":"male"},{"word":"the floor","x":0.68,"y":0.95,"voice":"male"}],
"question":"What is the teacher doing?","answer":["He","is","standing","at","the","whiteboard."],"answerVoice":"male",
"notes":"Man with blue hair: big in 0-4.5 s, then a small back-of-head in the background 8.5-12 s (boxes kept min size, cut away from the teacher's box); a second student with teal hair sits next to him late on. Man on the floor boxed only from 9.5 s; the crouching student at 8.5-9.0 s is probably him but uncertain, left off to avoid overlap with the blue-haired man's box. Teacher is small in the background; boxes at min width."}
json.dump(d,open("content/5025.json","w"),indent=1)
