import json
times=[i*0.5 for i in range(12)]
def k(x,y,w,h): return [{"t":t,"x":x,"y":y,"w":w,"h":h} for t in times]
mtn=k(0.42,0.43,0.51,0.24); sun=k(0.59,0.31,0.23,0.12); trees=k(0.07,0.45,0.34,0.19)
d={"mediaId":8063,"level":"A","keyWord":"mountain","defaultVoice":"male",
"taps":[{"phrase":"to stand in the middle","target":"the tall mountain","voice":"male","keys":mtn},
{"phrase":"to sit behind the mountain","target":"the sun","voice":"male","keys":sun},
{"phrase":"to grow on the left","target":"the trees","voice":"male","keys":trees}],
"stillS":2.0,
"nouns":[{"word":"a mountain","x":0.64,"y":0.56,"voice":"male"},{"word":"the sun","x":0.69,"y":0.38,"voice":"male"},
{"word":"trees","x":0.18,"y":0.56,"voice":"male"},{"word":"the sky","x":0.35,"y":0.20,"voice":"male"}],
"question":"What is behind the mountain?","answer":["The","sun","is","behind","the","mountain."],"answerVoice":"male",
"notes":"Static ink drawing, only birds/cloud move slightly. Grey circle could be sun or moon (description says either); called 'the sun'. Mountain box starts at y .43 to avoid overlapping the sun box, so the very peak tip (.40-.43) is outside. Birds too tiny to use."}
json.dump(d,open("content/8063.json","w"),indent=1)
