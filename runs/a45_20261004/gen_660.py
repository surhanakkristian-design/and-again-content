import json
T=[i*0.5 for i in range(21)]
def keys(rows):
    assert len(rows)==21
    out=[]
    for t,r in zip(T,rows):
        out.append({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]})
    return out
def nn(lst,dv):
    return [{"word":w,"x":x,"y":y,"voice":v or dv} for w,x,y,v in lst]
def write(i,d): json.dump(d,open(f'content/{i}.json','w'),indent=1,ensure_ascii=False)

# ---------- 660
Y=[[0,.24,.70,.36],[0,.24,.70,.36],[0,.20,.50,.42],[0,.18,.66,.52],[0,.15,.62,.61],[0,.15,.72,.61],
   [0,.12,.82,.62],[0,.12,.82,.58],[0,.18,.74,.51],[0,.17,.70,.57],[0,.12,.56,.66],[0,.15,.66,.65],
   [0,.15,.66,.65],[0,.15,.44,.62],[0,.15,.42,.62],[0,.15,.46,.62],[0,.15,.46,.62],[0,.33,.64,.42],
   [0,.33,.60,.42],[0,.33,.58,.42],[0,.30,.50,.42]]
G=[[.30,0,.70,.24],[.30,0,.70,.24],[.50,.38,.50,.24],[.66,.28,.34,.42],[.62,.36,.38,.40],[.72,.25,.28,.51],
   [.82,0,.18,.74],[.82,.05,.18,.95],[.74,.15,.26,.54],[.70,.20,.30,.54],[.56,.28,.44,.50],[.66,.28,.34,.52],
   [.66,.28,.34,.52],[.44,.28,.56,.49],[.42,.30,.58,.47],[.66,.30,.34,.47],[.68,.30,.32,.47],[.64,.10,.36,.65],
   [.70,.15,.30,.60],[.70,.22,.30,.53],[.55,.30,.45,.42]]
B=[[0,.60,1,.40],[0,.60,1,.40],[0,.62,1,.38],[0,.70,1,.30],[0,.76,1,.24],[0,.76,1,.24],
   [0,.74,.82,.26],[.03,.70,.79,.30],[.12,.69,.74,.31],[.22,.74,.73,.26],[.22,.78,.72,.22],[.25,.80,.67,.20],
   [.26,.80,.64,.20],[.22,.77,.60,.23],[.22,.77,.56,.23],[.20,.77,.58,.23],[.18,.77,.60,.23],[.20,.75,.66,.25],
   [.20,.75,.66,.25],[.20,.75,.60,.25],[.20,.72,.62,.28]]
write(660,{"mediaId":660,"level":"B","keyWord":"basin","defaultVoice":"female",
 "taps":[{"phrase":"to lather her friend's hair","target":"the woman in green","voice":"female","keys":keys(G)},
         {"phrase":"to lean over the basin","target":"the woman in yellow","voice":"female","keys":keys(Y)},
         {"phrase":"to collect the soapy water","target":"the basin","voice":"female","keys":keys(B)}],
 "stillS":10.0,
 "nouns":nn([("banana leaves",.50,.15,None),("a tap",.52,.66,None),("a basin",.50,.79,None),("a stool",.50,.93,None)],"female"),
 "question":"What is the woman in green doing?",
 "answer":["She","is","lathering","her","friend's","hair."],"answerVoice":"female",
 "notes":"The three targets overlap heavily (hair hangs into the basin, the friend's hands are in the hair), so the boxes are split along straight lines; the big foam pile is inside the yellow woman's box. 0.0-2.5 s: only arms/hands of the woman in green are visible (bottle arm, then hands from the right); the cupped hands at 0.0-1.0 s could not be attributed with certainty and lie in the yellow woman's box. In the last frame both women stand upright with thumbs up. 'to collect the soapy water' for the basin is a thing-as-subject phrase; fallback 'to stand on a wooden stool'."})

