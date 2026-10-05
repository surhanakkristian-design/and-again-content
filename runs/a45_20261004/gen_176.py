import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    return out
def tap(p,tg,v,d): return {"phrase":p,"target":tg,"voice":v,"keys":keys(d)}
def write(i,o):
    json.dump(o,open(f"content/{i}.json","w"),indent=1,ensure_ascii=False)

# ---------- 176
stove={1.5:(.58,.10,.42,.50),2.0:(.52,0,.48,.85),2.5:(.52,0,.48,.90),3.0:(.52,0,.48,.95),3.5:(.56,0,.44,.95),
 4.0:(.46,0,.54,.95),4.5:(.44,0,.56,.95),5.0:(.40,0,.60,1.0),5.5:(.19,0,.81,.90),6.0:(.19,0,.81,.85),6.5:(.19,0,.81,.85),
 7.0:(.19,0,.81,.90),7.5:(.29,0,.71,.92),8.0:(.23,0,.75,.84),8.5:(.21,0,.79,.84),9.0:(.19,0,.81,.95),9.5:(.05,0,.95,.95),10.0:(.03,0,.97,.95)}
dog={0.0:(.32,0,.62,.31),0.5:(.28,0,.52,.28),1.0:(.19,.20,.33,.42),1.5:(.08,.28,.44,.46),2.0:(.05,.38,.46,.40),
 2.5:(.14,.45,.36,.14),3.0:(.14,.76,.37,.19),3.5:(.12,.79,.40,.16),4.0:(.24,.64,.21,.28),4.5:(.12,.62,.30,.30),5.0:(.05,.75,.33,.20),
 7.5:(0,.58,.27,.24),8.0:(0,.41,.22,.30),8.5:(0,.42,.20,.30),9.0:(0,.44,.18,.30)}
wom={2.5:(0,.05,.18,.39),3.0:(0,.15,.50,.60),3.5:(0,.08,.55,.70),4.0:(0,.15,.44,.48),4.5:(0,.20,.38,.41),5.0:(0,.22,.36,.52),
 5.5:(0,.20,.18,.34),6.0:(0,.10,.18,.33),6.5:(0,.12,.18,.33),7.0:(0,.22,.18,.30),7.5:(0,.17,.24,.40),8.0:(0,.10,.18,.30)}
