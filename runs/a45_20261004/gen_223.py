import json
T=[i/2 for i in range(21)]
def keys(d): return [({"t":t,"off":True} if d.get(t) is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
def tap(p,t,v,d): return {"phrase":p,"target":t,"voice":v,"keys":keys(d)}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
import sys
vid=sys.argv[1]
if vid=='223':
    CAT={0.0:(0,.55,.90,.25),0.5:(0,.56,.90,.26),9.5:(0,.77,.22,.21),10.0:(0,.69,.30,.23)}
    CO={3.5:(.22,.26,.56,.74),4.0:(.23,.25,.50,.75),4.5:(.23,.25,.50,.75),5.0:(.28,.42,.40,.45),5.5:(.40,.50,.27,.26)}
    W={0.5:(.10,.36,.40,.19),1.0:(0,.48,.55,.24),1.5:(.08,0,.64,.86),2.0:(.20,.26,.31,.64),2.5:(.18,.20,.35,.67),3.0:(.08,.18,.38,.82),
       3.5:(0,.36,.21,.64),4.0:(0,.33,.22,.67),4.5:(0,.33,.22,.67),5.0:(0,.50,.25,.50),5.5:(0,.50,.32,.50),6.0:(0,.16,.38,.80),6.5:(0,.25,.50,.52),
       7.0:(0,.36,.36,.36),7.5:(0,.36,.36,.36),8.0:(0,.36,.38,.34),8.5:(.08,.32,.42,.38),9.0:(0,.40,.45,.30),9.5:(0,.40,.45,.30),10.0:(0,.40,.46,.28)}
    c={"mediaId":223,"level":"A","keyWord":"delivery","defaultVoice":"male",
    "taps":[tap("to lie on the sofa","the cat","male",CAT),tap("to bring the food","the man in the helmet","male",CO),tap("to wear an orange top","the woman","female",W)],
    "stillS":10.0,
    "nouns":[noun("a lamp",.50,.08,"male"),noun("a window",.62,.24,"male"),noun("a cat",.14,.78,"male"),noun("a sofa",.64,.76,"male")],
    "question":"Who is bringing the food?","answer":["A","man","in","a","helmet","is","bringing","the","food."],"answerVoice":"male",
    "notes":"Many cuts. Cat: lies on the sofa at 0.0-0.5, comes back at 9.5-10.0 (walking on the sofa back) - the couple sits ON/behind the sofa but never lies. Courier only 3.5-5.5 (small back view at 5.5). Woman: state phrase (orange top) because every action is shared with the man; at 0.0 only her hair top shows -> off; at 3.5-5.0 she is a cut-off figure at the left edge and her arms reach into the courier's box (split at x 0.22-0.25). defaultVoice male: mixed couple, odd id."}
if vid=='224':
    W={0.0:(0,.14,.36,.46),0.5:(0,.14,.40,.46),1.0:(0,.13,.37,.50),1.5:(.02,.17,.38,.42),2.0:(0,.14,.43,.45),2.5:(0,.08,.52,.53),3.0:(0,.03,.50,.73),
       4.5:(0,0,.22,.27),5.0:(0,0,.40,.42),5.5:(0,0,.48,.29),6.0:(0,0,.24,.45),6.5:(0,.08,.46,.50),7.0:(0,.34,.46,.38),7.5:(0,.33,.44,.39),
       8.0:(0,.13,.48,.46),8.5:(0,.12,.47,.47),9.0:(0,.13,.44,.28),9.5:(0,0,.40,.39),10.0:(0,.12,.44,.27)}
    M={0.0:(.37,.10,.63,.60),0.5:(.41,.05,.59,.60),1.0:(.38,.06,.62,.74),1.5:(.41,.23,.59,.57),2.0:(.44,.03,.56,.60),2.5:(.53,.03,.47,.62),3.0:(.51,0,.49,.72),
       3.5:(0,0,1,.56),4.5:(.24,0,.76,.36),5.0:(.48,0,.52,.44),5.5:(.50,0,.50,.72),6.0:(.27,0,.73,.62),6.5:(.47,.03,.53,.55),7.0:(.50,.31,.50,.45),7.5:(.48,.31,.52,.43),
       8.0:(.50,.11,.50,.53),8.5:(.49,.11,.51,.53),9.0:(.68,.07,.32,.64),9.5:(.42,.05,.58,.65),10.0:(.60,.06,.40,.55)}
    CAT={9.0:(0,.42,.31,.24),9.5:(0,.40,.41,.24),10.0:(0,.40,.38,.25)}
    c={"mediaId":224,"level":"B","keyWord":"designing","defaultVoice":"female",
    "taps":[tap("to sketch a chair","the man","male",M),tap("to point at the sketch","the woman","female",W),tap("to sniff the cardboard chair","the cat","female",CAT)],
    "stillS":1.5,
    "nouns":[noun("a sketch",.58,.70,"female"),noun("a jar",.12,.60,"female"),noun("a houseplant",.84,.27,"female")],
    "question":"What are they designing?","answer":["They","are","designing","a","chair."],"answerVoice":"female",
    "notes":"Man sketches at 0.0, 1.5 (pencil on paper); woman points at 2.5-3.0. Close-ups 3.5-6.0: only hands/torsos. 3.5 = the man's hand with eraser and ruler (white shirt). 4.0: a drawing hand whose owner is not clear (comes from the left, blue-shirt side) -> both people OFF there; verifier please check that this does not make 'to sketch a chair' fit the woman too. 5.5: the man's cutter hand lies in front of the woman, his box covers only his torso and right hand. Cat only 9.0-10.0, nose at the model chair. Jar holds pencils (no 'pencils' noun). defaultVoice female: mixed pair, even id."}
if vid=='226':
    M={0.0:(0,.16,.97,.84),0.5:(0,.16,1,.84),1.0:(0,.18,.50,.82),1.5:(0,.18,1,.82),2.0:(.10,.12,.66,.57),2.5:(.24,.12,.52,.56),3.0:(.18,.16,.58,.53),3.5:(.14,.15,.68,.58),
       4.0:(.14,.18,.68,.53),4.5:(.20,.35,.62,.35),5.0:(.24,.46,.58,.24),5.5:(.23,.38,.59,.32),6.0:(.15,.22,.62,.50),6.5:(.08,.15,.64,.58),7.0:(.06,.15,.68,.59),
       7.5:(.10,.38,.88,.62),8.0:(.06,.40,.94,.60),8.5:(.06,.40,.94,.60),9.0:(.06,.42,.94,.58),9.5:(.06,.42,.94,.58),10.0:(.06,.42,.92,.58)}
    C={2.0:(.18,.69,.60,.20),2.5:(.27,.68,.53,.21),3.0:(.28,.69,.50,.18),3.5:(.28,.73,.50,.14),4.0:(.27,.71,.52,.16),4.5:(.27,.70,.54,.16),5.0:(.26,.70,.52,.16),
       5.5:(.26,.70,.54,.16),6.0:(.25,.72,.51,.16),6.5:(.24,.73,.52,.16),7.0:(.24,.74,.52,.16)}
    c={"mediaId":226,"level":"B","keyWord":"despair","defaultVoice":"male",
    "taps":[tap("to play the accordion","the musician","male",M),tap("to crouch on the tiled floor","the musician","male",M),tap("to lie open and empty","the case","male",C)],
    "stillS":6.5,
    "nouns":[noun("an accordion",.50,.42,"male"),noun("graffiti",.86,.31,"male"),noun("a case",.50,.82,"male"),noun("a noticeboard",.20,.18,"male")],
    "question":"What is the musician playing?","answer":["He","is","playing","the","accordion."],"answerVoice":"male",
    "notes":"Only two usable targets (musician, his instrument case); passers-by are blurred and several, so none is a target. Musician crouches at 4.5-5.5; at 7.5-10.0 he sits slumped on the floor. Case visible 2.0-7.0, right under his feet (split along his shoe line; at 5.0 his arm reaches across the case). 'despair' is not a visible noun. Still 6.5 has slight motion blur."}
if vid=='227':
    J={0.0:(0,0,.40,.70),0.5:(0,0,.41,.74),1.0:(0,0,.42,.86),1.5:(0,0,.42,.92),2.0:(0,0,.38,.82),2.5:(0,0,.38,.86),3.0:(0,0,.40,1),3.5:(0,0,.42,1),4.0:(0,0,.46,.93),
       4.5:(0,0,.49,.94),5.0:(0,0,.52,.96),5.5:(0,0,.55,.96),6.0:(0,0,.66,.70),6.5:(0,.15,.41,.48),7.0:(0,.15,.42,.50),7.5:(0,.15,.44,.52),8.0:(0,.15,.44,.50),
       8.5:(0,.17,.44,.69),9.0:(0,.24,.39,.67),9.5:(0,.35,.39,.49),10.0:(0,.40,.41,.44)}
    R={0.0:(.42,0,.58,.44),0.5:(.42,0,.58,.46),1.0:(.43,0,.57,.62),1.5:(.44,0,.56,.70),2.0:(.40,0,.60,.70),2.5:(.40,0,.60,.72),3.0:(.42,0,.58,.86),3.5:(.44,0,.56,.86),
       4.0:(.48,0,.52,.78),4.5:(.51,0,.49,.80),5.0:(.54,.05,.46,.86),5.5:(.57,.03,.43,.88),6.0:(.68,0,.32,.62),6.5:(.45,0,.55,.50),7.0:(.45,0,.55,.57),7.5:(.45,0,.55,.37),
       8.0:(.45,0,.55,.32),8.5:(.46,0,.54,.50),9.0:(.41,0,.59,.68),9.5:(.40,0,.60,.57),10.0:(.43,0,.57,.56)}
    K={6.5:(.20,0,.24,.14),7.0:(.20,0,.24,.14),7.5:(.20,0,.24,.14),8.0:(.20,0,.24,.14),8.5:(.19,0,.24,.16),9.0:(.14,.07,.25,.16),9.5:(.12,.18,.26,.16),10.0:(.09,.25,.32,.14)}
    c={"mediaId":227,"level":"B","keyWord":"diamond","defaultVoice":"female",
    "taps":[tap("to hold a magnifying glass","the woman in gloves","female",J),tap("to gasp in amazement","the red-haired woman","female",R),tap("to rest on the windowsill","the cat","female",K)],
    "stillS":8.5,
    "nouns":[noun("a diamond",.52,.48,"female"),noun("a cushion",.72,.63,"female"),noun("a cat",.30,.09,"female"),noun("a chain",.70,.85,"female")],
    "question":"What is the red-haired woman staring at?","answer":["She","is","staring","at","a","sparkling","diamond."],"answerVoice":"female",
    "notes":"Jeweller = the dark-haired woman in white gloves (left), customer = red-haired woman (right); they sit close, boxes split along a vertical line between them. From 6.5 the jeweller is mostly torso + gloved hand; her fingertip reaches under the customer at 7.5-8.0 (customer box shortened there). Grey cat in the background from 6.5 (small, top of the picture, windowsill clear at 9.0-10.0). Magnifying glass is held 0.0-6.0. Still 8.5: the diamond is the stone on the ring; 'a chain' = the silver chain on the green mat (could also be called a necklace)."}
json.dump(c,open(f'content/{vid}.json','w'),indent=1)
