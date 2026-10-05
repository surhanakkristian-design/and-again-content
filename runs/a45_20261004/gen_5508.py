import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
B={0.2:(0.33,0.19,0.33,0.24),0.7:(0.4,0.16,0.31,0.28),1.2:(0.44,0.15,0.3,0.3),1.7:(0.51,0.13,0.33,0.39),
2.2:(0.51,0.11,0.33,0.39),2.7:(0.54,0.1,0.32,0.4),3.2:(0.55,0.09,0.34,0.41),3.7:(0.53,0.09,0.36,0.41)}
M={0.2:(0.0,0.44,0.53,0.44),0.7:(0.0,0.45,0.54,0.43),1.2:(0.0,0.46,0.53,0.43),1.7:(0.0,0.46,0.5,0.43),
2.2:(0.0,0.46,0.5,0.43),2.7:(0.0,0.47,0.53,0.42),3.2:(0.0,0.47,0.53,0.42),3.7:(0.0,0.47,0.52,0.42)}
Y={0.2:(0.58,0.69,0.32,0.31),0.7:(0.57,0.68,0.36,0.32),1.2:(0.56,0.67,0.33,0.33),1.7:(0.55,0.67,0.35,0.33),
2.2:(0.55,0.65,0.37,0.35),2.7:(0.58,0.63,0.4,0.37),3.2:(0.58,0.63,0.4,0.37),3.7:(0.58,0.6,0.41,0.4)}
def keys(d):
    return [dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
c={"mediaId":5508,"level":"B","keyWord":"able","defaultVoice":"female",
"taps":[{"phrase":"to hold a sofa overhead","target":"the woman in blue","voice":"female","keys":keys(B)},
{"phrase":"to clutch a large cushion","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to carry a floor lamp","target":"the woman in yellow","voice":"female","keys":keys(Y)}],
"stillS":2.2,
"nouns":[{"word":"a sofa","x":0.45,"y":0.12,"voice":"female"},
{"word":"a cardboard box","x":0.83,"y":0.43,"voice":"female"},
{"word":"a cushion","x":0.12,"y":0.58,"voice":"female"},
{"word":"a floor lamp","x":0.66,"y":0.7,"voice":"female"}],
"question":"What is the woman in blue doing?",
"answer":["She","is","holding","a","sofa","above","her","head."],
"answerVoice":"female",
"notes":"The woman in blue stands on the landing right above the man's head; 0.2-1.2 s their boxes are split horizontally just above his head, so her feet (about 0.44-0.53) fall outside her box; from 1.7 s they are split vertically at x 0.50-0.55. Her box covers her body only, not the sofa above her. Key word 'able' is an adjective, not placed."}
json.dump(c,open('content/5508.json','w'),indent=1)
