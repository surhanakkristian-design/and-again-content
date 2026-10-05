import json
def K(rows):
    return [{"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)} for t,x0,y0,x1,y1 in rows]
M=K([(0.2,0,0.36,0.56,1),(0.7,0,0.35,0.58,1),(1.2,0,0.36,0.60,1),(1.7,0,0.35,0.62,1),(2.2,0,0.31,0.64,1),(2.7,0,0.30,0.67,1),(3.2,0,0.30,0.49,1),(3.7,0,0.31,0.41,1)])
W=K([(0.2,0.57,0.27,1,1),(0.7,0.59,0.26,1,1),(1.2,0.61,0.27,1,1),(1.7,0.63,0.26,1,1),(2.2,0.65,0.22,1,1),(2.7,0.68,0.17,1,1),(3.2,0.50,0.19,1,1),(3.7,0.42,0.19,1,1)])
d={"mediaId":5535,"level":"A","keyWord":"aged","defaultVoice":"male",
"taps":[
 {"phrase":"to blow out the candles","target":"the old man","voice":"male","keys":M},
 {"phrase":"to hold a birthday cake","target":"the young woman","voice":"female","keys":W},
 {"phrase":"to kiss the old man","target":"the young woman","voice":"female","keys":W}],
"stillS":2.2,
"nouns":[{"word":"an old man","x":0.18,"y":0.68,"voice":"male"},
 {"word":"a cake","x":0.62,"y":0.58,"voice":"male"},
 {"word":"flowers","x":0.42,"y":0.28,"voice":"male"},
 {"word":"the sky","x":0.68,"y":0.07,"voice":"male"}],
"question":"What is the old man doing?",
"answer":["He","is","blowing","out","the","candles."],
"answerVoice":"male",
"notes":"defaultVoice male: main person is the old man (key word aged). Woman and man overlap at 3.2-3.7 (kiss): split vertically along the line between his head and hers; his knees on the right are cut there. Cake is held by her, so it sits in her box."}
json.dump(d,open("content/5535.json","w"),indent=1)
