import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
M=[(0.01,0.27,0.69,0.48),(0.04,0.28,0.64,0.48),(0.04,0.31,0.62,0.47),(0.24,0.39,0.40,0.39),(0.12,0.38,0.53,0.41),(0.13,0.29,0.51,0.48),(0.05,0.29,0.61,0.49),(0.02,0.29,0.64,0.49)]
H=[(0.70,0.30,0.30,0.53),(0.68,0.30,0.32,0.55),(0.66,0.30,0.34,0.56),(0.64,0.30,0.36,0.55),(0.66,0.31,0.34,0.60),(0.64,0.29,0.36,0.55),(0.66,0.30,0.34,0.59),(0.66,0.27,0.34,0.58)]
mk=[k(t,b) for t,b in zip(T,M)]; hk=[k(t,b) for t,b in zip(T,H)]
d={"mediaId":7345,"level":"B","keyWord":"middle","defaultVoice":"male",
"taps":[{"phrase":"to spread his arms wide","target":"the man","voice":"male","keys":mk},
{"phrase":"to balance on short skis","target":"the man","voice":"male","keys":mk},
{"phrase":"to tow a skier","target":"the brown horse","voice":"male","keys":hk}],
"stillS":2.2,
"nouns":[{"word":"a wooden cabin","x":0.20,"y":0.28,"voice":"male"},{"word":"spectators","x":0.24,"y":0.37,"voice":"male"},
{"word":"a rope","x":0.57,"y":0.55,"voice":"male"},{"word":"a horse","x":0.84,"y":0.70,"voice":"male"}],
"question":"Where is the rope tied?","answer":["It","is","tied","around","his","middle."],"answerVoice":"male",
"notes":"Man and horse boxes split along a vertical line (his outstretched glove reaches over the horse at 0.2-1.2 and 3.2-3.7). Rider on a second horse in the background not used as a target (overlaps both). 'a horse' pill is on the front horse; the second horse is small and far behind. Question uses key word 'middle'; 'his middle' refers to the man - answer subject 'It' -> default voice male."}
json.dump(d,open('content/7345.json','w'),indent=1)
