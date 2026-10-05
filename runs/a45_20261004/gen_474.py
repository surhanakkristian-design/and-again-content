import json
R=lambda t,x0,y0,x1,y1:{"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
O=lambda t:{"t":t,"off":True}
T=[i/2 for i in range(21)]
W=[R(0.0,.08,.05,1,.88),R(0.5,.08,.05,1,.88),R(1.0,.08,.06,1,.9),R(1.5,.08,.06,1,.9),R(2.0,.08,.05,1,.9),R(2.5,.08,.04,1,.9)]
W+=[R(t,.2,.31,.68,.77) for t in T[6:14]]
W+=[R(7.0,.2,.35,.65,.8),R(7.5,.28,.39,.62,.71),R(8.0,.36,.44,.59,.67),R(8.5,.40,.48,.58,.64),R(9.0,.39,.52,.57,.64),R(9.5,.40,.48,.58,.62),R(10.0,.41,.47,.59,.61)]
M=[O(t) for t in T[:6]]+[R(3.0,.69,.22,1,.6),R(3.5,.69,.28,1,.62),R(4.0,.69,.31,1,.61),R(4.5,.69,.33,1,.61),R(5.0,.69,.34,1,.62),R(5.5,.69,.34,1,.62),R(6.0,.69,.33,1,.62),R(6.5,.69,.33,1,.62),
R(7.0,.66,.35,.97,.62),R(7.5,.63,.38,.87,.61),R(8.0,.60,.41,.78,.56),R(8.5,.59,.44,.77,.58),R(9.0,.58,.45,.76,.59),O(9.5),O(10.0)]
B=[O(t) for t in T[:6]]+[R(t,.13,.78,.56,.97) for t in T[6:14]]+[R(7.0,.17,.81,.55,.98),R(7.5,.30,.72,.52,.86),R(8.0,.34,.67,.54,.81),R(8.5,.36,.64,.54,.78),R(9.0,.37,.64,.55,.78),R(9.5,.40,.62,.58,.76),R(10.0,.40,.61,.58,.75)]
d={"mediaId":474,"level":"B","keyWord":"meditation","defaultVoice":"female",
"taps":[{"phrase":"to reach for her phone","target":"the woman in front","voice":"female","keys":W},
{"phrase":"to meditate without a shirt","target":"the man without a shirt","voice":"male","keys":M},
{"phrase":"to rest on a wooden stand","target":"the singing bowl","voice":"female","keys":B}],
"stillS":5.0,
"nouns":[{"word":"a singing bowl","x":.34,"y":.87,"voice":"female"},{"word":"a deck","x":.78,"y":.80,"voice":"female"},
{"word":"palm trees","x":.30,"y":.15,"voice":"female"},{"word":"a bun","x":.49,"y":.37,"voice":"female"}],
"question":"What is the group doing?","answer":["They","are","meditating","on","a","wooden","deck."],"answerVoice":"female",
"notes":"The camera pulls back: from 8.0 s the targets are tiny and the boxes are near the minimum size; at 9.5 and 10.0 s the shirtless man cannot be told apart in the crowd (off). The woman reaches for her phone only at 2.0-2.5 s. The singing bowl phrase is a state (the bowl is struck by a hand at 5.5-6.5 s, but the hand is only briefly in the picture). At 10.0 s other bowls stand at the deck edge too; the box is on the one in front of the woman. 'a deck' pill sits on the wooden floor bottom right."}
json.dump(d,open("content/474.json","w"),indent=1,ensure_ascii=False)
