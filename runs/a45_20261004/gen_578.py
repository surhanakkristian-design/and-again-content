import json
exec(open("gen_575.py").read().split("# ---------- 575")[0])
t=T(21)
me={0.0:(.15,.17,.50,.68),0.5:(.15,.10,.58,.78),1.0:(.08,.07,.90,.86),1.5:(.08,.07,.82,.90),2.0:(.05,.10,.92,.88),
 2.5:(.18,.05,.70,.95),3.0:(.18,.10,.70,.90),3.5:(.14,.30,.44,.70),4.0:(.15,.33,.37,.67),4.5:(.20,.09,.68,.85),
 5.0:(.17,.09,.66,.86),5.5:(.16,.10,.65,.90),6.0:(.16,.12,.67,.88),6.5:(.12,.19,.60,.66),7.0:(.28,.17,.44,.76),
 7.5:(.30,.17,.37,.77),8.0:(.31,.15,.39,.77),8.5:(.31,.14,.43,.78),9.0:(.26,.17,.50,.75),9.5:(.27,.16,.46,.76),
 10.0:(.27,.12,.46,.78)}
om={2.5:(0,.29,.17,.30),3.0:(0,.30,.17,.32),3.5:(0,.27,.13,.20),4.0:(0,.27,.14,.23),4.5:(0,.30,.19,.28),
 5.0:(0,.33,.16,.29),5.5:(0,.34,.15,.28),6.0:(0,.35,.15,.25),6.5:(0,.27,.11,.36),7.0:(0,.27,.22,.50),
 7.5:(0,.25,.29,.52),8.0:(0,.23,.30,.40),8.5:(0,.22,.28,.40),9.0:(0,.24,.20,.50)}
j={"mediaId":578,"level":"B","keyWord":"pride","defaultVoice":"female",
 "taps":[{"phrase":"to wheel out a motorcycle","target":"the mechanic","voice":"female","keys":K(t,me)},
  {"phrase":"to polish the fuel tank","target":"the mechanic","voice":"female","keys":K(t,me)},
  {"phrase":"to pat her shoulder","target":"the old man","voice":"male","keys":K(t,om)}],
 "stillS":4.0,
 "nouns":[{"word":"a bandana","x":.30,"y":.48,"voice":"female"},{"word":"a fuel tank","x":.68,"y":.56,"voice":"female"},
  {"word":"an engine","x":.62,"y":.72,"voice":"female"},{"word":"cobblestones","x":.65,"y":.90,"voice":"female"}],
 "question":"What is the mechanic doing?",
 "answer":["She","is","presenting","her","motorcycle","with","pride."],
 "answerVoice":"female",
 "notes":"Third target is the old man on the left (pats her shoulder at 7.5-8.0 s); the other neighbours overlap each other and her too much to box. 'to cross her arms' was dropped: the woman on the left also has crossed arms at 10.0 s. At 3.5-4.0 s the mechanic crouches in front of the old man: her box starts right of him, so the lower-left part of her back is outside it. Old man is a sliver at the frame edge at 9.5-10.0 s: off. The question is open (she does several things); the model answer sums up the second half of the clip with the key word."}
json.dump(j,open("content/578.json","w"),indent=1)
