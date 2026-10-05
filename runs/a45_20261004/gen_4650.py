import json
def keys(T,d):
    out=[]
    for t in T:
        if t in d:
            x,y,w,h=d[t]; out.append({"t":t,"x":x,"y":y,"w":round(w,2),"h":round(h,2)})
        else: out.append({"t":t,"off":True})
    return out
def save(c): json.dump(c,open('content/%d.json'%c["mediaId"],'w'),indent=1,ensure_ascii=False)

# ---------- 4650
T=[i*0.5 for i in range(19)]
man={0.0:(.02,.05,.96,.68),0.5:(.02,.05,.96,.68),1.0:(.03,.07,.95,.68),1.5:(.08,.06,.92,.68),
 2.0:(.15,.0,.85,.75),2.5:(.27,.0,.73,.74),3.0:(.28,.0,.72,.83),3.5:(.28,.0,.72,.83),
 4.0:(.36,.02,.64,.44),4.5:(.44,.05,.56,.41),5.0:(.27,.10,.73,.37),5.5:(.28,.14,.72,.35),
 6.0:(.67,.17,.33,.65),6.5:(.72,.25,.28,.62),7.0:(.64,.36,.36,.62),7.5:(.65,.42,.35,.53),
 8.0:(.60,.38,.39,.47),8.5:(.58,.36,.36,.42),9.0:(.63,.45,.37,.47)}
foam={4.0:(.30,.47,.37,.40),4.5:(.20,.47,.52,.42),5.0:(.18,.48,.54,.52),5.5:(.16,.50,.64,.50),
 6.0:(.10,.15,.56,.85),6.5:(.15,.0,.56,.97),7.0:(.12,.0,.51,1.0),7.5:(.18,.0,.46,1.0),
 8.0:(.07,.08,.52,.86),8.5:(.07,.09,.50,.80),9.0:(.0,.06,.62,.94)}
save({"mediaId":4650,"level":"B","keyWord":"reaction","defaultVoice":"male",
 "taps":[
  {"phrase":"to pour a blue liquid","target":"the man in front","voice":"male","keys":keys(T,man)},
  {"phrase":"to overflow onto the bench","target":"the foam","voice":"male","keys":keys(T,foam)},
  {"phrase":"to rise towards the ceiling","target":"the foam","voice":"male","keys":keys(T,foam)}],
 "stillS":5.0,
 "nouns":[{"word":"safety goggles","x":.70,"y":.27,"voice":"male"},{"word":"a lab coat","x":.76,"y":.47,"voice":"male"},
          {"word":"foam","x":.45,"y":.68,"voice":"male"},{"word":"flasks","x":.28,"y":.93,"voice":"male"}],
 "question":"What is the foam doing?",
 "answer":["The","foam","is","overflowing","onto","the","bench."],
 "answerVoice":"male",
 "notes":"Key word 'reaction' is abstract: no noun slot, not in the answer. Two phrases share the foam (the classmates in the back are tiny and only watch). The foam exists as a target from 4.0 s (at 3.5 s it is still inside the flask): off before. From 4.0 s the foam stands in front of the man, so the boxes are split: 4.0-5.5 s the man keeps his upper body above the foam (his hands beside the flask fall outside his box), 6.0-9.0 s split by a vertical line between the column and the man. Classmates in the background also wear coats and goggles but are small; the pills sit on the man in front."})

# ---------- 4652
T=[i*0.5 for i in range(21)]
W={0.0:(.07,.09,.68,.63),0.5:(.22,.08,.75,.62),1.0:(.20,.10,.80,.60),1.5:(.18,.09,.82,.60),
 2.0:(.02,.11,.80,.60),2.5:(.13,.08,.80,.62),3.0:(.12,.09,.88,.64),3.5:(.12,.09,.88,.66),
 4.0:(.11,.10,.89,.62),4.5:(.12,.09,.88,.60),5.0:(.10,.09,.64,.62),5.5:(.12,.09,.72,.62),
 6.0:(.13,.11,.72,.62),6.5:(.13,.11,.77,.62),7.0:(.11,.10,.74,.62),7.5:(.12,.11,.70,.60),
 8.0:(.13,.12,.74,.59),8.5:(.12,.13,.82,.57),9.0:(.10,.12,.70,.63),9.5:(.10,.09,.76,.67),10.0:(.17,.08,.83,.64)}
