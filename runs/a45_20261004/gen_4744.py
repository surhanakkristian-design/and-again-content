import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        if v is None: out.append({"t":t,"off":True})
        else:
            x,y,w,h=v; out.append({"t":t,"x":round(x,2),"y":round(y,2),"w":round(w,2),"h":round(h,2)})
    return out
def dump(i,o):
    json.dump(o,open(f"content/{i}.json","w"),indent=1,ensure_ascii=False)

# ---------- 4744
hat={0.5:(0,0,1,1),1.0:(0,0,1,1),1.5:(0,.12,1,.88),2.0:(0,.18,1,.82),2.5:(0,.25,1,.75),
3.0:(0,.33,1,.67),3.5:(0,.34,1,.66),4.0:(0,.31,1,.69),4.5:(0,.29,1,.71),5.0:(0,.29,1,.71),5.5:(0,.28,1,.72),
6.0:(.20,.28,.70,.72),6.5:(.25,.27,.57,.73),7.0:(.25,.28,.57,.72),7.5:(.23,.29,.59,.69),8.0:(.25,.29,.57,.66),
8.5:(.25,.30,.57,.64),9.0:(.25,.33,.57,.62),9.5:(.25,.35,.57,.59),10.0:(.25,.37,.55,.56),10.5:(.25,.39,.55,.54),
11.0:(.25,.40,.55,.60),11.5:(.25,.42,.55,.58),12.0:(.25,.42,.52,.50)}
rear={3.0:(.52,.21,.48,.12),3.5:(.52,.20,.46,.14),4.0:(.54,.18,.46,.13),4.5:(.55,.16,.45,.13),5.0:(.55,.16,.45,.13),
5.5:(.56,.15,.44,.13),6.0:(.56,.13,.44,.14),6.5:(.57,.13,.43,.13),7.0:(.57,.14,.43,.14),7.5:(.57,.15,.43,.14),
8.0:(.57,.15,.43,.14),8.5:(.57,.16,.43,.14),9.0:(.57,.19,.43,.14),9.5:(.57,.21,.43,.14),10.0:(.57,.23,.43,.14),
10.5:(.57,.25,.43,.14),11.0:(.57,.26,.43,.14),11.5:(.57,.28,.43,.14),12.0:(.55,.28,.45,.14)}
dump(4744,{"mediaId":4744,"level":"A","keyWord":"to relax","defaultVoice":"female",
"taps":[
 {"phrase":"to read a magazine","target":"the woman in the hat","voice":"female","keys":keys(hat)},
 {"phrase":"to wear a big hat","target":"the woman in the hat","voice":"female","keys":keys(hat)},
 {"phrase":"to wear a black swimsuit","target":"the woman at the back","voice":"female","keys":keys(rear)}],
"stillS":10.0,
"nouns":[{"word":"a hat","x":.52,"y":.42,"voice":"female"},{"word":"a magazine","x":.53,"y":.51,"voice":"female"},
 {"word":"feet","x":.52,"y":.87,"voice":"female"},{"word":"hills","x":.35,"y":.07,"voice":"female"}],
"question":"What is the woman in front doing?",
"answer":["She","is","reading","a","magazine","in","the","water."],"answerVoice":"female",
"notes":"Two of three phrases are states (hat, black swimsuit): the two men and the second woman at the back only lie still, no action fits only one of them. The black swimsuit of the woman at the back is small (straps and top only). Her box is split from the hat woman's box along the top of the straw hat. Two rubber ducks are in the picture from about 8 s, so the duck is not used. Frame 0.0 is only fog: off."})

