import json
T=[i*0.5 for i in range(19)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
woman={}; dent={}
for t in T:
    if t<3.0: woman[t]=(0.0,0.0,1.0,1.0); dent[t]=None
    elif t<5.0:
        woman[t]=(0.0,0.27,0.80,0.73); dent[t]=(0.81,0.03,0.19,0.97)
    else: woman[t]=(0.0,0.03,1.0,0.97); dent[t]=None
W=[k(t,woman[t]) for t in T]; D=[k(t,dent[t]) for t in T]
c={"mediaId":5409,"level":"A","keyWord":"tooth","defaultVoice":"female",
"taps":[{"phrase":"to show her teeth","target":"the young woman","voice":"female","keys":W},
{"phrase":"to eat a red apple","target":"the young woman","voice":"female","keys":W},
{"phrase":"to hold a small mirror","target":"the dentist","voice":"female","keys":D}],
"stillS":1.0,
"nouns":[{"word":"a nose","x":0.50,"y":0.38,"voice":"female"},
{"word":"teeth","x":0.55,"y":0.57,"voice":"female"},
{"word":"a finger","x":0.18,"y":0.78,"voice":"female"},
{"word":"a jumper","x":0.75,"y":0.90,"voice":"female"}],
"question":"What is the young woman eating?",
"answer":["She","is","eating","a","red","apple."],"answerVoice":"female",
"notes":"Dentist visible only 3.0-4.5 s; her hand with mirror reaches to the woman's mouth, box split at x 0.80 so the dentist box covers only her body at the right edge. Key word given as plural 'teeth' (many teeth visible, no single tooth stands apart)."}
json.dump(c,open("content/5409.json","w"),indent=1)
