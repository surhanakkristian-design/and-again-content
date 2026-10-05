import json
T21=[i*0.5 for i in range(21)]
def keys(times, d):
    out=[]
    for t in times:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else: out.append({"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---- 438
W={0.0:(0,.15,1,.37),0.5:(0,.10,1,.42),1.0:(0,.33,1,.45),1.5:(0,.33,1,.45),
   2.0:(0,.15,.57,.70),2.5:(0,.15,.60,.70),
   3.0:(.02,.02,.96,.98),3.5:(.02,.02,.96,.98),4.0:(.02,.02,.96,.98),4.5:(.02,.02,.96,.98),5.0:(.02,.02,.96,.98),
   9.0:(0,.29,.49,.39),9.5:(0,.31,.49,.37),10.0:(0,.28,.49,.40)}
M={2.0:(.58,.20,.42,.63),2.5:(.61,.20,.39,.63),5.5:(0,.05,1,.95),6.0:(0,.05,1,.95),
   9.0:(.51,.29,.49,.39),9.5:(.51,.31,.49,.37),10.0:(.50,.28,.50,.40)}
C={1.0:(.42,.17,.56,.15),1.5:(.43,.15,.57,.17),7.5:(.74,.33,.26,.18),8.0:(.66,.33,.34,.17),8.5:(.72,.34,.28,.19),
   9.0:(.24,.69,.34,.14),9.5:(.24,.69,.36,.14),10.0:(.22,.69,.38,.13)}
save({"mediaId":438,"level":"A","keyWord":"lemon","defaultVoice":"female",
 "taps":[{"phrase":"to bite a lemon","target":"the woman","voice":"female","keys":keys(T21,W)},
         {"phrase":"to have a dark beard","target":"the man","voice":"male","keys":keys(T21,M)},
         {"phrase":"to lie on the wall","target":"the cat","voice":"female","keys":keys(T21,C)}],
 "stillS":1.0,
 "nouns":[{"word":"a lemon","x":.50,"y":.67,"voice":"female"},{"word":"a knife","x":.20,"y":.41,"voice":"female"},
          {"word":"a hand","x":.82,"y":.50,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","biting","a","lemon."],"answerVoice":"female",
 "notes":"Many cuts. Woman's box at 0.0-1.5 is only her hand/arm (the cutting shot). Hands at 6.5-8.5 (squeezing, pouring, spoon) are off for both people: owner not identifiable. Cat off at 0.0/0.5 (blur hidden behind the hand), on at 1.0/1.5 where the striped cat is recognisable but out of focus. Man: state phrase, because every action he does (pull a sour face, drink, toast) the woman does too; he is never seen biting."})

# ---- 439
W={5.5:(.77,.28,.23,.72),6.0:(.46,0,.54,1),6.5:(.39,.04,.61,.96),7.0:(.35,.08,.65,.92),7.5:(.44,.08,.56,.92),
   8.0:(.56,.02,.44,.98),8.5:(.56,.39,.44,.61),9.0:(.50,.43,.50,.57),9.5:(.61,.18,.39,.82),10.0:(.73,.22,.27,.78)}
D={5.0:(0,.52,.36,.48),5.5:(0,.52,.62,.46),6.0:(0,.58,.33,.40),6.5:(0,.60,.24,.36),7.5:(0,.62,.30,.36),
   8.0:(.08,.52,.30,.35),9.5:(.05,.57,.50,.36),10.0:(.08,.57,.40,.27)}
F={4.5:(.80,.05,.20,.42),5.0:(.56,.08,.44,.50),5.5:(.26,.22,.50,.28),6.0:(.02,.19,.43,.38),6.5:(.05,.20,.33,.38),
   7.0:(.12,.24,.22,.22),7.5:(.20,.20,.23,.22),8.0:(.36,.16,.19,.34),8.5:(.47,.18,.40,.20),9.0:(.46,.25,.40,.17),
   9.5:(.40,.28,.20,.14),10.0:(.52,.32,.20,.24)}
save({"mediaId":439,"level":"A","keyWord":"lemonade","defaultVoice":"female",
 "taps":[{"phrase":"to drink cold lemonade","target":"the woman","voice":"female","keys":keys(T21,W)},
         {"phrase":"to lie on the floor","target":"the dog","voice":"female","keys":keys(T21,D)},
         {"phrase":"to grow in a pot","target":"the red flowers","voice":"female","keys":keys(T21,F)}],
 "stillS":6.0,
 "nouns":[{"word":"lemonade","x":.60,"y":.44,"voice":"female"},{"word":"flowers","x":.22,"y":.30,"voice":"female"},
          {"word":"a dog","x":.14,"y":.72,"voice":"female"},{"word":"a woman","x":.83,"y":.62,"voice":"female"}],
 "question":"What is the woman doing?","answer":["She","is","drinking","cold","lemonade."],"answerVoice":"female",
 "notes":"Hand-held clip, everything moves. 'The woman' = the seated woman in the dark top who drinks (6.0 on); she is off before 5.5 (only a hand/knee; a different person carries the jar at 1.5-2.5). Woman, flowers and dog overlap in the picture, so the woman's box is split and loses part of her legs (6.0-10.0) and her face sliver at the frame edge at 8.5/9.0. Flowers are off while only a tiny red blur (0.0-2.0). Dog off at 7.0/8.5/9.0 (hidden behind jar and glasses). Third target is a plant with a state-like phrase (the pot shows at 6.0/6.5/10.0); other people show only hands, so no fair third person."})

# ---- 440
T11=[i*0.5 for i in range(11)]
Mn={0.0:(.01,.20,.92,.72),0.5:(.03,.22,.95,.70),1.0:(.04,.04,.88,.96),1.5:(.05,.17,.85,.83),2.0:(.02,.21,.90,.79),
    2.5:(.06,.12,.83,.88),3.0:(.06,.14,.83,.86),3.5:(.06,.15,.83,.85),4.0:(.06,.12,.84,.88),4.5:(0,.30,1,.70),5.0:(0,.38,.98,.62)}
k=keys(T11,Mn)
save({"mediaId":440,"level":"A","keyWord":"lifting","defaultVoice":"male",
 "taps":[{"phrase":"to lift heavy weights","target":"the man","voice":"male","keys":k},
         {"phrase":"to wear a wide belt","target":"the man","voice":"male","keys":k},
         {"phrase":"to smile at the end","target":"the man","voice":"male","keys":k}],
 "stillS":3.5,
 "nouns":[{"word":"a man","x":.58,"y":.51,"voice":"male"},{"word":"a belt","x":.45,"y":.93,"voice":"male"},
          {"word":"a window","x":.80,"y":.20,"voice":"male"}],
 "question":"What is the man doing?","answer":["He","is","lifting","heavy","weights."],"answerVoice":"male",
 "notes":"Only one possible target (the animated strongman), so all three phrases use him. The key word is the activity, not a visible noun. 'a man' (pill on the face) and 'a belt' are on the same large figure but far apart (0.4 in y)."})

# ---- 442
W={0.0:(.08,.25,.77,.55),0.5:(.08,.23,.77,.56),1.0:(.08,.21,.74,.57),1.5:(.08,.18,.76,.60),2.0:(.05,.12,.80,.65),
   2.5:(.03,.03,.87,.84),3.0:(.04,.11,.84,.89),3.5:(.07,.17,.73,.83),4.0:(0,.20,.66,.80),4.5:(.02,.23,.64,.77),
   5.0:(.02,.26,.61,.74),5.5:(.02,.27,.52,.73),6.0:(.05,.22,.39,.78),6.5:(.07,.27,.33,.73),7.0:(.14,.30,.29,.68),
   7.5:(.15,.36,.26,.55),8.0:(.02,.34,.34,.52),8.5:(0,.33,.32,.53),9.0:(0,.34,.30,.63),9.5:(0,.35,.32,.63),10.0:(0,.36,.32,.52)}
M={3.5:(.82,.08,.18,.90),4.0:(.67,.16,.33,.84),4.5:(.67,.22,.33,.78),5.0:(.64,.26,.36,.74),5.5:(.60,.27,.40,.73),
   6.0:(.60,.25,.40,.75),6.5:(.60,.28,.40,.72),7.0:(.58,.30,.36,.68),7.5:(.57,.32,.40,.58),8.0:(.62,.30,.38,.56),
   8.5:(.68,.30,.32,.56),9.0:(.65,.31,.35,.66),9.5:(.72,.30,.28,.68),10.0:(.70,.29,.30,.60)}
kw=keys(T21,W)
save({"mediaId":442,"level":"B","keyWord":"teamwork","defaultVoice":"female",
 "taps":[{"phrase":"to struggle with a box","target":"the woman","voice":"female","keys":kw},
         {"phrase":"to lend a helping hand","target":"the man","voice":"male","keys":keys(T21,M)},
         {"phrase":"to crouch behind a box","target":"the woman","voice":"female","keys":kw}],
 "stillS":10.0,
 "nouns":[{"word":"a cat","x":.46,"y":.37,"voice":"female"},{"word":"cardboard boxes","x":.50,"y":.63,"voice":"female"},
          {"word":"a beard","x":.87,"y":.40,"voice":"female"},{"word":"a wooden floor","x":.50,"y":.92,"voice":"female"}],
 "question":"What are the man and woman doing?","answer":["They","are","stacking","cardboard","boxes","together."],"answerVoice":"female",
 "notes":"The woman's box includes the carton she carries (0.0-5.0). Man off until 3.5 (before that only a sock / a hand at the frame edge). The cat is not a tap target: it is only in the last two frames (9.5 ears, 10.0 sitting on the stack). Two phrases share the woman. Nouns: pills 'a cat' and 'a beard' are 0.41 apart in x at nearly the same height."})
