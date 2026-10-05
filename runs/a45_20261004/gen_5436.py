import json
T=[i*0.5 for i in range(19)]
w={0.0:(0.15,0.22,0.55,0.46),0.5:(0.0,0.14,0.95,0.58),1.0:(0.10,0.12,0.80,0.62),1.5:(0.18,0.13,0.66,0.62),
2.0:(0.23,0.0,0.77,0.84),2.5:(0.10,0.0,0.90,0.86),3.0:(0.0,0.0,1.0,0.86),3.5:(0.0,0.08,0.86,0.75),4.0:(0.10,0.18,0.86,0.77),
7.0:(0.02,0.10,0.94,0.68),7.5:(0.24,0.28,0.22,0.28),8.0:(0.28,0.28,0.22,0.27),8.5:(0.28,0.30,0.22,0.26),9.0:(0.26,0.31,0.23,0.27)}
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,ww,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(min(ww,1-x),2),"h":round(min(h,1-y),2)})
        else: out.append({"t":t,"off":True})
    return out
c={"mediaId":5436,"level":"B","keyWord":"twist","defaultVoice":"female",
"taps":[{"phrase":"to wring out a wet cloth","target":"the blonde woman","voice":"female","keys":keys(w)},
{"phrase":"to open a pickle jar","target":"the blonde woman","voice":"female","keys":keys(w)},
{"phrase":"to twist a long balloon","target":"the blonde woman","voice":"female","keys":keys(w)}],
"stillS":8.5,
"nouns":[{"word":"a kitchen cabinet","x":0.30,"y":0.17,"voice":"female"},{"word":"dough","x":0.45,"y":0.48,"voice":"female"},
{"word":"a glass bowl","x":0.17,"y":0.67,"voice":"female"},{"word":"towels","x":0.90,"y":0.56,"voice":"female"}],
"question":"What is the woman squeezing water from?","answer":["She","is","squeezing","water","from","a","cloth."],"answerVoice":"female",
"notes":"All three phrases on the blonde woman in the black top: every other person does only the dough twisting, which the whole group shares, so no unique phrase fits them. Off at 4.5-6.5 (other hands shaping a pretzel; brunette shot). Jar shot 2.0-3.0 shows only her hands (ring) and part of her face; assumed the same woman. In the group shots 7.5-9.0 she is third from the left. 'Blonde woman' is not unique in the group shot (rightmost girl is also fair-haired), verifier please check the name."}
json.dump(c,open('content/5436.json','w'),indent=1)
