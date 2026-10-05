import json
def K(times, boxes):
    out=[]
    for t,b in zip(times,boxes):
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]})
    assert len(out)==len(times)==len(boxes)
    return out
def T(n): return [i*0.5 for i in range(n)]
def save(d): json.dump(d,open(f"content/{d['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# 363
t=T(12)
ltop=[.49,.49,.50,.50,.50,.50,.54,.55,.55,.53,.55,.55]
lbot=[.76,.77,.78,.78,.79,.80,.82,.83,.84,.85,.85,.86]
man=[(0,.03,.72,round(y-.03,2)) for y in ltop]
lap=[(.50,y,.50,round(b-y,2)) for y,b in zip(ltop,lbot)]
lamp=[(.73,.14,.27,.29)]*12
save({"mediaId":363,"level":"B","keyWord":"research","defaultVoice":"male",
"taps":[{"phrase":"to jot down notes","target":"the man","voice":"male","keys":K(t,man)},
{"phrase":"to illuminate the desk","target":"the lamp","voice":"male","keys":K(t,lamp)},
{"phrase":"to display a document","target":"the laptop","voice":"male","keys":K(t,lap)}],
"stillS":1.5,
"nouns":[{"word":"a desk lamp","x":.84,"y":.31,"voice":"male"},{"word":"a cardigan","x":.16,"y":.50,"voice":"male"},
{"word":"a laptop","x":.76,"y":.67,"voice":"male"},{"word":"sticky notes","x":.45,"y":.83,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","doing","research","at","his","desk."],"answerVoice":"male",
"notes":"Man's box stops at the laptop's top edge so the two boxes do not overlap: his forearm/hand on the keyboard and, from 3.0 s, his writing hand below the laptop line lie outside his box (head and torso inside). 'to display a document': screen shows text, seen at an angle. Key word 'research' is abstract, used in the answer, not as a noun label."})

# 364
t=T(12)
man=[(.14,0,.86,.68),(.14,0,.86,.68),(.12,0,.88,.71),(.12,0,.88,.71),(.05,0,.95,.68),(.05,0,.95,.70),
(.04,0,.96,.76),(.05,0,.95,.77),(.03,0,.97,.78),(.05,0,.95,.78),(.03,0,.97,.82),(0,0,1,.87)]
save({"mediaId":364,"level":"A","keyWord":"artist","defaultVoice":"male",
"taps":[{"phrase":"to draw on paper","target":"the man","voice":"male","keys":K(t,man)},
{"phrase":"to hold an orange pencil","target":"the man","voice":"male","keys":K(t,man)},
{"phrase":"to smile at the camera","target":"the man","voice":"male","keys":K(t,man)}],
"stillS":4.0,
"nouns":[{"word":"a face","x":.72,"y":.17,"voice":"male"},{"word":"a T-shirt","x":.50,"y":.37,"voice":"male"},
{"word":"a pencil","x":.20,"y":.50,"voice":"male"},{"word":"a drawing","x":.36,"y":.88,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","drawing","with","an","orange","pencil."],"answerVoice":"male",
"notes":"Only one possible target (the man), used for all three phrases. He smiles at the camera only from about 3.0 s. Key word 'artist' not used as a label: he says he is not one."})

# 366
t=T(11)
w=[(0,0,.84,1),(0,0,.85,1),(0,0,.88,1),(0,0,.88,1),(0,0,.88,1),(0,.16,.97,.84),(.04,.16,.70,.84),(0,.08,.90,.92),(0,.24,.95,.76),(0,.11,1,.89),(0,.08,1,.92)]
save({"mediaId":366,"level":"B","keyWord":"heal","defaultVoice":"female",
"taps":[{"phrase":"to remove a bandage","target":"the woman","voice":"female","keys":K(t,w)},
{"phrase":"to grip a gymnastic ring","target":"the woman","voice":"female","keys":K(t,w)},
{"phrase":"to pump her fist","target":"the woman","voice":"female","keys":K(t,w)}],
"stillS":2.0,
"nouns":[{"word":"a sleeve","x":.62,"y":.33,"voice":"female"},{"word":"a fist","x":.22,"y":.71,"voice":"female"},
{"word":"a coffee cup","x":.84,"y":.78,"voice":"female"},{"word":"car keys","x":.74,"y":.94,"voice":"female"}],
"question":"What is the woman gripping?","answer":["She","is","gripping","a","gymnastic","ring."],"answerVoice":"female",
"notes":"Only one possible target (the woman). The bandage is on her arm at 0.0 s and flying off at 0.5 s, the unwrapping itself is very short. 0.0-2.0 s show only her torso and arm (no face). Key word 'heal' is a verb, not shown as a label and not natural in a picture-only answer."})

# 367
t=T(21)
woman=[(0,.27,.24,.73),(0,.26,.23,.74),(0,.28,.18,.72),(0,.59,.28,.41),None,None,None,None,
(0,.20,.13,.78),(0,.21,.19,.77),(0,.30,.20,.70),(0,.29,.24,.71),(0,.59,.42,.29),(0,.34,.44,.66),(0,.35,.47,.65),
(.03,.41,.50,.59),(0,.34,.49,.66),(0,.24,.55,.76),(0,.36,.42,.64),(0,.22,.35,.78),(0,.24,.44,.76)]
man=[(.46,.14,.54,.86),(.46,.08,.54,.92),(.40,0,.60,1),(.38,0,.62,1),(.35,0,.65,1),(.30,0,.70,1),(.26,0,.74,1),(.28,0,.72,1),
(.36,.02,.64,.98),(.46,.12,.54,.88),(.48,.20,.52,.80),(.60,.22,.40,.78),(.68,.35,.32,.50),(.70,.33,.30,.50),(.62,.20,.38,.80),
(.55,.29,.45,.71),(.52,.25,.48,.75),(.56,.19,.44,.81),(.44,.24,.56,.76),(.50,.17,.50,.83),(.56,.20,.44,.80)]
dog=[(.25,.43,.18,.14),(.23,.44,.18,.14),(.19,.45,.18,.14),(.12,.45,.18,.14),(.09,.44,.18,.14),(.07,.44,.18,.14),(.05,.44,.18,.14),(.09,.44,.18,.14),
(.14,.44,.18,.14),(.19,.44,.18,.14),(.20,.45,.18,.14),(.24,.45,.18,.14),(.11,.45,.18,.14)]+[None]*8
save({"mediaId":367,"level":"A","keyWord":"heat","defaultVoice":"male",
"taps":[{"phrase":"to eat an ice pop","target":"the man","voice":"male","keys":K(t,man)},
{"phrase":"to hold a fan","target":"the woman","voice":"female","keys":K(t,woman)},
{"phrase":"to lie on the ground","target":"the dog","voice":"male","keys":K(t,dog)}],
"stillS":4.5,
"nouns":[{"word":"the sky","x":.45,"y":.10,"voice":"male"},{"word":"a fountain","x":.52,"y":.47,"voice":"male"},
{"word":"a shirt","x":.86,"y":.72,"voice":"male"},{"word":"a dress","x":.10,"y":.76,"voice":"male"}],
"question":"What is the man eating?","answer":["He","is","eating","an","orange","ice","pop."],"answerVoice":"male",
"notes":"'ice pop' (ice lolly / popsicle) is the exact word but slightly above A1; from 3.5 s only the stick is left. Woman set off at 2.0-3.5 s (only a sliver of her arm at the left edge). At 1.5 s her box covers the fan and lower arm (the sliver of upper arm at the left edge is outside); at 6.0 s her box covers arm + fan, her head (left edge, above the dog) is outside. Dog is small and far (box 0.18 x 0.14), hidden from 6.5 s. The woman's box is cut on the right where the dog box starts (0.0-0.5 s), so part of her arm/fan is outside. Key word 'heat' is not a visible noun. defaultVoice male: mixed couple, odd id."})
