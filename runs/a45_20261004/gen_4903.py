import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
crowd={2.0:(0.38,0.4,0.26,0.16),2.5:(0.38,0.4,0.24,0.15),3.0:(0.38,0.41,0.24,0.17),3.5:(0.35,0.36,0.3,0.24),4.0:(0.34,0.32,0.3,0.27),
 4.5:(0.36,0.28,0.3,0.3),5.0:(0.3,0.35,0.38,0.3),5.5:(0.27,0.32,0.46,0.33),6.0:(0.25,0.32,0.52,0.36),6.5:(0.18,0.3,0.6,0.44),
 7.0:(0.18,0.32,0.64,0.46),7.5:(0.16,0.28,0.7,0.58),8.0:(0.12,0.27,0.76,0.56),8.5:(0.08,0.22,0.88,0.64),9.0:(0.08,0.27,0.88,0.65)}
bld={0.0:(0,0,1,0.2),0.5:(0,0,1,0.2),1.0:(0,0,1,0.2),1.5:(0,0,1,0.18),2.0:(0,0,1,0.15)}
for t in (2.5,3.0,3.5,4.0,4.5,5.0,5.5): bld[t]=(0,0,1,0.14)
c={"mediaId":4903,"level":"B","keyWord":"crowd","defaultVoice":"male",
"taps":[
 {"phrase":"to crowd into the middle","target":"the crowd","voice":"male","keys":keys(crowd)},
 {"phrase":"to grow denser and denser","target":"the crowd","voice":"male","keys":keys(crowd)},
 {"phrase":"to overlook the plaza","target":"the glass building","voice":"male","keys":keys(bld)}],
"stillS":2.0,
"nouns":[{"word":"a glass roof","x":0.50,"y":0.05,"voice":"male"},{"word":"an entrance","x":0.50,"y":0.15,"voice":"male"},
 {"word":"paving","x":0.20,"y":0.62,"voice":"male"}],
"question":"What are the people doing?",
"answer":["They","are","crowding","into","the","middle","of","the","square."],
"answerVoice":"male",
"notes":"Aerial shot, individuals tiny and interchangeable, so no single person is a target; the crowd is used twice (boxed from 2.0 s when the first knot forms in the centre, growing to the dense mass), the glass building once (visible at the top until 5.5 s). 'to overlook' is a state verb for the building. Only 3 nouns: the paving is otherwise full of near-identical walkers."}
json.dump(c,open('content/4903.json','w'),indent=1)
