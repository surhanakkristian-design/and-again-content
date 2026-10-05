import json
times=[i*0.5 for i in range(31)]
def keys(d):
    out=[]
    for t in times:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
def cb(cx,cy,w=0.18,h=0.14):
    return (round(cx-w/2,2),round(cy-h/2,2),w,h)

# ---------- 4025
kit={0.0:(0,.16,.53,.52),0.5:(0,.17,.62,.52),1.0:(0,.14,.68,.61),1.5:(0,.14,.58,.64),2.0:(0,.20,.60,.59),
2.5:(0,.24,.52,.55),3.0:(0,.26,.51,.51),3.5:(0,.27,.66,.50),4.0:(0,.26,.51,.49),4.5:(0,.28,.43,.46),
5.0:(0,.33,.62,.38),5.5:(0,.32,.62,.38),6.0:(0,.32,.51,.40),6.5:(0,.32,.72,.42),7.0:(0,.23,.47,.60),
7.5:(0,.28,.47,.54),8.0:(0,.23,.41,.50),8.5:(0,.23,.53,.50),9.0:(0,.09,.61,.72),9.5:(0,.05,.93,.79),
10.0:(0,.06,.93,.72),10.5:(0,.05,.99,.74),11.0:(0,.07,.99,.83),11.5:(0,.08,.99,.84),12.0:(0,.08,.93,.74),
12.5:(0,.11,.88,.71),13.0:(0,.10,.90,.82),13.5:(0,.10,.90,.82),14.0:(0,.08,.90,.37),14.5:(0,.05,.88,.55),15.0:(0,.10,.82,.55)}
ball={0.0:(.54,.27,.18,.14),0.5:(.63,.29,.18,.14),1.0:(.69,.28,.18,.14),1.5:(.66,.30,.18,.14),2.0:(.78,.38,.18,.14),
2.5:(.53,.43,.18,.14),3.0:(.52,.42,.18,.14),4.0:(.52,.52,.18,.14),4.5:(.44,.59,.18,.14),5.0:(.41,.72,.18,.14),
5.5:(.38,.71,.18,.14),6.0:(.52,.60,.18,.14),7.0:(.48,.39,.18,.14),7.5:(.48,.57,.18,.14),8.0:(.42,.19,.18,.14),
8.5:(.54,.24,.18,.14),9.0:(.62,.34,.18,.14),14.0:(.36,.46,.18,.14),14.5:(.33,.61,.18,.14),15.0:(.24,.66,.18,.14)}
c={"mediaId":4025,"level":"B","keyWord":"chase","defaultVoice":"male",
"taps":[
 {"phrase":"to chase a rolling ball","target":"the kitten","voice":"male","keys":keys(kit)},
 {"phrase":"to swat with one paw","target":"the kitten","voice":"male","keys":keys(kit)},
 {"phrase":"to roll down the ramps","target":"the ball","voice":"male","keys":keys(ball)}],
"stillS":8.5,
"nouns":[{"word":"a kitten","x":0.24,"y":0.50,"voice":"male"},
 {"word":"a ball","x":0.63,"y":0.31,"voice":"male"},
 {"word":"a windowsill","x":0.50,"y":0.80,"voice":"male"},
 {"word":"branches","x":0.35,"y":0.10,"voice":"male"}],
"question":"What is the kitten doing?",
"answer":["It","is","chasing","a","ball","down","the","ramps."],
"answerVoice":"male",
"notes":"Two targets only (kitten twice, ball once); the wooden tower does nothing of its own. Kitten and ball touch in most frames: the kitten box is cut along the edge of the ball box (so a paw or the lower body is outside it in some frames, e.g. 5.0-6.0, 14.0). Ball is OFF at 3.5 and 6.5 (covered by the paw) and 9.5-13.5 (under the kitten's face / in its mouth, not rolling and inseparable from the kitten). 'windowsill' is a dark stone sill - might read as a worktop."}
json.dump(c,open("content/4025.json","w"),indent=1)

