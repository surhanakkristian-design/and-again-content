import json
times=[i*0.5 for i in range(24)]
carw=[.47,.53,.58,.63,.68,.73,.77,.81,.87,.91,.93,.96]+[1.0]*12
tc=[.50,.495,.49,.485,.485,.48,.475,.475,.47,.47,.46,.46,.455,.455,.445,.44,.435,.43,.42,.415,.405,.405,.40,.395]
car=[{"t":t,"x":0.0,"y":0.55,"w":carw[i],"h":0.26} for i,t in enumerate(times)]
tow=[{"t":t,"x":round(tc[i]-.10,2),"y":0.23,"w":0.20,"h":0.31} for i,t in enumerate(times)]
bird=[{"t":t,"x":0.04,"y":0.31,"w":round(round(tc[i]-.10,2)-.04,2),"h":0.16} for i,t in enumerate(times)]
d={"mediaId":4162,"level":"B","keyWord":"plaza","defaultVoice":"female",
"taps":[
 {"phrase":"to be parked on a plaza","target":"the car","voice":"female","keys":car},
 {"phrase":"to rise above the skyline","target":"the tower","voice":"female","keys":tow},
 {"phrase":"to circle in a flock","target":"the birds","voice":"female","keys":bird}],
"stillS":8.0,
"nouns":[{"word":"a plaza","x":0.50,"y":0.88,"voice":"female"},
 {"word":"a tower","x":0.44,"y":0.29,"voice":"female"},
 {"word":"a flock","x":0.20,"y":0.38,"voice":"female"},
 {"word":"columns","x":0.86,"y":0.33,"voice":"female"}],
"question":"What is parked on the plaza?",
"answer":["A","sports","car","is","parked","on","the","plaza."],
"answerVoice":"female",
"notes":"Birds are a faint flock of dots left of the tower (very faint in the first 1-1.5 s, clear from 2.0 s; late in the clip some spread to the right of the tower too). Bird box is split from the tower box at the tower's left edge. The car does not move, so its phrase is a state. Building on the right also stands tall, but the tower phrase refers to the distant skyline it rises above."}
json.dump(d,open("content/4162.json","w"),indent=1,ensure_ascii=False)
