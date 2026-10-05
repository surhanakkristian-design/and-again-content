import json
times=[i*0.5 for i in range(26)]
W={0.0:(0,0.02,0.40,0.65),0.5:(0,0.02,0.40,0.65),1.0:(0,0.02,0.40,0.65),1.5:(0,0.02,0.40,0.65),2.0:(0,0.02,0.40,0.65),2.5:(0,0.02,0.45,0.65),
4.0:(0,0.07,0.63,0.93),4.5:(0,0.05,0.75,0.95),
8.5:(0.16,0.06,0.58,0.33),9.0:(0.14,0.06,0.60,0.33),9.5:(0.16,0.06,0.60,0.33),10.0:(0.14,0.06,0.66,0.35),10.5:(0.14,0.06,0.86,0.37),
11.0:(0.50,0.08,0.50,0.78),11.5:(0.26,0.09,0.74,0.77),12.0:(0.27,0.11,0.73,0.71),12.5:(0.25,0.13,0.75,0.69)}
B={0.0:(0.40,0.36,0.46,0.36),0.5:(0.40,0.36,0.46,0.36),1.0:(0.40,0.36,0.46,0.36),1.5:(0.40,0.36,0.48,0.37),2.0:(0.42,0.37,0.58,0.38),
5.5:(0.22,0.58,0.34,0.30),6.0:(0.31,0.59,0.39,0.27),6.5:(0.32,0.68,0.32,0.17),7.0:(0.29,0.69,0.29,0.16),7.5:(0.23,0.53,0.30,0.32),8.0:(0.16,0.38,0.34,0.48),
8.5:(0.18,0.39,0.50,0.37),9.0:(0.12,0.39,0.54,0.38),9.5:(0.24,0.39,0.42,0.40),10.0:(0.24,0.41,0.42,0.37),10.5:(0.24,0.43,0.42,0.37),
11.0:(0.06,0.44,0.44,0.19),11.5:(0.0,0.43,0.26,0.54),12.0:(0.0,0.43,0.27,0.45),12.5:(0.0,0.43,0.25,0.45)}
M={5.5:(0.56,0.10,0.44,0.86),6.0:(0.70,0.22,0.30,0.64),6.5:(0.64,0.30,0.36,0.56),7.0:(0.58,0.33,0.42,0.52),7.5:(0.53,0.26,0.47,0.44),8.0:(0.50,0.18,0.50,0.56),
8.5:(0.74,0.12,0.26,0.88),9.0:(0.74,0.13,0.26,0.87),9.5:(0.76,0.10,0.24,0.90),10.0:(0.82,0.10,0.18,0.90),10.5:(0.68,0.80,0.32,0.20),
11.0:(0.74,0.86,0.26,0.14),11.5:(0.76,0.86,0.24,0.14),12.0:(0.76,0.82,0.24,0.18),12.5:(0.76,0.82,0.24,0.18)}
def keys(T):
    return [({"t":t,"x":T[t][0],"y":T[t][1],"w":T[t][2],"h":T[t][3]} if t in T else {"t":t,"off":True}) for t in times]
d={"mediaId":4069,"level":"B","keyWord":"rod","defaultVoice":"male",
"taps":[
 {"phrase":"to hold a fishing rod","target":"the small bird","voice":"male","keys":keys(B)},
 {"phrase":"to emerge from the sea","target":"the mermaid","voice":"female","keys":keys(M)},
 {"phrase":"to glare at the mermaid","target":"the white pigeon","voice":"male","keys":keys(W)}],
"stillS":1.5,
"nouns":[{"word":"the sky","x":0.66,"y":0.15,"voice":"male"},{"word":"a pigeon","x":0.21,"y":0.27,"voice":"male"},{"word":"a fishing rod","x":0.76,"y":0.46,"voice":"male"},{"word":"planks","x":0.26,"y":0.67,"voice":"male"}],
"question":"What is the small bird holding?",
"answer":["It","is","holding","a","thin","fishing","rod."],
"answerVoice":"male",
"notes":"Animated clip with cuts. The three figures overlap from 5.5 s on (mermaid holds the small bird; the small bird stands in front of the white pigeon; the pigeon's wing covers it at the end), so boxes are split rectangles: at 8.5-10.5 s the white pigeon's box is only its head and chest above the small bird; at 11.0 s it is the right half of the pigeon. From 10.5 s only the mermaid's hand is in the picture (small box bottom right). The rod is visible only 0-1.5 s; the mermaid emerges at 5.5 s (5.0 s is empty). 3.0, 3.5 and 5.0 s: no target. defaultVoice male by the evenId rule (birds). 'a pigeon' pill is on the white bird; the small bird has no noun."}
json.dump(d,open("content/4069.json","w"),indent=1)
