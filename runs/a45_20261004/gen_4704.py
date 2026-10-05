import json
# t, man top, split y, man width
R=[(0.0,.18,.75,.82),(0.5,.18,.75,.82),(1.0,.17,.76,.82),(1.5,.17,.74,1),(2.0,.16,.74,1),(2.5,.16,.74,1),(3.0,.17,.75,1),
(3.5,.17,.75,1),(4.0,.17,.75,1),(4.5,.18,.76,1),(5.0,.20,.91,1),(5.5,.23,.91,1),(6.0,.23,.81,1),(6.5,.23,.80,1),
(7.0,.23,.92,1),(7.5,.23,.93,1),(8.0,.23,.82,1),(8.5,.26,.85,1),(9.0,.28,.89,1),(9.5,.28,.91,1),(10.0,.26,.87,1),
(10.5,.24,.89,1),(11.0,.24,.94,1),(11.5,.23,.94,1),(12.0,.24,.91,1)]
man=[{"t":t,"x":0.0,"y":a,"w":w,"h":round(s-a,2)} for t,a,s,w in R]
st=[{"t":t,"x":0.0,"y":s,"w":1.0,"h":round(1-s,2)} for t,a,s,w in R]
d={"mediaId":4704,"level":"A","keyWord":"hat","defaultVoice":"male",
"taps":[
 {"phrase":"to wear a warm hat","target":"the man","voice":"male","keys":man},
 {"phrase":"to lie around a fire","target":"the stones","voice":"male","keys":st},
 {"phrase":"to pour out some water","target":"the man","voice":"male","keys":man}],
"stillS":2.0,
"nouns":[{"word":"a hat","x":0.36,"y":0.25,"voice":"male"},{"word":"a window","x":0.78,"y":0.23,"voice":"male"},
 {"word":"a towel","x":0.38,"y":0.72,"voice":"male"},{"word":"stones","x":0.45,"y":0.88,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","pouring","water","on","the","stones."],"answerVoice":"male",
"notes":"Two targets (man, stones), split on a horizontal line at the top of the stone pit; the camera tilts, so at 5.0-5.5, 7.0-7.5 and 11.0-11.5 s only a thin strip of stones is left at the bottom edge (stone box 0.06-0.09 high). At 8.5-10.0 s the man is partly hidden in steam; his box stays on him. 'to lie around a fire' = the stones around the orange glow; a state, because the stones do nothing else. The man's box includes the ladle and, on the right, the bucket (no target)."}
json.dump(d,open("content/4704.json","w"),indent=1)
