import json
T=[i*0.5 for i in range(25)]
man={0.0:(0.40,0.50,0.60,0.40),0.5:(0.25,0.45,0.75,0.42),1.0:(0.68,0.36,0.32,0.64),1.5:(0.33,0.30,0.67,0.70),
2.0:(0.15,0.31,0.85,0.69),2.5:(0.15,0.29,0.85,0.71),3.0:(0.18,0.26,0.70,0.74),3.5:(0.40,0.30,0.56,0.70),
4.0:(0.35,0.31,0.55,0.69),4.5:(0.33,0.32,0.62,0.68),5.0:(0.20,0.33,0.62,0.67),5.5:(0.15,0.34,0.62,0.66),
6.0:(0.10,0.38,0.50,0.62),6.5:(0.18,0.33,0.44,0.67),7.0:(0.20,0.33,0.40,0.67),7.5:(0.24,0.34,0.56,0.66),
8.0:(0.20,0.30,0.67,0.70),8.5:(0.10,0.29,0.82,0.71),9.0:(0.06,0.31,0.83,0.69),9.5:(0.0,0.29,0.63,0.71),
10.0:(0.0,0.29,0.50,0.71),10.5:(0.0,0.29,0.53,0.71),11.0:(0.0,0.28,0.57,0.72),11.5:(0.0,0.26,0.62,0.74),12.0:(0.0,0.22,0.64,0.78)}
ppl={6.0:(0.61,0.33,0.24,0.14),6.5:(0.63,0.30,0.22,0.14),7.0:(0.62,0.33,0.22,0.14),
10.0:(0.50,0.40,0.22,0.14),10.5:(0.53,0.40,0.20,0.14),11.0:(0.58,0.41,0.24,0.14),
11.5:(0.63,0.41,0.24,0.14),12.0:(0.64,0.44,0.26,0.14)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(w,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":5433,"level":"B","keyWord":"turn on","defaultVoice":"male",
"taps":[{"phrase":"to flip a light switch","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to gaze up at the lights","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to gather by the front door","target":"the people by the house","voice":"male","keys":keys(ppl)}],
"stillS":10.0,
"nouns":[{"word":"a palm tree","x":0.25,"y":0.12,"voice":"male"},{"word":"fairy lights","x":0.70,"y":0.30,"voice":"male"},
{"word":"a front door","x":0.60,"y":0.45,"voice":"male"},{"word":"a stone path","x":0.48,"y":0.66,"voice":"male"}],
"question":"What is the man looking at?","answer":["He","is","gazing","up","at","the","lights."],"answerVoice":"male",
"notes":"Key word 'turn on' is a verb, so not among the nouns. The people by the house are tiny distant figures: marked off at 0-5.5 (not visible or hidden behind the man's head/shoulder box) and 7.5-9.5 (behind/next to the man's outstretched arm, boxes would overlap). Man box at 0.0-0.5 holds only his arm and hand (he films himself)."}
json.dump(c,open('content/5433.json','w'),indent=1)
