import json
O={"off":True}
def B(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
times=[i*0.5 for i in range(21)]
W=[B(.18,.18,.56,.46),B(.20,.08,.70,.56),B(.05,.02,.74,.84),B(.10,.08,.55,.66),B(.02,.09,.60,.60),B(0,.14,.55,.50),
   B(.12,0,.76,.38),B(.10,0,.80,.30),B(0,0,.90,.30),B(0,0,1.0,.30),B(0,0,.72,.42),B(0,0,.78,.36),
   B(0,.11,.50,.50),B(0,.14,.51,.47),B(.06,.19,.41,.43),B(.06,.19,.40,.44),B(.03,.19,.47,.44),B(.02,.19,.47,.44),B(0,.23,.49,.40),B(.27,.31,.24,.32),B(.30,.34,.19,.29)]
M=[O,O,O,B(.66,.15,.18,.32),B(.63,.10,.37,.52),B(.56,.07,.44,.57),O,O,O,O,O,O,
   B(.51,.04,.49,.57),B(.52,.09,.48,.52),B(.48,.09,.52,.53),B(.47,.09,.53,.54),B(.51,.09,.49,.54),B(.50,.09,.50,.54),B(.50,.18,.50,.45),B(.51,.32,.27,.31),B(.49,.34,.18,.28)]
P=[O,O,O,O,O,O,B(0,.39,1.0,.38),B(0,.36,1.0,.44),B(0,.34,1.0,.48),B(0,.34,1.0,.50),B(0,.45,1.0,.48),B(0,.40,1.0,.53),
   B(.26,.62,.48,.14),B(.26,.62,.48,.14),B(.28,.63,.46,.14),B(.28,.64,.46,.14),B(.28,.64,.46,.14),B(.28,.64,.46,.14),B(.28,.64,.46,.14),B(.28,.64,.46,.14),B(.28,.64,.46,.14)]
def K(l): return [dict(t=t,**k) for t,k in zip(times,l)]
d={"mediaId":506,"level":"B","keyWord":"nutrition","defaultVoice":"female",
"taps":[
 {"phrase":"to crack an egg","target":"the woman","voice":"female","keys":K(W)},
 {"phrase":"to grab his backpack","target":"the man","voice":"male","keys":K(M)},
 {"phrase":"to be topped with berries","target":"the plate","voice":"female","keys":K(P)}],
"stillS":10.0,
"nouns":[{"word":"a doorway","x":.47,"y":.27,"voice":"female"},{"word":"a platter","x":.48,"y":.65,"voice":"female"},{"word":"a mango","x":.70,"y":.74,"voice":"female"},{"word":"oats","x":.86,"y":.83,"voice":"female"}],
"question":"What are the man and woman preparing?",
"answer":["They","are","preparing","a","platter","of","fresh","ingredients."],
"answerVoice":"female",
"notes":"Key word 'nutrition' is abstract and not used. Close-ups 3.0-5.5: the woman is boxed by her orange top above the plate (her hands over the plate fall in the plate box); the man is OFF there (only an arm / blue edge). The plate is topped with berries only from 5.5 on, but is boxed from 3.0 when it first appears. The man grabs/swings the backpack at 9.0 and wears it at 9.5-10.0. The egg is cracked at 2.0. Boxes of woman/man end above the plate box in 6.0-10.0. 'a platter' = the arranged plate; tap target is called 'the plate'. A small bowl of blueberries stands next to the plate (not 'topped')."}
json.dump(d,open("content/506.json","w"),indent=1)
