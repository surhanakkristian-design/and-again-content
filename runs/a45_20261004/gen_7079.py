from gen_7075_7076_7077_7079_w import write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
M=[(0.08,0.15,0.58,0.56),(0.08,0.15,0.56,0.56),(0.08,0.15,0.56,0.56),(0.06,0.15,0.58,0.56),(0.05,0.15,0.55,0.60),(0.06,0.14,0.54,0.62),(0.06,0.14,0.54,0.64),(0.02,0.11,0.55,0.65)]
W=[(0.66,0.27,0.26,0.30),(0.64,0.27,0.29,0.30),(0.64,0.27,0.28,0.31),(0.64,0.26,0.30,0.33),(0.60,0.27,0.32,0.31),(0.60,0.26,0.32,0.33),(0.60,0.26,0.32,0.33),(0.58,0.26,0.34,0.33)]
d={"mediaId":7079,"level":"B","keyWord":"element","defaultVoice":"male",
"taps":[
 {"phrase":"to examine the amber glass","target":"the man","voice":"male","boxes":M},
 {"phrase":"to set down the glass","target":"the man","voice":"male","boxes":M},
 {"phrase":"to arrange small glass pieces","target":"the woman","voice":"female","boxes":W}],
"stillS":3.2,
"nouns":[{"word":"a stained-glass panel","x":0.70,"y":0.62,"voice":"male"},
 {"word":"a tin of nails","x":0.86,"y":0.78,"voice":"male"},
 {"word":"a coil","x":0.14,"y":0.83,"voice":"male"},
 {"word":"a soldering iron","x":0.56,"y":0.87,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","examining","a","piece","of","amber","glass."],
"answerVoice":"male",
"notes":"Man holds the amber piece up to the light 0.2-1.7, then lays it on the paper pattern 2.2-3.7. Answer fits the first half of the clip. Woman behind works on small glass pieces at the far end of the table and looks up smiling at 3.7. Man/woman boxes split at x~0.60-0.66; the top right corner of the raised amber glass (x~0.68) is cut at 0.7-1.2. Key word 'element' not used as a noun (abstract)."}
write(d,T)
