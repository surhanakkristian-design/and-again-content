import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":round(r[2]-r[0],2),"h":round(r[3]-r[1],2)}) for t,r in zip(T,rows)]
woman=K([(.53,.28,.88,.69),(.51,.28,1,.68),(.49,.25,.98,.67),(.52,.22,.85,.67),(.48,.22,.78,.64),(.45,.22,.70,.61),(.45,.23,.67,.59),(.46,.23,.67,.57)])
jelly=K([(.68,.70,.90,.84),(.60,.69,.83,.83),(.58,.68,.78,.82),(.60,.68,.80,.82),(.58,.68,.83,.82),(.62,.70,.86,.84),(.62,.72,.89,.86),(.64,.73,.90,.87)])
dog=K([(.34,.26,.52,.40),(.32,.26,.50,.40),(.30,.26,.48,.40),(.29,.26,.47,.40),(.29,.26,.47,.40),(.26,.26,.44,.40),(.26,.28,.44,.42),(.27,.28,.45,.42)])
c={"mediaId":7010,"level":"B","keyWord":"cut","defaultVoice":"female",
"taps":[{"phrase":"to cut across the wet sand","target":"the cyclist","voice":"female","keys":woman},
{"phrase":"to lie stranded on the sand","target":"the jellyfish","voice":"female","keys":jelly},
{"phrase":"to sit beside its owner","target":"the dog","voice":"female","keys":dog}],
"stillS":2.2,
"nouns":[{"word":"a dog","x":0.39,"y":0.32,"voice":"female"},{"word":"a bike","x":0.65,"y":0.50,"voice":"female"},
{"word":"tyre tracks","x":0.16,"y":0.64,"voice":"female"},{"word":"a jellyfish","x":0.70,"y":0.75,"voice":"female"}],
"question":"What is the cyclist doing?",
"answer":["She","is","cutting","across","the","wet","sand."],"answerVoice":"female",
"notes":"The dog is tiny and far away (next to its owner at the water); its box is the minimum size and contains the owner too. Cyclist box is split from the dog box by a vertical line (at 0.2/0.7 her rear wheel and left foot fall outside her box, later her left hand on the handlebar is cut slightly) and from the jellyfish box by a horizontal line (bottom of the wheels cut). The dog appears to sit; check that it is not standing."}
json.dump(c,open('content/7010.json','w'),indent=1)
