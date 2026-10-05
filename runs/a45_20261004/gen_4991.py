import json
M={0.0:(0.0,0.08,0.57,0.70),0.5:(0.0,0.04,0.53,0.70),1.0:(0.0,0.0,0.57,0.72),1.5:(0.0,0.0,0.54,0.72),
2.0:(0.0,0.0,0.66,0.78),2.5:(0.01,0.03,0.73,0.80),3.0:(0.06,0.06,0.75,0.90),3.5:(0.06,0.06,0.76,0.90),
4.0:(0.66,0.14,0.34,0.22),4.5:(0.45,0.0,0.55,0.31),5.0:(0.42,0.03,0.58,0.28),5.5:(0.40,0.02,0.60,0.28),
6.0:(0.38,0.03,0.62,0.27),6.5:(0.38,0.03,0.62,0.27),7.0:(0.38,0.0,0.62,0.31),7.5:(0.35,0.0,0.65,0.30),
8.0:(0.32,0.0,0.68,0.30),8.5:(0.32,0.0,0.68,0.30),9.0:(0.18,0.0,0.82,0.98),9.5:(0.18,0.0,0.82,1.0),
10.0:(0.38,0.06,0.62,0.94),10.5:(0.38,0.08,0.62,0.92),11.0:(0.38,0.09,0.62,0.91),11.5:(0.38,0.10,0.62,0.90),
12.0:(0.40,0.09,0.60,0.91)}
I={4.0:(0.37,0.14,0.29,0.30),4.5:(0.25,0.31,0.50,0.19),5.0:(0.22,0.31,0.48,0.21),5.5:(0.20,0.30,0.53,0.23),
6.0:(0.18,0.30,0.60,0.26),6.5:(0.16,0.30,0.65,0.27),7.0:(0.14,0.31,0.67,0.28),7.5:(0.11,0.30,0.72,0.31),
8.0:(0.09,0.30,0.77,0.33),8.5:(0.07,0.30,0.82,0.37)}
times=[i*0.5 for i in range(25)]
def keys(D):
    out=[]
    for t in times:
        if t in D:
            x,y,w,h=D[t]; out.append(dict(t=t,x=x,y=y,w=w,h=h))
        else: out.append(dict(t=t,off=True))
    return out
d={"mediaId":4991,"level":"B","keyWord":"messy","defaultVoice":"male",
"taps":[{"phrase":"to pull a face","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to glide over a creased shirt","target":"the iron","voice":"male","keys":keys(I)},
{"phrase":"to hold up a smooth shirt","target":"the man","voice":"male","keys":keys(M)}],
"stillS":0.0,
"nouns":[{"word":"a curtain","x":0.80,"y":0.25,"voice":"male"},
{"word":"a houseplant","x":0.62,"y":0.55,"voice":"male"},
{"word":"a heap of clothes","x":0.65,"y":0.80,"voice":"male"},
{"word":"a duvet","x":0.18,"y":0.93,"voice":"male"}],
"question":"What is the man ironing?","answer":["He","is","ironing","a","creased","blue","shirt."],"answerVoice":"male",
"notes":"In the iron close-ups (4.0-8.5) only the man's arm is visible; man box = arm above the line of the iron handle, iron box below (hand split between them). 'to pull a face' = grimace at 1.5-3.5. Key word 'messy' is an adjective, not used as a noun."}
json.dump(d,open("content/4991.json","w"),indent=1)
