import json
T=[i*0.5 for i in range(25)]
M={0.0:(.35,.12,.36,.42),0.5:(.37,.24,.30,.37),1.0:(.42,.31,.26,.30),1.5:(.42,.32,.24,.29),2.0:(.41,.31,.24,.28),
2.5:(.32,.32,.38,.27),3.0:(.44,.30,.23,.29),3.5:(.38,.35,.35,.25),4.0:(0,0,.70,.82),4.5:(.14,.05,.56,.85),
5.0:(0,.02,.70,.87),5.5:(0,.05,.86,.95),6.0:(0,.08,.90,.92),6.5:(0,.16,.55,.84),7.0:(0,.22,.46,.78),7.5:(0,.15,.44,.85),
8.0:(0,.12,.40,.88),8.5:(0,.30,1.0,.70),9.0:(0,.31,.72,.69),9.5:(0,.31,.70,.69),10.0:(0,.30,.70,.70),10.5:(0,.30,.73,.70),
11.0:(0,.30,.70,.70),11.5:(0,.26,.72,.74),12.0:(0,.22,.96,.78)}
def keys(b):
    return [{"t":t,"off":True} if b.get(t) is None else dict(zip("txywh",(t,)+b[t])) for t in T]
mk=keys(M)
c={"mediaId":5297,"level":"B","keyWord":"ruin","defaultVoice":"female",
"taps":[{"phrase":"to walk up a cobbled path","target":"the woman","voice":"female","keys":mk},
{"phrase":"to throw her arms open","target":"the woman","voice":"female","keys":mk},
{"phrase":"to splash the turquoise water","target":"the woman","voice":"female","keys":mk}],
"stillS":1.0,
"nouns":[{"word":"the sky","x":0.45,"y":0.08,"voice":"female"},{"word":"a ruin","x":0.35,"y":0.26,"voice":"female"},
{"word":"a backpack","x":0.54,"y":0.44,"voice":"female"},{"word":"a cobbled path","x":0.52,"y":0.66,"voice":"female"}],
"question":"Where is the woman walking?","answer":["She","is","walking","towards","an","old","ruin."],"answerVoice":"female",
"notes":"Three shots (castle ruin 0-3.5, railing above the lake 4.0-8.0, boat in the gorge 8.5-12.0); the woman is the only clear target, so all three phrases use her. A boatman with a pole is visible small and blurred at the back of the boat (8.5-11.5, top-left) - not used as a target and his area (x<.26, y .25-.38) partly inside her box at 8.5-11.5. 'to walk up a cobbled path' 0.0-2.0, 'to throw her arms open' 2.5-3.5, 'to splash the turquoise water' 8.5-11.0. The boot at the bottom of 0.0 belongs to the camera person, not inside her box."}
json.dump(c,open('content/5297.json','w'),indent=1)
