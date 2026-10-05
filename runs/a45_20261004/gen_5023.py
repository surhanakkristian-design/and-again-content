import json
T=[i*0.5 for i in range(25)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
man={0.0:(0.40,0.33,0.60,0.67),0.5:(0.58,0.30,0.42,0.70),1.0:(0.58,0.29,0.42,0.71),1.5:(0.64,0.26,0.36,0.74),
2.0:(0.60,0.25,0.40,0.75),2.5:(0.56,0.23,0.44,0.77),3.0:(0.56,0.22,0.44,0.78),3.5:(0.66,0.22,0.34,0.78),
4.0:(0.60,0.23,0.40,0.77),4.5:(0.64,0.23,0.36,0.77),5.0:(0.68,0.23,0.32,0.77),5.5:(0.70,0.23,0.30,0.77),
6.0:(0.66,0.24,0.34,0.76),6.5:(0.58,0.25,0.42,0.75),7.0:(0.48,0.30,0.52,0.70),7.5:(0.46,0.32,0.54,0.68),
8.0:(0.74,0.38,0.26,0.62),8.5:(0.78,0.34,0.22,0.66),9.0:(0.70,0.30,0.30,0.70),9.5:(0.70,0.32,0.30,0.68),
10.0:(0.66,0.32,0.34,0.68),10.5:(0.48,0.41,0.52,0.59),11.0:(0.06,0.28,0.94,0.72),11.5:(0.06,0.32,0.94,0.68),12.0:(0.02,0.31,0.96,0.69)}
bird={0.0:(0.0,0.42,0.38,0.22),0.5:(0.0,0.32,0.56,0.30),1.0:(0.0,0.33,0.42,0.29),1.5:(0.0,0.40,0.44,0.22),
2.0:(0.0,0.42,0.38,0.22),2.5:(0.0,0.40,0.34,0.22),3.0:(0.0,0.41,0.28,0.22),3.5:(0.0,0.42,0.34,0.20),4.0:(0.0,0.43,0.28,0.20)}
plane={8.0:(0.0,0.13,0.73,0.42),8.5:(0.0,0.11,0.77,0.38),9.0:(0.0,0.26,0.69,0.32),9.5:(0.0,0.24,0.69,0.34),
10.0:(0.0,0.09,0.65,0.47),10.5:(0.10,0.02,0.90,0.38)}
d={"mediaId":5023,"level":"A","keyWord":"airplane","defaultVoice":"male",
"taps":[{"phrase":"to raise both arms","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to stand on a post","target":"the bird","voice":"male","keys":keys(bird)},
{"phrase":"to fly over the man","target":"the big airplane","voice":"male","keys":keys(plane)}],
"stillS":4.0,
"nouns":[{"word":"an airplane","x":0.42,"y":0.43,"voice":"male"},{"word":"a bird","x":0.12,"y":0.51,"voice":"male"},
{"word":"grass","x":0.30,"y":0.80,"voice":"male"},{"word":"the sky","x":0.40,"y":0.15,"voice":"male"}],
"question":"What is flying over the man?","answer":["A","big","airplane","is","flying","over","him."],"answerVoice":"male",
"notes":"Big airliner overlaps the man at 8.0-10.5 s: plane box cut at the man's box edge (nose / rear parts partly outside). Plane hidden behind the man from 11.0 s, set off. Small plane in background is not a target. Bird leaves frame after 4.0 s."}
json.dump(d,open("content/5023.json","w"),indent=1)
