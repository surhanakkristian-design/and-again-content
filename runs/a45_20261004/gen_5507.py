import json
T=[i*0.5 for i in range(19)]
M={0.0:(0,0.05,0.52,0.95),0.5:(0,0.08,0.5,0.92),1.0:(0,0.1,0.43,0.9),1.5:(0,0.1,0.48,0.9),2.0:(0,0.1,0.47,0.9),
2.5:(0,0.12,0.85,0.88),3.0:(0,0.22,0.73,0.78),3.5:(0,0.24,0.5,0.76),4.0:(0,0.3,0.3,0.7),4.5:(0,0.27,0.4,0.73),
5.0:(0,0.26,0.27,0.74),5.5:(0,0.3,0.18,0.7),6.0:(0,0.45,0.5,0.55),6.5:(0,0.48,0.47,0.52),7.0:(0,0.48,0.4,0.52),
7.5:(0,0.51,0.38,0.49),8.0:(0,0.5,0.4,0.5),8.5:(0,0.48,0.33,0.52),9.0:(0,0.47,0.41,0.53)}
G={0.0:(0.53,0.25,0.47,0.55),0.5:(0.51,0.2,0.49,0.55),1.0:(0.44,0.2,0.56,0.55),1.5:(0.49,0.15,0.51,0.6),2.0:(0.48,0.1,0.52,0.62)}
F={6.0:(0.36,0,0.64,0.44),6.5:(0.38,0,0.62,0.47),7.0:(0.41,0,0.59,0.62),7.5:(0.22,0,0.78,0.5),8.0:(0.26,0,0.74,0.5),
8.5:(0.33,0,0.67,0.48),9.0:(0.42,0.02,0.58,0.62)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":5507,"level":"A","keyWord":"zoo","defaultVoice":"male",
"taps":[{"phrase":"to eat from his hands","target":"the goat","voice":"male","keys":keys(G)},
{"phrase":"to eat green leaves","target":"the giraffe","voice":"male","keys":keys(F)},
{"phrase":"to hold a sheet of paper","target":"the man","voice":"male","keys":keys(M)}],
"stillS":3.0,
"nouns":[{"word":"rocks","x":0.7,"y":0.13,"voice":"male"},
{"word":"penguins","x":0.84,"y":0.27,"voice":"male"},
{"word":"water","x":0.72,"y":0.46,"voice":"male"},
{"word":"a man","x":0.2,"y":0.6,"voice":"male"}],
"question":"What is the giraffe eating?",
"answer":["The","giraffe","is","eating","green","leaves."],
"answerVoice":"male",
"notes":"Goat only 0-2 s, penguins 2.5-5.5 s, giraffe 6-9 s. Man and goat overlap at his hands (goat eats hay from them): split vertically, part of his hands fall in the goat box. In the giraffe shot the man's hand holding the branch (top right, 6-7 s) lies inside the giraffe box; the man's box excludes the paper there because the giraffe's neck is behind it. Man holds the sheet from 2.5 s on (not in the goat shot). 'penguins' = the group of three on the rocks at right; one more penguin swims at left. Key word 'zoo' not placed."}
json.dump(c,open('content/5507.json','w'),indent=1)
