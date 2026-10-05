import json
T=[i*0.5 for i in range(25)]
man=[(.37,.27,.63,.73),(.37,.26,.63,.74),(.07,.27,.93,.73),(.09,.27,.91,.73),(.45,.27,.55,.73),(.42,.27,.58,.73),(0,.50,.42,.50),(0,.47,.55,.53),(0,.38,.33,.62),(0,.45,.61,.55),(0,.43,.55,.40),(.02,.65,.52,.35),(0,.65,.58,.35),(0,.72,.92,.28),(0,.62,.52,.38),(0,.80,.93,.20),(0,.73,.92,.27),(.35,.27,.58,.73),(.27,.29,.73,.71),(.07,.29,.93,.71),(.32,.29,.68,.71),(.57,.29,.43,.71),(.55,.30,.45,.70),(.57,.30,.43,.70),(.47,.29,.53,.71)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,man)]
d={"mediaId":4470,"level":"B","keyWord":"store","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to open the cupboard doors","to store plates and bowls","to grin at the camera"]],
"stillS":11.0,
"nouns":[{"word":"jars","x":.45,"y":.23,"voice":"male"},{"word":"plates","x":.22,"y":.34,"voice":"male"},{"word":"tiles","x":.25,"y":.63,"voice":"male"},{"word":"a worktop","x":.30,"y":.77,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","storing","plates","in","the","cupboard."],
"answerVoice":"male",
"notes":"Only the man is a target, all three phrases use him. 3.0-8.0 s are close-ups of the cupboard: only his hands and forearms are in the picture, the box follows them (the dishes on the shelves are outside the box where possible). He opens the doors at 0.5-1.0 and 9.0-9.5 s, puts plates and bowls in at 3.0-8.0 s, grins at the camera at 10.5-12 s. Key word 'store' is a verb: phrase 2 and the answer. 'jars' pill = the row on the top shelf (jars also stand on the lower shelves), 'plates' = the rainbow stack on the middle shelf (a second stack on the bottom shelf); 'a worktop' is British English (US countertop)."}
json.dump(d,open("content/4470.json","w"),indent=1,ensure_ascii=False)
