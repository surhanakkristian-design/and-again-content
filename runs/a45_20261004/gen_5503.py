import json
O=None
Y=0.695
def b(x,y,x2,y2): return (x,y,round(x2-x,3),round(y2-y,3))
W={0.0:b(0.0,0.27,0.89,1.0),0.5:b(0.16,0.27,0.99,1.0),1.0:b(0.0,0.32,0.83,1.0),1.5:b(0.14,0.23,1.0,1.0),
 2.0:b(0.18,0.43,1.0,Y),2.5:b(0.18,0.43,1.0,Y),3.0:b(0.19,0.47,1.0,Y),3.5:b(0.19,0.47,1.0,Y),4.0:b(0.18,0.39,1.0,Y),
 4.5:b(0.20,0.33,1.0,Y),5.0:b(0.20,0.34,1.0,Y),5.5:b(0.20,0.34,1.0,Y),6.0:b(0.19,0.33,1.0,Y),6.5:b(0.19,0.32,1.0,Y),
 7.0:b(0.19,0.32,1.0,Y),7.5:b(0.19,0.33,1.0,Y),8.0:b(0.15,0.27,1.0,Y),8.5:b(0.31,0.37,1.0,0.79),9.0:b(0.23,0.37,1.0,0.78),
 9.5:b(0.19,0.34,1.0,0.81),10.0:b(0.0,0.33,1.0,0.685)}
P={0.0:O,0.5:O,1.0:O,1.5:O}
for t in [2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5]: P[t]=b(0.12,0.70,0.38,0.85)
P[8.0]=b(0.10,0.70,0.37,0.84); P[8.5]=b(0.03,0.67,0.30,0.85); P[9.0]=b(0.0,0.69,0.22,0.86); P[9.5]=b(0.0,0.69,0.185,0.86); P[10.0]=b(0.0,0.69,0.21,0.85)
def keys(D):
    return [{"t":t,"off":True} if D[t] is None else {"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} for t in sorted(D)]
c={"mediaId":5503,"level":"B","keyWord":"position","defaultVoice":"female",
 "taps":[{"phrase":"to hold a forearm plank","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to collapse onto her back","target":"the woman","voice":"female","keys":keys(W)},
  {"phrase":"to time her workout","target":"the phone","voice":"female","keys":keys(P)}],
 "stillS":6.0,
 "nouns":[{"word":"curtains","x":0.55,"y":0.15,"voice":"female"},{"word":"a water bottle","x":0.12,"y":0.60,"voice":"female"},
  {"word":"a phone","x":0.27,"y":0.76,"voice":"female"},{"word":"an exercise mat","x":0.72,"y":0.78,"voice":"female"}],
 "question":"What position is the woman holding?","answer":["She","is","holding","a","forearm","plank."],"answerVoice":"female",
 "notes":"Phone (timer app counting) sits right under her clasped hands from 2.0-8.0: boxes split horizontally at y=0.695/0.70, so the woman's box cuts her hands' lower edge and the phone's box starts slightly below its top. Phone not in picture 0.0-1.5. Key word 'position' used in the question (body position)."}
json.dump(c,open('content/5503.json','w'),indent=1)
