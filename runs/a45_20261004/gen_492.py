import json
T=[i*0.5 for i in range(21)]
Y={0.0:(0,0,1,0.47),0.5:(0,0,1,0.42),1.0:(0,0.29,0.92,0.39),1.5:(0,0.23,0.92,0.51),2.0:(0,0.23,0.92,0.57),2.5:(0,0.25,0.92,0.59),
 3.0:(0,0.25,1,0.75),3.5:(0,0.33,1,0.67),4.0:(0,0,0.60,1),4.5:(0,0,0.61,1),5.0:(0,0,0.60,1),5.5:(0,0,0.60,1),6.0:(0,0,0.60,1),
 6.5:(0,0,0.60,1),7.0:(0,0,0.68,1),7.5:(0,0,0.67,1),8.0:(0,0,0.70,1),8.5:(0,0,0.66,1),9.0:(0,0,0.58,1),9.5:(0,0,0.66,1),10.0:(0,0,0.68,1)}
B={1.0:(0.52,0,0.48,0.28),1.5:(0.50,0,0.50,0.22),2.0:(0.55,0,0.45,0.22),2.5:(0.50,0,0.50,0.24),3.0:(0.62,0,0.38,0.24),3.5:(0.62,0,0.38,0.32),
 4.0:(0.62,0,0.38,0.46),4.5:(0.63,0,0.37,0.50),5.0:(0.62,0,0.38,0.58),5.5:(0.62,0.03,0.38,0.60),6.0:(0.62,0.04,0.38,0.58),
 6.5:(0.62,0.06,0.38,0.52),7.0:(0.70,0.08,0.30,0.60),7.5:(0.69,0.10,0.31,0.64),8.0:(0.72,0.12,0.28,0.58),8.5:(0.68,0.13,0.32,0.60),
 9.0:(0.60,0.15,0.40,0.58),9.5:(0.68,0.14,0.32,0.60),10.0:(0.70,0.13,0.30,0.60)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":492,"level":"A","keyWord":"nail polish","defaultVoice":"female",
"taps":[{"phrase":"to paint her nails","target":"the woman in yellow","voice":"female","keys":keys(Y)},
{"phrase":"to laugh at her friend","target":"the woman in blue","voice":"female","keys":keys(B)},
{"phrase":"to hold a small brush","target":"the woman in yellow","voice":"female","keys":keys(Y)}],
"stillS":10.0,
"nouns":[{"word":"nail polish","x":0.60,"y":0.94,"voice":"female"},{"word":"a glass","x":0.85,"y":0.78,"voice":"female"},
{"word":"a table","x":0.40,"y":0.85,"voice":"female"},{"word":"a bird","x":0.64,"y":0.36,"voice":"female"}],
"question":"What is the woman in yellow doing?",
"answer":["She","is","painting","her","nails."],"answerVoice":"female",
"notes":"The two women overlap in the picture in almost every frame (the yellow sleeve and painted hand lie in front of the blue shirt). 1.0-3.5 s: split horizontally (blue = headless shirt at the top, yellow = hands and lower body, her upper shirt/chin left out). 4.0-10.0 s: split vertically at about x 0.6-0.7 so the yellow box holds her face and brush hand and most of the painted hand; the blue box keeps the head, braid and right part of the shirt, the left part of the blue shirt and at 8.5/9.0/9.5 her reaching hand fall into the yellow box. The fingertips of the painted hand right of the split are outside the yellow box at 4.0-6.5. The green bird (3.5-10 s) is too small and too close to the woman in blue for its own phrase; its noun pill at 10.0 sits next to her face. Two phrases share the woman in yellow."}
json.dump(c,open("content/492.json","w"),indent=1)
