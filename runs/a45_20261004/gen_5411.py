import json
T=[i*0.5 for i in range(25)]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
man={0.0:(0.0,0.02,0.82,0.80),0.5:(0.0,0.0,0.82,0.80),1.0:(0.0,0.0,0.76,0.82),1.5:(0.0,0.0,0.80,0.85),
2.0:(0.0,0.0,0.78,0.78),2.5:(0.0,0.04,0.75,0.75),3.0:(0.0,0.07,0.74,0.75)}
wom={}
for t in T:
    if t<3.5: continue
    if t<7.0: wom[t]=(0.0,0.0,1.0,0.80)
    elif t<9.0: wom[t]=(0.0,0.0,1.0,0.50)
    elif t<11.0: wom[t]=(0.0,0.0,1.0,0.53)
    else: wom[t]=(0.0,0.0,1.0,0.56)
M=[k(t,man.get(t)) for t in T]; W=[k(t,wom.get(t)) for t in T]
c={"mediaId":5411,"level":"B","keyWord":"swirl","defaultVoice":"female",
"taps":[{"phrase":"to screw up his face","target":"the man","voice":"male","keys":M},
{"phrase":"to squeeze out toothpaste swirls","target":"the young woman","voice":"female","keys":W},
{"phrase":"to stare with wide eyes","target":"the young woman","voice":"female","keys":W}],
"stillS":12.0,
"nouns":[{"word":"a headband","x":0.50,"y":0.08,"voice":"female"},
{"word":"a T-shirt","x":0.82,"y":0.45,"voice":"female"},
{"word":"swirls","x":0.50,"y":0.61,"voice":"female"},
{"word":"toothbrushes","x":0.50,"y":0.85,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","squeezing","toothpaste","onto","three","toothbrushes."],"answerVoice":"female",
"notes":"Two shots, people never together: man 0.0-3.0 s, woman 3.5-12.0 s. From 7.0 s the woman's boxes stop above the counter so the toothbrushes are outside. Key word as plural 'swirls' (three identical swirls side by side). defaultVoice female: woman is the main person (longest on screen)."}
json.dump(c,open("content/5411.json","w"),indent=1)
