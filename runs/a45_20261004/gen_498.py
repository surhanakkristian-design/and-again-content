import json
OFF=None
def keys(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
T21=[i*0.5 for i in range(21)]; T15=[i*0.5 for i in range(15)]
def tap(p,tg,v,k): return {"phrase":p,"target":tg,"voice":v,"keys":k}
def noun(w,x,y,v): return {"word":w,"x":x,"y":y,"voice":v}
def save(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 498
C=[0,.02,1.0,.98]
man=keys(T21,[[.45,.10,.55,.90],[.29,.19,.71,.81],[.33,.20,.67,.80],[.45,.17,.55,.83],[.31,.12,.69,.88],
 C,C,C,C,C,C,C,C,
 [.37,.12,.63,.88],[.39,.15,.61,.85],[.36,.17,.64,.83],[.21,.27,.79,.73],[.31,.17,.69,.83],[.25,.20,.72,.80],[.12,.20,.83,.80],[.12,.22,.80,.78]])
wom=keys(T21,[[0,.27,.24,.70],[0,.29,.26,.60],[0,.31,.24,.66],[0,.30,.24,.55],[0,.30,.20,.55],
 OFF,OFF,OFF,OFF,OFF,OFF,OFF,OFF,
 [0,.29,.36,.65],[0,.30,.38,.55],[0,.30,.26,.62],[0,.29,.19,.65],[0,.45,.20,.42],OFF,OFF,OFF])
save({"mediaId":498,"level":"A","keyWord":"nervous","defaultVoice":"male",
 "taps":[tap("to drink some water","the man","male",man),
         tap("to point at the stage","the woman","female",wom),
         tap("to carry a guitar","the man","male",man)],
 "stillS":10.0,
 "nouns":[noun("lights",.50,.07,"male"),noun("people",.25,.45,"male"),noun("a man",.45,.59,"male"),noun("a guitar",.72,.72,"male")],
 "question":"Who is nervous?",
 "answer":["The","man","with","the","guitar","is","nervous."],
 "answerVoice":"male",
 "notes":"Two targets only (musician, stage manager); the crowd is visible only in the last two frames. The man's box does not include the guitar neck where it reaches towards the woman. 'a man' pill sits on his back, 'a guitar' on the guitar body at his right hip - same figure but clearly different places."})

# 499
W=[[.05,.05,.65,.93],[0,.12,1,.86],[0,.10,1,.88],[0,.10,1,.88],[0,.10,1,.75],[0,.07,1,.75],
 [0,.05,.60,.87],[0,.05,.77,.87],[0,.09,.66,.82],[0,.09,.60,.80],[0,.13,.60,.87],[0,.11,.57,.89],[0,.17,.60,.76],
 [0,.05,.72,.82],[0,0,.58,.95],[0,0,.66,.80],[0,0,.67,.98],[0,0,.54,.98],[0,0,.58,.90],[0,0,.45,.80],OFF]
M=[[.71,.42,.29,.38],OFF,OFF,OFF,OFF,OFF,
 [.61,.20,.39,.72],[.78,.22,.22,.70],[.67,.15,.33,.75],[.61,.12,.39,.82],[.61,.15,.39,.85],[.58,.14,.42,.86],[.61,.12,.39,.82],
 [.73,.08,.27,.80],[.59,.03,.41,.92],[.67,.18,.33,.64],[.68,.20,.32,.78],[.57,.03,.43,.95],[.59,0,.41,1.0],[.57,0,.43,1.0],OFF]
w=keys(T21,W); m=keys(T21,M)
save({"mediaId":499,"level":"A","keyWord":"newspaper","defaultVoice":"female",
 "taps":[tap("to hide behind a newspaper","the woman","female",w),
         tap("to wear a green shirt","the man","male",m),
         tap("to fold the newspaper","the woman","female",w)],
 "stillS":1.5,
 "nouns":[noun("a newspaper",.50,.40,"female"),noun("coffee",.78,.74,"female"),noun("a croissant",.22,.82,"female"),noun("a table",.55,.93,"female")],
 "question":"What is the woman hiding behind?",
 "answer":["She","is","hiding","behind","a","big","newspaper."],
 "answerVoice":"female",
 "notes":"The woman's box includes the newspaper she holds. The man is 'off' from 0.5 to 2.5 s (only a sliver of his shirt shows behind the paper). His shirt is teal / blue-green; 'green shirt' is the simple A-level word, verifier may prefer another phrase. Two glasses of coffee at the still: the 'coffee' pill sits on the dark one, no other noun names the second glass. Last frame (10.0) shows only the table and pigeons: both targets off."})

# 500
P=[[.24,.09,.58,.68],[.21,.12,.50,.63],[.28,.25,.45,.56],[.20,.24,.34,.50],[.21,.27,.31,.42],[.24,.27,.47,.41],
 [.13,.27,.37,.42],[.18,.28,.36,.38],[.26,.30,.32,.28],[.31,.27,.26,.27],[.36,.30,.22,.24],[.34,.31,.22,.23],[.38,.32,.22,.23],[.38,.33,.25,.23],[.38,.36,.25,.20]]
D=[OFF,OFF,OFF,[.55,.28,.20,.34],[.53,.28,.20,.23],OFF,[.51,.30,.25,.24],[.68,.28,.32,.54],OFF,OFF,OFF,OFF,OFF,OFF,OFF]
p=keys(T15,P); d=keys(T15,D)
save({"mediaId":500,"level":"B","keyWord":"dribble","defaultVoice":"male",
 "taps":[tap("to dribble past the defender","the player in the hoodie","male",p),
         tap("to block the attacker's path","the defender","male",d),
         tap("to sprint towards the goal","the player in the hoodie","male",p)],
 "stillS":3.5,
 "nouns":[noun("a floodlight",.37,.14,"male"),noun("a goal",.74,.33,"male"),noun("a defender",.84,.48,"male"),noun("a football",.34,.53,"male")],
 "question":"What is the attacker doing?",
 "answer":["He","is","dribbling","past","the","defender."],
 "answerVoice":"male",
 "notes":"The defender (teal kit) is largely hidden behind the attacker until 3.0 s; he is boxed at 1.5, 2.0, 3.0 and 3.5 s only, split along the line between the two bodies (at 2.0 and 3.0 s the attacker's trailing right leg falls outside his own box). The ball always lies inside the attacker's box, so it is not a target. 'a football' pill sits on the ball at the attacker's feet."})

# 501
W=[[.32,.35,.18,.33],[.33,.37,.18,.34],[.36,.41,.18,.34],[.34,.51,.21,.38],[.29,.64,.21,.36],[.18,.78,.26,.22],[.27,.86,.22,.14],[.27,.86,.20,.14],
 [.16,.78,.28,.22],[0,.68,.43,.32],[.06,.56,.45,.44],[.09,.48,.50,.52],[.14,.39,.53,.60],[0,.34,.58,.66],[0,.32,.48,.68],[0,.29,.48,.71],[0,.29,.48,.71],OFF,OFF,OFF,OFF]
M=[[.51,.34,.19,.34],[.52,.35,.19,.36],[.55,.38,.20,.37],[.56,.46,.23,.43],[.51,.59,.26,.41],[.45,.71,.34,.29],[.50,.82,.33,.18],[.49,.79,.36,.21],
 [.45,.70,.44,.30],[.44,.59,.48,.41],[.52,.46,.48,.54],[.61,.37,.39,.63],[.68,.31,.32,.69],[.66,.22,.34,.78],[.68,.14,.32,.86],[.76,.06,.24,.94],[.82,0,.18,.50],
 [.29,.39,.24,.33],[.32,.41,.24,.28],[.39,.43,.23,.27],[.43,.41,.23,.28]]
Cc=[[0,.47,.18,.18],[.02,.49,.19,.18],[.10,.53,.20,.18],[.14,.66,.19,.20],[.10,.83,.18,.17]]+[OFF]*12+[[.06,.54,.20,.18],[.08,.55,.21,.19],[.13,.59,.20,.18],[.14,.58,.20,.17]]
save({"mediaId":501,"level":"A","keyWord":"night","defaultVoice":"male",
 "taps":[tap("to open the blue door","the woman","female",keys(T21,W)),
         tap("to smile at the woman","the man","male",keys(T21,M)),
         tap("to walk on four legs","the cat","male",keys(T21,Cc))],
 "stillS":10.0,
 "nouns":[noun("the moon",.62,.11,"male"),noun("a man",.54,.53,"male"),noun("a cat",.24,.66,"male")],
 "question":"What is the man doing?",
 "answer":["He","is","walking","down","the","street","at night."],
 "answerVoice":"male",
 "notes":"Couple = mixed pair, evenId false -> defaultVoice male. The couple walk close together at the start: boxes split on the line between them. The cat is out of frame from 2.5 to 8.0 s. Only 3 nouns: two street lamps are visible at the still, so 'a lamp' was left out; the key word 'night' is not a placeable thing and appears in the answer instead. The moon is small at the still (x .62, y .11)."})
