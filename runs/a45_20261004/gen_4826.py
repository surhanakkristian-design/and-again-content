import json
W=[dict(t=i*0.5,x=0.03,y=0.36,w=0.97,h=0.64) for i in range(13)]
T=[dict(t=i*0.5,x=0.0,y=0.10,w=1.0,h=0.24) for i in range(13)]
d={"mediaId":4826,"level":"A","keyWord":"dam","defaultVoice":"female",
"taps":[{"phrase":"to pour over the dam","target":"the water","voice":"female","keys":W},
{"phrase":"to fall into the valley","target":"the water","voice":"female","keys":W},
{"phrase":"to cover the hills","target":"the trees","voice":"female","keys":T}],
"stillS":3.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.06,"voice":"female"},{"word":"trees","x":0.30,"y":0.22,"voice":"female"},
{"word":"a dam","x":0.50,"y":0.40,"voice":"female"},{"word":"water","x":0.45,"y":0.75,"voice":"female"}],
"question":"What is the water doing?",
"answer":["The","water","is","pouring","over","the","dam."],"answerVoice":"female",
"notes":"No people; static camera, one shot. Water box starts at the reservoir surface (y 0.36) and covers the falls; tree box stops above it (y 0.34). The concrete dam block (x 0.40-0.65, y 0.33-0.44) lies inside the water box but is not a tap target. 'a dam' pill sits on the concrete dam block."}
json.dump(d,open("content/4826.json","w"),indent=1)
