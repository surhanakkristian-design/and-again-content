import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
M={0.0:(0.28,0.14,0.60,0.82),0.5:(0.18,0.10,0.80,0.87),2.0:(0.18,0.18,0.54,0.82),2.5:(0.08,0.16,0.62,0.84),3.0:(0,0.18,0.72,0.82),
3.5:(0,0.14,0.72,0.84),4.0:(0,0,0.82,1),4.5:(0,0,0.80,1),5.0:(0,0.15,0.59,0.85),5.5:(0,0.14,0.66,0.86),6.0:(0,0.16,0.67,0.84),
6.5:(0,0.18,0.66,0.82),7.0:(0,0.20,0.59,0.80),7.5:(0,0.22,0.57,0.78),8.0:(0,0,0.18,1),8.5:(0,0,0.19,1),9.0:(0.12,0.18,0.62,0.52),
9.5:(0.22,0.22,0.70,0.78),10.0:(0.22,0.34,0.58,0.66)}
W={1.0:(0.28,0,0.72,0.74),1.5:(0.20,0,0.80,0.60),2.0:(0.72,0.44,0.28,0.56),2.5:(0.70,0.43,0.30,0.57),3.0:(0.72,0.08,0.28,0.84),
3.5:(0.74,0,0.26,0.70),4.0:(0.82,0.70,0.18,0.16),4.5:(0.80,0.62,0.20,0.26),5.0:(0.61,0.48,0.39,0.52),5.5:(0.69,0.46,0.31,0.54),
6.0:(0.67,0.38,0.33,0.62),6.5:(0.66,0.38,0.34,0.62),7.0:(0.61,0.38,0.33,0.62),7.5:(0.59,0.38,0.35,0.62),8.0:(0.18,0.16,0.82,0.84),
8.5:(0.19,0.18,0.81,0.82),9.0:(0.74,0.46,0.26,0.54)}
d={"mediaId":331,"level":"A","keyWord":"gentleman","defaultVoice":"male",
"taps":[{"phrase":"to pick up an orange","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to carry a basket","target":"the old woman","voice":"female","keys":keys(W)},
{"phrase":"to take off his hat","target":"the man","voice":"male","keys":keys(M)}],
"stillS":6.0,
"nouns":[{"word":"an umbrella","x":0.50,"y":0.14,"voice":"male"},{"word":"a gentleman","x":0.25,"y":0.50,"voice":"male"},
{"word":"a woman","x":0.85,"y":0.62,"voice":"female"},{"word":"a basket","x":0.68,"y":0.82,"voice":"male"}],
"question":"What is the old woman carrying?","answer":["She","is","carrying","a","basket","of","oranges."],"answerVoice":"female",
"notes":"Two targets only (man, old woman). 1.0-1.5 s show only the woman's coat, hand and basket; 4.0-4.5 s only her hands at the right edge (small box). 6.0-7.5 s the two stand close: boxes split on a vertical line, so the left part of her basket falls in the man's box and his umbrella hand is near the line. 8.0-8.5 s the man is only a coat edge on the left; 9.0 s the woman's back covers the man's lower right, his box stops at y 0.70. No 'a hat' noun because both wear hats. He lifts his hat at 5.5 s and 9.0 s."}
json.dump(d,open("content/331.json","w"),indent=1)
