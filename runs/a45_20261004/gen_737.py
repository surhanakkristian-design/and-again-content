import json
T=[i*0.5 for i in range(21)]
M={0.0:(0,.05,.55,.92),0.5:(0,.05,.55,.92),1.0:(0,.07,.55,.93),1.5:(0,.07,.55,.93),2.0:(0,.07,.55,.90),2.5:(0,.05,.55,.92),3.0:(0,.03,.45,.97),
3.5:(0,0,.18,.62),4.0:(0,0,.22,.64),4.5:(0,0,.22,.64),5.0:(0,0,.18,.68),5.5:(0,0,.18,.68),6.0:(0,0,.18,.62),6.5:(0,.10,.24,.48),7.0:None,
7.5:(0,.05,.52,.95),8.0:(.25,.65,.75,.35),8.5:(.56,.08,.44,.90),9.0:(.22,.17,.33,.83),9.5:(.10,.66,.90,.34),10.0:(.37,.62,.63,.38)}
B={0.0:(.58,.19,.42,.78),0.5:(.58,.19,.42,.78),1.0:(.58,.19,.42,.78),1.5:(.58,.19,.42,.78),2.0:(.58,.17,.42,.80),2.5:(.58,.17,.42,.80),3.0:(.48,.12,.52,.88),
3.5:(.18,0,.82,.72),4.0:(.22,0,.78,.66),4.5:(.22,0,.78,.66),5.0:(.18,.02,.82,.74),5.5:(.18,.02,.82,.74),6.0:(.18,0,.82,.68),6.5:(.24,.08,.76,.62),7.0:(.05,.15,.95,.82),
7.5:(.52,.17,.48,.83),8.0:(.25,.02,.75,.63),8.5:(.24,.24,.32,.68),9.0:(.55,.17,.45,.83),9.5:(.38,.15,.62,.51),10.0:(.44,.03,.56,.57)}
W={t:None for t in T}
W.update({8.0:(.03,.27,.22,.66),8.5:(.02,.33,.22,.64),9.0:(.02,.37,.20,.55),9.5:(.10,.36,.26,.30),10.0:(.02,.32,.33,.66)})
def keys(d): return [({"t":t,"off":True} if d[t] is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
c={"mediaId":737,"level":"B","keyWord":"stepfather","defaultVoice":"male",
"taps":[{"phrase":"to tighten a bolt","target":"the man","voice":"male","keys":keys(M)},
{"phrase":"to leap into his arms","target":"the boy","voice":"male","keys":keys(B)},
{"phrase":"to watch from the doorway","target":"the woman","voice":"female","keys":keys(W)}],
"stillS":2.5,
"nouns":[{"word":"glasses","x":.28,"y":.26,"voice":"male"},{"word":"a wheel","x":.20,"y":.62,"voice":"male"},
{"word":"a saddle","x":.87,"y":.58,"voice":"male"},{"word":"a pedal","x":.64,"y":.87,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","tightening","a","bolt","on","the","wheel."],"answerVoice":"male",
"notes":"Three shots. Kitchen shot 3.5-6.5 s: only the man's arm and hands are in the picture (left edge), his box is that strip. Hug 8.0-10.0 s: man and boy overlap heavily, boxes are split roughly (8.0 s boy = upper block incl. the man's head, man = lower body; 8.5 s man = right side with head, boy = orange shirt and shorts at the left; 9.0 s vertical split; 9.5/10.0 s boy above, man below) - verifier please look at these. The woman is only in the picture from 8.0 s, blurred in the doorway. Key word 'stepfather' is not placeable as a noun (the relation cannot be seen)."}
json.dump(c,open('content/737.json','w'),indent=1)
