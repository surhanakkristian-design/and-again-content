import json
T=[i*0.5 for i in range(19)]
man=[(.05,.02,.92,.98),(.07,.03,.93,.97),(.10,.04,.90,.96),(.10,.03,.90,.97),(.05,.05,.95,.95),(0,.20,1,.80),(.09,.12,.91,.88),(.04,.20,.96,.80),(.13,.15,.87,.85),(.15,.15,.85,.85),(.28,.25,.72,.75),(.41,.38,.59,.62),(0,.50,1,.50),(0,.39,1,.61),(0,.29,1,.71),(0,.20,1,.80),(0,.20,1,.80),(0,.20,1,.80),(0,.18,1,.82)]
wom=[None]*8+[(0,.28,.12,.70),(0,.27,.14,.68),(0,.28,.27,.38),(0,.35,.40,.33),(0,.06,.78,.43),(0,.09,.76,.29),(.08,.03,.92,.25),(.05,0,.90,.19),(.05,0,.90,.19),(.02,0,.96,.19),(.02,0,.96,.17)]
k=lambda L:[({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True}) for t,b in zip(T,L)]
c={"mediaId":4356,"level":"B","keyWord":"sore","defaultVoice":"male",
"taps":[{"phrase":"to rub his sore back","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to give someone a piggyback","target":"the man","voice":"male","keys":k(man)},
{"phrase":"to cling to his shoulders","target":"the woman","voice":"female","keys":k(wom)}],
"stillS":4.5,
"nouns":[{"word":"ferns","x":.35,"y":.10,"voice":"male"},{"word":"a rucksack","x":.33,"y":.34,"voice":"male"},{"word":"a checked shirt","x":.40,"y":.66,"voice":"male"},{"word":"a trail","x":.78,"y":.80,"voice":"male"}],
"question":"What is the man rubbing?",
"answer":["He","is","rubbing","his","sore","back."],
"answerVoice":"male",
"notes":"In the piggyback shots (6.0-9.0 s) the woman and the man overlap; split with a horizontal line at the top of his head: the woman's box holds her head and shoulders only, her arms and legs around him fall into the man's box. At 4.0-5.5 s she is at the left edge behind the rucksack (narrow box). Before 4.0 s only a sliver of her sleeve/hair shows: off. Two walkers far behind are not targets. 'sore' is shown only by his grimace and rubbing."}
json.dump(c,open('content/4356.json','w'),indent=1)