P={0.0:(.0,.75,.49,.13),0.5:(.05,.73,.50,.14),1.0:(.05,.76,.48,.13),1.5:(.02,.76,.48,.14),
 2.0:(.0,.76,.43,.13),2.5:(.07,.74,.48,.14),3.0:(.07,.77,.46,.13),3.5:(.07,.78,.48,.13),
 4.0:(.03,.77,.48,.13),4.5:(.03,.76,.48,.15),5.0:(.0,.79,.50,.13),5.5:(.02,.80,.50,.13),
 6.0:(.09,.76,.44,.13),6.5:(.09,.75,.46,.14),7.0:(.07,.76,.46,.13),7.5:(.07,.77,.48,.13),
 8.0:(.09,.78,.46,.13),8.5:(.09,.80,.46,.13),9.0:(.09,.82,.46,.13),9.5:(.09,.83,.46,.13),10.0:(.12,.84,.42,.13)}
D={7.5:(.58,.73,.26,.24),8.0:(.61,.72,.28,.24),8.5:(.60,.72,.30,.26),9.0:(.62,.76,.28,.22),9.5:(.62,.77,.28,.23),10.0:(.60,.76,.30,.24)}
save({"mediaId":4652,"level":"B","keyWord":"compete","defaultVoice":"female",
 "taps":[
  {"phrase":"to cry out with effort","target":"the woman in the middle","voice":"female","keys":keys(T,W)},
  {"phrase":"to cushion an elbow","target":"the red pad","voice":"female","keys":keys(T,P)},
  {"phrase":"to have a plastic lid","target":"the orange drink","voice":"female","keys":keys(T,D)}],
 "stillS":4.0,
 "nouns":[{"word":"a crowd","x":.82,"y":.07,"voice":"female"},{"word":"a flower","x":.45,"y":.17,"voice":"female"},
          {"word":"a barrier","x":.86,"y":.41,"voice":"female"},{"word":"a pad","x":.25,"y":.83,"voice":"female"}],
 "question":"What is happening at the table?",
 "answer":["Two","people","are","competing","in","an","arm-wrestling","match."],
 "answerVoice":"female",
 "notes":"AI clip with morphing: the opponent on the left is a man until 5.5 s and a woman with a red flower from 6.0 s, a second man comes and goes on the right, so no opponent is a target and the woman is named 'in the middle' (she faces the camera in every frame). The crowd is not a tap target because its faces surround her head and could not be boxed without overlapping her. 'to cry out with effort' = her wide open mouth 3.0-5.5 s (the man on the right only laughs at 5.0 s). The orange drink is on the table only 7.5-10.0 s (6.0-7.0 s it is in a hand, half hidden: off); a second, clear cup without a lid is in her hand 8.0-10.0 s. Answer: 'arm-wrestling' is one chip."})

# ---------- 4653
T=[i*0.5 for i in range(25)]
M={0.0:(.31,.22,.44,.63),0.5:(.26,.18,.52,.68),1.0:(.24,.01,.60,.99),1.5:(.20,.07,.66,.93),
 2.0:(.20,.02,.68,.95),2.5:(.21,.05,.66,.91),3.0:(.22,.02,.65,.96),3.5:(.21,.02,.66,.96),4.0:(.24,.10,.64,.87),
 4.5:(.12,.0,.88,.73),5.0:(.02,.0,.88,.85),5.5:(.0,.0,1.0,.85),6.0:(.07,.0,.93,.71),6.5:(.15,.0,.85,.73),
 7.0:(.0,.0,.93,.81),7.5:(.07,.0,.93,.80),8.0:(.02,.0,.98,.73),
 8.5:(.30,.10,.46,.66),9.0:(.30,.07,.50,.90),9.5:(.29,.05,.54,.93),10.0:(.28,.07,.55,.81),
 10.5:(.21,.07,.63,.80),11.0:(.27,.05,.54,.86),11.5:(.25,.05,.57,.86),12.0:(.25,.03,.56,.88)}
Dr={0.0:(.76,.0,.22,.88),0.5:(.79,.0,.19,.87),1.0:(.85,.0,.11,.86),
 8.5:(.08,.0,.21,.87),9.0:(.06,.0,.23,.95),9.5:(.06,.0,.22,.90),10.0:(.06,.0,.21,.86),
 10.5:(.03,.0,.17,.86),11.0:(.05,.0,.21,.92),11.5:(.05,.0,.19,.90),12.0:(.05,.0,.19,.88)}
