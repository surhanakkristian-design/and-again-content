import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
W={0.0:(0,0,1,0.70),0.5:(0,0,1,0.73),1.0:(0.38,0.36,0.62,0.38),1.5:(0.42,0.22,0.58,0.56),2.0:(0.55,0.22,0.45,0.70),
2.5:(0.28,0.30,0.72,0.48),3.0:(0.20,0,0.80,0.92),3.5:(0.25,0,0.75,0.95),4.0:(0.25,0,0.75,1),4.5:(0.28,0,0.72,1),
5.0:(0.22,0,0.78,1),5.5:(0.20,0,0.80,1),6.0:(0.22,0,0.78,0.95),6.5:(0.28,0,0.72,1),7.0:(0.12,0,0.88,1),
7.5:(0.48,0,0.52,0.75),8.0:(0.51,0,0.49,0.72),8.5:(0.60,0,0.40,0.68),9.0:(0.52,0.10,0.48,0.68),9.5:(0.52,0.10,0.48,0.75),10.0:(0.56,0.10,0.44,0.64)}
C={7.5:(0.08,0.18,0.30,0.45),8.0:(0.06,0.26,0.28,0.36),8.5:(0.05,0.30,0.28,0.34),9.0:(0.03,0.35,0.27,0.33),9.5:(0.02,0.36,0.19,0.36)}
M={8.0:(0.34,0.04,0.17,0.58),8.5:(0.33,0.08,0.26,0.40),9.0:(0.30,0.09,0.22,0.55),9.5:(0.21,0.07,0.31,0.68),10.0:(0,0.08,0.56,0.58)}
d={"mediaId":328,"level":"A","keyWord":"garlic","defaultVoice":"female",
"taps":[{"phrase":"to peel the garlic","target":"the woman","voice":"female","keys":keys(W)},
{"phrase":"to sit in the kitchen","target":"the cat","voice":"female","keys":keys(C)},
{"phrase":"to walk into the kitchen","target":"the man","voice":"male","keys":keys(M)}],
"stillS":2.0,
"nouns":[{"word":"a pot","x":0.27,"y":0.27,"voice":"female"},{"word":"a knife","x":0.22,"y":0.72,"voice":"female"},{"word":"garlic","x":0.62,"y":0.86,"voice":"female"}],
"question":"What is the woman smelling?","answer":["She","is","smelling","the","garlic."],"answerVoice":"female",
"notes":"0.0-3.0 s only the woman's hands/arms are in the picture; her box is on them. Peeling is short (2.5-3.0 s). The man steps in from the doorway 8.0-10.0 s. Cat hidden behind the man at 10.0 s."}
json.dump(d,open("content/328.json","w"),indent=1)