# ---------- 661
S=[[.40,.38,.26,.16],[.41,.33,.37,.27],[.40,.32,.48,.27],[.39,.30,.57,.30],[.39,.29,.61,.31],[.36,.28,.64,.34],
   [.23,.28,.77,.38],[.16,.28,.84,.38],[.13,.28,.87,.37],[.13,.26,.87,.39],[.04,.26,.96,.42],[.02,.26,.98,.46],
   [0,.28,1,.47],[0,.22,1,.60],[0,.17,1,.80],[0,.08,1,.92],[0,.20,1,.76],[0,.18,1,.75],[0,.13,1,.87],
   [0,.18,.96,.82],[0,.02,.80,.82]]
F=[[0,0,1,.38],[0,0,1,.33],[0,0,1,.32],[0,0,1,.30],[0,0,1,.29],[0,0,1,.28],[0,.05,1,.23],[0,.08,1,.20],
   [0,.08,1,.20],[0,.08,1,.18],[.05,.12,.65,.14],[.35,.12,.60,.14],[.55,.14,.45,.14]]+[None]*8
write(661,{"mediaId":661,"level":"A","keyWord":"shark","defaultVoice":"male",
 "taps":[{"phrase":"to open its big mouth","target":"the shark","voice":"male","keys":keys(S)},
         {"phrase":"to come very close","target":"the shark","voice":"male","keys":keys(S)},
         {"phrase":"to swim in a big group","target":"the small fish","voice":"male","keys":keys(F)}],
 "stillS":2.0,
 "nouns":nn([("fish",.30,.12,None),("a shark",.68,.43,None),("water",.72,.62,None),("coral",.35,.86,None)],"male"),
 "question":"What is the shark doing?",
 "answer":["The","shark","is","opening","its","big","mouth."],"answerVoice":"male",
 "notes":"Only two real targets (shark, school of fish). The fish surround the shark, so their box is the dense band of fish above the shark (0.0-6.0 s); fish to the left of and below the shark are outside it. From 6.5 s only a few tiny far-away fish remain behind the shark's back and cannot be boxed without overlapping the shark: OFF. 'coral' is slightly above A level but is the only name for the ground here; 'water' sits on the open blue area."})

# ---------- 662
W=[[0,.36,.62,.46],[0,.36,.62,.48],[0,.27,.52,.55],[0,.25,.54,.50],[0,0,.44,.84],[0,0,.50,.92],
   [0,.05,.54,.90],[0,0,.46,.90],[0,.35,.62,.29],[0,.40,.52,.30],[0,.36,.40,.31],[0,.47,.42,.30],
   [0,.43,.22,.26],[0,.63,.44,.24],[0,0,.32,1.0],[0,0,.44,1.0],[0,0,.44,1.0],[0,0,.39,.88],
   [0,.23,.50,.54],[0,.44,.38,.42],[0,.60,.28,.32]]
M=[[.66,.16,.34,.42],[.68,.16,.32,.40],[.66,.05,.34,.38],[.72,.05,.28,.38],[.82,.24,.18,.30],[.82,.44,.18,.18],
   [.82,.44,.18,.28],[.77,.28,.23,.30],[.64,0,.36,.50],[.52,0,.48,.47],[.42,0,.58,.50],[.42,0,.58,.55],
   [.36,0,.64,.56],[.46,0,.54,.62],[.64,.08,.36,.62],[.58,.43,.42,.24],[.56,.42,.44,.30],[.68,.10,.32,.50],
   [.52,0,.48,.46],[.52,0,.48,.46],[.40,0,.60,.60]]
H=[[.28,.14,.34,.22],[.28,.14,.36,.22],[.30,.07,.32,.20],[.32,.04,.36,.20],[.46,.14,.34,.22],[.52,.22,.30,.20],
   [.54,.24,.28,.18],[.47,.24,.29,.19],[.36,.14,.27,.21],[.24,.12,.28,.20],[.16,.15,.26,.20],[.10,.17,.31,.22],
   [.06,.22,.30,.20],[.14,.25,.31,.19],[.33,.25,.29,.18],[.45,.24,.29,.18],[.45,.24,.29,.17],[.40,.17,.28,.19],
   [.25,.02,.26,.20],[.20,.04,.31,.20],[.14,.19,.26,.19]]
