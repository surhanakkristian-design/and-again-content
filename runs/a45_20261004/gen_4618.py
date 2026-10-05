import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
B={0.0:(0.17,0.21,0.70,0.79),0.5:(0.02,0.21,0.96,0.79),1.0:(0.08,0.20,0.84,0.80),1.5:(0.15,0.23,0.80,0.77),
 2.0:(0.16,0.25,0.78,0.75),2.5:(0.16,0.26,0.76,0.73),3.0:(0.21,0.30,0.67,0.65),3.5:(0.26,0.33,0.50,0.56),
 4.0:(0.27,0.33,0.45,0.49),4.5:(0.32,0.32,0.24,0.38),5.0:(0.30,0.33,0.26,0.36),5.5:(0.36,0.33,0.24,0.36),
 6.0:(0.34,0.35,0.24,0.34),6.5:(0.36,0.34,0.22,0.33),7.0:(0.31,0.34,0.31,0.38),7.5:(0.39,0.32,0.30,0.37),
 8.0:(0.38,0.32,0.34,0.38),8.5:(0.36,0.31,0.36,0.44),9.0:(0.17,0.16,0.57,0.65),9.5:(0.14,0.09,0.79,0.78),10.0:(0.05,0.04,0.95,0.89)}
C={0.0:(0,0.05,1,0.15),0.5:(0,0.05,1,0.15),1.0:(0,0.05,1,0.14),1.5:(0,0.08,1,0.14),2.0:(0,0.09,1,0.15),2.5:(0,0.09,1,0.16),
 3.0:(0,0.14,1,0.15),3.5:(0,0.18,1,0.14),4.0:(0,0.19,1,0.13),4.5:(0,0.18,1,0.13),5.0:(0,0.19,1,0.13),5.5:(0,0.19,1,0.13),
 6.0:(0,0.20,1,0.14),6.5:(0,0.19,1,0.14),7.0:(0,0.20,1,0.13),7.5:(0,0.18,1,0.13),8.0:(0,0.18,1,0.13),8.5:(0,0.17,1,0.13),
 9.0:(0.75,0.24,0.25,0.13),9.5:(0.0,0.22,0.13,0.18)}
c={"mediaId":4618,"level":"B","keyWord":"charge","defaultVoice":"male",
"taps":[
 {"phrase":"to crouch behind a blue shield","target":"the bald man","voice":"male","keys":keys(B)},
 {"phrase":"to fill the grandstand","target":"the crowd","voice":"male","keys":keys(C)},
 {"phrase":"to raise a sword triumphantly","target":"the bald man","voice":"male","keys":keys(B)}],
"stillS":10.0,
"nouns":[{"word":"a sword","x":0.13,"y":0.17,"voice":"male"},{"word":"spectators","x":0.42,"y":0.29,"voice":"male"},
 {"word":"a shield","x":0.84,"y":0.33,"voice":"male"},{"word":"a beard","x":0.50,"y":0.43,"voice":"male"}],
"question":"What is the bald man doing?",
"answer":["He","is","crouching","behind","a","blue","shield."],
"answerVoice":"male",
"notes":"Only two clean targets: the bald red-bearded man (two phrases: crouching 0-3.5, sword raised 9-10) and the crowd in the stand. The other fighters all do the same things (hold shields, push, fall), so no third target. Crowd box = the band of the stand above the bald man's box; at 9.0 / 9.5 only the strip beside his raised arms (9.5 strip is narrow, 0.13), at 10.0 off because his raised sword and shield frame the whole crowd. From 4.5 to 7.0 the bald man is mostly hidden behind the two attackers: box = his head + the visible part of the blue shield. Still 10.0: 'a shield' is on the raised blue shield (red and green shields elsewhere carry no noun)."}
json.dump(c,open('content/4618.json','w'),indent=1)