# ---------- 4026
wom={0.0:(.14,0,.86,.35),0.5:(.20,0,.80,.35),1.0:(.18,0,.80,.46),1.5:(.16,0,.72,.50),2.0:(0,0,.70,.47),2.5:(0,0,.62,.43),
3.0:(.13,0,.47,.45),3.5:(.20,.05,.45,.39),4.0:(.34,.21,.30,.27),4.5:(.36,.20,.32,.27),5.0:(.36,.23,.28,.25),5.5:(.34,.27,.28,.21),
6.0:(.34,.24,.30,.22),6.5:(.38,.25,.30,.22),7.0:(.38,.26,.28,.21),7.5:(.38,.26,.28,.20),8.0:(.40,.25,.30,.22),8.5:(.38,.25,.32,.22),
9.0:(.40,.25,.30,.22),9.5:(.38,.25,.32,.23),10.0:(.40,.21,.30,.25),10.5:(.40,.23,.34,.24),11.0:(.34,.21,.28,.21),11.5:(.38,.21,.30,.22),
12.0:(.41,.16,.31,.28),12.5:(.39,.13,.35,.33),13.0:(.36,.10,.42,.41),13.5:(.28,.09,.58,.50),14.0:(.32,.02,.66,.60),14.5:(.38,.02,.54,.80),15.0:(.48,0,.52,.97)}
brd={0.0:(0,.36,.86,.26),0.5:(0,.36,.86,.26),1.0:(.08,.47,.92,.20),1.5:(.05,.51,.93,.17),2.0:(.04,.48,.72,.24),2.5:(.08,.44,.58,.22),
3.0:(.18,.46,.42,.16),3.5:(.28,.45,.36,.15),4.0:(.31,.49,.34,.14),4.5:(.33,.48,.34,.14),5.0:(.32,.49,.34,.14),5.5:(.30,.49,.34,.14),
6.0:(.31,.47,.34,.14),6.5:(.37,.48,.34,.14),7.0:(.36,.48,.34,.14),7.5:(.36,.47,.34,.14),8.0:(.39,.48,.34,.14),8.5:(.39,.48,.34,.14),
9.0:(.41,.48,.34,.14),9.5:(.38,.49,.34,.14),10.0:(.40,.47,.34,.14),10.5:(.45,.48,.34,.14),11.0:(.34,.43,.34,.14),11.5:(.43,.44,.34,.14),
12.0:(.43,.45,.34,.14),12.5:(.45,.47,.34,.14),13.0:(.48,.52,.34,.14),13.5:(.34,.60,.40,.14),14.0:(0,.63,.45,.27)}
c={"mediaId":4026,"level":"A","keyWord":"smooth","defaultVoice":"female",
"taps":[
 {"phrase":"to stand on a board","target":"the woman","voice":"female","keys":keys(wom)},
 {"phrase":"to step off the board","target":"the woman","voice":"female","keys":keys(wom)},
 {"phrase":"to carry the woman","target":"the board","voice":"female","keys":keys(brd)}],
"stillS":7.0,
"nouns":[{"word":"a woman","x":0.50,"y":0.42,"voice":"female"},
 {"word":"a big wheel","x":0.20,"y":0.17,"voice":"female"},
 {"word":"rocks","x":0.82,"y":0.33,"voice":"female"},
 {"word":"water","x":0.50,"y":0.82,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","riding","a","board","on","smooth","water."],
"answerVoice":"female",
"notes":"Two targets (woman twice, board once). The woman stands on the board, so the boxes are split at foot level; in the close top-down frames 0.0-2.5 the split is rough (her feet/legs lie over the board). Board is off at 14.5-15.0 (out of frame). 'to step off the board' happens only at about 13.5-14.5. 'rocks' = the grey concrete blocks of the breakwater; 'a big wheel' = the Ferris wheel in the background. Key word 'smooth' (adjective) is in the answer only."}
json.dump(c,open("content/4026.json","w"),indent=1)

# ---------- 4027
man={0.0:(.28,0,.68,1.0),0.5:(.23,0,.75,1.0),1.0:(.23,0,.77,1.0),1.5:(.29,0,.71,1.0),2.0:(.38,.03,.62,.97),2.5:(.44,.05,.56,.95),
3.0:(0,.09,.50,.60),3.5:(0,.09,.50,.62),4.0:(0,.09,.46,.66),4.5:(0,.09,.48,.62),5.0:(0,.09,.47,.62),5.5:(0,.09,.47,.62),
6.0:(0,0,.40,.61),6.5:(0,0,.36,.60),7.0:(0,0,.31,.56),7.5:(.60,0,.40,.97),8.0:(.48,.50,.52,.28),8.5:(.36,.45,.64,.27),
9.0:(.61,.52,.39,.13),9.5:(.84,.28,.16,.18),10.0:(.40,.37,.60,.16),10.5:(0,.19,.52,.56),11.0:(0,.19,.48,.63),11.5:(0,.19,.44,.60),
12.0:(0,.20,.40,.55),12.5:(0,.22,.37,.52),13.0:(0,.25,.37,.65),13.5:(0,.31,.40,.59),14.0:(0,.33,.44,.44),14.5:(0,.33,.44,.44),15.0:(0,.33,.42,.44)}
cow={0.0:(0,.19,.27,.64),0.5:(0,.19,.22,.62),1.0:(0,.19,.22,.79),1.5:(.04,.19,.24,.76),2.0:(0,.19,.37,.73),2.5:(0,.19,.43,.72),
3.0:(.51,.17,.49,.47),3.5:(.51,.17,.49,.43),4.0:(.47,.12,.53,.46),4.5:(.49,.09,.51,.47),5.0:(.48,.12,.52,.47),5.5:(.48,.14,.52,.46),
6.0:(.41,0,.59,.48),6.5:(.37,0,.63,.47),7.0:(.32,0,.68,.52),7.5:(.16,0,.43,.57),8.0:(.22,0,.78,.44),8.5:(.40,0,.60,.44),
9.0:(.38,.03,.62,.48),9.5:(.56,.03,.27,.62),10.0:(.55,0,.45,.36),10.5:(.53,0,.47,.66),11.0:(.49,.04,.51,.70),11.5:(.45,.07,.55,.66),
12.0:(.41,.02,.59,.70),12.5:(.38,.04,.62,.71),13.0:(.38,.04,.62,.84),13.5:(.41,0,.59,.80),14.0:(.45,0,.55,.68),14.5:(.45,0,.55,.68),15.0:(.43,0,.57,.68)}
c={"mediaId":4027,"level":"B","keyWord":"pie","defaultVoice":"male",
"taps":[
 {"phrase":"to roll out the dough","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to arrange apple slices","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to devour the whole pie","target":"the cow","voice":"male","keys":keys(cow)}],
"stillS":11.0,
"nouns":[{"word":"a pie","x":0.38,"y":0.77,"voice":"male"},
 {"word":"a cow","x":0.70,"y":0.45,"voice":"male"},
 {"word":"a man","x":0.26,"y":0.52,"voice":"male"},
 {"word":"a glass of milk","x":0.80,"y":0.72,"voice":"male"}],
"question":"What is the man baking?",
"answer":["He","is","baking","a","golden","apple","pie."],
"answerVoice":"male",
"notes":"Two targets (man twice, cow once). Clip has cuts at about 3.0, 6.0, 7.5 and 10.5 s. Man and cow stand side by side and overlap: boxes split along a vertical line between them, so the cow's hat / ear or the man's far hand can fall outside its box. 7.5-10.0: only the man's arm / hands are in the picture (boxes on those; 9.5 is just a hand at the right edge, 10.0 the arm crosses the cow, cow box = part above the arm). 'to devour the whole pie': the cow's muzzle is in the pie at 11.5-12.5 and the plate is empty from 13.0; the eating itself is short. Two forks and two chef's hats in the still, so neither is a noun. 'a glass of milk' pill is wide and sits near the right edge."}
json.dump(c,open("content/4027.json","w"),indent=1)

# ---------- 4028
dog={0.0:(.44,.41,.26,.24),0.5:(.41,.43,.23,.22),1.0:(.39,.43,.22,.22),1.5:(.39,.43,.22,.23),2.0:(.38,.44,.21,.22),2.5:(.37,.45,.21,.22),
3.0:(.36,.45,.23,.22),3.5:(.39,.46,.22,.21),4.0:(.45,.46,.21,.21),4.5:(.41,.46,.23,.21),5.0:(.42,.46,.21,.21),5.5:(.41,.46,.23,.20),
6.0:(.30,.46,.30,.19),6.5:(.33,.46,.31,.18),7.0:(.37,.45,.29,.18),7.5:(.44,.44,.26,.18),8.0:(.44,.44,.24,.18),8.5:(.46,.43,.24,.18),
9.0:(.53,.44,.18,.16),9.5:(.45,.44,.19,.16),10.0:(.38,.45,.18,.16),10.5:(.38,.45,.21,.16),11.0:(.37,.45,.25,.16),11.5:(.37,.45,.25,.17),
12.0:(.36,.45,.24,.19),12.5:(.36,.44,.25,.21),13.0:(.37,.43,.25,.23),13.5:(.38,.42,.27,.24),14.0:(.35,.36,.31,.32),14.5:(.30,.32,.41,.42),15.0:(.21,.24,.63,.74)}
flag={0.0:(.40,.24,.18,.14),0.5:(.43,.24,.18,.14),1.0:(.47,.25,.18,.14),1.5:(.51,.25,.18,.14),2.0:(.56,.24,.18,.14),2.5:(.59,.23,.18,.14),
3.0:(.61,.24,.18,.14),3.5:(.60,.24,.18,.14),4.0:(.58,.21,.18,.14),4.5:(.57,.19,.18,.14),5.0:(.57,.26,.18,.14),5.5:(.53,.26,.18,.14),
6.0:(.38,.07,.20,.23),6.5:(.13,0,.20,.27)}
c={"mediaId":4028,"level":"A","keyWord":"turn","defaultVoice":"female",
"taps":[
 {"phrase":"to ride a skateboard","target":"the dog","voice":"female","keys":keys(dog)},
 {"phrase":"to turn and come back","target":"the dog","voice":"female","keys":keys(dog)},
 {"phrase":"to hang on a pole","target":"the flag","voice":"female","keys":keys(flag)}],
"stillS":2.0,
"nouns":[{"word":"a dog","x":0.48,"y":0.55,"voice":"female"},
 {"word":"a flag","x":0.66,"y":0.30,"voice":"female"},
 {"word":"a tree","x":0.50,"y":0.15,"voice":"female"},
 {"word":"a road","x":0.50,"y":0.84,"voice":"female"}],
"question":"What is the dog doing?",
"answer":["It","is","riding","a","skateboard","on","the","road."],
"answerVoice":"female",
"notes":"Two targets (dog twice, flag once). The flag is small (minimum-size box) and visible only 0.0-6.5 s; from 7.0 it is out of frame. The dog turns at about 6.0-11.0 s and rides back towards the camera. Several caravans and cars, so neither is a noun. The flag pill lies in front of the big tree; the tree pill is higher up on the crown."}
json.dump(c,open("content/4028.json","w"),indent=1)
