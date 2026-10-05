import json
times=[i*0.5 for i in range(26)]
def k(x,y,w,h): return [{"t":t,"x":x,"y":y,"w":w,"h":h} for t in times]
toad=k(0.33,0.32,0.42,0.17); smoke=k(0.59,0.18,0.22,0.14)
d={"mediaId":8064,"level":"B","keyWord":"toad","defaultVoice":"female",
"taps":[{"phrase":"to puff on a pipe","target":"the toad","voice":"female","keys":toad},
{"phrase":"to perch on a mushroom","target":"the toad","voice":"female","keys":toad},
{"phrase":"to drift into the air","target":"the smoke","voice":"female","keys":smoke}],
"stillS":0.0,
"nouns":[{"word":"a toad","x":0.40,"y":0.44,"voice":"female"},{"word":"a straw hat","x":0.45,"y":0.355,"voice":"female"},
{"word":"smoke","x":0.70,"y":0.27,"voice":"female"},{"word":"grass","x":0.20,"y":0.68,"voice":"female"}],
"question":"What is the toad doing?","answer":["The","toad","is","puffing","on","a","pipe."],"answerVoice":"female",
"notes":"Nearly static cartoon; only smoke puffs, eyes and head move. Toad box starts at y .30 so the hat tip (.29-.32) falls outside, to stay clear of the smoke box above the hat brim. Smoke is faint in some frames."}
json.dump(d,open("content/8064.json","w"),indent=1)
