import json
def k(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
man={0.0:(.0,.12,.80,.88),0.5:(.04,.17,.80,.83),1.0:(.0,.13,.80,.87),1.5:(.04,.18,.80,.82),2.0:(.09,.17,.74,.83),2.5:(.10,.20,.75,.80),
3.0:(.06,.22,.71,.78),3.5:(.14,.22,.71,.78),4.0:(.14,.21,.74,.79),4.5:(.10,.11,.77,.89),5.0:(.07,.16,.83,.84),
5.5:(.43,.30,.57,.65),6.0:(.43,.29,.54,.57),6.5:(.42,.26,.58,.56),7.0:(.41,.23,.59,.68),7.5:(.34,.12,.66,.88),8.0:(.52,.10,.48,.80),
8.5:(.42,.11,.58,.79),9.0:(.50,.02,.50,.90),9.5:(.41,.16,.59,.78),10.0:(.54,.12,.46,.78),10.5:(.49,.03,.51,.86),11.0:(.46,.06,.54,.88),
11.5:(.47,.07,.53,.86),12.0:(.52,.05,.48,.87)}
tall={t:None for t in [0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0]}
tall.update({5.5:(.18,0,.24,1.0),6.0:(.17,0,.25,1.0),6.5:(.12,0,.29,1.0),7.0:(.09,0,.30,1.0),7.5:(.09,0,.24,1.0),8.0:(.10,0,.24,1.0),
8.5:(.11,0,.24,1.0),9.0:(.11,0,.24,1.0),9.5:(.12,0,.23,1.0),10.0:(.12,0,.24,1.0),10.5:(.11,0,.24,1.0),11.0:(.11,0,.23,1.0),
11.5:(.11,0,.23,1.0),12.0:(.09,.02,.23,.98)})
M=[k(t,b) for t,b in man.items()]; T=[k(t,b) for t,b in tall.items()]
d={"mediaId":4810,"level":"B","keyWord":"post","defaultVoice":"male",
"taps":[{"phrase":"to hammer in a nail","target":"the man","voice":"male","keys":M},
{"phrase":"to wipe his brow","target":"the man","voice":"male","keys":M},
{"phrase":"to hold up the wire fence","target":"the tall post","voice":"male","keys":T}],
"stillS":12.0,
"nouns":[{"word":"a tall post","x":0.20,"y":0.15,"voice":"male"},
{"word":"trees","x":0.45,"y":0.36,"voice":"male"},
{"word":"a hammer","x":0.58,"y":0.61,"voice":"male"},
{"word":"a hole","x":0.55,"y":0.91,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","hammering","a","post","into","the","ground."],
"answerVoice":"male",
"notes":"Two shots: 0-5.0 s the man hammers a nail into the top of a square post (the tall post of shot 2 is not identifiable there, so it is off); 5.5-12.0 s he kneels, sets a short round post in a fresh hole and hammers it down, then wipes his brow (10.5-11.5 s). 'The tall post' has wire wrapped round it and the wire mesh fence attached on its left - check 'to hold up the wire fence' reads as true. Man's box starts right of the tall post; the short round post in front of him is inside his box at 6.0-7.0 s (not a target)."}
json.dump(d,open("content/4810.json","w"),indent=1)
