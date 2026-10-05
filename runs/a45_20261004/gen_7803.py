import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
G=[(0.15,0.23,0.53,0.73),(0.12,0.23,0.50,0.73),(0.10,0.25,0.48,0.71),(0.10,0.27,0.47,0.70),(0.11,0.31,0.51,0.67),(0.02,0.35,0.58,0.63),(0.09,0.51,0.50,0.49),(0.10,0.51,0.51,0.49)]
C=[(0.74,0.00,0.26,0.22),(0.71,0.00,0.29,0.20),(0.69,0.00,0.31,0.21),(0.66,0.00,0.30,0.31),(0.63,0.00,0.32,0.32),(0.61,0.01,0.32,0.35),(0.60,0.04,0.31,0.33),(0.59,0.04,0.31,0.33)]
k=lambda B:[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":round(min(b[3],1-b[1]),2)} for t,b in zip(T,B)]
d={"mediaId":7803,"level":"B","keyWord":"desperately","defaultVoice":"male",
"taps":[
 {"phrase":"to strum an acoustic guitar","target":"the guitarist","voice":"male","keys":k(G)},
 {"phrase":"to kneel on the cobbles","target":"the guitarist","voice":"male","keys":k(G)},
 {"phrase":"to watch from the balcony","target":"the couple","voice":"male","keys":k(C)}],
"stillS":3.2,
"nouns":[{"word":"a lantern","x":0.43,"y":0.22,"voice":"male"},{"word":"a balcony","x":0.80,"y":0.35,"voice":"male"},
 {"word":"a guitar case","x":0.84,"y":0.83,"voice":"male"},{"word":"roses","x":0.60,"y":0.94,"voice":"male"}],
"question":"What is the guitarist doing?","answer":["He","is","strumming","an","acoustic","guitar."],"answerVoice":"male",
"notes":"Couple on the balcony is cut by the top edge at 0.2-1.2 s (only legs/torsos visible), fully visible from 1.7 s; target is the couple as one box (mixed group -> defaultVoice). 'to kneel on the cobbles' is true only from ~3.0 s (he drops to his knees at the end). 'the guitarist' used instead of 'the man' because a second man stands on the balcony."}
json.dump(d,open("content/7803.json","w"),indent=1)
