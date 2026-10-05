import json
N="nurse";M="man";T="therm"
F={
0.0:{N:(0.03,0.08,0.72,0.92)},
0.5:{N:(0,0,0.66,1.0),T:(0.67,0.19,0.20,0.52)},
1.0:{N:(0,0.52,0.36,0.48),T:(0.37,0.07,0.27,0.93)},
1.5:{N:(0,0.08,0.51,0.36),T:(0.12,0.45,0.38,0.32),M:(0.52,0.27,0.48,0.73)},
2.0:{N:(0,0.08,0.47,0.44),T:(0.14,0.53,0.42,0.14),M:(0.57,0.27,0.43,0.73)},
2.5:{N:(0,0.08,0.52,0.48),T:(0.25,0.57,0.31,0.14),M:(0.57,0.27,0.43,0.73)},
3.0:{N:(0,0.08,0.50,0.47),T:(0.26,0.56,0.30,0.14),M:(0.57,0.37,0.43,0.63)},
3.5:{N:(0,0.08,0.50,0.46),T:(0.26,0.55,0.30,0.14),M:(0.57,0.35,0.43,0.65)},
4.0:{N:(0,0.08,0.48,0.47),T:(0.24,0.56,0.32,0.14),M:(0.57,0.28,0.43,0.72)},
4.5:{M:(0,0,1,0.43),T:(0,0.44,1,0.56)},
5.0:{M:(0,0,1,0.43),T:(0,0.44,1,0.56)},
5.5:{M:(0,0,1,0.43),T:(0,0.44,1,0.56)},
6.0:{M:(0.21,0.05,0.79,0.95),T:(0,0.63,0.20,0.14)},
6.5:{N:(0,0,0.58,1.0),T:(0.59,0.05,0.24,0.85)},
7.0:{N:(0,0,0.52,1.0),T:(0.53,0.05,0.27,0.95)},
7.5:{N:(0,0.07,0.52,0.93),M:(0.54,0.26,0.46,0.74)},
8.0:{N:(0,0.08,0.37,0.82),T:(0.38,0.18,0.18,0.24),M:(0.57,0.20,0.43,0.80)},
8.5:{N:(0,0.08,0.37,0.82),T:(0.38,0.18,0.18,0.24),M:(0.57,0.20,0.43,0.80)},
9.0:{N:(0,0.08,0.37,0.82),T:(0.38,0.18,0.18,0.24),M:(0.57,0.20,0.43,0.80)},
9.5:{N:(0,0.05,0.69,0.95),T:(0.70,0.25,0.20,0.65)},
10.0:{N:(0,0.03,0.66,0.97),T:(0.68,0.25,0.22,0.53)},
}
def keys(k):
    out=[]
    for t in sorted(F):
        if k in F[t]:
            x,y,w,h=F[t][k]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
d={"mediaId":773,"level":"B","keyWord":"thermometer","defaultVoice":"female",
"taps":[
 {"phrase":"to take his temperature","target":"the nurse","voice":"female","keys":keys(N)},
 {"phrase":"to turn bright red","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to show a high temperature","target":"the thermometer","voice":"female","keys":keys(T)}],
"stillS":10.0,
"nouns":[{"word":"a window","x":0.72,"y":0.10,"voice":"female"},
 {"word":"a thermometer","x":0.74,"y":0.38,"voice":"female"},
 {"word":"a nurse","x":0.28,"y":0.70,"voice":"female"},
 {"word":"a bowl","x":0.78,"y":0.89,"voice":"female"}],
"question":"What is the nurse doing?",
"answer":["She","is","taking","his","temperature","with","a","thermometer."],
"answerVoice":"female",
"notes":"Cartoon. 4.5-5.5 s is a close-up inside the man's mouth: upper part = the man, lower part = the thermometer. 'to turn bright red' is the man's face (6.0-8.0 s); the thermometer's red line also rises, hence the thermometer phrase is about the reading. Thermometer is small in the wide shots (8.0-9.0 s), box at minimum size between nurse and man."}
json.dump(d,open("content/773.json","w"),indent=1,ensure_ascii=False)
