import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
mo=[(0.22,0.35,0.64,0.26),(0.20,0.35,0.58,0.25),(0.19,0.34,0.58,0.27),(0.19,0.32,0.58,0.29),(0.21,0.32,0.56,0.28),(0.19,0.31,0.58,0.28),(0.19,0.31,0.58,0.28),(0.18,0.30,0.60,0.29)]
fo=[(0.52,0.61,0.38,0.29),(0.57,0.60,0.34,0.29),(0.52,0.61,0.38,0.30),(0.56,0.61,0.37,0.30),(0.49,0.60,0.42,0.30),(0.49,0.59,0.44,0.31),(0.45,0.59,0.50,0.31),(0.41,0.59,0.52,0.32)]
ca=[(0.0,0.37,0.20,0.14),(0.0,0.37,0.20,0.14),(0.0,0.37,0.19,0.14),(0.0,0.36,0.19,0.14),(0.0,0.35,0.20,0.14),(0.0,0.36,0.19,0.14),(0.0,0.35,0.18,0.14),(0.0,0.35,0.18,0.14)]
k=lambda b:[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,(x,y,w,h) in zip(T,b)]
d={"mediaId":7262,"level":"B","keyWord":"jenny","defaultVoice":"female",
"taps":[{"phrase":"to wear a straw hat","target":"the jenny","voice":"female","keys":k(mo)},
{"phrase":"to suckle from its mother","target":"the foal","voice":"female","keys":k(fo)},
{"phrase":"to rest on the windowsill","target":"the cat","voice":"female","keys":k(ca)}],
"stillS":0.7,
"nouns":[{"word":"a jenny","x":0.36,"y":0.52,"voice":"female"},{"word":"a foal","x":0.76,"y":0.70,"voice":"female"},
{"word":"a bucket","x":0.20,"y":0.85,"voice":"female"},{"word":"bougainvillea","x":0.78,"y":0.22,"voice":"female"}],
"question":"What is the foal doing?","answer":["It","is","suckling","from","its","mother."],"answerVoice":"female",
"notes":"The foal stands under and against the jenny all the time, so the boxes split horizontally at her belly line: the jenny's box is her head, hat and body; her legs below the belly fall in no box (left) or in the foal's box. The foal suckles 0.2-2.7 s, then steps forward. Cat box is the minimum size at the left edge; the cat half rises at 2.2-2.7 s but stays on the sill. Phrase 1 is a state (the jenny only stands)."}
json.dump(d,open("content/7262.json","w"),indent=1)
