import json
def K(times, f):
    out=[]
    for t in times:
        b=f(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def T(n,step=0.5): return [round(i*step,1) for i in range(n)]
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4011
t=T(27)
pup=K(t,lambda x:(.32,.32,.47,.29) if x<7 else (.22,.34,.63,.31))
pan=K(t,lambda x:(.25,.66,.50,.30) if x<7 else None)
pen=K(t,lambda x:None if x<7 else (.19,.66,.64,.26))
save({"mediaId":4011,"level":"A","keyWord":"audience","defaultVoice":"male",
 "taps":[{"phrase":"to play the guitar","target":"the puppy","voice":"male","keys":pup},
         {"phrase":"to sit close together","target":"the small pandas","voice":"male","keys":pan},
         {"phrase":"to stand in a row","target":"the small penguins","voice":"male","keys":pen}],
 "stillS":2.0,
 "nouns":[{"word":"a puppy","x":.50,"y":.39,"voice":"male"},{"word":"a guitar","x":.50,"y":.53,"voice":"male"},
          {"word":"a log","x":.50,"y":.63,"voice":"male"},{"word":"bamboo","x":.16,"y":.20,"voice":"male"}],
 "question":"What is the puppy doing?",
 "answer":["It","is","playing","the","guitar","for","an","audience."],
 "answerVoice":"male",
 "notes":"Cut at 7.0 s (pandas -> penguins). Key word 'audience' is used in the answer only, not as a noun slot: the listeners are spread all round the picture, no single clear place. The big pandas also sit, but apart; 'close together' fits only the two small ones. The big penguins stand left and right of the rock, only the three chicks stand in a row. Puppy and guitar pills are 0.14 apart in y on the same animal."})

# ---------- 4013
t=T(25)
def boots(x):
    if x<=2.5: return (.28,.74,.52,.26)
    if x<=3.5: return (.26,.84,.52,.16)
def berg(x):
    w={4.0:.80,4.5:.83,5.0:.86,5.5:.88,6.0:.93,6.5:.96,7.0:1.0,7.5:1.0}.get(x)
    return (0,.15,w,.40) if w else None
mt=lambda x:(0,.20,1.0,.23) if x>=8 else None
save({"mediaId":4013,"level":"B","keyWord":"deck","defaultVoice":"male",
 "taps":[{"phrase":"to rest on a wooden beam","target":"the boots","voice":"male","keys":K(t,boots)},
         {"phrase":"to tower over the ship","target":"the iceberg","voice":"male","keys":K(t,berg)},
         {"phrase":"to rise on the horizon","target":"the mountains","voice":"male","keys":K(t,mt)}],
 "stillS":2.0,
 "nouns":[{"word":"a deck","x":.46,"y":.64,"voice":"male"},{"word":"boots","x":.52,"y":.88,"voice":"male"},
          {"word":"a sail","x":.26,"y":.10,"voice":"male"},{"word":"ice","x":.10,"y":.72,"voice":"male"}],
 "question":"Where are the boots resting?",
 "answer":["They","are","resting","on","a","beam","above","the","deck."],
 "answerVoice":"male",
 "notes":"Three shots: 0-3.5 view straight down from the rigging (boots on a varnished spar, deck far below), 4.0-7.5 iceberg behind the rail, 8.0-12.0 mountains over the bowsprit. No person visible except the boots; defaultVoice from evenId=false. 'beam' is used for the spar the boots stand on (the exact sailing term would be 'yard'). The deck is the narrow strip of planks seen from above between the rails; the pill sits on its left half. 'ice' sits on the big floe at the left edge; small floes are scattered elsewhere. Several furled sails are visible, the pill is on the large one top left."})

# ---------- 4014
t=T(29)
M={0.0:(.49,.37,.18,.21),0.5:(.49,.38,.18,.22),1.0:(.48,.38,.18,.26),1.5:(.46,.34,.19,.32),2.0:(.45,.27,.21,.41),
 2.5:(.32,.17,.47,.50),3.0:(.25,.25,.47,.36),3.5:(.25,.25,.42,.38),4.0:(.29,.20,.37,.39),4.5:(.34,.21,.36,.38),
 5.0:(.38,.23,.31,.36),5.5:(.38,.23,.31,.37),6.0:(.36,.13,.34,.40),6.5:(.35,.12,.36,.39),7.0:(.36,.12,.34,.40),
 7.5:(.34,.12,.34,.39),8.0:(.31,.12,.35,.38),8.5:(.32,.12,.35,.38),9.0:(.37,.19,.28,.52),9.5:(.40,.19,.28,.49),
 10.0:(.40,.22,.23,.42),10.5:(.38,.25,.19,.37),11.0:(.35,.30,.18,.32),11.5:(.33,.30,.18,.29),12.0:(.36,.31,.18,.28),
 12.5:(.36,.33,.18,.24),13.0:(.36,.34,.18,.22),13.5:(.37,.33,.18,.21),14.0:(.38,.34,.18,.20)}
S={0.0:(.30,.43,.18,.15),0.5:(.30,.44,.18,.16),1.0:(.29,.45,.18,.20),1.5:(.27,.44,.18,.22),2.0:(.24,.44,.20,.27),
 2.5:(.57,.68,.35,.29),3.0:(.53,.62,.30,.33),3.5:(.50,.64,.27,.31),4.0:(.50,.60,.25,.21),4.5:(.53,.60,.25,.21),
 5.0:(.57,.60,.24,.20),5.5:(.57,.61,.25,.20),6.0:(.55,.54,.25,.22),6.5:(.55,.52,.18,.16),7.0:(.54,.53,.18,.15),
 7.5:(.54,.52,.18,.15),8.0:(.50,.51,.18,.16),8.5:(.53,.51,.18,.16),9.0:(.66,.40,.19,.28),9.5:(.69,.40,.19,.27),
 10.0:(.64,.41,.19,.24),10.5:(.58,.41,.18,.21),11.0:(.54,.44,.18,.18),11.5:(.52,.43,.18,.18),12.0:(.55,.42,.18,.17),
 12.5:(.55,.42,.18,.16),13.0:(.55,.40,.18,.16),13.5:(.56,.40,.18,.15),14.0:(.57,.40,.18,.14)}
mk=K(t,lambda x:M[x]); sk=K(t,lambda x:S[x])
save({"mediaId":4014,"level":"B","keyWord":"roll","defaultVoice":"male",
 "taps":[{"phrase":"to glide on a skateboard","target":"the man","voice":"male","keys":mk},
         {"phrase":"to push off with one foot","target":"the man","voice":"male","keys":mk},
         {"phrase":"to roll alongside the skateboard","target":"the suitcase","voice":"male","keys":sk}],
 "stillS":10.0,
 "nouns":[{"word":"the sun","x":.17,"y":.18,"voice":"male"},{"word":"a cloud","x":.65,"y":.15,"voice":"male"},
          {"word":"a backpack","x":.55,"y":.35,"voice":"male"},{"word":"a suitcase","x":.71,"y":.56,"voice":"male"}],
 "question":"What is the young man doing?",
 "answer":["He","is","rolling","a","suitcase","alongside","his","skateboard."],
 "answerVoice":"male",
 "notes":"Four shots: 0-2.0 car park (man comes towards the camera, suitcase on HIS right = picture left), 2.5-5.5 glazed walkway from behind, 6.0 cross-dissolve, 6.5-8.5 travelator (suitcase mostly hidden behind his legs, only a dark strip to the right of them), 9.0-14.0 roof deck. Man and suitcase overlap in most frames: from 2.5 to 8.5 the man's box is cut off at the top of the suitcase body, so his lower legs fall outside his box and the suitcase handle falls outside the suitcase box; from 9.0 the two are split by a vertical line. Only two targets (man, suitcase): the skateboard is too small and under his feet, the sun is doubtful on the travelator (reflections). He pushes off with one foot at 0-1.0, 3.0-3.5 and 9.0-9.5."})

# ---------- 4016
C={0.0:(0,0,.85,.57),0.5:(0,0,.87,.59),1.0:(0,0,.87,.59),1.5:(0,0,.87,.60),2.0:(0,0,.85,.50),2.5:(0,0,.83,.44),
 3.0:(0,0,.82,.44),3.5:(0,0,.83,.44),4.0:(0,0,.85,.45),4.5:(0,0,.83,.47),5.0:(0,0,.87,.54),5.5:(.02,0,.86,.54),
 6.0:(0,0,.90,.51),6.5:(0,0,.91,.53),7.0:(.05,0,.86,.50),7.5:(.08,0,.84,.51),8.0:(.06,0,.86,.59),8.5:(.08,0,.86,.60),
 9.0:(.10,.02,.82,.64),9.5:(.09,.01,.85,.51),10.0:(.08,.03,.84,.45),10.5:(.13,.05,.83,.47),11.0:(.06,.04,.85,.54),
 11.5:(0,.04,1.0,.56),12.0:(0,.07,1.0,.55),12.5:(.15,.06,.85,.56),13.0:(.33,.03,.67,.57),13.5:(.66,.07,.34,.43),14.0:None}
Y={0.0:(.40,.58,.34,.18),0.5:(.40,.60,.34,.17),1.0:(.40,.60,.34,.17),1.5:(.40,.61,.34,.16),2.0:(.40,.59,.34,.19),
 2.5:(.40,.60,.34,.19),3.0:(.40,.61,.34,.19),3.5:(.40,.60,.34,.19),4.0:(.40,.59,.32,.20),4.5:(.40,.59,.32,.20),
 5.0:(.40,.60,.32,.21),5.5:(.40,.60,.32,.21),6.0:(.38,.59,.30,.21),6.5:(.38,.58,.30,.21),7.0:(.38,.57,.30,.21),
 7.5:(.38,.58,.30,.21),8.0:(.38,.60,.30,.20),8.5:(.38,.61,.30,.20),9.0:(.40,.73,.24,.15),9.5:(.40,.75,.24,.15),
 10.0:(.38,.79,.24,.15),10.5:(.40,.84,.24,.15),11.0:(.44,.86,.24,.14)}
t=T(29)
ck=K(t,lambda x:C[x]); yk=K(t,lambda x:Y.get(x))
save({"mediaId":4016,"level":"A","keyWord":"bath","defaultVoice":"female",
 "taps":[{"phrase":"to touch the water","target":"the cat","voice":"female","keys":ck},
         {"phrase":"to sit on the bath","target":"the cat","voice":"female","keys":ck},
         {"phrase":"to float on the water","target":"the toys","voice":"female","keys":yk}],
 "stillS":4.0,
 "nouns":[{"word":"a cat","x":.30,"y":.15,"voice":"female"},{"word":"a wall","x":.80,"y":.08,"voice":"female"},
          {"word":"a bath","x":.75,"y":.46,"voice":"female"},{"word":"toys","x":.52,"y":.68,"voice":"female"}],
 "question":"What is the cat doing?",
 "answer":["It","is","touching","the","water","in","the","bath."],
 "answerVoice":"female",
 "notes":"One shot; the camera pans away at the end (cat gone at 14.0, toys out of frame from 11.5). The two small dark things on the water are called 'toys' after the packet description; they look like little turtles and do not move by themselves. From 9.0 only the bigger one is visible. The cat's paw touches the water at 0.5-1.5 and 8.5-9.0; there the cat box ends just above the toys box. 'a bath' sits on the white inner wall of the bath above the water line, 'toys' between the two toys; 'water' is not a noun slot because it would compete with 'a bath'."})
