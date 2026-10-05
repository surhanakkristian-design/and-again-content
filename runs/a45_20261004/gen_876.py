import json
T=[i*0.5 for i in range(21)]
N=None
W=[(.22,.38,.78,.44),(.25,.38,.75,.36),(.36,0,.64,.27),(.45,.08,.55,.92),(.13,.35,.87,.32),(0,.03,1,.30),(0,.50,.56,.50),(0,0,.60,1),(0,0,.62,1),(0,0,.62,1),(0,.06,.72,.94),(0,.07,.74,.93),(0,.06,.76,.94),(0,.10,.72,.90),(0,.18,.52,.82),(0,.18,.50,.82),(0,.17,.52,.83),(0,.17,.52,.83),(0,.20,.45,.80),(.07,.32,.39,.68),(.04,.34,.42,.66)]
M=[N]*10+[(.80,.60,.20,.25),(.78,.55,.22,.32),(.78,.38,.22,.36),(.78,.36,.22,.36),(.54,.28,.46,.72),(.55,.27,.45,.73),(.57,.25,.43,.75),(.60,.25,.40,.75),(.58,.27,.42,.73),(.46,.30,.54,.70),(.47,.32,.53,.68)]
def k(L): return [({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}) for t,b in zip(T,L)]
d={"mediaId":876,"level":"A","keyWord":"wine","defaultVoice":"female",
"taps":[{"phrase":"to touch the grapes","target":"the woman","voice":"female","keys":k(W)},
{"phrase":"to pour the wine","target":"the woman","voice":"female","keys":k(W)},
{"phrase":"to have a short beard","target":"the man","voice":"male","keys":k(M)}],
"stillS":2.5,
"nouns":[{"word":"a bottle","x":.35,"y":.20,"voice":"female"},{"word":"wine","x":.50,"y":.52,"voice":"female"},{"word":"cheese","x":.80,"y":.61,"voice":"female"},{"word":"a table","x":.40,"y":.88,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","pouring","wine","into","a","glass."],"answerVoice":"female",
"notes":"Many cuts. Only two possible targets (woman, man), so the woman has two phrases. In the close-ups at 0-1.0 s and 2.5 s only her hand is in the picture: the box is on the hand (at 2.5 s on both hands and the bottle they hold). The man does nothing only he does (both hold and drink), so his phrase is a state; at 5.0-6.5 s only his hand with a glass is visible, at 9.5-10 s both are seen from behind. 'to smell the wine' was avoided because the man holds his glass to his nose/mouth at 7.0 s."}
json.dump(d,open("content/876.json","w"),indent=1)
