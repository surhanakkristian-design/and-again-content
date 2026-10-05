import json
T=[round(i*0.5,1) for i in range(25)]
def keys(d):
    return [{"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":round(d[t][2]-d[t][0],2),"h":round(d[t][3]-d[t][1],2)} for t in T]
M={0.0:(0.17,0.46,1.0,1.0),0.5:(0.05,0.49,0.74,1.0),1.0:(0.08,0.48,0.88,1.0),1.5:(0.06,0.49,0.70,1.0),2.0:(0.08,0.47,1.0,1.0),
 2.5:(0.08,0.46,0.84,1.0),3.0:(0.03,0.47,0.98,1.0),3.5:(0.03,0.47,1.0,1.0),
 4.0:(0.63,0.40,1.0,1.0),4.5:(0.64,0.40,1.0,1.0),5.0:(0.64,0.41,1.0,1.0),5.5:(0.64,0.41,1.0,1.0),6.0:(0.62,0.40,1.0,1.0),
 6.5:(0.64,0.40,1.0,1.0),7.0:(0.62,0.40,1.0,1.0),7.5:(0.64,0.40,1.0,1.0),8.0:(0.64,0.40,1.0,1.0),
 8.5:(0.66,0.34,1.0,1.0),9.0:(0.62,0.35,1.0,1.0),9.5:(0.60,0.37,1.0,1.0),10.0:(0.48,0.37,1.0,1.0),10.5:(0.42,0.36,1.0,1.0),
 11.0:(0.38,0.39,1.0,1.0),11.5:(0.36,0.40,1.0,1.0),12.0:(0.32,0.39,1.0,1.0)}
G={0.5:(0.55,0.06,1.0,0.48),1.0:(0.0,0.01,1.0,0.47),1.5:(0.0,0.01,1.0,0.48),2.0:(0.0,0.0,1.0,0.46),2.5:(0.0,0.0,1.0,0.45),
 3.0:(0.0,0.0,1.0,0.46),3.5:(0.0,0.0,1.0,0.46)}
C={4.0:(0.18,0.18,0.61,0.43),4.5:(0.16,0.18,0.62,0.43),5.0:(0.17,0.19,0.62,0.45),5.5:(0.17,0.19,0.62,0.45),6.0:(0.15,0.19,0.60,0.44),
 6.5:(0.14,0.19,0.62,0.44),7.0:(0.13,0.20,0.60,0.46),7.5:(0.12,0.20,0.62,0.46),8.0:(0.12,0.20,0.62,0.45)}
c={"mediaId":4779,"level":"A","keyWord":"germany","defaultVoice":"male",
"taps":[
 {"phrase":"to take a selfie","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to have horses on top","target":"the gate","voice":"male","keys":keys(G)},
 {"phrase":"to stand on a hill","target":"the castle","voice":"male","keys":keys(C)}],
"stillS":6.0,
"nouns":[{"word":"a castle","x":0.36,"y":0.31,"voice":"male"},
 {"word":"trees","x":0.20,"y":0.58,"voice":"male"},
 {"word":"a man","x":0.80,"y":0.62,"voice":"male"},
 {"word":"a wall","x":0.32,"y":0.86,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","taking","a","selfie","in","Germany."],
"answerVoice":"male",
"notes":"Three shots: Brandenburg Gate 0-3.5 s, castle 4-8 s, beer tent 8.5-12 s. Gate at 0.0 s is only a side building -> off. Many people in the beer tent (men in green hats, clinking mugs) so no tent target besides the selfie man. 'He is taking a selfie' holds in shots 1 and 3; in shot 2 he looks at the castle. Key word 'germany' is not a placeable noun; used in the answer (Brandenburg Gate / Bavarian castle / beer tent)."}
json.dump(c,open("content/4779.json","w"),indent=1)
