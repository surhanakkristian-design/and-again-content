import json
T=[i*0.5 for i in range(17)]
tw={0.0:(.14,.39,.24,.14),0.5:(.06,.39,.32,.17),1.0:(.08,.40,.30,.17),1.5:(.08,.40,.30,.17),2.0:(.12,.40,.24,.14),2.5:(.10,.38,.24,.14),
3.0:(.12,.40,.24,.14),3.5:(.08,.40,.24,.14),4.0:(.04,.38,.27,.14),4.5:(0,.40,.30,.16),5.0:(0,.40,.32,.16),5.5:(0,.40,.34,.16),
6.0:(0,.39,.33,.17),6.5:(0,.39,.32,.17),7.0:(0,.40,.32,.17),7.5:(0,.40,.32,.17),8.0:(0,.40,.32,.17)}
yw={0.0:(.22,.53,.23,.35),0.5:(.08,.56,.36,.32),1.0:(.08,.57,.36,.31),1.5:(.08,.57,.36,.31),2.0:(.18,.54,.25,.33),2.5:(.20,.52,.24,.35),
3.0:(.20,.54,.24,.33),3.5:(.12,.54,.30,.35),4.0:(.15,.52,.24,.35),4.5:(.08,.56,.28,.31),5.0:(.02,.56,.36,.31),5.5:(.03,.56,.36,.31),
6.0:(.04,.56,.36,.31),6.5:(0,.56,.32,.31),7.0:(0,.57,.34,.30),7.5:(0,.57,.34,.30),8.0:(0,.57,.34,.30)}
tree={0.0:(.32,0,.68,.38),0.5:(.36,0,.64,.38),1.0:(.32,0,.68,.39),1.5:(.32,0,.68,.39),2.0:(.34,0,.66,.38),2.5:(.44,0,.56,.38),
3.0:(.50,0,.50,.40),3.5:(.66,0,.34,.38),4.0:(.70,0,.30,.38),4.5:(.76,0,.24,.36),5.0:(.78,.04,.22,.36),5.5:(.80,.05,.20,.36),
6.0:(.80,.04,.20,.32),6.5:(.82,.04,.18,.33),7.0:(.82,.04,.18,.33),7.5:(.82,.04,.18,.32),8.0:(.82,.04,.18,.32)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":436,"level":"A","keyWord":"left","defaultVoice":"female",
"taps":[
 {"phrase":"to have long grey hair","target":"the woman with long hair","voice":"female","keys":keys(tw)},
 {"phrase":"to wear a yellow skirt","target":"the woman in the yellow skirt","voice":"female","keys":keys(yw)},
 {"phrase":"to have pink flowers","target":"the tree","voice":"female","keys":keys(tree)}],
"stillS":0.0,
"nouns":[{"word":"the sky","x":.20,"y":.07,"voice":"female"},{"word":"a tree","x":.68,"y":.18,"voice":"female"},
 {"word":"the sea","x":.18,"y":.33,"voice":"female"},{"word":"a skirt","x":.33,"y":.72,"voice":"female"}],
"question":"Where are the people pointing?",
"answer":["They","are","pointing","to","the","left."],
"answerVoice":"female",
"notes":"All seven people do the same actions (point left, step left), so no action fits only one target: the three phrases are states. The woman in the yellow skirt stands in front of the long-haired teacher: boxes split horizontally, the teacher's box holds only her head, upper body and pointing arm, her legs fall outside or in the other box. The old woman on the right also has grey hair but in a bun (not long). 'a skirt' pill is on the yellow skirt; the old woman's blue skirt is at the right edge. Glitch 3.5-4.5 s: the boy and the old woman swap places / hug."}
json.dump(c,open("content/436.json","w"),indent=1)
