import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
wom={0.0:(0,0,0.82,0.90),0.5:(0,0,0.74,0.88),1.0:(0,0,0.68,0.97),1.5:(0,0.02,0.66,0.96),2.0:(0,0.03,0.64,0.85),2.5:(0,0,0.86,0.88),
3.0:(0,0.24,0.72,0.76),3.5:(0.12,0.20,0.72,0.80),4.0:(0.20,0.14,0.64,0.86),4.5:(0.27,0.02,0.63,0.98),5.0:(0.27,0.02,0.65,0.98),
5.5:(0.27,0.02,0.65,0.98),6.0:(0.24,0,0.76,1.0),6.5:(0,0,0.96,1.0),7.0:(0,0.12,0.82,0.88),7.5:(0,0.12,0.80,0.88),
8.0:(0,0.14,0.76,0.86),8.5:(0,0.18,0.70,0.82),9.0:(0,0.16,0.66,0.84),9.5:(0,0.07,0.60,0.93),10.0:(0,0.19,0.62,0.81)}
man={4.0:(0,0.03,0.18,0.60),4.5:(0,0,0.25,0.56),5.0:(0,0,0.25,0.58),5.5:(0,0,0.24,0.56),6.0:(0,0.10,0.20,0.58)}
rab={7.0:(0.82,0.55,0.18,0.20),7.5:(0.80,0.54,0.20,0.22),8.0:(0.77,0.48,0.23,0.20),8.5:(0.71,0.48,0.24,0.20),
9.0:(0.67,0.49,0.20,0.19),9.5:(0.62,0.47,0.20,0.19),10.0:(0.63,0.44,0.20,0.19)}
c={"mediaId":141,"level":"A","keyWord":"carrot","defaultVoice":"female",
"taps":[{"phrase":"to pull out a carrot","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to pour water","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to stand in a cage","target":"the rabbit","voice":"female","keys":keys(rab)}],
"stillS":8.5,
"nouns":[{"word":"the sky","x":0.60,"y":0.10,"voice":"female"},{"word":"a woman","x":0.40,"y":0.31,"voice":"female"},
{"word":"a carrot","x":0.18,"y":0.58,"voice":"female"},{"word":"a rabbit","x":0.80,"y":0.60,"voice":"female"}],
"question":"What is the woman eating?","answer":["She","is","eating","a","big","carrot."],"answerVoice":"female",
"notes":"The man is only partly in the picture (face/arm with the watering can at the left edge, 4.0-6.0). The rabbit is small, in the hutch in the background from 7.0; at 6.0-6.5 only a sliver at the right edge, set off. 'cage' = the rabbit hutch (A2). Woman box includes the carrot she holds."}
json.dump(c,open("content/141.json","w"),indent=1)