# ---------- 4745
man={0.0:(.28,0,.72,.66),0.5:(.45,0,.55,.72),1.0:(.48,0,.52,.47),1.5:(.52,0,.48,.40),2.0:(.74,0,.26,.66),2.5:(.76,0,.24,.72),
3.0:(.82,.74,.18,.24),8.0:(0,.17,.13,.22),8.5:(0,.17,.13,.60),9.0:(0,.18,.10,.74),9.5:(0,.18,.10,.74),10.0:(0,.40,.10,.42),
10.5:(0,.42,.10,.42),11.0:(0,.45,.10,.53),11.5:(0,.45,.11,.53),12.0:(0,.20,.11,.72)}
boat={0.0:(.12,.66,.40,.18),0.5:(.17,.60,.28,.20),1.0:(.40,.47,.22,.16),1.5:(.50,.41,.20,.15),2.0:(.52,.40,.20,.14),
2.5:(.51,.42,.20,.14),3.0:(.48,.46,.22,.14),3.5:(.21,.40,.26,.14),4.0:(.20,.42,.27,.14),4.5:(.25,.43,.27,.14),
5.0:(.28,.45,.26,.14),5.5:(.26,.45,.25,.14),6.0:(.27,.45,.22,.14),6.5:(.31,.45,.19,.14),7.0:(.32,.44,.18,.14),
7.5:(.35,.44,.18,.14),8.0:(.42,.49,.18,.14),8.5:(.39,.49,.18,.14),9.0:(.35,.48,.18,.14),9.5:(.31,.47,.18,.14),
10.0:(.28,.46,.18,.14),10.5:(.27,.45,.18,.14),11.0:(.25,.45,.18,.14),11.5:(.24,.44,.18,.14)}
bridge={7.0:(0,0,.36,.24),7.5:(0,0,.60,.27),8.0:(.13,0,.87,.46),8.5:(.13,0,.87,.48),9.0:(.10,0,.90,.47),9.5:(.10,0,.90,.46),
10.0:(.10,0,.90,.45),10.5:(.10,0,.90,.44),11.0:(.10,0,.90,.44),11.5:(.11,0,.89,.43),12.0:(.11,0,.89,.55)}
dump(4745,{"mediaId":4745,"level":"B","keyWord":"flow","defaultVoice":"male",
"taps":[
 {"phrase":"to crouch on the pebbles","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to drift downstream","target":"the paper boat","voice":"male","keys":keys(boat)},
 {"phrase":"to span the river","target":"the bridge","voice":"male","keys":keys(bridge)}],
"stillS":8.5,
"nouns":[{"word":"a stone bridge","x":.60,"y":.08,"voice":"male"},{"word":"rapids","x":.20,"y":.39,"voice":"male"},
 {"word":"a paper boat","x":.47,"y":.56,"voice":"male"},{"word":"grass","x":.30,"y":.88,"voice":"male"}],
"question":"Where is the river flowing?",
"answer":["It","is","flowing","under","a","stone","bridge."],"answerVoice":"male",
"notes":"The person is called a boy in the description but looks like a young adult with glasses: target 'the man'. He crouches only in 0-3 s; later he stands at the left edge (only a strip of him is visible, narrow box). From 9 s the paper boat is a very small white dot; at 12.0 it is not visible: off. The bridge box leaves out the strip at the left edge where the man stands and the lower end of the right pier where the boat box lies. 'to span the river' is a state of the bridge (no action possible)."})

# ---------- 4746
man={0.0:(.05,.52,.56,.48),0.5:(.05,.53,.58,.47),1.0:(.05,.54,.56,.46),1.5:(.05,.55,.55,.45),2.0:(.05,.54,.54,.46),
2.5:(.05,.53,.54,.47),3.0:(0,.54,.58,.46),3.5:(.05,.56,.54,.44),4.0:(0,.57,.58,.43),4.5:(0,.57,.58,.43),5.0:(0,.62,.57,.38),
5.5:(.05,.57,.53,.43),6.0:(.05,.53,.53,.47),6.5:(.05,.53,.53,.47),7.0:(0,.54,.57,.46),7.5:(0,.55,.56,.45),8.0:(0,.61,.57,.39),
8.5:(.05,.67,.52,.33),9.0:(.05,.72,.52,.28),9.5:(0,.75,.54,.25),10.0:(0,.55,.52,.45),10.5:(.20,.62,.30,.38),11.0:(.28,.76,.24,.24)}
ph={0.0:(.61,.51,.39,.29),0.5:(.63,.51,.37,.30),1.0:(.62,.52,.38,.30),1.5:(.60,.52,.40,.30),2.0:(.59,.54,.41,.28),
2.5:(.59,.52,.41,.30),3.0:(.58,.53,.42,.30),3.5:(.59,.53,.41,.30),4.0:(.58,.54,.42,.30),4.5:(.58,.56,.42,.28),5.0:(.57,.57,.43,.28),
5.5:(.58,.57,.42,.26),6.0:(.58,.53,.42,.30),6.5:(.58,.52,.42,.32),7.0:(.57,.52,.43,.33),7.5:(.56,.52,.44,.33),8.0:(.57,.52,.43,.33),
8.5:(.57,.53,.43,.33),9.0:(.57,.55,.43,.33),9.5:(.55,.57,.45,.35),10.0:(.54,.64,.46,.36),10.5:(.56,.84,.44,.16)}
plane={0.0:(.32,.37,.30,.14),0.5:(.25,.26,.42,.24),1.0:(.41,.40,.18,.14),1.5:(.42,.41,.18,.14),2.0:(.41,.40,.22,.14),
2.5:(.40,.38,.24,.14),3.0:(.38,.35,.28,.17),3.5:(.36,.30,.34,.22),4.0:(.33,.19,.46,.35),4.5:(.26,0,.72,.55),5.0:(.38,.43,.28,.14),
5.5:(.36,.42,.30,.14),6.0:(.33,.39,.36,.14),6.5:(.31,.38,.40,.14),7.0:(.27,.37,.45,.15),7.5:(.25,.35,.49,.17),8.0:(.23,.32,.54,.19),
8.5:(.19,.29,.63,.22),9.0:(.15,.24,.70,.28),9.5:(.09,.16,.80,.37),10.0:(.02,.02,.94,.52),10.5:(0,0,1,.59),11.0:(0,0,1,.66),
11.5:(0,0,1,.75),12.0:(0,0,1,.78)}
dump(4746,{"mediaId":4746,"level":"A","keyWord":"photographer","defaultVoice":"male",
"taps":[
 {"phrase":"to point at the plane","target":"the man in the blue jacket","voice":"male","keys":keys(man)},
 {"phrase":"to take photos of planes","target":"the photographers","voice":"male","keys":keys(ph)},
 {"phrase":"to fly over the men","target":"the plane","voice":"male","keys":keys(plane)}],
"stillS":7.5,
"nouns":[{"word":"a plane","x":.50,"y":.45,"voice":"male"},{"word":"a photographer","x":.83,"y":.72,"voice":"male"},
 {"word":"a jacket","x":.30,"y":.88,"voice":"male"},{"word":"the sky","x":.30,"y":.15,"voice":"male"}],
"question":"What is the photographer doing?",
"answer":["He","is","taking","photos","of","a","plane."],"answerVoice":"male",
"notes":"Three planes fly over one after another (a small propeller plane 0-0.5 s, a jet 1-4.5 s, the jumbo 5-12 s) and two are in the air at once until 4.5 s: the plane box is the union of the planes in the air, so a tap on any flying plane counts. Parked planes on the apron are outside it. The man in the jacket points only at 10-11 s; his box is cut at the telephoto lens and loses the right part of his jacket; the photographers box (the group on the right, heads, cameras, bodies) stops at y about 0.8 so that it does not take the jacket. Noun 'a plane' sits on the big flying plane; small parked planes are far in the background."})