save({"mediaId":4653,"level":"B","keyWord":"mud","defaultVoice":"male",
 "taps":[
  {"phrase":"to stamp on the doormat","target":"the man","voice":"male","keys":keys(T,M)},
  {"phrase":"to step into the hallway","target":"the man","voice":"male","keys":keys(T,M)},
  {"phrase":"to stand wide open","target":"the front door","voice":"male","keys":keys(T,Dr)}],
 "stillS":6.5,
 "nouns":[{"word":"waterproof trousers","x":.50,"y":.10,"voice":"male"},{"word":"rubber boots","x":.45,"y":.34,"voice":"male"},
          {"word":"mud","x":.74,"y":.61,"voice":"male"},{"word":"a doormat","x":.28,"y":.74,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","stamping","the","mud","off","his","boots."],
 "answerVoice":"male",
 "notes":"Only one person; boots and doormat touch him in every shot, so they are not separate tap targets (the man's box holds his boots; in the close-ups 4.5-8.0 s it is his legs and boots). Third target is the front door: boxed at 0.0-1.0 s (outside view, on the right) and 8.5-12.0 s (inside view, on the left); 1.5-8.0 s it is almost fully hidden behind the man or not recognisable in the close-up: off. At 10.5 s his hand reaches the door: split at x .21. Nouns on the close-up 6.5 s: the 'mud' pill sits on the caked toe of the right boot, 'rubber boots' on the upper shaft of the left boot; lumps of mud also lie on the mat left of the 'a doormat' pill."})

# ---------- 4654
T=[i*0.5 for i in range(21)]
Wm={0.0:(.0,.39,.50,.61),0.5:(.0,.39,.54,.61),1.0:(.0,.40,.52,.60),1.5:(.0,.35,.52,.65),
 2.0:(.0,.39,.55,.61),2.5:(.0,.38,.62,.62),3.0:(.0,.43,.50,.57),3.5:(.0,.43,.57,.57),
 4.0:(.0,.36,.55,.64),4.5:(.0,.35,.62,.65),5.0:(.0,.42,.19,.58),5.5:(.0,.29,.59,.71),
 6.0:(.0,.28,.62,.72),6.5:(.0,.28,.62,.72),7.0:(.0,.29,.53,.71),7.5:(.0,.39,.53,.61),
 8.0:(.0,.39,.53,.61),8.5:(.0,.41,.53,.59),9.0:(.0,.42,.53,.58),9.5:(.0,.43,.53,.57),10.0:(.0,.42,.53,.58)}
Mn={0.0:(.08,.24,.34,.14),0.5:(.10,.25,.34,.13),1.0:(.10,.26,.34,.13),1.5:(.14,.22,.30,.12),
 2.0:(.10,.25,.32,.13),2.5:(.10,.24,.32,.13),3.0:(.17,.28,.30,.14),3.5:(.14,.27,.30,.15),
 4.0:(.15,.22,.28,.13),4.5:(.15,.22,.28,.12),5.0:(.14,.27,.20,.14),
 7.5:(.06,.26,.28,.12),8.0:(.06,.26,.26,.12),8.5:(.08,.27,.28,.13),9.0:(.08,.27,.28,.14),9.5:(.12,.28,.30,.14),10.0:(.10,.27,.30,.14)}
C={5.0:(.20,.42,.28,.19),5.5:(.60,.40,.34,.22),6.0:(.63,.41,.30,.21),6.5:(.63,.42,.30,.20),7.0:(.54,.41,.38,.21),
 7.5:(.54,.41,.38,.21),8.0:(.54,.42,.38,.20),8.5:(.54,.42,.38,.20),9.0:(.54,.41,.38,.21),9.5:(.54,.41,.38,.21),10.0:(.54,.41,.38,.21)}
save({"mediaId":4654,"level":"A","keyWord":"doubt","defaultVoice":"female",
 "taps":[
  {"phrase":"to cross her arms","target":"the woman","voice":"female","keys":keys(T,Wm)},
  {"phrase":"to stand behind the woman","target":"the man","voice":"male","keys":keys(T,Mn)},
  {"phrase":"to stay on the shelf","target":"the cup","voice":"female","keys":keys(T,C)}],
 "stillS":8.0,
 "nouns":[{"word":"a cup","x":.72,"y":.52,"voice":"female"},{"word":"a shelf","x":.76,"y":.68,"voice":"female"},
          {"word":"a woman","x":.22,"y":.74,"voice":"female"},{"word":"a plant","x":.52,"y":.88,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","putting","a","cup","on","the","shelf."],
 "answerVoice":"female",
 "notes":"Key word 'doubt' is abstract: no noun slot, not in the answer. The man stands right behind the woman, mostly only his head shows above hers: his box is his head and stops where her hair begins; his blue T-shirt and his hand with the screwdriver beside her fall into her box or outside (3.0-3.5 s and 9.5-10.0 s are the weakest frames). He is hidden 5.5-7.0 s: off. The cup appears at 5.0 s in her hands (her box is cut to her face there) and stands on the shelf from 5.5 s. Two shelves are in the picture; the 'a shelf' pill is on the lower one, no noun is on the upper one."})
