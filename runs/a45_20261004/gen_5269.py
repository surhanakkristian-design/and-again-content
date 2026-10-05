import json
T=[i*0.5 for i in range(19)]
W={0.0:(0.17,0.37,0.63,0.63),0.5:(0.33,0.26,0.50,0.74),1.0:(0.30,0.21,0.70,0.79),1.5:(0.10,0.20,0.90,0.80),
2.0:(0.31,0.19,0.69,0.81),2.5:(0.28,0.18,0.72,0.82),3.0:(0.30,0.24,0.70,0.76),3.5:(0.18,0.27,0.82,0.73),
4.0:(0.18,0.27,0.82,0.73),4.5:(0.10,0.24,0.70,0.75),5.0:(0.30,0.38,0.21,0.31),5.5:(0.25,0.40,0.24,0.35),
7.0:(0.0,0.36,0.90,0.64),7.5:(0.28,0.34,0.50,0.66),8.0:(0.28,0.32,0.40,0.62),8.5:(0.20,0.33,0.47,0.57),9.0:(0.24,0.34,0.62,0.64)}
def keys(D):
    out=[]
    for t in T:
        if t in D: x,y,w,h=D[t]; out.append({"t":t,"x":x,"y":y,"w":w,"h":h})
        else: out.append({"t":t,"off":True})
    return out
k=keys(W)
c={"mediaId":5269,"level":"B","keyWord":"purchase","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":k} for p in ["to clutch two chocolate bars","to purchase an olive coat","to blow a kiss"]],
"stillS":8.0,
"nouns":[{"word":"escalators","x":0.55,"y":0.15,"voice":"female"},{"word":"a beret","x":0.48,"y":0.39,"voice":"female"},
{"word":"a glass door","x":0.88,"y":0.27,"voice":"female"},{"word":"a gift bag","x":0.46,"y":0.66,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","purchasing","an","olive","coat."],"answerVoice":"female",
"notes":"Only one real target (the woman); the shop assistant is just a hand at 0.5-2.0, so all three phrases use the woman. 3.0-4.0 mirror: box covers her reflection holding the coat plus her real shoulder/arm at the right edge. 6.0-6.5 atrium shots without her -> off. Kiss blown at 8.0 (hand at mouth). Paying at the till is at 4.5 (card terminal)."}
json.dump(c,open('content/5269.json','w'),indent=1)
