import json
T=[0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0]
Wm={0.0:(0,0,.45,.45),0.5:(0,0,.50,.47),1.0:(0,0,.50,.55),1.5:(0,0,.68,.65),2.0:(0,.08,.62,.92),2.5:(0,.08,.85,.92),
3.0:(0,0,.78,1),3.5:(0,.07,.60,.93),4.0:(0,.14,.62,.86),4.5:(0,.20,.72,.80),5.0:(0,.23,.62,.77),5.5:(0,.22,.62,.78),
6.0:(0,.20,.68,.80),6.5:(0,.26,.58,.74),7.0:(.06,.32,.78,.68),7.5:(0,.31,.84,.69),8.0:(0,.31,.60,.69),8.5:(0,.37,.60,.63),
9.0:(0,.40,.60,.60),9.5:(0,.44,.60,.56),10.0:(0,.46,.48,.54),10.5:(0,.47,.50,.53),11.0:(.03,.47,.47,.53),11.5:(.04,.47,.46,.53),12.0:(.03,.47,.45,.53)}
Sf={6.5:(.60,0,.40,.55),7.0:(.40,0,.60,.31),7.5:(.15,0,.85,.30),8.0:(.25,0,.70,.30),8.5:(.15,0,.75,.35),9.0:(.20,0,.62,.38),
9.5:(.20,0,.65,.42),10.0:(.15,.02,.70,.42),10.5:(.15,.03,.70,.42),11.0:(.12,.04,.70,.42),11.5:(.10,.03,.72,.43),12.0:(.10,.03,.70,.43)}
def ks(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
wk=ks(Wm); sk=ks(Sf)
c={"mediaId":4801,"level":"A","keyWord":"tall","defaultVoice":"female",
"taps":[{"phrase":"to water the plants","target":"the woman","voice":"female","keys":wk},
{"phrase":"to look up and smile","target":"the woman","voice":"female","keys":wk},
{"phrase":"to grow very tall","target":"the sunflower","voice":"female","keys":sk}],
"stillS":10.5,
"nouns":[{"word":"a sunflower","x":.52,"y":.13,"voice":"female"},{"word":"the sky","x":.82,"y":.35,"voice":"female"},
{"word":"a woman","x":.22,"y":.70,"voice":"female"},{"word":"tomatoes","x":.84,"y":.75,"voice":"female"}],
"question":"What is the woman looking at?","answer":["She","is","looking","at","a","tall","sunflower."],"answerVoice":"female",
"notes":"Sunflower box covers only the upper plant (head + upper leaves) from 6.5 s so it never overlaps the woman, who stands at its lower left; before 6.5 s it is off. A small worker in a conical hat appears in the far background 8.5-12 s (not used; 'a hat' avoided as a noun for that reason). 'to look up and smile' is true 8.0-12.0 s."}
json.dump(c,open('content/4801.json','w'),indent=1)
