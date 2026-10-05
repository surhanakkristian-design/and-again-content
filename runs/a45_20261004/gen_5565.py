import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(boxes): return [ {"t":t,"off":True} if b is None else {"t":t,"x":round(b[0],2),"y":round(b[1],2),"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)} for t,b in zip(T,boxes)]
man=[(0.52,0.33,0.89,0.87),(0.47,0.34,0.88,0.87),(0.50,0.33,0.82,0.87),(0.53,0.33,0.83,0.87),(0.55,0.33,0.83,0.87),(0.56,0.33,0.86,0.87),(0.57,0.33,0.84,0.87),(0.57,0.33,0.84,0.87)]
wom=[(0.20,0.32,0.52,0.88),(0.20,0.32,0.47,0.88),(0.19,0.32,0.50,0.88),(0.19,0.32,0.53,0.88),(0.18,0.32,0.55,0.88),(0.18,0.32,0.56,0.88),(0.17,0.32,0.57,0.88),(0.18,0.32,0.56,0.88)]
ch=[(0.25,0.0,0.61,0.22)]*8
c={"mediaId":5565,"level":"B","keyWord":"arrest","defaultVoice":"male",
"taps":[{"phrase":"to head for the revolving door","target":"the man","voice":"male","keys":K(man)},
{"phrase":"to hold out her palm","target":"the woman","voice":"female","keys":K(wom)},
{"phrase":"to hang above the lobby","target":"the chandelier","voice":"male","keys":K(ch)}],
"stillS":2.2,
"nouns":[{"word":"a chandelier","x":0.42,"y":0.10,"voice":"male"},{"word":"a staircase","x":0.14,"y":0.25,"voice":"male"},
{"word":"a luggage trolley","x":0.16,"y":0.49,"voice":"male"},{"word":"a handbag","x":0.73,"y":0.67,"voice":"male"}],
"question":"What is the man holding?","answer":["He","is","holding","a","quilted","handbag."],"answerVoice":"male",
"notes":"Receptionist (in green) is tiny and sits between the two main figures, so not used as a tap target; man/woman boxes split where her hand touches his jacket. 'head for the revolving door' is true until ~1.7 s, afterwards he stands by the door."}
json.dump(c,open('content/5565.json','w'),indent=1)
