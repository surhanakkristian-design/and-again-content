import json
T=[i*0.5 for i in range(19)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
W={0.0:(0,0,0.46,1),0.5:(0,0,0.46,1),1.0:(0,0,0.43,1),1.5:(0,0,0.44,1),2.0:(0,0,0.41,1),2.5:(0,0,0.45,1),
   3.0:(0,0.08,0.30,0.92),3.5:(0,0.27,0.31,0.73),4.0:(0,0.2,0.26,0.8),4.5:(0,0.2,0.26,0.8),5.0:(0,0.24,0.39,0.76),5.5:(0,0.24,0.39,0.76),
   6.0:(0,0.2,0.30,0.8),6.5:(0,0.26,0.38,0.74),7.0:(0,0.30,0.45,0.70),7.5:(0,0.22,0.32,0.78),8.0:(0,0.32,0.52,0.68),8.5:(0,0.11,0.35,0.87),9.0:(0.09,0.43,0.33,0.50)}
M={0.0:(0.47,0,0.53,1),0.5:(0.47,0,0.53,1),1.0:(0.44,0,0.56,1),1.5:(0.45,0,0.55,1),2.0:(0.42,0,0.58,1),2.5:(0.46,0,0.54,1),
   3.0:(0.75,0.08,0.25,0.92),3.5:(0.65,0.26,0.35,0.74),4.0:(0.75,0.17,0.25,0.83),4.5:(0.75,0.17,0.25,0.83),5.0:(0.66,0.18,0.34,0.82),5.5:(0.66,0.18,0.34,0.82),
   6.0:(0.56,0.17,0.44,0.83),6.5:(0.56,0.17,0.44,0.83),7.0:(0.58,0.18,0.42,0.82),7.5:(0.65,0.17,0.35,0.83),8.0:(0.66,0.17,0.34,0.83),8.5:(0.62,0.11,0.38,0.80),9.0:(0.48,0.43,0.36,0.48)}
L={3.0:(0.31,0,0.43,0.36),3.5:(0.15,0,0.70,0.25),4.0:(0.27,0.03,0.47,0.42),4.5:(0.27,0.03,0.47,0.42),5.0:(0.40,0.04,0.25,0.50),5.5:(0.40,0.04,0.25,0.50),
   6.0:(0.31,0.04,0.24,0.41),6.5:(0.20,0.04,0.35,0.21),7.0:(0.20,0.04,0.37,0.25),7.5:(0.33,0.04,0.31,0.50),8.0:(0.15,0.03,0.50,0.28),8.5:(0.36,0.03,0.25,0.42),9.0:(0.15,0.05,0.62,0.37)}
c={"mediaId":354,"level":"B","keyWord":"guidebook","defaultVoice":"female",
 "taps":[
  {"phrase":"to flip through a guidebook","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to wear a sun hat","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to spout a stream of water","target":"the stone lion","voice":"female","keys":keys(L)}],
 "stillS":6.5,
 "nouns":[{"word":"a statue","x":0.42,"y":0.13,"voice":"female"},{"word":"a sun hat","x":0.80,"y":0.28,"voice":"female"},
          {"word":"an earring","x":0.16,"y":0.50,"voice":"female"},{"word":"a guidebook","x":0.45,"y":0.67,"voice":"female"}],
 "question":"What are the two tourists doing?",
 "answer":["They","are","flipping","through","a","guidebook."],
 "answerVoice":"female",
 "notes":"Man's phrase is a state (he has no action that the woman does not also do: both point and lean). Lion statue is off 0.0-2.5 (only blurred bits). Where the lion sits between the two heads its box is narrowed to the face/top band; at 3.0 the woman's box leaves out her pointing arm to avoid the lion box. Woman flips pages at 0.0-0.5 and 6.0."}
json.dump(c,open('content/354.json','w'),indent=1)
