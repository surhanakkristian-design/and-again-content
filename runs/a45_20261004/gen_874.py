import json
T=[i*0.5 for i in range(21)]
W=[(.18,.03,.75,.25),(.20,0,.78,.41),(.15,.15,.75,.30),(.10,0,.82,.46),(.08,.14,.76,.33),(.08,.17,.72,.30),(.15,.18,.58,.30),(.10,.17,.55,.33),(.05,.18,.52,.29),(.08,.18,.49,.29),(.05,.18,.47,.29),(.05,.19,.47,.28),(.08,.18,.47,.27),(.05,.19,.52,.28),(.03,.19,.52,.28),(0,0,.58,.48),(0,.21,.58,.27),(0,.21,.50,.29),(0,.23,.48,.29),(.03,.17,.50,.35),(.18,.24,.38,.24)]
M=[None,None,None,None,(.84,.35,.16,.30),(.80,.22,.20,.42),(.74,.18,.26,.55),(.66,.17,.34,.53),(.58,.16,.42,.46),(.58,.19,.42,.43),(.55,.18,.45,.42),(.55,.19,.45,.43),(.56,.17,.44,.43),(.58,.17,.42,.45),(.57,.17,.43,.50),(.60,.18,.40,.55),(.60,.17,.40,.53),(.52,.17,.48,.51),(.49,.17,.51,.58),(.55,.19,.45,.60),(.56,.19,.44,.49)]
H=[(.10,.28,.75,.64),(.20,.41,.58,.57),(.13,.45,.55,.55),(.12,.46,.53,.54),(.12,.47,.53,.51),(.12,.47,.55,.51),(.05,.48,.52,.52),(.02,.50,.50,.50),(0,.47,.46,.48),(0,.47,.46,.47),(0,.47,.46,.50),(0,.47,.46,.50),(0,.45,.46,.47),(0,.47,.46,.47),(0,.47,.46,.53),(0,.48,.46,.52),(0,.48,.46,.49),(0,.50,.44,.47),(0,.52,.40,.48),(0,.52,.46,.48),(.03,.48,.46,.48)]
def k(L): return [({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}) for t,b in zip(T,L)]
d={"mediaId":874,"level":"B","keyWord":"a wig","defaultVoice":"female",
"taps":[{"phrase":"to try on a pink wig","target":"the woman","voice":"female","keys":k(W)},
{"phrase":"to grab the ginger wig","target":"the man","voice":"male","keys":k(M)},
{"phrase":"to stand on the dressing table","target":"the mannequin head","voice":"female","keys":k(H)}],
"stillS":4.5,
"nouns":[{"word":"fairy lights","x":.50,"y":.14,"voice":"female"},{"word":"a mannequin head","x":.28,"y":.58,"voice":"female"},{"word":"a wig","x":.72,"y":.69,"voice":"female"},{"word":"sequins","x":.60,"y":.90,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","trying","on","a","pink","wig."],"answerVoice":"female",
"notes":"Two wigs are visible at the still (pink on her head, ginger on the table); the 'a wig' pill sits on the ginger one on the table and no noun labels the woman. Man is only partly in frame at 2.0-2.5 s. Mannequin box and woman box are split along the top of the mannequin head, so her lower body is in no box."}
json.dump(d,open("content/874.json","w"),indent=1)