write(176,{"mediaId":176,"level":"B","keyWord":"coal","defaultVoice":"male",
 "taps":[tap("to contain a blazing fire","the stove","male",stove),
         tap("to stick its tongue out","the dog","male",dog),
         tap("to burst out laughing","the woman","female",wom)],
 "stillS":6.0,
 "nouns":[{"word":"coal","x":.14,"y":.90,"voice":"male"},{"word":"a stove","x":.60,"y":.38,"voice":"male"},
          {"word":"a window","x":.25,"y":.08,"voice":"male"},{"word":"a sleeve","x":.80,"y":.64,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","putting","coal","into","the","stove."],"answerVoice":"male",
 "notes":"Clip differs from the description: a dog sits by the stove; the coal is first held by the camera person's hand (dark sleeve), the man in the green sweater shows a sooty palm and feeds the stove at 5.5-7.0 s. The man is not a tap target (his hand overlaps the stove in most frames). Woman: only sleeve/hands before 2.5 s (off); she laughs at 3.0-3.5 s, the man only smiles - check 'to burst out laughing'. Dog is hidden behind the stove door 5.5-7.0 s and a sliver at 9.5-10 s (off); tongue out at 0.5-1.0 and 5.0 s. Stove boxes include the hands in front of it."})

# ---------- 177
W={0.0:(.35,.17,.65,.83),0.5:(.24,.15,.76,.85),1.0:(.19,.15,.81,.85),1.5:(.26,.10,.74,.90),2.0:(.25,.03,.75,.97),
 2.5:(.21,0,.79,1.0),3.0:(.20,0,.80,1.0),3.5:(.19,0,.81,1.0),4.0:(.19,0,.81,1.0),4.5:(.22,0,.78,1.0),5.0:(.27,0,.73,1.0),
 5.5:(.34,0,.66,1.0),6.0:(.31,0,.69,1.0),6.5:(.31,.05,.69,.95),7.0:(.26,.15,.74,.85),7.5:(.26,.15,.74,.85),
 8.0:(.37,.13,.50,.87),8.5:(.42,.18,.48,.82),9.0:(.41,.25,.57,.75),9.5:(.41,.25,.59,.75),10.0:(.44,.20,.40,.80)}
M={0.0:(.12,.30,.22,.20),0.5:(.03,.29,.20,.14),1.0:(0,.36,.18,.62),1.5:(0,.25,.25,.75),2.0:(0,.22,.24,.52),
 2.5:(0,.08,.20,.20),3.0:(0,.07,.19,.25),3.5:(0,.07,.18,.25),4.0:(0,.08,.18,.20),4.5:(0,.09,.21,.22),5.0:(0,.12,.26,.88),
 5.5:(0,.15,.33,.46),6.0:(0,.16,.30,.84),6.5:(0,.18,.30,.46),7.0:(0,.23,.25,.72),7.5:(0,.25,.25,.70),
 8.0:(.08,.25,.28,.75),8.5:(.15,.26,.26,.74),9.0:(.12,.28,.28,.72),9.5:(.12,.28,.28,.72),10.0:(.15,.26,.28,.72)}
write(177,{"mediaId":177,"level":"A","keyWord":"coat","defaultVoice":"female",
 "taps":[tap("to put on a coat","the woman","female",W),
         tap("to tie a belt","the woman","female",W),
         tap("to hold up his thumb","the man","male",M)],
 "stillS":8.0,
 "nouns":[{"word":"a coat","x":.55,"y":.64,"voice":"female"},{"word":"a man","x":.24,"y":.45,"voice":"male"},
          {"word":"a lamp","x":.88,"y":.33,"voice":"female"},{"word":"the sky","x":.45,"y":.08,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","putting","on","a","brown","coat."],"answerVoice":"female",
 "notes":"Only two targets (woman, man); the woman has two phrases. The man stands close behind her, boxes are split along a vertical line, so the edge of his hood or of her sleeve is cut in some frames; the open coat wings at 0.0-1.0 s reach beyond her box. Thumbs up visible at 5.5 and 6.5 s."})

# ---------- 178
man={0.0:(0,.35,.56,.32),0.5:(0,.15,.58,.47),1.5:(0,.24,.74,.38),2.0:(0,.20,.70,.32),2.5:(0,.08,.74,.75),3.0:(0,.03,.70,.97),
 3.5:(0,.05,.65,.95),4.0:(0,.28,.53,.72),4.5:(0,.30,.42,.70),5.0:(0,.48,.31,.30),5.5:(0,0,.52,.60),6.0:(0,0,.53,.52),
 6.5:(0,0,.53,.52),7.0:(0,.02,.53,.58),7.5:(0,0,.40,.92),8.0:(0,0,.50,.86),8.5:(0,0,.46,.86),9.0:(0,0,.48,.95),
 9.5:(0,.20,.47,.80),10.0:(0,.23,.50,.77)}
wo={4.5:(.80,.51,.20,.19),5.0:(.81,.36,.19,.40),5.5:(.80,.22,.20,.58),6.0:(.73,.13,.27,.55),6.5:(.73,.13,.27,.55),
 7.0:(.73,.13,.27,.63),7.5:(.82,.18,.18,.62),8.0:(.82,.18,.18,.52),8.5:(.82,.49,.18,.22),9.5:(.58,.33,.42,.52),10.0:(.58,.36,.42,.42)}
cat={4.0:(.72,.40,.28,.22),4.5:(.64,.36,.30,.14),5.0:(.57,.49,.23,.26),5.5:(.55,.31,.24,.27),6.0:(.54,.30,.18,.20),
 6.5:(.54,.30,.18,.20),7.0:(.54,.33,.18,.18),7.5:(.60,.31,.21,.22),8.0:(.60,.31,.21,.21),8.5:(.58,.30,.42,.18),9.0:(.58,.30,.42,.19)}
write(178,{"mediaId":178,"level":"B","keyWord":"cocktail","defaultVoice":"male",
 "taps":[tap("to shake a cocktail","the man","male",man),
         tap("to wear large hoop earrings","the woman","female",wo),
         tap("to perch on the bar","the cat","male",cat)],
 "stillS":8.5,
 "nouns":[{"word":"a cocktail","x":.52,"y":.70,"voice":"male"},{"word":"a cat","x":.80,"y":.37,"voice":"male"},
          {"word":"a cherry","x":.36,"y":.45,"voice":"male"},{"word":"a beard","x":.15,"y":.32,"voice":"male"}],
 "question":"What is the man doing?",
 "answer":["He","is","preparing","a","cocktail","with","a","cherry."],"answerVoice":"male",
 "notes":"Many cuts. The man is only hands/arm in the first shots (0.0-2.5 s; at 1.0 s only the juice carton, off). The woman phrase is a state: her hoop earring shows at 5.5-7.0 and 10.0 s; her look changes in the last shot (headscarf gone, blond) - same person in the story. At 4.0 s only her fingers show (off). The cat sits on the bar in the background 4.0-9.0 s, small and partly behind the strainer at 6.0-7.0 s; its box and the woman's are split where they meet."})

# ---------- 179
m={0.0:(.02,.15,.60,.85),0.5:(0,.12,.80,.88),1.0:(0,.18,.72,.82),1.5:(0,.20,.49,.80),2.0:(0,.18,.57,.44),2.5:(0,0,.95,.49),
 3.0:(0,.02,.75,.47),3.5:(0,.02,.78,.47),4.0:(0,.03,.88,.38),4.5:(0,0,1.0,.46),6.0:(0,0,.74,.54),6.5:(0,.08,1.0,.92),
 7.0:(0,.07,1.0,.93),7.5:(0,.05,1.0,.95),8.0:(0,0,1.0,1.0),8.5:(0,.03,1.0,.97),9.0:(0,.12,.92,.88),9.5:(0,.15,.80,.85),10.0:(0,.16,.80,.84)}
w={1.5:(.64,.22,.36,.46),2.0:(.58,.18,.42,.44),9.5:(.81,.38,.19,.62),10.0:(.81,.38,.19,.62)}
p={1.0:(.73,.66,.27,.30),1.5:(.50,.69,.22,.25),2.0:(.42,.63,.26,.25),2.5:(.15,.50,.83,.50),3.0:(.45,.50,.37,.40),
 3.5:(.40,.50,.40,.42),4.0:(.40,.42,.40,.42),4.5:(.20,.47,.80,.53),5.0:(.08,0,.88,.70),5.5:(0,.05,1.0,.95)}
write(179,{"mediaId":179,"level":"A","keyWord":"coffee","defaultVoice":"male",
 "taps":[tap("to drink some coffee","the man","male",m),
         tap("to smile at the man","the woman","female",w),
         tap("to stand on the stove","the coffee pot","male",p)],
 "stillS":10.0,
 "nouns":[{"word":"coffee","x":.37,"y":.62,"voice":"male"},{"word":"a woman","x":.86,"y":.50,"voice":"female"},
          {"word":"a curtain","x":.86,"y":.20,"voice":"male"},{"word":"a window","x":.22,"y":.20,"voice":"male"}],
 "question":"What is the man drinking?",
 "answer":["He","is","drinking","a","cup","of","coffee."],"answerVoice":"male",
 "notes":"Many cuts. The woman is visible only at 1.5-2.0 s and 9.5-10.0 s (a sliver at 9.0 s, off). Where the man holds the pot (3.0-4.5 s) his box is the head and shoulders above the pot, the pot box is below. The pot stands on the stove at 3.5-5.0 s. 'coffee' is placed on the full cup in his hand."})
