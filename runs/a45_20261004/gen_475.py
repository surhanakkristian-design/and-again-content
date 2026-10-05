import json
R=lambda t,x0,y0,x1,y1:{"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
G=[R(0.0,.34,.1,.67,.54),R(0.5,.29,.13,.67,.66),R(1.0,.26,.27,.74,.8),R(1.5,.14,.21,.84,.8),R(2.0,.06,.13,.94,.8),R(2.5,0,.13,1,.95),
R(3.0,0,.14,1,1),R(3.5,0,.1,1,1),R(4.0,0,.08,1,1),R(4.5,0,.1,1,1),R(5.0,0,.12,1,1),R(5.5,0,.05,1,.82),R(6.0,.02,0,1,.72),
R(6.5,.03,0,.97,.88),R(7.0,0,0,.97,.92),R(7.5,0,0,1,.95),R(8.0,.16,.17,.86,.82),R(8.5,.14,.14,.92,.88),R(9.0,.18,.14,.86,1),R(9.5,.24,.14,.76,1),R(10.0,.21,.14,.79,1)]
d={"mediaId":475,"level":"B","keyWord":"memory","defaultVoice":"female",
"taps":[{"phrase":"to listen to a seashell","target":"the girl","voice":"female","keys":G},
{"phrase":"to fasten her roller skates","target":"the girl","voice":"female","keys":G},
{"phrase":"to glide down the hallway","target":"the girl","voice":"female","keys":G}],
"stillS":5.5,
"nouns":[{"word":"roller skates","x":.48,"y":.55,"voice":"female"},{"word":"a bracelet","x":.24,"y":.30,"voice":"female"},
{"word":"a lid","x":.25,"y":.93,"voice":"female"},{"word":"a box","x":.50,"y":.74,"voice":"female"}],
"question":"What is the girl fastening?","answer":["She","is","fastening","her","roller","skates."],"answerVoice":"female",
"notes":"Only one possible target (the girl), used for all three phrases. The key word 'memory' is abstract, so it is not among the nouns. From 6.5 to 7.5 s only her legs, hands and the skates are in the picture; the box covers them. The lid is the cardboard lid lying bottom left at 5.5 s."}
json.dump(d,open("content/475.json","w"),indent=1,ensure_ascii=False)
