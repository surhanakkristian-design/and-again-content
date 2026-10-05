import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(o):
    json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 4149
t=T(24)
bv={}
for x in (0,.5,1,1.5,2,2.5): bv[x]=(0,.23,1,.70)
bv.update({3.5:(.33,.26,.29,.23),4.0:(.37,.26,.21,.17),4.5:(.38,.25,.19,.15),5.0:(.38,.22,.19,.16),5.5:(.32,.13,.31,.20),
 6.0:(.11,.42,.76,.17),6.5:(.09,.20,.82,.41),7.0:(.09,.22,.82,.39),7.5:(.09,.23,.82,.38),8.0:(.09,.21,.82,.39),
 8.5:(.09,.18,.82,.42),9.0:(.04,.26,.88,.35),9.5:(.08,.26,.92,.72),10.0:(.06,.15,.88,.68),10.5:(.18,.16,.82,.66),
 11.0:(.16,.19,.82,.72),11.5:(.18,.22,.82,.72)})
rp={6.0:(0,.59,1,.36),6.5:(0,.61,1,.34),7.0:(0,.61,1,.34),7.5:(0,.61,1,.34),8.0:(0,.60,1,.35),8.5:(0,.60,1,.35),
 9.0:(0,.61,1,.34),10.5:(0,.38,.18,.20),11.5:(0,0,1,.22)}
bk=K(t,bv); rk=K(t,rp)
save({"mediaId":4149,"level":"B","keyWord":"giant","defaultVoice":"male",
 "taps":[{"phrase":"to tumble through the sky","target":"the beaver","voice":"male","keys":bk},
         {"phrase":"to open a huge eye","target":"the giant reptile","voice":"male","keys":rk},
         {"phrase":"to flee across the lake","target":"the beaver","voice":"male","keys":bk}],
 "stillS":8.5,
 "nouns":[{"word":"pine trees","x":.5,"y":.12,"voice":"male"},{"word":"a beaver","x":.5,"y":.45,"voice":"male"},
          {"word":"a giant","x":.5,"y":.65,"voice":"male"}],
 "question":"What is the beaver sitting on?",
 "answer":["It","is","sitting","on","a","giant's","head."],"answerVoice":"male",
 "notes":"Key word 'giant' = the enormous reptile; noun 'a giant' sits on its scaly head just above the opening eye. Reptile marked off at 9.5/10.0/11.0 (only blurred slivers at the edge); at 10.5 a small box at the left edge, at 11.5 the open jaws above the beaver. 'pine trees' pill is on the misty forest above the beaver."})

# 4150
t=T(25)
car={}
for x in (0,.5,1,1.5,2): car[x]=(.33,0,.67,1)
for x in (2.5,3,3.5,4): car[x]=(0,.16,1,.84)
for x in (4.5,5,5.5,6): car[x]=(0,0,1,.93)
for x in (6.5,7,7.5,8): car[x]=(.06,.35,.88,.33)
for x in (8.5,9,9.5,10): car[x]=(0,.42,1,.58)
car.update({10.5:(.08,.38,.49,.28),11.0:(.08,.38,.54,.27),11.5:(.08,.39,.57,.26),12.0:(.08,.38,.61,.28)})
man={10.5:(.57,.32,.25,.36),11.0:(.62,.33,.21,.31),11.5:(.65,.34,.21,.30),12.0:(.69,.33,.20,.31)}
ck=K(t,car); mk=K(t,man)
save({"mediaId":4150,"level":"B","keyWord":"speed","defaultVoice":"male",
 "taps":[{"phrase":"to speed along a country road","target":"the sports car","voice":"male","keys":ck},
         {"phrase":"to approach the parked car","target":"the man","voice":"male","keys":mk},
         {"phrase":"to wear a brown T-shirt","target":"the man","voice":"male","keys":mk}],
 "stillS":12.0,
 "nouns":[{"word":"the sky","x":.5,"y":.15,"voice":"male"},{"word":"a sports car","x":.33,"y":.52,"voice":"male"},
          {"word":"a man","x":.79,"y":.44,"voice":"male"},{"word":"gravel","x":.5,"y":.78,"voice":"male"}],
 "question":"What is the sports car doing?",
 "answer":["It","is","speeding","along","a","country","road."],"answerVoice":"male",
 "notes":"Only two targets (car, man); third phrase is a state of the man. In the last shot the man overlaps the car: boxes split along his left side, the car's tail right of him is given up. Ground is sand mixed with gravel; 'gravel' chosen (pebbles clear in the wheel close-up). Car is parked in the last shots, speeding in the others."})

# 4151
t=T(25)
hand={0:(.32,.02,.68,.58),.5:(.63,.02,.37,.58),1:(.52,.02,.48,.54),1.5:(.60,.05,.40,.58),2:(.61,0,.39,.60),
 2.5:(.58,0,.42,.52),3:(.70,0,.30,.60),3.5:(.72,.07,.28,.53),4:(.34,0,.66,.42),4.5:(.58,0,.42,.42),
 7:(.40,0,.60,.50),7.5:(.40,0,.60,.50),8:(.42,0,.58,.50)}
