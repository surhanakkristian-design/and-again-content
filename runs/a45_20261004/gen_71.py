import json
T=[i*0.5 for i in range(21)]
def keys(d):
    return [({"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3])) for t in T]
M={1.5:(0.0,0.30,0.18,0.52),2.0:(0.0,0.0,0.40,1.0),2.5:(0.0,0.10,0.36,0.90),3.0:(0.0,0.15,0.38,0.85),3.5:(0.0,0.17,0.37,0.83),4.0:(0.0,0.17,0.32,0.75)}
W={2.0:(0.82,0.25,0.18,0.40),2.5:(0.70,0.30,0.30,0.39),3.0:(0.68,0.34,0.32,0.33),3.5:(0.67,0.34,0.33,0.29),4.0:(0.64,0.37,0.36,0.63),4.5:(0.0,0.30,0.65,0.70),
   6.0:(0.0,0.37,0.30,0.63),6.5:(0.0,0.37,0.44,0.63),7.0:(0.0,0.35,0.47,0.65),7.5:(0.0,0.35,0.49,0.65),8.0:(0.0,0.35,0.56,0.65),8.5:(0.0,0.33,0.67,0.67),
   9.0:(0.0,0.12,0.67,0.88),9.5:(0.0,0.0,0.70,1.0),10.0:(0.0,0.0,0.71,1.0)}
P={1.5:(0.72,0.78,0.28,0.22),2.0:(0.64,0.70,0.22,0.28),2.5:(0.62,0.70,0.24,0.24),3.0:(0.62,0.68,0.22,0.20),3.5:(0.58,0.64,0.20,0.21),4.0:(0.45,0.57,0.18,0.20)}
c={"mediaId":71,"level":"B","keyWord":"bark","defaultVoice":"male",
 "taps":[
  {"phrase":"to knock on the trunk","target":"the man","voice":"male","keys":keys(M)},
  {"phrase":"to cling to the trunk","target":"the woodpecker","voice":"male","keys":keys(P)},
  {"phrase":"to peel off birch bark","target":"the woman","voice":"female","keys":keys(W)}],
 "stillS":3.5,
 "nouns":[{"word":"bark","x":0.50,"y":0.28,"voice":"male"},{"word":"a man","x":0.17,"y":0.45,"voice":"male"},
          {"word":"a woman","x":0.85,"y":0.50,"voice":"female"},{"word":"a woodpecker","x":0.68,"y":0.74,"voice":"male"}],
 "question":"What is the woman doing?",
 "answer":["She","is","peeling","bark","off","a","birch."],
 "answerVoice":"female",
 "notes":"The bare hand on the pine at 0.0-1.0 s cannot be assigned to the man or the woman (no sleeve visible), so both are off there; verifier may decide. 1.5 s: hand with a dark sleeve at the left edge = the man. The knocking fist is seen at 2.0 s only. The hands at 6.0-8.5 s have the woman's olive cuff and are boxed as the woman. Woodpecker and woman touch at 3.0-4.0 s: boxes split, her chin / jacket is cut. defaultVoice male: mixed pair, odd id. 'a man' / 'a woman' are plain words for level B but nothing more specific is clearly visible."}
json.dump(c,open('content/71.json','w'),indent=1)
