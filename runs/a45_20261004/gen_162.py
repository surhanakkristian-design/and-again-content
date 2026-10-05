import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T21=[i*0.5 for i in range(21)]
T17=[i*0.5 for i in range(17)]
def dump(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 162
man={t:(0,0,1,1) for t in (3.5,4.0,4.5,5.0,5.5,6.0)}
man.update({9.0:(.63,0,.37,1),9.5:(.64,0,.36,1),10.0:(.64,0,.36,1)})
woman={9.0:(0,.07,.37,.93),9.5:(0,.07,.35,.93),10.0:(0,.08,.36,.92)}
dog={9.0:(.37,.62,.26,.38),9.5:(.35,.60,.28,.40),10.0:(.36,.57,.27,.38)}
dump({"mediaId":162,"level":"A","keyWord":"chocolate","defaultVoice":"male",
 "taps":[
  {"phrase":"to point at his mouth","target":"the man","voice":"male","keys":K(T21,man)},
  {"phrase":"to have long hair","target":"the woman","voice":"female","keys":K(T21,woman)},
  {"phrase":"to stand between two people","target":"the dog","voice":"male","keys":K(T21,dog)}],
 "stillS":6.5,
 "nouns":[{"word":"a window","x":.25,"y":.15,"voice":"male"},
          {"word":"a spoon","x":.75,"y":.07,"voice":"male"},
          {"word":"chocolate","x":.35,"y":.50,"voice":"male"},
          {"word":"a pot","x":.50,"y":.74,"voice":"male"}],
 "question":"What is the man eating?",
 "answer":["He","is","eating","a","piece","of","chocolate."],
 "answerVoice":"male",
 "notes":"Man = off at 0-3.0 and 6.5-8.5 (only hands / a sleeve are visible). Woman and dog are visible only in the last shot (9.0-10.0 s), a short tap window. In that shot the three boxes are columns split between the figures, so each person's hand holding the strawberry (it reaches towards the dog's column) is partly outside its box. 'to have long hair' is a state: the woman's only action (eating a strawberry) is also done by the man. Spoon pill sits on the handle; the spoon bowl is covered in chocolate."})

# ---------- 164
man={0.0:(0,0,1,.46),0.5:(0,0,1,.48),1.0:(0,0,1,.55),1.5:(0,0,1,.58),2.0:(0,0,1,.58),
 2.5:(0,.25,.24,.42),3.0:(0,.56,.37,.26),3.5:(0,.56,.23,.30),4.0:(0,.48,.23,.28),4.5:(0,.48,.24,.29),
 5.0:(0,.56,.29,.29),5.5:(0,.57,.28,.28),6.0:(0,0,.58,.50),6.5:(0,0,.62,.49),7.0:(0,0,.72,.61),
 7.5:(0,0,.68,.70),8.0:(0,0,.62,.67),8.5:(0,0,.82,.61),9.0:(0,0,.62,.70),9.5:(0,0,.56,.70),10.0:(0,0,.45,.74)}
woman={3.0:(.38,.05,.62,.80),3.5:(.24,.05,.76,.80),4.0:(.24,.05,.76,.72),4.5:(.26,.05,.74,.72),
 5.0:(.31,.05,.69,.80),5.5:(.29,.05,.71,.83)}
st={0.0:(.12,.47,.83,.36),0.5:(.10,.49,.84,.34),1.0:(.05,.56,.85,.40),1.5:(.07,.59,.85,.38),2.0:(.04,.59,.80,.35),
 2.5:(0,.67,.66,.33),3.0:(0,.84,.36,.16),3.5:(0,.86,.27,.14),4.0:(0,.78,.28,.22),4.5:(0,.79,.28,.21),
 5.0:(0,.86,.30,.14),5.5:(0,.86,.28,.14),6.0:(.09,.51,.78,.32),6.5:(.13,.50,.80,.33),7.0:(.16,.62,.78,.33),
 7.5:(.11,.71,.78,.29),8.0:(.10,.68,.79,.32),8.5:(.16,.62,.78,.31),9.0:(.17,.71,.80,.29),9.5:(.11,.71,.78,.29),10.0:(.10,.75,.76,.25)}
dump({"mediaId":164,"level":"B","keyWord":"dumpling","defaultVoice":"male",
 "taps":[
  {"phrase":"to devour a whole dumpling","target":"the man","voice":"male","keys":K(T21,man)},
  {"phrase":"to demonstrate the chopstick grip","target":"the woman","voice":"female","keys":K(T21,woman)},
  {"phrase":"to contain steamed dumplings","target":"the open steamer","voice":"male","keys":K(T21,st)}],
 "stillS":4.5,
 "nouns":[{"word":"a lantern","x":.50,"y":.06,"voice":"male"},
          {"word":"chopsticks","x":.42,"y":.53,"voice":"male"},
          {"word":"a bowl","x":.55,"y":.88,"voice":"male"},
          {"word":"a dumpling","x":.13,"y":.87,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","devouring","a","whole","dumpling."],
 "answerVoice":"male",
 "notes":"0-2.0: both hands with one chopstick each are taken as the man's (white shirt, his face at the top left). 2.5-5.5: only the man's shirt / left hand is visible, small box. 6.0-8.0 the hand with chopsticks at the right edge is the woman's (dark sleeve): woman = off there (only a hand), and that hand is outside the man's box. 2.5: woman's reaching hand not boxed (off). 'the open steamer' = the front basket with dumplings, not the closed stack behind; at 9.5-10.0 the clip shows noodles rising from it (generation artefact). 'to contain' is a state. Several lanterns are visible; the pill sits on the big one at the top."})

# ---------- 165
girl={0.0:(0,.04,.53,.75),0.5:(.02,.07,.56,.90),1.0:(0,.35,.52,.52),1.5:(0,.37,.52,.53),2.0:(.02,.43,.50,.44),2.5:(.02,.47,.50,.42),
 3.0:(.52,.57,.40,.41),3.5:(.52,.57,.40,.41),4.0:(.53,.57,.42,.41),4.5:(0,.14,.42,.86),5.0:(0,.24,.44,.76),5.5:(0,.17,.44,.83),
 6.0:(0,.24,.46,.76),6.5:(0,.31,.50,.69),7.0:(0,.32,.50,.68),7.5:(.50,.57,.19,.15),8.0:(.50,.58,.19,.15)}
boy={0.0:(.54,.22,.46,.60),0.5:(.59,.24,.41,.66),1.0:(.56,.29,.44,.58),1.5:(.56,.40,.44,.52),2.0:(.55,.42,.45,.44),2.5:(.55,.43,.45,.46),
 3.0:(.04,.52,.42,.46),3.5:(.02,.52,.42,.46),4.0:(.02,.52,.42,.46),4.5:(.43,.04,.57,.96),5.0:(.45,.05,.55,.95),5.5:(.45,.05,.55,.95),
 6.0:(.48,.14,.52,.86),6.5:(.51,.26,.49,.74),7.0:(.51,.32,.49,.68),7.5:(.30,.57,.19,.15),8.0:(.30,.58,.19,.15)}
rocket={3.0:(.24,.28,.24,.16),3.5:(.24,.30,.24,.16),4.0:(.24,.31,.24,.16),7.5:(.26,.26,.24,.16),8.0:(.27,.27,.24,.16)}
dump({"mediaId":165,"level":"A","keyWord":"cinema","defaultVoice":"male",
 "taps":[
  {"phrase":"to hold the popcorn","target":"the boy","voice":"male","keys":K(T17,boy)},
  {"phrase":"to wear a blue jacket","target":"the girl","voice":"female","keys":K(T17,girl)},
  {"phrase":"to fly to the stars","target":"the rocket","voice":"male","keys":K(T17,rocket)}],
 "stillS":6.5,
 "nouns":[{"word":"a girl","x":.20,"y":.48,"voice":"female"},
          {"word":"a boy","x":.82,"y":.45,"voice":"male"},
          {"word":"popcorn","x":.78,"y":.70,"voice":"male"},
          {"word":"seats","x":.32,"y":.35,"voice":"male"}],
 "question":"Where are the girl and the boy?",
 "answer":["They","are","at","the","cinema."],
 "answerVoice":"male",
 "notes":"Back views (3.0-4.0, 7.5-8.0): the boy (curly hair, yellow hoodie) is on the LEFT, the girl (braided bun, blue jacket) on the right; at 7.5-8.0 both are tiny (minimum-size boxes side by side). 'to wear a blue jacket' is a state: no action is clearly the girl's alone. In the close-ups (4.5-5.5) the popcorn bucket reaches under the girl's box. The rocket is a drawing on the screen. defaultVoice male: mixed pair, odd id."})

# ---------- 167
w={0.0:(.18,0,.82,.78),0.5:(.18,0,.82,.78),1.0:(.19,0,.81,.92),1.5:(.31,0,.69,.97),2.0:(.28,.06,.72,.86),2.5:(.31,.10,.69,.83),
 3.0:(.41,.13,.59,.84),3.5:(.17,.09,.73,.61),4.0:(.14,.13,.75,.49),4.5:(.24,.19,.65,.47),5.0:(.22,.24,.63,.56),5.5:(.22,.23,.60,.57),
 6.0:(.26,.34,.50,.66),6.5:(.23,.32,.58,.68),7.0:(.21,.33,.64,.67),7.5:(.18,.30,.71,.70),8.0:(.16,.29,.71,.71),8.5:(.11,.29,.78,.71),
 9.0:(.18,.29,.66,.71),9.5:(.18,.33,.68,.67),10.0:(.26,.35,.63,.65)}
bag={3.5:(.04,.71,.88,.29),4.0:(.04,.63,.84,.37),4.5:(.07,.67,.80,.33),5.0:(.12,.81,.74,.19),5.5:(.09,.81,.76,.19)}
dump({"mediaId":167,"level":"B","keyWord":"citizen","defaultVoice":"female",
 "taps":[
  {"phrase":"to cast her ballot","target":"the woman in the headscarf","voice":"female","keys":K(T21,w)},
  {"phrase":"to clutch her passport","target":"the woman in the headscarf","voice":"female","keys":K(T21,w)},
  {"phrase":"to fill up with litter","target":"the rubbish bag","voice":"female","keys":K(T21,bag)}],
 "stillS":7.5,
 "nouns":[{"word":"flags","x":.24,"y":.17,"voice":"female"},
          {"word":"a headscarf","x":.55,"y":.42,"voice":"female"},
          {"word":"a passport","x":.52,"y":.61,"voice":"female"},
          {"word":"a cardigan","x":.31,"y":.71,"voice":"female"}],
 "question":"What is the citizen clutching?",
 "answer":["The","citizen","is","clutching","her","passport."],
 "answerVoice":"female",
 "notes":"Two phrases share the main woman: the other people (two officials at the desk, two volunteers at the frame edges) only do things in pairs, so no phrase fits one of them alone; the flags fill both sides of the frame and cannot get a box apart from the woman. In the park shot the woman stands behind the rubbish bag: boxes split along the bag's upper edge (her legs below it are in the bag's box). The dark blue booklet is read as a passport. 'flags' pill on the left row (flags are on both sides). The answer uses the key word 'citizen' for the woman holding her passport."})
