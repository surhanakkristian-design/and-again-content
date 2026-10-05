import json
O={"off":True}
def b(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
times=[i*0.5 for i in range(21)]
Rf={t:O for t in times}; Pl={t:O for t in times}; Pk={t:O for t in times}
for t in (0.0,0.5,1.0): Rf[t]=b(0,0,1.0,0.31); Pk[t]=b(0.20,0.32,0.62,0.37)
Rf[1.5]=b(0.22,0.02,0.51,0.39); Pk[1.5]=b(0.41,0.42,0.18,0.14); Pl[1.5]=b(0.74,0.02,0.26,0.78)
Rf[2.0]=b(0.21,0,0.45,0.62); Pk[2.0]=b(0.31,0.63,0.34,0.17); Pl[2.0]=b(0.68,0,0.32,0.52)
Pl[2.5]=b(0.30,0,0.70,0.29); Pk[2.5]=b(0.24,0.35,0.76,0.27)
Pk[3.0]=b(0.23,0.39,0.64,0.18)
Pk[3.5]=b(0.19,0.45,0.60,0.17)
Pl[4.0]=b(0.03,0.12,0.60,0.40); Pk[4.0]=b(0.45,0.53,0.24,0.14)
Pl[4.5]=b(0,0.16,0.68,0.41); Pk[4.5]=b(0.52,0.58,0.22,0.14)
Pl[5.0]=b(0.09,0.10,0.71,0.72); Pk[5.0]=b(0.82,0.40,0.18,0.14)
Pk[6.0]=b(0.51,0.12,0.20,0.14)
Pk[6.5]=b(0.53,0.31,0.29,0.19)
Pk[7.0]=b(0.48,0.54,0.19,0.14)
Pk[7.5]=b(0.44,0.64,0.19,0.14)
Pl[8.0]=b(0.27,0.39,0.48,0.34)
Pl[8.5]=b(0.33,0.37,0.52,0.45)
Pl[9.0]=b(0,0.28,1.0,0.72); Pk[9.0]=b(0.58,0.11,0.24,0.16)
Pl[9.5]=b(0,0.26,1.0,0.74); Pk[9.5]=b(0.58,0.08,0.25,0.17)
Pl[10.0]=b(0,0.26,1.0,0.74); Pk[10.0]=b(0.58,0.08,0.25,0.17)
def keys(d): return [dict(t=t,**d[t]) for t in times]
c={"mediaId":587,"level":"B","keyWord":"puck","defaultVoice":"female",
"taps":[{"phrase":"to drop the puck","target":"the referee","voice":"male","keys":keys(Rf)},
{"phrase":"to celebrate her goal","target":"the player in yellow","voice":"female","keys":keys(Pl)},
{"phrase":"to fly into the net","target":"the puck","voice":"female","keys":keys(Pk)}],
"stillS":10.0,
"nouns":[{"word":"a puck","x":0.70,"y":0.16,"voice":"female"},{"word":"a glove","x":0.80,"y":0.31,"voice":"female"},{"word":"a helmet","x":0.28,"y":0.35,"voice":"female"},{"word":"a jersey","x":0.40,"y":0.82,"voice":"female"}],
"question":"What is the player in yellow doing?","answer":["She","is","celebrating","her","goal."],"answerVoice":"female",
"notes":"Many cuts. Referee visible only 0.0-2.0; at 0.0-1.0 (close-up of his hand with the puck) his box is the strip above the puck, at 1.5 only his upper body (the puck is in his hand in front of his legs). Puck off at 5.5 (only a shadow), 8.0 and 8.5 (hidden at her stick / in her glove). Player in yellow off at 3.0/3.5 (only a stick tip / sliver at the edge). At 9.0-10.0 the puck is in her raised glove: puck box on top, player box below. The purple goalie (5.5-6.0) and the purple player (1.5-2.0) are not targets."}
json.dump(c,open('content/587.json','w'),indent=1)
