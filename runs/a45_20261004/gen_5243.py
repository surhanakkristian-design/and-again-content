import json
T=[i*0.5 for i in range(21)]
# woman (x,y,w,h) ; notebook (x,y,w,h)
W={0.0:(0.0,0.21,0.80,0.59),0.5:(0.0,0.22,0.82,0.58),1.0:(0.0,0.22,0.82,0.58),1.5:(0.0,0.21,0.61,0.60),
2.0:(0.0,0.21,0.42,0.79),2.5:(0.0,0.21,0.42,0.79),3.0:(0.0,0.21,0.80,0.53),3.5:(0.0,0.22,0.71,0.55),
4.0:(0.0,0.23,0.65,0.56),4.5:(0.0,0.23,0.64,0.54),5.0:(0.0,0.22,0.69,0.58),5.5:(0.0,0.22,0.81,0.58),
6.0:(0.0,0.21,0.95,0.60),6.5:(0.0,0.21,0.71,0.61),7.0:(0.0,0.22,0.83,0.61),7.5:(0.0,0.23,0.93,0.60),
8.0:(0.0,0.24,0.96,0.57),8.5:(0.0,0.25,0.93,0.55),9.0:(0.0,0.28,0.78,0.51),9.5:(0.0,0.28,0.40,0.72),10.0:(0.0,0.29,0.36,0.71)}
N={0.0:(0.11,0.80,0.68,0.20),0.5:(0.12,0.80,0.68,0.20),1.0:(0.11,0.80,0.68,0.20),1.5:(0.12,0.81,0.69,0.19),
2.0:(0.42,0.72,0.34,0.28),2.5:(0.42,0.72,0.33,0.28),3.0:(0.11,0.74,0.67,0.26),3.5:(0.12,0.77,0.64,0.23),
4.0:(0.11,0.79,0.64,0.21),4.5:(0.11,0.77,0.64,0.23),5.0:(0.09,0.80,0.66,0.20),5.5:(0.09,0.80,0.69,0.20),
6.0:(0.09,0.81,0.66,0.19),6.5:(0.09,0.82,0.67,0.18),7.0:(0.09,0.83,0.67,0.17),7.5:(0.09,0.83,0.67,0.17),
8.0:(0.09,0.81,0.66,0.19),8.5:(0.15,0.80,0.59,0.19),9.0:(0.18,0.79,0.58,0.19),9.5:(0.40,0.75,0.36,0.22),10.0:(0.36,0.72,0.42,0.18)}
def keys(d): return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c={"mediaId":5243,"level":"B","keyWord":"schedule","defaultVoice":"female",
"taps":[{"phrase":"to put up sticky notes","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to have coloured tabs","target":"the notebook","voice":"female","keys":keys(N)},
{"phrase":"to jot down notes","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":10.0,
"nouns":[{"word":"a plant","x":0.36,"y":0.20,"voice":"female"},{"word":"sticky notes","x":0.72,"y":0.40,"voice":"female"},
{"word":"a fan","x":0.52,"y":0.73,"voice":"female"},{"word":"a notebook","x":0.56,"y":0.82,"voice":"female"}],
"question":"What is the woman covering with notes?","answer":["She","is","covering","the","calendar","with","sticky","notes."],"answerVoice":"female",
"notes":"Key word 'schedule' is a verb, not placed. Notebook phrase is a state (things do no action). Woman/notebook boxes split horizontally at the notebook's top edge (her hands writing at 1.5 fall in the notebook box) and vertically at 2.0/2.5 and 9.5/10.0. 'jot down notes' = writing in the notebook at 1.5-2.5."}
json.dump(c,open('content/5243.json','w'),indent=1)
