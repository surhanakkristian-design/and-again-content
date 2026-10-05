import json
T=[i*0.5 for i in range(16)]
ea={0.0:(.13,.15,.76,.19),0.5:(.16,.16,.84,.19),1.0:(.15,.21,.85,.17),1.5:(.09,.26,.91,.17),2.0:(.02,.30,.98,.16),2.5:(0,.31,1,.16),
3.0:(0,.29,1,.18),3.5:(0,.26,1,.18),4.0:(0,.29,1,.20),4.5:(0,.34,1,.23),5.0:(0,.35,1,.26),5.5:(0,.33,1,.27),6.0:(0,.31,1,.30),
6.5:(0,.30,1,.36),7.0:(0,.29,1,.45),7.5:(0,.28,1,.49)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
v="female"
o={"mediaId":4192,"level":"B","keyWord":"fish","defaultVoice":v,
"taps":[{"phrase":"to glide above the waves","target":"the eagle","voice":v,"keys":keys(ea)},
{"phrase":"to spread its wings wide","target":"the eagle","voice":v,"keys":keys(ea)},
{"phrase":"to fish with its talons","target":"the eagle","voice":v,"keys":keys(ea)}],
"stillS":7.5,
"nouns":[{"word":"a wing","x":.86,"y":.38,"voice":v},{"word":"a beak","x":.42,"y":.44,"voice":v},
{"word":"a fish","x":.43,"y":.72,"voice":v},{"word":"the sea","x":.5,"y":.92,"voice":v}],
"question":"What is the eagle doing?","answer":["The","eagle","is","snatching","a","fish","from","the","sea."],"answerVoice":v,
"notes":"Only one real target: the eagle is alone in the clip, so all three phrases use it. The fish appears only in the last frame (7.5; at 7.0 it is a sliver under the feet), too short to tap, so it is no tap target and lies inside the eagle box at the end. Key word 'fish' is a verb (phrase 3); the noun 'a fish' is also placed. 'a wing': the eagle has two wings, the pill sits on the right one and no other noun is on the left one. The shore/forest is gone from the picture by 7.5."}
json.dump(o,open("content/4192.json","w"),indent=1)