pink={0:(0,.20,.32,.75),.5:(0,.20,.63,.75),1:(0,.20,.52,.75),1.5:(0,.20,.60,.75),2:(0,.20,.61,.75),2.5:(0,.20,.58,.75),
 3:(0,.20,.70,.75),3.5:(0,.20,.72,.75),4:(0,.42,1,.55),4.5:(0,.42,1,.56),5:(0,0,1,.95),5.5:(0,.03,1,.85),6:(0,.03,1,.80),
 6.5:(0,.02,1,.96),7:(0,.10,.40,.80),7.5:(0,.10,.40,.80),8:(0,.08,.42,.82),8.5:(0,.31,1,.33),9:(0,.31,1,.33),9.5:(0,.31,1,.33),
 10:(.05,.36,.90,.27),10.5:(.04,.36,.94,.27),11:(.02,.36,.96,.28),11.5:(.02,.36,.96,.28),12:(.01,.35,.98,.29)}
blue={10:(.12,.04,.76,.24),10.5:(.12,.03,.78,.25),11:(.11,.03,.78,.24),11.5:(.11,.03,.78,.24),12:(.09,.01,.82,.25)}
save({"mediaId":4151,"level":"A","keyWord":"art","defaultVoice":"male",
 "taps":[{"phrase":"to hold a pen","target":"the hand","voice":"male","keys":K(t,hand)},
         {"phrase":"to turn pink","target":"the pink car","voice":"male","keys":K(t,pink)},
         {"phrase":"to hang on the wall","target":"the blue car","voice":"male","keys":K(t,blue)}],
 "stillS":12.0,
 "nouns":[{"word":"a blue car","x":.5,"y":.13,"voice":"male"},{"word":"a pink car","x":.5,"y":.48,"voice":"male"},
          {"word":"a table","x":.5,"y":.88,"voice":"male"}],
 "question":"What is the hand doing?",
 "answer":["It","is","drawing","a","pink","car."],"answerVoice":"male",
 "notes":"Key word 'art' is abstract, so it is not a noun slot and not in the answer. The hand box holds hand + pen; hand marked off 5.0-6.5 where only the pen (or a sliver of finger) is in the picture. In the drawing shots the pink car's box is the part of the drawing beside/below the hand (split line at the pen tip). 'to turn pink' is only 3 words. Gender of the hand unclear -> default voice by odd id."})

# 4152
t=T(17)
ramp={0:(.10,.16,.80,.45),.5:(.10,.16,.80,.45),1:(.10,.16,.80,.45),1.5:(.10,.16,.80,.45),2:(.06,.21,.88,.40),2.5:(.06,.23,.88,.38),
 3:(.05,.27,.90,.34),3.5:(.04,.31,.92,.30),4:(.03,.35,.94,.26),4.5:(.03,.40,.94,.21),5:(.02,.48,.96,.13),5.5:(.02,.52,.96,.14),
 6:(0,.55,1,.14),6.5:(0,.56,1,.14),7:(0,.56,1,.16),7.5:(0,.56,1,.20),8:(0,.56,1,.21)}
car={5:(.22,.33,.56,.15),5.5:(.22,.34,.56,.18),6:(.22,.33,.56,.22),6.5:(.22,.33,.56,.23),7:(.22,.33,.56,.23),7.5:(.22,.33,.56,.23),8:(.22,.33,.56,.23)}
trees={x:(0,0,1,.16) for x in t}
save({"mediaId":4152,"level":"B","keyWord":"vehicle","defaultVoice":"female",
 "taps":[{"phrase":"to lower onto the gravel","target":"the ramp","voice":"female","keys":K(t,ramp)},
         {"phrase":"to stand inside the trailer","target":"the sports car","voice":"female","keys":K(t,car)},
         {"phrase":"to tower above the trailer","target":"the trees","voice":"female","keys":K(t,trees)}],
 "stillS":8.0,
 "nouns":[{"word":"a trailer","x":.5,"y":.24,"voice":"female"},{"word":"a sports car","x":.5,"y":.44,"voice":"female"},
          {"word":"a ramp","x":.5,"y":.65,"voice":"female"},{"word":"gravel","x":.5,"y":.86,"voice":"female"}],
 "question":"What does the ramp reveal?",
 "answer":["The","ramp","reveals","a","vehicle","inside","the","trailer."],"answerVoice":"female",
 "notes":"The trailer itself is no tap target (its box would hold ramp and car). The ramp = the back wall from 0.0 on. Car marked off at 4.5 (only the roof line shows above the ramp). Trees box = the strip above the trailer; trees also stand at both sides. Key word 'vehicle' is used in the answer for the car; 'a trailer' pill sits on the dark inside above the car. Question in present simple (result of the clip), not continuous."})