write(662,{"mediaId":662,"level":"A","keyWord":"sharpener","defaultVoice":"female",
 "taps":[{"phrase":"to draw a star","target":"the woman","voice":"female","keys":keys(W)},
         {"phrase":"to have short hair","target":"the man","voice":"male","keys":keys(M)},
         {"phrase":"to eat grass","target":"the horse","voice":"female","keys":keys(H)}],
 "stillS":3.5,
 "nouns":nn([("a horse",.62,.34,None),("a sharpener",.62,.60,None),("a notebook",.60,.78,None),("a bowl",.22,.90,None)],"female"),
 "question":"What is the woman drawing?",
 "answer":["She","is","drawing","a","star."],"answerVoice":"female",
 "notes":"In the picture it is the WOMAN's hands (from the left) that hold pencil and sharpener at 3.5-5.5 s, against the packet description, so no phrase says who sharpens. The man: no action fits only him (both look surprised, both smile, the hand holding the shaving at 6.0-6.5 s cannot be attributed), hence the state 'to have short hair'; his head is out of frame at 0.0-3.5 s and 7.5-8.0 s (body/hand only). 'to eat grass' is 3 words. The horse stands behind the woman's hands/face in many frames: the woman's box is cut where it would cover the horse (0.0-1.5, 4.0-6.5, 9.0-10.0 s it holds her hands and pencil but not her face at the top edge; 3.0-3.5 and 7.0-8.5 s it holds face and body but not the hand/pencil tip right of x 0.45). The star is drawn only from 9.0 s."})

# ---------- 663
Bm=[[.50,.12,.50,.88],[.50,.12,.50,.88],[.52,.13,.48,.87],[.46,.11,.54,.89],[.41,.08,.59,.92],[.40,.09,.60,.91],
    [.42,.15,.58,.85],[.46,.15,.54,.85],[.50,.15,.50,.85],[.51,.14,.49,.86],[.48,.16,.52,.84],[.44,.15,.56,.85],
    [.42,.17,.58,.83],[.46,.18,.54,.82],[.48,.17,.52,.83],[.50,.18,.50,.82],[.50,.17,.50,.83],[.38,.17,.62,.83],
    [.33,.17,.67,.83],[.27,.18,.73,.82],[.17,.19,.83,.81]]
O=[[.15,.24,.34,.19],[.17,.22,.33,.14],[.16,.23,.34,.14],[.12,.25,.33,.26],[.03,.25,.37,.43],[.02,.26,.36,.32],
   [.03,.29,.38,.31],[0,.29,.44,.33],[.03,.29,.46,.36],[0,.29,.50,.38],[0,.31,.48,.42]]+[None]*10
write(663,{"mediaId":663,"level":"A","keyWord":"shaving foam","defaultVoice":"male",
 "taps":[{"phrase":"to put foam on his face","target":"the man in blue","voice":"male","keys":keys(Bm)},
         {"phrase":"to look in the mirror","target":"the man in blue","voice":"male","keys":keys(Bm)},
         {"phrase":"to watch his friend","target":"the man in orange","voice":"male","keys":keys(O)}],
 "stillS":7.0,
 "nouns":nn([("lamps",.30,.10,None),("a mirror",.20,.29,None),("shaving foam",.80,.48,None),("a tap",.38,.91,None)],"male"),
 "question":"What is the man in blue doing?",
 "answer":["He","is","putting","shaving","foam","on","his","face."],"answerVoice":"male",
 "notes":"Only two people; the man in blue has two phrases. 0.0-1.5 s his outstretched arm with the can crosses in front of the man in orange: the blue box holds his head, body and the palm with the foam, the can arm left of x 0.5 is in neither box; the orange box is the visible face (later face and shoulder). The man in orange is gone after the cut at 5.5 s (OFF). The mirror image of the man in blue (5.5-10.0 s) is not in his box. 'shaving foam' is on the real face; the reflection also shows foam. A dog is faintly visible in the mirror at 7.5-9.0 s, not used."})
