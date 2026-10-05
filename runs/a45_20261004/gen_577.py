import json
exec(open("gen_575.py").read().split("# ---------- 575")[0])
t=T(13)
cl={0.0:(.17,.09,.56,.23),0.5:(.17,.08,.58,.24),1.0:(.17,.07,.58,.24),1.5:(.17,.07,.58,.24),2.0:(.17,.05,.59,.25),
 2.5:(.17,.04,.61,.25),3.0:(.17,.04,.62,.26),3.5:(.17,.02,.63,.24),4.0:(.17,.01,.64,.20),4.5:(.17,.01,.66,.20),
 5.0:(.18,0,.65,.20),5.5:(.18,0,.67,.20),6.0:(.18,0,.68,.19)}
man={0.0:(.12,.42,.43,.28),0.5:(.12,.42,.43,.28),1.0:(.10,.43,.45,.28),1.5:(.09,.42,.47,.29),2.0:(.07,.41,.48,.30),
 2.5:(.07,.40,.48,.31),3.0:(.07,.41,.47,.30),3.5:(.04,.41,.47,.30),4.0:(0,.42,.51,.29),4.5:(0,.40,.50,.31),
 5.0:(0,.39,.52,.32),5.5:(0,.39,.51,.32),6.0:(0,.39,.49,.32)}
wo={0.0:(.56,.39,.40,.31),0.5:(.56,.39,.40,.31),1.0:(.56,.39,.40,.32),1.5:(.57,.39,.40,.32),2.0:(.56,.38,.40,.32),
 2.5:(.56,.37,.40,.33),3.0:(.55,.39,.43,.32),3.5:(.52,.39,.46,.32),4.0:(.52,.37,.45,.34),4.5:(.51,.37,.46,.34),
 5.0:(.53,.37,.44,.34),5.5:(.52,.37,.45,.34),6.0:(.50,.36,.48,.35)}
j={"mediaId":577,"level":"B","keyWord":"predict","defaultVoice":"female",
 "taps":[{"phrase":"to predict the rain","target":"the woman","voice":"female","keys":K(t,wo)},
  {"phrase":"to burst out laughing","target":"the man","voice":"male","keys":K(t,man)},
  {"phrase":"to bring a sudden shower","target":"the dark cloud","voice":"female","keys":K(t,cl)}],
 "stillS":4.5,
 "nouns":[{"word":"a storm cloud","x":.47,"y":.11,"voice":"female"},{"word":"an umbrella","x":.53,"y":.26,"voice":"female"},
  {"word":"a shawl","x":.76,"y":.61,"voice":"female"},{"word":"grass","x":.45,"y":.85,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","sheltering","under","a","yellow","umbrella."],
 "answerVoice":"female",
 "notes":"'to predict the rain' is read from her pointing at the dark cloud and getting the umbrella ready before the rain starts. The woman's box covers her body and the hand on the handle, not the umbrella canopy (it would overlap the cloud box and cover the man). From 4.0 s the lower part of the cloud is hidden behind the umbrella; the cloud box is the part above it. The man also ends up under the umbrella, but he does not hold it; the question names the woman."}
json.dump(j,open("content/577.json","w"),indent=1)
