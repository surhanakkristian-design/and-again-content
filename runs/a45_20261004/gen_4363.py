import json
T=[i*0.5 for i in range(19)]
man=[(0,.23,.54,.77),(0,.23,.55,.77),(0,.18,.42,.82),(0,.24,.46,.76),(0,.17,.46,.83),(0,.10,.50,.90),(0,.13,.36,.87),(0,.14,.34,.86),(0,.14,.40,.86),(0,.12,.57,.88),(0,.17,.41,.83),(0,.15,.47,.85),(0,.12,.42,.88),(0,.25,.85,.37),(0,.07,.52,.42),(0,.07,.40,.44),(0,.14,.18,.14),(0,.17,.40,.28),(0,.20,.50,.29)]
bag=[None]*11+[(.48,.38,.24,.18),(.43,.42,.35,.20),(.36,.63,.64,.36),(.10,.50,.78,.50),(.02,.52,.98,.48),(0,.29,1,.71),(0,.46,1,.54),(0,.50,.75,.50)]
k=lambda L:[({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True}) for t,b in zip(T,L)]
m="the man in the hoodie"
c={"mediaId":4363,"level":"B","keyWord":"appear","defaultVoice":"male",
"taps":[{"phrase":"to lean on the railing","target":m,"voice":"male","keys":k(man)},
{"phrase":"to clutch a red backpack","target":m,"voice":"male","keys":k(man)},
{"phrase":"to land in his arms","target":"the red backpack","voice":"male","keys":k(bag)}],
"stillS":6.0,
"nouns":[{"word":"a neck pillow","x":.22,"y":.43,"voice":"male"},{"word":"a backpack","x":.60,"y":.54,"voice":"male"},{"word":"a conveyor belt","x":.68,"y":.78,"voice":"male"},{"word":"a railing","x":.22,"y":.92,"voice":"male"}],
"question":"What has appeared on the belt?",
"answer":["A","red","backpack","has","appeared","on","the","belt."],
"answerVoice":"male",
"notes":"'to appear on the belt' was NOT used as a tap phrase because the suitcases appear on the belt too; the key word is in the question/answer instead (present perfect, the backpack has just come out; other suitcases appeared earlier as well). From 6.5 s the man and the backpack overlap: split with a horizontal line at the top of the backpack, so his hands and lower body on/behind the backpack fall into the backpack box; at 8.0 s only a sliver of his head is visible (small box top left). Other passengers reach over the belt at 2.5-4.5 s but do not lean on the railing; the arm reaching from the left at 4.0 s may be another passenger's. The backpack is first seen at 5.5 s."}
json.dump(c,open('content/4363.json','w'),indent=1)
