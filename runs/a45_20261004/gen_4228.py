import json
OFF=None
def keys(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4228
t=T(24)
man={0.0:(.09,.24,.58,.58),0.5:(.08,.20,.76,.62),1.0:(.12,.19,.44,.77),1.5:(.17,.19,.45,.80),2.0:(.15,.16,.54,.76),
     2.5:(0,.18,.72,.82),3.0:(.12,.18,.70,.82),5.0:(.20,.49,.66,.51),5.5:(.14,.51,.68,.49),6.0:(.06,.49,.86,.51),
     6.5:(.09,.49,.83,.51),7.0:(0,0,1,.40),7.5:(0,0,1,.39),8.0:(0,0,1,.31),
     10.5:(.12,.34,.80,.27),11.0:(.15,.32,.65,.31),11.5:(0,.31,1.0,.32)}
eggs={7.0:(.15,.41,.64,.27),7.5:(.13,.40,.74,.32),8.0:(.15,.32,.68,.29),8.5:(.13,.40,.85,.22),9.0:(.02,.37,.98,.29),
      9.5:(.05,.37,.95,.29),10.0:(.02,.38,.98,.29),10.5:(.37,.62,.20,.14),11.0:(.37,.64,.20,.14),11.5:(.37,.64,.20,.14)}
save({"mediaId":4228,"level":"A","keyWord":"shore","defaultVoice":"male",
 "taps":[{"phrase":"to open his arms wide","target":"the man","voice":"male","keys":keys(t,man)},
         {"phrase":"to climb into a helicopter","target":"the man","voice":"male","keys":keys(t,man)},
         {"phrase":"to cook in a pan","target":"the eggs","voice":"male","keys":keys(t,eggs)}],
 "stillS":11.0,
 "nouns":[{"word":"a mountain","x":.50,"y":.17,"voice":"male"},{"word":"a lake","x":.78,"y":.42,"voice":"male"},
          {"word":"a table","x":.46,"y":.78,"voice":"male"},{"word":"the shore","x":.84,"y":.70,"voice":"male"}],
 "question":"Where is the man eating?",
 "answer":["He","is","eating","eggs","on","the","shore."],"answerVoice":"male",
 "notes":"Last shot (10.5-11.5): the eggs on the plate sit between the man's legs, so the man's box is cut above the table (legs not covered) to avoid overlap. 7.0-8.0: the man's hands hold/crack the eggs; split by a horizontal line. 9.5/10.0: only fingertips with the fork in the corner, man set off. 'a table' pill lies on the food-covered table top. 'the shore' = the stony bank on the right."})

# ---------- 4229
t=T(21)
per={}; mon={}
for x in (0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5):
    per[x]=(0,0,.24,1.0); mon[x]=(.25,.23,.68,.58)
per[5.0]=(0,.40,.24,.60); mon[5.0]=(.25,.23,.68,.66)
per[5.5]=(0,.22,.24,.78); mon[5.5]=(.25,.23,.68,.62)
per[6.0]=(0,0,.24,1.0);  mon[6.0]=(.25,.23,.68,.56)
per[6.5]=(0,0,.26,1.0);  mon[6.5]=(.27,.23,.66,.56)
per[7.0]=(0,0,.30,1.0);  mon[7.0]=(.31,.21,.62,.68)
per[7.5]=(0,0,.26,1.0);  mon[7.5]=(.27,.36,.60,.56)
per[8.0]=(0,0,.25,1.0);  mon[8.0]=(.26,.37,.60,.48)
per[8.5]=(0,0,.21,1.0);  mon[8.5]=(.22,.40,.64,.46)
per[9.0]=(0,.06,.23,.94);mon[9.0]=(.24,.48,.72,.52)
per[9.5]=(0,.16,.24,.84);mon[9.5]=(.30,.49,.65,.50)
per[10.0]=(0,.26,.18,.14);mon[10.0]=(.74,.76,.26,.18)
save({"mediaId":4229,"level":"B","keyWord":"free","defaultVoice":"male",
 "taps":[{"phrase":"to free a frozen monkey","target":"the person","voice":"male","keys":keys(t,per)},
         {"phrase":"to sit trapped in ice","target":"the monkey","voice":"male","keys":keys(t,mon)},
         {"phrase":"to leap off the railing","target":"the monkey","voice":"male","keys":keys(t,mon)}],
 "stillS":8.0,
 "nouns":[{"word":"icicles","x":.50,"y":.39,"voice":"male"},{"word":"a monkey","x":.48,"y":.57,"voice":"male"},
          {"word":"a hammer","x":.50,"y":.79,"voice":"male"}],
 "question":"What is the person doing?",
 "answer":["The","person","is","freeing","a","frozen","monkey."],"answerVoice":"male",
 "notes":"Person's gender not clear (hat, coat, gloves): target 'the person', default voice by odd id = male. Person and monkey split by a vertical line near x 0.25; the gloves/hammer reaching over the monkey fall into the monkey's box. The lifted ice shell (8.0-10.0) belongs to no box. 9.5-10.0 the monkey jumps away, at 10.0 only a brown blur bottom right. Only 3 nouns (the two gloves are apart, the railing is under snow)."})

# ---------- 4230
t=T(25)
small={0.0:(.10,.30,.20,.22),0.5:(.07,.33,.22,.21),1.0:(.04,.34,.22,.23),1.5:(.06,.35,.23,.22),2.0:(.07,.35,.23,.22),
 2.5:(.08,.34,.23,.21),3.0:(.08,.34,.23,.23),3.5:(.08,.34,.23,.23),4.0:(.08,.33,.24,.22),4.5:(.08,.33,.24,.22),
 5.0:(.08,.34,.24,.22),5.5:(.09,.33,.24,.22),6.0:(.09,.31,.23,.23),6.5:(.09,.31,.23,.23),7.0:(.09,.31,.23,.24),
 7.5:(.09,.31,.23,.24),8.0:(.09,.30,.23,.23),8.5:(.08,.30,.23,.23),9.0:(.05,.32,.24,.24),9.5:(.36,.24,.28,.22)}
big={0.0:(.31,.17,.36,.31),0.5:(.30,.19,.38,.31),1.0:(.27,.21,.38,.31),1.5:(.30,.22,.38,.30),2.0:(.31,.21,.39,.31),
 2.5:(.32,.20,.38,.30),3.0:(.32,.21,.39,.31),3.5:(.32,.21,.38,.31),4.0:(.33,.19,.39,.32),4.5:(.33,.19,.37,.32),
 5.0:(.33,.20,.40,.31),5.5:(.34,.19,.38,.31),6.0:(.33,.18,.40,.30),6.5:(.33,.18,.40,.30),7.0:(.33,.18,.40,.31),
 7.5:(.33,.18,.40,.31),8.0:(.33,.17,.40,.31),8.5:(.32,.17,.39,.31),9.0:(.30,.18,.39,.33)}
truck={x:(0,.58,1.0,.42) for x in T(19)}
truck.update({9.5:(0,.47,1.0,.53),10.0:(0,.27,.80,.60),10.5:(0,.31,.62,.28),11.0:(.17,.36,.33,.18),11.5:(.41,.39,.24,.15),12.0:(.45,.34,.20,.14)})
save({"mediaId":4230,"level":"A","keyWord":"seat","defaultVoice":"female",
 "taps":[{"phrase":"to sit in the driver's seat","target":"the big dog","voice":"female","keys":keys(t,big)},
         {"phrase":"to wear an orange hat","target":"the small dog","voice":"female","keys":keys(t,small)},
         {"phrase":"to have a red door","target":"the truck","voice":"female","keys":keys(t,truck)}],
 "stillS":6.0,
 "nouns":[{"word":"a seat","x":.21,"y":.29,"voice":"female"},{"word":"an orange hat","x":.25,"y":.40,"voice":"female"},
          {"word":"a steering wheel","x":.66,"y":.38,"voice":"female"},{"word":"a door","x":.50,"y":.75,"voice":"female"}],
 "question":"Where is the big dog sitting?",
 "answer":["It","is","sitting","in","the","driver's","seat."],"answerVoice":"female",
 "notes":"The two dogs overlap (orange hat in front of the big dog's side): split by a vertical line, the big dog's left ear falls outside its box. Truck box in the first shot = the door below the window only. 9.5 is a blurred pan: only the orange hat is recognisable. States for the small dog and the truck: no action fits only them. 'a seat' pill = the grey seat back/headrest between the two dogs."})

# ---------- 4231
t=T(24)
left={1.5:(.12,.32,.38,.31),2.0:(.08,.30,.43,.33),2.5:(.09,.31,.43,.33),3.0:(.09,.32,.44,.32),3.5:(.09,.31,.44,.33),
 4.0:(.08,.30,.44,.34),4.5:(.08,.30,.44,.34),5.0:(.06,.31,.45,.33),5.5:(.06,.31,.45,.33),
 10.0:(0,.26,.66,.36),10.5:(.14,.28,.25,.20)}
right={2.0:(.52,.32,.26,.30),2.5:(.53,.32,.27,.32),3.0:(.54,.33,.27,.31),3.5:(.54,.33,.27,.31),4.0:(.53,.32,.27,.32),
 4.5:(.53,.32,.27,.32),5.0:(.52,.33,.28,.31),5.5:(.52,.33,.28,.31),10.0:(.67,.31,.18,.24)}
for x in (6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5):
    left[x]=(.04,.30,.47,.34); right[x]=(.52,.32,.28,.32)
truck={0.0:(0,0,1,1),0.5:(0,0,1,1),1.0:(0,0,1,1),10.0:(0,.63,1.0,.37),10.5:(.40,.20,.60,.80),11.0:(.11,.28,.89,.68),11.5:(.21,.33,.61,.29)}
for x in T(20)[3:]: truck[x]=(0,.66,1.0,.34)
save({"mediaId":4231,"level":"A","keyWord":"window","defaultVoice":"male",
 "taps":[{"phrase":"to put its paws up","target":"the dog on the left","voice":"male","keys":keys(t,left)},
         {"phrase":"to wear a red hat","target":"the dog on the right","voice":"male","keys":keys(t,right)},
         {"phrase":"to have a red door","target":"the truck","voice":"male","keys":keys(t,truck)}],
 "stillS":8.0,
 "nouns":[{"word":"a window","x":.60,"y":.28,"voice":"male"},{"word":"dogs","x":.44,"y":.53,"voice":"male"},
          {"word":"a seat","x":.85,"y":.47,"voice":"male"},{"word":"a door","x":.45,"y":.82,"voice":"male"}],
 "question":"What are the dogs doing?",
 "answer":["They","are","looking","out","of","the","window."],"answerVoice":"male",
 "notes":"0.0-1.0 the window is fogged, no dog recognisable: truck box = whole picture; from 1.5 the truck box is the door below the window. The right dog's hat is white in front with a red peak and red back (the left dog's is green-brown). Dogs split by a vertical line at x 0.52. 'a seat' = the beige seat back right of the dogs."})