# ---------- 4747
M={0.0:(.63,.42,.37,.58),0.5:(.59,.41,.41,.59),1.0:(.58,.42,.42,.58),1.5:(.59,.42,.41,.58),2.0:(.57,.42,.43,.58),
2.5:(.57,.44,.43,.56),3.0:(.54,.46,.46,.54),3.5:(.52,.47,.48,.53),4.0:(.51,.46,.49,.54),4.5:(.51,.46,.49,.54),
5.0:(.36,.46,.64,.54),5.5:(.30,.46,.70,.54),6.0:(.18,.47,.72,.53),6.5:(.18,.48,.74,.52),7.0:(.17,.49,.76,.51),
7.5:(.17,.50,.76,.50),8.0:(.14,.50,.76,.50),8.5:(.14,.51,.76,.49),9.0:(.16,.53,.74,.47),9.5:(.15,.53,.75,.47),
10.0:(.13,.53,.78,.47),10.5:(.12,.53,.78,.47),11.0:(.12,.53,.78,.47),11.5:(.17,.55,.75,.45),12.0:(.14,.53,.80,.47)}
G={0.0:(0,.26,.63,.36),0.5:(0,.26,.59,.36),1.0:(0,.40,.58,.24),1.5:(.20,.40,.39,.23),2.0:(.06,.32,.51,.32),
2.5:(0,.26,.57,.36),3.0:(0,.26,.54,.34),3.5:(.03,.26,.49,.30),4.0:(.12,.27,.39,.33),4.5:(0,.14,.51,.47),
5.0:(0,.16,1,.30),5.5:(0,.10,1,.36),6.0:(0,.04,1,.43),6.5:(0,.04,1,.44),7.0:(0,0,1,.49),7.5:(0,0,1,.50),8.0:(0,0,1,.50),
8.5:(0,0,1,.51),9.0:(0,0,1,.53),9.5:(0,0,1,.53),10.0:(0,0,1,.53),10.5:(0,0,1,.53),11.0:(0,0,1,.53),11.5:(0,0,1,.55),12.0:(0,0,1,.53)}
dump(4747,{"mediaId":4747,"level":"A","keyWord":"seagull","defaultVoice":"male",
"taps":[
 {"phrase":"to hold some bread","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to smile at the birds","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to fly around the man","target":"the seagulls","voice":"male","keys":keys(G)}],
"stillS":0.5,
"nouns":[{"word":"a seagull","x":.28,"y":.47,"voice":"male"},{"word":"a cap","x":.72,"y":.47,"voice":"male"},
 {"word":"bread","x":.86,"y":.82,"voice":"male"},{"word":"the sea","x":.20,"y":.70,"voice":"male"}],
"question":"What are the seagulls doing?",
"answer":["They","are","flying","around","the","man."],"answerVoice":"male",
"notes":"Only two targets (the man, the seagulls). 0-4.5 s: one seagull hangs at the man's left shoulder and overlaps him, so the picture is split left/right: the man's box keeps his head and the right part of his body and loses his left arm. From 5 s the seagulls are everywhere: their box is the whole band of sky above the man's cap; birds that fly lower at his sides (e.g. 7.5 s, 9.0 s right of his head) fall outside it or into the man's box. Still picture 0.5 s is chosen because exactly one seagull is in the picture there."})
