import json
def K(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
T17=[i*0.5 for i in range(17)]
T21=[i*0.5 for i in range(21)]
def tap(p,tg,v,keys): return {"phrase":p,"target":tg,"voice":v,"keys":keys}
def save(d):
    json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 149
W={0.0:(0,0,1,.36),0.5:(0,0,1,.45),1.0:(0,0,1,.47),1.5:(0,.14,.56,.62),2.0:(.03,.18,.55,.53),2.5:(0,.18,.58,.54),
   3.0:(.03,.18,.55,.60),3.5:(.05,.18,.55,.62),4.0:(.03,.18,.48,.52),4.5:(0,.18,.40,.46),
   5.0:(0,.02,.56,.40),5.5:(0,.02,.56,.40),6.0:(0,.02,.56,.34),
   6.5:(.03,.22,.50,.42),7.0:(.03,.23,.50,.48),7.5:(.03,.23,.51,.48),8.0:(.03,.22,.49,.40)}
M={1.5:(.66,.24,.34,.59),2.0:(.62,.25,.38,.48),2.5:(.62,.25,.38,.48),3.0:(.61,.27,.39,.54),3.5:(.61,.27,.39,.54),
   4.0:(.52,.25,.48,.50),4.5:(.41,.25,.59,.50),6.5:(.54,.30,.46,.39),7.0:(.54,.31,.46,.46),7.5:(.55,.31,.45,.46),8.0:(.54,.31,.46,.37)}
D={1.5:(.62,.84,.38,.16),2.0:(.58,.73,.42,.20),2.5:(.58,.74,.42,.18),3.0:(.58,.82,.42,.18),3.5:(.58,.82,.42,.18),
   4.0:(.58,.76,.42,.20),4.5:(.58,.76,.42,.18),5.0:(0,.52,1,.48),5.5:(0,.52,1,.48),6.0:(0,.48,1,.52),
   6.5:(.20,.70,.80,.22),7.0:(.18,.78,.82,.22),7.5:(.18,.78,.82,.22),8.0:(.18,.69,.82,.25)}
save({"mediaId":149,"level":"B","keyWord":"censor","defaultVoice":"female",
 "taps":[tap("to censor a letter","the woman","female",K(T17,W)),
         tap("to clutch a straw hat","the man","male",K(T17,M)),
         tap("to stand wide open","the drawer","female",K(T17,D))],
 "stillS":8.0,
 "nouns":[{"word":"a letter","x":.36,"y":.45,"voice":"female"},{"word":"a drawer","x":.50,"y":.80,"voice":"female"},
          {"word":"a straw hat","x":.68,"y":.63,"voice":"female"},{"word":"a lampshade","x":.16,"y":.07,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","censoring","the","man's","letter."],"answerVoice":"female",
 "notes":"Close-ups 0.0-1.0 and 5.0-6.0 show only the woman's hand: boxed as the woman. Third target is a thing (the open drawer) to get three targets; in the last shot (6.5-8.0) two drawers are open (the big one in front, a small one under the hat): the drawer box covers both, so the man's legs lie inside it."})

# ---------- 150
M={0.0:(.05,.40,.85,.42),0.5:(.03,.12,.80,.50),1.0:(0,0,.74,.40),1.5:(.43,.14,.45,.40),2.0:(.08,0,.80,.66),2.5:(.14,.03,.68,.63),
   3.0:(.13,.16,.66,.60),3.5:(.12,.14,.67,.64),4.0:(0,.20,.70,.52),4.5:(0,.46,.26,.24),5.0:(0,.30,.66,.54),5.5:(.10,.15,.60,.60),
   6.0:(0,.10,.66,.50),6.5:(0,.08,.66,.60),7.0:(0,0,.61,.62),7.5:(.08,0,.64,.52),8.0:(0,.02,.63,.64),8.5:(0,.24,.56,.46),
   9.0:(0,.25,.57,.62),9.5:(0,.27,.57,.60),10.0:(0,.15,.56,.47)}
W={1.0:(.77,.03,.23,.40),3.0:(.80,.43,.20,.34),3.5:(.80,.42,.20,.35),4.0:(.71,.28,.29,.42),4.5:(.27,.25,.68,.45),5.0:(.72,.42,.28,.42),
   5.5:(.72,.22,.28,.44),6.0:(.67,.20,.33,.40),6.5:(.67,.18,.33,.42),7.0:(.62,0,.38,.62),7.5:(.73,0,.27,.48),8.0:(.64,.14,.36,.50),
   8.5:(.57,.29,.43,.40),9.0:(.58,.30,.42,.52),9.5:(.58,.29,.42,.48),10.0:(.58,.18,.42,.42)}
mk=K(T21,M)
save({"mediaId":150,"level":"A","keyWord":"cereal","defaultVoice":"male",
 "taps":[tap("to eat with a spoon","the man","male",mk),
         tap("to pour milk into a bowl","the woman","female",K(T21,W)),
         tap("to close his eyes","the man","male",mk)],
 "stillS":6.0,
 "nouns":[{"word":"cereal","x":.72,"y":.80,"voice":"male"},{"word":"a spoon","x":.22,"y":.71,"voice":"male"},
          {"word":"a bottle","x":.82,"y":.47,"voice":"male"},{"word":"a table","x":.72,"y":.93,"voice":"male"}],
 "question":"What is the man eating?",
 "answer":["He","is","eating","cereal","with","a","spoon."],"answerVoice":"male",
 "notes":"Two phrases share the man; the dog appears only in the last 1.5 s so it is not a target. A hand in the foreground (1.0-3.0, camera side) belongs to nobody identifiable and is in no box. The woman is only a sleeve/hand before 3.0 (off at 0.0, 0.5, 1.5-2.5)."})

# ---------- 151
C={0.0:(0,.13,.22,.19),0.5:(.02,.10,.27,.19),1.0:(.14,.07,.22,.20),1.5:(.40,.03,.22,.18),2.0:(.48,0,.24,.14),2.5:(.56,0,.26,.14),
   3.0:(.60,0,.28,.14),4.0:(.62,0,.28,.14),4.5:(.62,0,.28,.14),5.0:(.62,0,.28,.14),5.5:(.63,.01,.26,.14),6.0:(.62,0,.30,.15),
   6.5:(.62,0,.30,.16),7.0:(.62,.01,.28,.17),7.5:(.62,.01,.28,.17),8.0:(.60,.01,.28,.17),8.5:(.62,.01,.28,.17),9.0:(.60,.05,.28,.16),
   9.5:(.58,.06,.28,.16),10.0:(.57,.06,.28,.16)}
H={0.0:(0,.62,.34,.36),0.5:(0,.58,.37,.36),1.0:(0,.42,.36,.50),1.5:(0,.18,.39,.82),2.0:(0,.15,.29,.80),2.5:(0,.08,.32,.90),
   3.0:(0,.06,.51,.94),3.5:(0,.05,.55,.95),4.0:(0,.06,.45,.94),4.5:(0,.08,.58,.92),5.0:(0,.11,.55,.89),5.5:(0,.13,.56,.87),
   6.0:(.02,.14,.54,.86),6.5:(.03,.14,.52,.86),7.0:(.03,.17,.50,.83),7.5:(.03,.17,.44,.83),8.0:(.03,.17,.43,.83),8.5:(.01,.17,.54,.83),
   9.0:(.01,.19,.54,.81),9.5:(.01,.19,.54,.81),10.0:(.01,.19,.52,.81)}
B={0.0:(.52,.05,.48,.95),0.5:(.42,0,.58,1.0),1.0:(.37,.12,.63,.88),1.5:(.47,.23,.53,.77),2.0:(.30,.14,.70,.86),2.5:(.40,.16,.60,.80),
   3.0:(.52,.38,.48,.62),3.5:(.56,.05,.44,.95),4.0:(.46,.14,.54,.86),4.5:(.60,.22,.40,.78),5.0:(.56,.20,.44,.80),5.5:(.57,.18,.43,.82),
   6.0:(.57,.18,.43,.82),6.5:(.56,.22,.44,.78),7.0:(.55,.25,.45,.75),7.5:(.48,.25,.52,.75),8.0:(.47,.22,.53,.78),8.5:(.56,.21,.44,.79),
   9.0:(.59,.23,.41,.77),9.5:(.66,.23,.34,.77),10.0:(.66,.23,.34,.77)}
save({"mediaId":151,"level":"A","keyWord":"chain","defaultVoice":"male",
 "taps":[tap("to hold a heavy chain","the bald man","male",K(T21,B)),
         tap("to stand behind the gate","the man with the headscarf","male",K(T21,H)),
         tap("to sit on a wall","the cat","male",K(T21,C))],
 "stillS":10.0,
 "nouns":[{"word":"a chain","x":.38,"y":.63,"voice":"male"},{"word":"a cat","x":.72,"y":.14,"voice":"male"},
          {"word":"a gate","x":.22,"y":.13,"voice":"male"},{"word":"a wall","x":.70,"y":.36,"voice":"male"}],
 "question":"What are the two men doing?",
 "answer":["They","are","locking","the","gate","with","a","chain."],"answerVoice":"male",
 "notes":"0.0-3.0 the bald man is only a hand/arm with the chain close to the camera; the other man is only hands at 0.0-0.5. The cat is hidden behind the bald man's head at 3.5 (off). No handshake is visible in the frames. The bald man holds the chain only until about 7.0 (then it hangs on the gate)."})

# ---------- 152
W={0.0:(.40,0,.60,.92),0.5:(.35,.03,.65,.90),1.0:(.16,.07,.48,.85),1.5:(.17,.10,.49,.83),2.0:(.16,.12,.50,.80),2.5:(.17,.14,.50,.80),
   3.0:(.18,.15,.50,.80),3.5:(.18,.15,.49,.80),4.0:(.22,.19,.44,.73),4.5:(.24,.10,.42,.82),5.0:(.22,.10,.42,.85),5.5:(.22,.10,.42,.85),
   6.0:(.27,.18,.35,.60),6.5:(0,.18,.60,.68),7.0:(.19,.22,.81,.50),7.5:(.26,.25,.74,.70),8.0:(.30,.25,.42,.47),8.5:(.45,.22,.28,.48),
   9.0:(.26,.19,.56,.65),9.5:(.69,.20,.31,.72),10.0:(.77,.20,.18,.47)}
M={0.0:(0,.08,.18,.68),0.5:(0,.08,.18,.68),1.0:(0,.08,.15,.80),1.5:(0,.08,.16,.82),2.0:(0,0,.15,.78),2.5:(0,0,.16,.78),
   3.0:(0,0,.17,.88),3.5:(0,0,.17,.88),4.0:(0,0,.17,.80),4.5:(0,.12,.16,.68),5.0:(0,.02,.16,.88),5.5:(0,.17,.15,.73),
   6.0:(0,.18,.18,.62),7.0:(0,.06,.18,.90),7.5:(0,.06,.25,.88),8.0:(0,.06,.27,.86),8.5:(0,.06,.26,.88),9.0:(0,.10,.24,.90),
   9.5:(0,.10,.38,.82),10.0:(.28,.23,.48,.72)}
C={1.0:(.65,.27,.35,.15),1.5:(.67,.26,.33,.14),2.0:(.67,.27,.33,.14),2.5:(.68,.27,.32,.14),3.0:(.69,.27,.31,.14),3.5:(.68,.27,.32,.14),
   4.0:(.67,.28,.33,.14),4.5:(.67,.29,.33,.14),5.0:(.65,.30,.35,.14),5.5:(.65,.31,.35,.14),6.0:(.63,.31,.37,.13),6.5:(.66,.30,.34,.14),
   8.0:(.73,.36,.27,.14),8.5:(.74,.36,.26,.14),9.0:(.82,.40,.18,.14),9.5:(.51,.38,.18,.14)}
save({"mediaId":152,"level":"A","keyWord":"chair","defaultVoice":"female",
 "taps":[tap("to open her arms wide","the woman","female",K(T21,W)),
         tap("to cross his arms","the man","male",K(T21,M)),
         tap("to lie by the window","the cat","female",K(T21,C))],
 "stillS":8.5,
 "nouns":[{"word":"a chair","x":.45,"y":.62,"voice":"female"},{"word":"a cat","x":.85,"y":.44,"voice":"female"},
          {"word":"a man","x":.14,"y":.30,"voice":"male"},{"word":"a woman","x":.62,"y":.33,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","sitting","in","a","chair."],"answerVoice":"female",
 "notes":"The man is a narrow strip at the left edge until 7.0 (box narrower than the minimum so it does not touch the woman). The woman's box is cut on the right (feet, hands) where the cat lies behind her. At 10.0 the man bends in front of the woman: boxes split at x 0.76. In the last second the man starts to sit in the chair too; the question is about the woman."})
