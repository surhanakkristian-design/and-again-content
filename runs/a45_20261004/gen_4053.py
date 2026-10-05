import json
T=[i*0.5 for i in range(31)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
knife={0.0:(0,0.05,1,0.20),0.5:(0,0.05,1,0.21),1.0:(0,0.06,1,0.20),1.5:(0.10,0.07,0.90,0.21),2.0:(0.18,0.12,0.82,0.21),
2.5:(0.36,0.26,0.64,0.14),3.0:(0.40,0.29,0.60,0.13),3.5:(0.76,0.44,0.24,0.22),4.0:(0.70,0.60,0.30,0.18),4.5:(0.72,0.60,0.28,0.15),
5.0:(0.68,0.70,0.32,0.20),
8.0:(0.18,0.16,0.82,0.16),8.5:(0.30,0.21,0.70,0.12),9.0:(0.63,0.34,0.37,0.17),9.5:(0.64,0.27,0.36,0.16),10.0:(0.50,0.11,0.48,0.19),
10.5:(0.40,0.16,0.20,0.14),11.0:(0.40,0.17,0.20,0.14),11.5:(0.40,0.18,0.20,0.14),12.0:(0.42,0.70,0.20,0.22),12.5:(0.41,0.69,0.20,0.14),
13.0:(0.41,0.81,0.20,0.14),13.5:(0.47,0.16,0.20,0.14)}
cup={0.0:(0.47,0.33,0.53,0.34),0.5:(0.47,0.33,0.53,0.34),1.0:(0.47,0.33,0.53,0.34),1.5:(0.47,0.33,0.53,0.34),2.0:(0.45,0.33,0.55,0.35),
2.5:(0.45,0.40,0.55,0.27),3.0:(0.45,0.42,0.55,0.25),3.5:(0.43,0.30,0.33,0.38),4.0:(0.42,0.29,0.58,0.31),4.5:(0.25,0.27,0.75,0.33),
5.0:(0.12,0.38,0.88,0.32),5.5:(0.10,0.35,0.90,0.53),6.0:(0.08,0.24,0.92,0.53),6.5:(0.08,0.19,0.92,0.59),7.0:(0.05,0.17,0.95,0.61),7.5:(0.03,0.12,0.97,0.63)}
corn={8.0:(0.37,0.32,0.27,0.39),8.5:(0.37,0.33,0.28,0.36),9.0:(0.37,0.28,0.26,0.42),9.5:(0.37,0.29,0.27,0.41),10.0:(0.37,0.30,0.27,0.40),
10.5:(0.37,0.30,0.28,0.40),11.0:(0.37,0.31,0.30,0.40),11.5:(0.37,0.32,0.30,0.39),12.0:(0.36,0.26,0.33,0.44),12.5:(0.34,0.26,0.35,0.43),
13.0:(0.32,0.27,0.37,0.54),13.5:(0.30,0.30,0.43,0.55),14.0:(0.29,0.25,0.42,0.49),14.5:(0.29,0.25,0.42,0.49),15.0:(0.28,0.25,0.43,0.62)}
d={"mediaId":4053,"level":"A","keyWord":"corn","defaultVoice":"male",
"taps":[
{"phrase":"to cut the corn","target":"the knife","voice":"male","keys":keys(knife)},
{"phrase":"to have chocolate inside","target":"the orange cup","voice":"male","keys":keys(cup)},
{"phrase":"to be yellow inside","target":"the corn in the middle","voice":"male","keys":keys(corn)}],
"stillS":8.5,
"nouns":[{"word":"a knife","x":0.50,"y":0.29,"voice":"male"},{"word":"a hand","x":0.90,"y":0.31,"voice":"male"},{"word":"corn","x":0.30,"y":0.50,"voice":"male"}],
"question":"What is the knife cutting?",
"answer":["The","knife","is","cutting","the","corn."],
"answerVoice":"male",
"notes":"Two shots (cut at 8.0 s). The knife overlaps the orange cup at 2.5-5.0 s and the middle corn from 9.0 s: boxes split, knife box small there. From 10.5 to 13.0 s the blade stands inside the middle corn; the knife box is the blade part outside the corn. The hand at 8.5 s is small at the right edge (pill at x 0.90). The cup and the corn are in fact cakes; 'to have chocolate inside' = orange cup only, 'to be yellow inside' = middle corn only."}
json.dump(d,open("content/4053.json","w"),indent=1,ensure_ascii=False)
