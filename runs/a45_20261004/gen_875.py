import json
T=[i*0.5 for i in range(21)]
N=None
W=[(0,.30,1,.70),(0,.22,.60,.78),(0,.20,.62,.80),N,N,N,N,N,N,N,(0,.75,.25,.23),(0,.46,.20,.54),(0,.42,.14,.58),(0,.43,.42,.55),(0,.47,.50,.53),(0,.45,.60,.55),(0,.46,.67,.54),(0,.47,.62,.53),(0,.52,.60,.48),(0,.52,.60,.48),(0,.47,.62,.53)]
S=[N]*7+[(.76,.40,.24,.19),(.60,.28,.40,.32),(.36,.28,.64,.48),(.08,.28,.92,.46),(.20,.36,.80,.28),(.14,.38,.86,.47),(.72,.38,.28,.26),(.74,.40,.26,.20),(.78,.38,.22,.16),(.80,.40,.20,.18),(.82,.44,.18,.14),N,N,N]
B=[N]*9+[(0,0,.26,.14),(0,0,.30,.14),(0,.01,.36,.14),(0,.03,.46,.15),(0,.08,.54,.14),(0,.09,.56,.14),(0,.08,.62,.15),(0,.07,.65,.15),(0,.07,.74,.16),(.04,.06,.78,.17),(.11,.06,.80,.18),(.14,.08,.83,.17)]
def k(L): return [({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}) for t,b in zip(T,L)]
d={"mediaId":875,"level":"A","keyWord":"wind","defaultVoice":"female",
"taps":[{"phrase":"to wear a yellow scarf","target":"the woman","voice":"female","keys":k(W)},
{"phrase":"to hang on a line","target":"the white sheet","voice":"female","keys":k(S)},
{"phrase":"to fly high in the sky","target":"the birds","voice":"female","keys":k(B)}],
"stillS":7.0,
"nouns":[{"word":"birds","x":.25,"y":.15,"voice":"female"},{"word":"trees","x":.35,"y":.42,"voice":"female"},{"word":"a scarf","x":.36,"y":.70,"voice":"female"},{"word":"grass","x":.72,"y":.86,"voice":"female"}],
"question":"What is the woman wearing?","answer":["She","is","wearing","a","yellow","scarf."],"answerVoice":"female",
"notes":"Key word 'wind' is not a visible thing, so it is not a noun. The woman's phrase is a state (the man does everything else she does). The man stands right behind her, so parts of him fall inside her box in several frames; he has no phrase. At 5.0 s only her arm and scarf end are in the picture: her box is on the scarf end below the sheet; at 5.5-6.0 s her box and the sheet box are split along a vertical line. The scarf flies off alone at 1.5-2.5 s (woman set off there)."}
json.dump(d,open("content/875.json","w"),indent=1)
