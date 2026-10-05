import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T17=[i*0.5 for i in range(17)]; T19=[i*0.5 for i in range(19)]
# 4711
m={0.0:(.24,.19,.58,.60),0.5:(.18,.18,.70,.62),1.0:(.12,.22,.78,.69),1.5:(0,.19,1,.72),2.0:(.08,.21,.84,.67),2.5:(.15,.18,.80,.73),
3.0:(.08,.17,.88,.83),3.5:(.06,.14,.94,.86),4.0:(0,.17,1,.83),4.5:(.04,.15,.96,.85),5.0:(0,.08,1,.92),5.5:(0,.09,1,.91),6.0:(0,.12,1,.88),6.5:(0,.10,1,.90),7.0:(0,.02,1,.98),7.5:(0,0,1,1),8.0:(0,0,1,1)}
k=K(T17,m)
json.dump({"mediaId":4711,"level":"A","keyWord":"effort","defaultVoice":"male",
"taps":[{"phrase":"to row a small boat","target":"the man","voice":"male","keys":k},
{"phrase":"to make a big effort","target":"the man","voice":"male","keys":k},
{"phrase":"to open his mouth wide","target":"the man","voice":"male","keys":k}],
"stillS":1.0,
"nouns":[{"word":"the sky","x":.50,"y":.10,"voice":"male"},{"word":"people","x":.80,"y":.42,"voice":"male"},{"word":"water","x":.15,"y":.80,"voice":"male"},{"word":"a boat","x":.56,"y":.90,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","rowing","a","small","boat."],"answerVoice":"male",
"notes":"Only one tappable target (the rower); the crowd is a thin band split by him, so all three phrases use the man. From 5.0 s only his face is in frame, box = whole picture. 'people' pill sits on the right part of the far crowd; 'a boat' on the white deck in front of him. Key word 'effort' is abstract, used in a phrase, not as a noun."},
open("content/4711.json","w"),indent=1)
# 4712
w={0.0:(.05,0,.95,.78),0.5:(.05,0,.95,.78),1.0:(.08,.08,.92,.72),1.5:(.15,.08,.85,.72)}
b={3.0:(.08,.15,.84,.45),3.5:(.05,.13,.92,.47),4.0:(.04,.04,.92,.55),4.5:(.05,.07,.83,.68),5.0:(.03,.06,.90,.74),5.5:(.06,.10,.90,.72),
6.0:(.38,.17,.22,.20),6.5:(.38,.20,.22,.20),7.0:(.38,.22,.22,.20),7.5:(.38,.22,.22,.20),8.0:(.38,.22,.22,.20),8.5:(.38,.23,.22,.20),9.0:(.38,.25,.22,.19)}
c={3.0:(.03,.60,.94,.38),3.5:(0,.60,1,.38),4.0:(.03,.59,.94,.39)}
json.dump({"mediaId":4712,"level":"A","keyWord":"blow","defaultVoice":"male",
"taps":[{"phrase":"to blow on a window","target":"the man at the window","voice":"male","keys":K(T19,w)},
{"phrase":"to lean over a cake","target":"the man in the blue T-shirt","voice":"male","keys":K(T19,b)},
{"phrase":"to stand on a plate","target":"the cake","voice":"male","keys":K(T19,c)}],
"stillS":3.0,
"nouns":[{"word":"a woman","x":.76,"y":.20,"voice":"female"},{"word":"a T-shirt","x":.50,"y":.55,"voice":"male"},{"word":"candles","x":.50,"y":.66,"voice":"male"},{"word":"a cake","x":.50,"y":.82,"voice":"male"}],
"question":"What is the man in blue doing?","answer":["He","is","blowing out","the","candles."],"answerVoice":"male",
"notes":"Clip has cuts: frosted window (0-1.5, a dark-haired man), single candle close-up (2.0-2.5, no target boxed), birthday cake (3.0-4.0), party tubes/streamers (4.5-5.5), long table with a crowd (6.0-9.0). The window man and the cake man look like different people, so they are two targets. In the crowd shots the man in the blue T-shirt is the small figure in the centre behind the candles (small box). 'to blow out the candles' was avoided as a tap phrase because the whole crowd does it at the end; it is the model answer for the cake shot. 'blowing out' kept as one chip so only one order is possible. 'to stand on a plate' is a state (no action fits only the cake). Picture shows party tubes, not paper blowers as the description says."},
open("content/4712.json","w"),indent=1)
# 4713
o={0.0:(.22,.15,.60,.85),0.5:(.40,.30,.60,.70),1.0:(.38,.35,.62,.65),1.5:(.38,.33,.62,.65),2.0:(.26,.31,.68,.53),
5.0:(.36,.43,.22,.18),5.5:(.39,.42,.18,.14),6.0:(.39,.41,.18,.14),6.5:(.39,.41,.18,.14),7.0:(.39,.42,.18,.14),7.5:(.39,.42,.18,.14),8.0:(.40,.42,.18,.14),8.5:(.40,.42,.18,.14),9.0:(.41,.42,.18,.14)}
v={2.5:(0,.16,1,.38),3.0:(0,.17,1,.38),3.5:(0,.16,1,.38),4.0:(0,.16,1,.38),4.5:(0,.16,1,.38)}
ko=K(T19,o)
json.dump({"mediaId":4713,"level":"B","keyWord":"goodbye","defaultVoice":"male",
"taps":[{"phrase":"to board a rowing boat","target":"the white-haired man","voice":"male","keys":ko},
{"phrase":"to bend over a suitcase","target":"the white-haired man","voice":"male","keys":ko},
{"phrase":"to wave goodbye together","target":"the villagers","voice":"male","keys":K(T19,v)}],
"stillS":3.5,
"nouns":[{"word":"villagers","x":.45,"y":.33,"voice":"male"},{"word":"a rope","x":.60,"y":.555,"voice":"male"},{"word":"a quay","x":.25,"y":.65,"voice":"male"},{"word":"a rowing boat","x":.78,"y":.72,"voice":"male"}],
"question":"What are the villagers doing?","answer":["They","are","waving","goodbye","from","the","quay."],"answerVoice":"male",
"notes":"Two targets only: the helpers in caps change between shots (inconsistent), and the boat always overlaps the old man. In the quay shot (2.5-3.0) a man in a cap stands in the boat; he does not look like the white-haired man, so the old man is 'off' there - verifier please check. From 5.5 s the old man is a tiny figure in the distant boat (minimum-size box). 'a quay' pill sits on the stone face of the quay; 'a rope' on the rope lying on its edge."},
open("content/4713.json","w"),indent=1)
# 4714
e={0.0:(.10,.13,.90,.62),0.5:(.10,.13,.90,.62),1.0:(.10,.13,.90,.62),5.5:(.14,.14,.84,.74),6.0:(.12,.14,.86,.63),6.5:(.12,.14,.86,.61),
7.0:(.08,.14,.90,.56),7.5:(.08,.14,.90,.56),8.0:(.10,.13,.88,.57),8.5:(.10,.13,.88,.57),9.0:(.17,.14,.70,.56)}
for t in (1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0): e[t]=(0,0,1,1)
ke=K(T19,e)
json.dump({"mediaId":4714,"level":"A","keyWord":"expert","defaultVoice":"male",
"taps":[{"phrase":"to hold a vase","target":"the man with the bow tie","voice":"male","keys":ke},
{"phrase":"to wear white gloves","target":"the man with the bow tie","voice":"male","keys":ke},
{"phrase":"to talk to two people","target":"the man with the bow tie","voice":"male","keys":ke}],
"stillS":7.5,
"nouns":[{"word":"people","x":.50,"y":.10,"voice":"male"},{"word":"a bow tie","x":.52,"y":.42,"voice":"male"},{"word":"a vase","x":.52,"y":.62,"voice":"male"},{"word":"a table","x":.42,"y":.80,"voice":"male"}],
"question":"What is the expert holding?","answer":["The","expert","is","holding","a","vase."],"answerVoice":"male",
"notes":"One target for all three phrases: the vase and the crowd both overlap the expert's box, the couple in front is seen only from behind. His box in the wide shots also covers crowd faces behind him and the vase (none of them is a target). 'to talk to two people' rests on his open mouth and gaze at the couple (6.5-8.5); 'to wear white gloves' is a state. Key word used in question and answer rather than as a noun pill (the pill would sit on the same figure as 'a bow tie')."},
open("content/4714.json","w"),indent=1)
