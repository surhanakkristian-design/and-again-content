import json
def K(rows):
    out=[]
    for r in rows:
        if len(r)==1: out.append({"t":r[0],"off":True}); continue
        t,x0,y0,x1,y1=r
        out.append({"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)})
    return out
B=K([(0.2,0,0.22,0.39,0.85),(0.7,0.05,0.20,0.41,0.85),(1.2,0.05,0.21,0.43,0.86),(1.7,0.08,0.19,0.50,0.85),(2.2,0.04,0.17,0.52,0.87),(2.7,0.06,0.15,0.72,0.87),(3.2,0.44,0.16,0.87,0.91),(3.7,0.48,0.11,0.99,0.94)])
W=K([(0.2,0.40,0.29,0.90,0.85),(0.7,0.42,0.29,0.85,0.85),(1.2,0.44,0.28,0.79,0.86),(1.7,0.51,0.28,0.80,0.85),(2.2,0.53,0.28,0.77,0.86),(2.7,),(3.2,0.24,0.30,0.43,0.72),(3.7,0.14,0.31,0.47,0.89)])
d={"mediaId":5536,"level":"B","keyWord":"aggressive","defaultVoice":"female",
"taps":[
 {"phrase":"to clutch a rugby ball","target":"the player in blue","voice":"female","keys":B},
 {"phrase":"to fend off an opponent","target":"the player in blue","voice":"female","keys":B},
 {"phrase":"to chase the ball carrier","target":"the player in white","voice":"female","keys":W}],
"stillS":0.2,
"nouns":[{"word":"a cloud","x":0.45,"y":0.17,"voice":"female"},
 {"word":"a mountain","x":0.75,"y":0.28,"voice":"female"},
 {"word":"a rugby ball","x":0.17,"y":0.43,"voice":"female"},
 {"word":"a picket fence","x":0.84,"y":0.71,"voice":"female"}],
"question":"What is the player in blue doing?",
"answer":["She","is","fending","off","an","opponent."],
"answerVoice":"female",
"notes":"White player off at 2.7 (almost fully hidden behind the blue player). At 3.2 she is mostly behind the blue player: small box on her visible left part, blue box starts at 0.44 (blue's left knee cut). 'To chase the ball carrier' is clearest 2.2-3.7; earlier she grapples."}
json.dump(d,open("content/5536.json","w"),indent=1)
