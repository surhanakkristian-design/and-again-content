import json
def K(times, d):
    out=[]
    for t in times:
        b=d.get(t)
        if b is None: out.append({"t":t,"off":True})
        else:
            x,y,x2,y2=b
            out.append({"t":t,"x":round(x,2) if round(x,2)==x else x,"y":y,"w":round(x2-x,3),"h":round(y2-y,3)})
    return out
def T(n,step=0.5): return [round(i*step,1) for i in range(n)]
def save(o): json.dump(o,open(f"content/{o['mediaId']}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4199 (boxes as x1,y1,x2,y2)
t=T(24)
pilot={0.0:(.455,.15,.64,.29),0.5:(.485,.15,.67,.29),1.0:(.47,.205,.66,.345),1.5:(.49,.235,.68,.375),2.0:(.49,.255,.68,.395),
2.5:(.48,.295,.67,.435),3.0:(.47,.33,.66,.47),3.5:(.45,.33,.64,.47),4.0:(.43,.33,.62,.48),4.5:(.43,.33,.62,.48),
5.0:(.45,.29,.65,.45),5.5:(.51,.28,.72,.45),6.0:(.57,.29,.80,.48),6.5:(.60,.30,.87,.53),7.0:(.45,.35,.74,.60),
7.5:(.14,.38,.46,.64),8.0:(.05,.455,.34,.62),8.5:(.19,.41,.405,.61),9.0:(.31,.41,.50,.60),9.5:(.29,.41,.53,.60),
10.0:(.27,.44,.50,.60),10.5:(.31,.445,.51,.60),11.0:(.34,.465,.55,.61),11.5:(.38,.465,.58,.60)}
wing={0.0:(.29,.09,.455,.28),0.5:(.30,.08,.485,.28),1.0:(.32,.08,.62,.205),1.5:(.32,.10,.65,.235),2.0:(.31,.12,.68,.255),
2.5:(.29,.15,.71,.295),3.0:(.28,.18,.75,.33),3.5:(.29,.18,.79,.32),4.0:(.27,.15,.82,.32),4.5:(.23,.12,.84,.31),
5.0:(.19,.07,.89,.28),5.5:(.17,0,.96,.24),6.0:(.17,0,1,.27),6.5:(.19,0,1,.29),7.0:(.21,0,.84,.33),7.5:(.21,0,.80,.33),
8.0:(0,0,.82,.34),8.5:(0,0,.94,.34),9.0:(.04,.02,1,.34),9.5:(0,.05,.92,.34),10.0:(0,.12,.87,.415),10.5:(.07,.17,.90,.44),
11.0:(.09,.22,.90,.46),11.5:(.11,.31,.88,.46)}
spec={8.0:(.08,.36,.37,.45),8.5:(.405,.40,.56,.52),9.0:(.50,.40,1,.54),9.5:(.60,.40,.86,.54),10.0:(.67,.425,.94,.56),
10.5:(.74,.445,.98,.585),11.0:(.76,.465,1,.605),11.5:(.82,.465,1,.60)}
save({"mediaId":4199,"level":"B","keyWord":"drag","defaultVoice":"male",
"taps":[{"phrase":"to drag his feet","target":"the pilot","voice":"male","keys":K(t,pilot)},
{"phrase":"to collapse onto the meadow","target":"the red wing","voice":"male","keys":K(t,wing)},
{"phrase":"to watch the landing","target":"the spectators","voice":"male","keys":K(t,spec)}],
"stillS":5.0,
"nouns":[{"word":"a paraglider","x":.50,"y":.16,"voice":"male"},{"word":"spray","x":.70,"y":.42,"voice":"male"},
{"word":"a reflection","x":.50,"y":.67,"voice":"male"},{"word":"a shore","x":.22,"y":.33,"voice":"male"}],
"question":"What is the pilot doing?",
"answer":["He","is","dragging","his","feet","through","the","water."],"answerVoice":"male",
"notes":"Pilot's gender is not visible (helmet, dark suit); 'he' follows the description. Wing and pilot are close in 0.0-2.5 s, boxes split along a line (wing loses a tip). At 11.5 s the wing has sunk around the pilot: wing box covers only the arch above him. Spectators are tiny and partly behind the pilot at 8.0-8.5 s (box cut small there). Noun 'a paraglider' sits on the wing; 'a shore' is the thin grass strip on the left."})

# ---------- 4200
t=T(25)
woman={0.0:(.24,.41,.43,.55),0.5:(.42,.42,.60,.56),1.0:(.515,.44,.67,.60),1.5:(.37,.39,.62,.63)}
drone={1.5:(.62,.37,.80,.51),2.0:(.60,.395,.78,.535),2.5:(.36,.51,.58,.65),3.0:(.16,.53,.40,.67),3.5:(.24,.46,.46,.60),
4.0:(.40,.40,.60,.54),4.5:(.48,.36,.68,.50),5.0:(.46,.40,.66,.54),5.5:(.28,.445,.48,.585),6.0:(.17,.315,.36,.455),
6.5:(.10,.30,.29,.44),7.0:(.12,.385,.31,.525),7.5:(.27,.41,.46,.55),8.0:(.34,.415,.54,.555),8.5:(.21,.40,.42,.54),
9.0:(.26,.375,.44,.515),9.5:(.34,.375,.52,.515),10.0:(.325,.39,.505,.53),10.5:(.355,.39,.535,.53),11.0:(.515,.40,.70,.54),
11.5:(.515,.40,.70,.54),12.0:(.50,.40,.68,.54)}
sun={0.5:(.03,.37,.26,.54),1.0:(.34,.41,.515,.54),2.0:(.42,.37,.60,.54),2.5:(.54,.27,.76,.47),3.0:(.70,.13,.95,.33),
3.5:(.80,0,1,.14),5.0:(.40,.10,.70,.29),5.5:(.80,.26,1,.41),9.0:(.56,.28,.90,.48),9.5:(.54,.34,.80,.50),
10.0:(.505,.33,.72,.48),10.5:(.535,.34,.72,.50),11.0:(.36,.37,.515,.52),11.5:(.36,.37,.515,.52),12.0:(.33,.39,.50,.54)}
save({"mediaId":4200,"level":"B","keyWord":"gold","defaultVoice":"female",
"taps":[{"phrase":"to stand beneath a tree","target":"the woman","voice":"female","keys":K(t,woman)},
{"phrase":"to dive towards the bay","target":"the drone","voice":"female","keys":K(t,drone)},
{"phrase":"to turn the sea gold","target":"the sun","voice":"female","keys":K(t,sun)}],
"stillS":7.0,
"nouns":[{"word":"an arch","x":.76,"y":.38,"voice":"female"},{"word":"a cliff","x":.25,"y":.30,"voice":"female"},
{"word":"foam","x":.60,"y":.62,"voice":"female"},{"word":"the sky","x":.50,"y":.08,"voice":"female"}],
"question":"What is the sun doing?",
"answer":["It","is","turning","the","sea","gold."],"answerVoice":"female",
"notes":"The small object the camera follows from 1.5 s to the end is a second drone (rotors visible at 3.0-5.0 and 8.5 s); the description's 'lone swimmer' at 6-7.5 s is that same drone, so there is no swimmer target. The drone is tiny (min-size boxes). Sun: off where hidden (behind the woman at 1.5 s, behind cliffs 4.0-4.5 and 6.0-8.5 s); at 10.0-12.0 s drone and sun touch in the picture, boxes split between them. The woman is visible only 0.0-1.5 s. Key word 'gold' is a colour here, so it is in a phrase and the answer, not a noun."})

# ---------- 4201
riders={0.5:(.37,.49,.61,.63),1.0:(.45,.49,.70,.64),1.5:(.38,.49,.68,.65),2.0:(.36,.45,.75,.62),2.5:(.33,.44,.745,.595),
3.0:(.27,.42,.75,.60),3.5:(.24,.39,.745,.60),4.0:(.20,.37,.745,.60),4.5:(.17,.36,.745,.60),5.0:(.18,.37,.74,.605),
5.5:(.21,.40,.74,.605),6.0:(.25,.39,.74,.595),6.5:(.26,.40,.74,.59),7.0:(.26,.41,.72,.595),7.5:(.26,.41,.72,.595),
8.0:(.27,.40,.71,.595),8.5:(.32,.40,.72,.60),9.0:(.31,.40,.70,.61),9.5:(.32,.41,.66,.61),10.0:(.35,.43,.69,.605),
10.5:(.38,.44,.70,.60),11.0:(.38,.435,.70,.575),11.5:(.37,.41,.61,.55),12.0:(.31,.40,.55,.54)}
palms={0.5:(.62,.44,1,.55),1.0:(.71,.43,1,.56),1.5:(.70,.43,1,.57),2.0:(.76,.44,1,.57),2.5:(.755,.44,1,.585),
3.0:(.76,.45,1,.585),3.5:(.755,.44,1,.59),4.0:(.755,.45,1,.59),4.5:(.755,.45,1,.59),5.0:(.75,.46,1,.60),5.5:(.75,.47,1,.60),
6.0:(.75,.44,1,.59),6.5:(.75,.45,1,.585),7.0:(.73,.46,1,.59),7.5:(.74,.47,1,.59),8.0:(.72,.46,1,.59),8.5:(.74,.47,1,.595),
9.0:(.82,.47,1,.61)}
sandtop={2.5:.60,3.0:.605,3.5:.605,4.0:.605,4.5:.605,5.0:.61,5.5:.61,6.0:.60,6.5:.595,7.0:.60,7.5:.60,8.0:.60,8.5:.605,
9.0:.615,9.5:.615,10.0:.61,10.5:.605,11.0:.58,11.5:.555,12.0:.545}
sand={k:(0,v,1,1) for k,v in sandtop.items()}
save({"mediaId":4201,"level":"B","keyWord":"upright","defaultVoice":"male",
"taps":[{"phrase":"to hold their bikes upright","target":"the riders","voice":"male","keys":K(t,riders)},
{"phrase":"to line the shore","target":"the palm trees","voice":"male","keys":K(t,palms)},
{"phrase":"to reflect the pink clouds","target":"the wet sand","voice":"male","keys":K(t,sand)}],
"stillS":4.5,
"nouns":[{"word":"dirt bikes","x":.45,"y":.47,"voice":"male"},{"word":"palm trees","x":.84,"y":.56,"voice":"male"},
{"word":"a reflection","x":.35,"y":.75,"voice":"male"},{"word":"clouds","x":.50,"y":.15,"voice":"male"}],
"question":"What are the riders doing?",
"answer":["They","are","holding","their","bikes","upright."],"answerVoice":"male",
"notes":"The two riders do exactly the same thing the whole clip, so no phrase fits only one of them: they are ONE target ('the riders', one box around both real bikes, reflections excluded). The other targets are things: the palm trees (0.5-9.0 s; those right of the riders) and the wet sand (everything below the horizon from 2.5 s, where the mirror is clear; it holds the riders' reflections). The man filming himself at 0.0 s is on screen for one frame only and is not used. 'dirt bikes' is one plural pill between the two bikes; clouds above could also be read as 'the sky'."})

# ---------- 4202
t=T(17)
dogs={0.0:(0,.18,1,.85),0.5:(0,.17,1,.85),1.0:(0,.17,1,.855),1.5:(0,.15,1,.855),2.0:(0,.13,1,.82),2.5:(0,.12,1,.795),
3.0:(0,.11,1,.795),3.5:(0,.11,1,.795),4.0:(0,.10,1,.82),4.5:(0,.11,1,.82),5.0:(0,.11,1,.825),5.5:(0,.11,1,.855),
6.0:(0,.10,1,.70),6.5:(0,.10,1,.69),7.0:(0,.11,1,.75),7.5:(0,.12,1,.555),8.0:(0,.13,1,.49)}
hand={0.5:(.60,.86,.95,1),1.0:(.58,.86,.95,1),1.5:(.58,.86,.97,1),2.0:(.57,.83,1,1),2.5:(.59,.80,1,1),3.0:(.57,.80,1,1),
3.5:(.61,.80,1,1),4.5:(.64,.86,.98,1),5.0:(.63,.83,1,1),5.5:(.61,.86,1,1),6.0:(.61,.705,1,1),6.5:(.71,.69,1,1),7.0:(.86,.81,1,1)}
dog3={7.0:(.50,.86,.86,1),7.5:(.17,.555,.87,1),8.0:(.24,.49,1,1)}
save({"mediaId":4202,"level":"A","keyWord":"belly","defaultVoice":"female",
"taps":[{"phrase":"to lie on their backs","target":"the sleeping dogs","voice":"female","keys":K(t,dogs)},
{"phrase":"to hold a kitchen tool","target":"the hand","voice":"female","keys":K(t,hand)},
{"phrase":"to stand next to the hand","target":"the standing dog","voice":"female","keys":K(t,dog3)}],
"stillS":6.0,
"nouns":[{"word":"a belly","x":.55,"y":.25,"voice":"female"},{"word":"an ear","x":.31,"y":.65,"voice":"female"},
{"word":"a hand","x":.80,"y":.83,"voice":"female"}],
"question":"What are the two dogs doing?",
"answer":["They","are","lying","on","their","backs","in the sun."],"answerVoice":"female",
"notes":"The two dogs on their backs do the same thing, so they are ONE target with one box around both (the white turner lies over that box; it is not a target). The third dog (green collar) is visible only 7.0-8.0 s; at 7.5-8.0 s its box takes the lower part and the lying dogs' box is cut above it (the near dog's head/ear falls outside). The hand is off at 0.0, 4.0 (out of frame) and 7.5-8.0 (hidden behind the third dog). 'a belly' sits on the far dog's belly; the near dog shows its belly too. 'kitchen tool' is used because 'spatula/turner' is not A level."})
