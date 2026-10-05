import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2],2),"h":round(d[t][3],2)} if d.get(t) else {"t":t,"off":True}) for t in T]
F=(0,0,1,1)
W={0.0:(0.14,0.38,0.86,0.62),0.5:(0.18,0.33,0.82,0.67),1.0:(0.18,0.52,0.82,0.48),1.5:(0.12,0.42,0.88,0.58),2.0:(0.10,0.36,0.90,0.64),
2.5:(0.05,0,0.95,1),3.0:F,3.5:F,4.0:(0.05,0,0.95,1),4.5:(0.02,0,0.98,1),5.0:(0.05,0.02,0.95,0.98),5.5:(0.03,0.05,0.97,0.95),6.0:F,6.5:F,7.0:F,
7.5:(0.56,0,0.44,1),8.0:(0.63,0.08,0.37,0.46),8.5:(0.78,0.12,0.22,0.60),9.0:(0.80,0.33,0.20,0.38),9.5:(0.58,0.15,0.42,0.85),10.0:(0.57,0.22,0.43,0.78)}
M={7.5:(0,0.08,0.34,0.84),8.0:(0,0,0.32,0.70),8.5:(0,0.34,0.26,0.24),9.0:(0,0.33,0.22,0.25),9.5:(0,0.18,0.40,0.82),10.0:(0,0.26,0.43,0.72)}
B={7.5:(0.38,0.40,0.18,0.16),8.0:(0.40,0.30,0.22,0.17),8.5:(0.52,0.23,0.25,0.17),9.0:(0.52,0.17,0.30,0.15),9.5:(0.40,0.45,0.18,0.17),10.0:(0.43,0.48,0.14,0.15)}
c={"mediaId":46,"level":"A","keyWord":"apple","defaultVoice":"female",
"taps":[{"phrase":"to cut an apple","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to have a black beard","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to stand on a box","target":"the bird","voice":"female","keys":keys(B)}],
"stillS":7.5,
"nouns":[{"word":"a man","x":0.14,"y":0.36,"voice":"male"},{"word":"a woman","x":0.84,"y":0.24,"voice":"female"},
{"word":"a bird","x":0.47,"y":0.47,"voice":"female"},{"word":"an apple","x":0.45,"y":0.70,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","eating","a","red","apple."],"answerVoice":"female",
"notes":"0.0-2.0 only the woman's hands and arms are in the picture (box on them); 2.5-7.0 she fills the frame. The man and the bird appear from 7.5. The man does nothing only he does (both eat, both smile), so his phrase is a state. 8.5 and 9.0 are close-ups of hands: the dark hand on the left is taken as the man's, the hand on the right as the woman's - please check. At 10.0 the bird stands between the two people: its box is only 0.14 x 0.15 so it does not overlap them. The question is general; she eats the apple at 5.0-7.0 and again at 9.5-10.0."}
json.dump(c,open('content/46.json','w'),indent=1)
