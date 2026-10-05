import json
T=[i*0.5 for i in range(17)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
boy={0.0:(0.03,0.22,0.52,0.50),0.5:(0.0,0.18,0.70,0.60),1.0:(0.0,0.14,0.84,0.86),1.5:(0.0,0.14,0.92,0.86),
2.0:(0.0,0.28,0.70,0.72),2.5:(0.0,0.66,0.78,0.34),3.0:(0.40,0.84,0.60,0.16),3.5:(0.64,0.72,0.36,0.28),
4.0:(0.0,0.57,1.0,0.43),4.5:(0.0,0.59,1.0,0.41),5.0:(0.0,0.50,0.95,0.50),5.5:(0.10,0.58,0.80,0.42),
6.0:(0.07,0.59,0.75,0.41),6.5:(0.14,0.56,0.68,0.44),7.0:(0.16,0.58,0.80,0.42),7.5:(0.20,0.57,0.78,0.43),8.0:(0.14,0.50,0.80,0.50)}
star={2.5:(0.30,0.36,0.34,0.28),3.0:(0.20,0.40,0.47,0.38),3.5:(0.30,0.36,0.40,0.28),4.0:(0.38,0.39,0.30,0.17),4.5:(0.40,0.44,0.28,0.14)}
c={"mediaId":139,"level":"A","keyWord":"capital","defaultVoice":"male",
"taps":[{"phrase":"to walk up a hill","target":"the boy","voice":"male","keys":keys(boy)},
{"phrase":"to shine on the map","target":"the star","voice":"male","keys":keys(star)},
{"phrase":"to hold a map","target":"the boy","voice":"male","keys":keys(boy)}],
"stillS":6.5,
"nouns":[{"word":"the sky","x":0.50,"y":0.06,"voice":"male"},{"word":"a city","x":0.50,"y":0.30,"voice":"male"},
{"word":"a boy","x":0.44,"y":0.71,"voice":"male"},{"word":"a map","x":0.70,"y":0.82,"voice":"male"}],
"question":"What is the boy holding?","answer":["He","is","holding","a","map."],"answerVoice":"male",
"notes":"Key word 'capital' is not used as a label: the picture shows a city, that it is the capital needs guessing. In the close-ups 2.0-3.5 only the boy's hands/sleeve are visible (boy box = sleeve). Star: off after 4.5 (hidden by the head / only a tiny glint at 6.5). The golden dome also shines, but not on the map."}
json.dump(c,open("content/139.json","w"),indent=1)
