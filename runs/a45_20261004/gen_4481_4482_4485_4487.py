import json
def k(t,b): return {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} if b else {"t":t,"off":True}
def keys(T,M): return [k(t,M.get(t)) for t in T]
def T(n): return [i*0.5 for i in range(n)]
def save(d): json.dump(d,open("content/%d.json"%d["mediaId"],"w"),indent=1,ensure_ascii=False)

# ---------- 4481
t=T(19)
W={0:(0,.19,1,.81),.5:(0,.20,1,.80),1:(0,.19,1,.81),1.5:(0,.18,1,.82),2:(0,.13,1,.87),
2.5:(.15,.18,.85,.82),3:(.10,.19,.90,.81),3.5:(.32,.22,.68,.78),4:(0,.17,.82,.83),4.5:(.22,.17,.78,.83),
5:(.70,.37,.30,.63),5.5:(.63,.34,.37,.66),6:(.62,.40,.38,.60),6.5:(.62,.43,.38,.57),7:(.62,.46,.38,.54),
7.5:(.62,.43,.38,.57),8:(.61,.40,.39,.60),8.5:(.63,.40,.37,.60),9:(.61,.40,.39,.60)}
TR={5:(.30,.46,.40,.54),5.5:(.25,.50,.38,.50),6:(.22,.48,.40,.52),6.5:(.22,.50,.40,.50),7:(.22,.53,.40,.47),
7.5:(.22,.56,.40,.44),8:(.20,.50,.41,.50),8.5:(.22,.50,.41,.50),9:(.20,.49,.41,.51)}
save({"mediaId":4481,"level":"A","keyWord":"focus","defaultVoice":"female",
"taps":[
{"phrase":"to focus a big camera","target":"the woman","voice":"female","keys":keys(t,W)},
{"phrase":"to close one eye","target":"the woman","voice":"female","keys":keys(t,W)},
{"phrase":"to stand on three legs","target":"the tripod","voice":"female","keys":keys(t,TR)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":.70,"y":.12,"voice":"female"},{"word":"a camera","x":.22,"y":.31,"voice":"female"},
{"word":"a woman","x":.80,"y":.60,"voice":"female"},{"word":"houses","x":.13,"y":.80,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","focusing","her","big","camera."],
"answerVoice":"female",
"notes":"Three shots: flower stall with a small silver camera (0-2 s), street with a DSLR (2.5-4.5 s), viewpoint with a huge lens on a tripod (5-9 s). Only one person is a usable target (a cyclist passes for one frame at 3.0 s), so two phrases share the woman and the third is the tripod (a state, no action fits a thing). 'to close one eye' is the wink at 0.5-1.0 s. In the last shot the tripod legs cross her body: split along a vertical line at the right edge of the tripod head, so the right tripod leg lies in her box and her left hand on the pan handle (6.5-7.0 s) lies in the tripod box. Noun 'a camera' sits on the long lens of the big camera at 8.0 s."})

# ---------- 4482
t=T(21)
W={0:(0,.27,.50,.53),.5:(0,.28,.50,.52),1:(0,.29,.50,.60),1.5:(0,.30,.57,.57),2:(0,.30,.58,.47),
2.5:(0,.26,.96,.74),3:(0,.28,.93,.72),3.5:(0,.29,.95,.71),4:(0,.28,.95,.72),4.5:(0,.28,.95,.72),5:(0,.28,.93,.72),5.5:(0,.27,.93,.73),
6:(.48,.43,.52,.57),6.5:(.48,.43,.52,.57),7:(.48,.43,.52,.57),7.5:(.48,.43,.52,.57),8:(.48,.43,.52,.57),8.5:(.48,.43,.52,.57),
9:(.48,.40,.52,.60),9.5:(.57,.38,.43,.62),10:(.55,.39,.45,.61)}
TR={6:(.12,.55,.36,.45),6.5:(.12,.55,.36,.45),7:(.12,.55,.36,.45),7.5:(.12,.55,.36,.45),8:(.12,.55,.36,.45),8.5:(.12,.55,.36,.45),
9:(.10,.56,.38,.44),9.5:(.10,.55,.47,.45),10:(.10,.54,.45,.46)}
save({"mediaId":4482,"level":"B","keyWord":"shoot","defaultVoice":"female",
"taps":[
{"phrase":"to shoot the rooftops","target":"the woman","voice":"female","keys":keys(t,W)},
{"phrase":"to give a thumbs up","target":"the woman","voice":"female","keys":keys(t,W)},
{"phrase":"to support a heavy lens","target":"the tripod","voice":"female","keys":keys(t,TR)}],
"stillS":8.0,
"nouns":[{"word":"a lens","x":.20,"y":.44,"voice":"female"},{"word":"rooftops","x":.15,"y":.63,"voice":"female"},
{"word":"a braid","x":.87,"y":.70,"voice":"female"},{"word":"a tripod","x":.35,"y":.86,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","shooting","the","rooftops","with","a","huge","lens."],
"answerVoice":"female",
"notes":"Three shots: flower stall filmed from her own eyes (0-2 s, only her arm and the small camera are visible: her box there is the arm with the camera), street with a DSLR (2.5-5.5 s), terrace with a huge lens on a tripod (6-10 s). Only one person, so two phrases share the woman; the third is the tripod. The thumbs up is at 9.5-10 s only. On the terrace her body stands behind the right tripod leg: vertical split at the right edge of the tripod head, the right leg lies in her box. 'a braid' pill sits on her back where the braid hangs at 8.0 s."})

# ---------- 4485
t=T(25)
M={0:(.30,.62,.70,.38),.5:(0,.34,1,.66),1:(.05,.42,.95,.58),1.5:(.04,.46,.96,.54),2:(.05,.47,.93,.53),2.5:(.06,.49,.94,.51),
3:(.05,.64,.92,.36),3.5:(.04,.65,.96,.35),
4:(.03,.40,.67,.60),4.5:(.08,.38,.67,.62),5:(.12,.38,.61,.62),5.5:(.10,.37,.66,.63),6:(.10,.38,.66,.62),6.5:(.10,.40,.65,.60),
7:(.17,.42,.83,.58),7.5:(.25,.43,.75,.57),8:(.06,.42,.94,.58),8.5:(0,.40,1,.60),9:(.02,.35,.98,.65),9.5:(0,.39,1,.61),
10:(.02,.40,.98,.60),10.5:(.08,.38,.92,.62),11:(.08,.38,.92,.62),11.5:(.08,.38,.92,.62),12:(.04,.38,.96,.62)}
MT={.5:(0,0,1,.30),1:(0,0,1,.34),1.5:(0,0,1,.35),2:(0,0,1,.35),2.5:(0,.02,1,.36),3:(0,.03,1,.38),3.5:(0,.04,1,.37),4:(0,.05,1,.33)}
WF={4:(.70,.42,.30,.17),4.5:(.75,.36,.25,.21),5:(.73,.34,.27,.20),5.5:(.76,.33,.24,.20),6:(.76,.30,.24,.22),6.5:(.75,.31,.25,.22)}
save({"mediaId":4485,"level":"A","keyWord":"powerful","defaultVoice":"male",
"taps":[
{"phrase":"to hold a red leaf","target":"the man","voice":"male","keys":keys(t,M)},
{"phrase":"to fall with great power","target":"the waterfall","voice":"male","keys":keys(t,WF)},
{"phrase":"to have snow on top","target":"the mountains","voice":"male","keys":keys(t,MT)}],
"stillS":2.0,
"nouns":[{"word":"mountains","x":.28,"y":.14,"voice":"male"},{"word":"trees","x":.76,"y":.28,"voice":"male"},
{"word":"a lake","x":.74,"y":.52,"voice":"male"},{"word":"a man","x":.50,"y":.72,"voice":"male"}],
"question":"What is the man holding?",
"answer":["He","is","holding","a","red","leaf."],
"answerVoice":"male",
"notes":"Three shots: canoe on a lake (0-3.5 s; at 0.0 s only his hand on the paddle), waterfall (4-6.5 s, 4.0 s is a dissolve where the mountains are still faintly visible and the falls already show at the right), red forest (7-12 s, the leaf from 9.5 s). The key word is an adjective; it is carried by the waterfall phrase ('with great power'). The waterfall runs behind his head: its box is only the clear curve of falling water right of his hood, and the man's box is cut at that line during the waterfall shot, so his outstretched arm at the lower right falls outside his box there. Falling water directly above his head (x .5-.7) is in no box. 'to have snow on top' is a state: no action fits the mountains."})

# ---------- 4487
t=T(25)
M={0:(0,.03,.80,.97),.5:(0,.08,.72,.92),1:(0,.08,.60,.92),1.5:(0,.02,.56,.98),2:(0,.03,.45,.97),2.5:(0,0,.33,1),3:(0,0,.36,1),3.5:(0,0,.33,1),
4:(0,.05,.40,.95),4.5:(0,.05,.50,.95),
5:(.44,.17,.56,.83),5.5:(.46,.17,.54,.83),6:(.49,.12,.51,.88),6.5:(.51,.19,.49,.81),7:(.48,.14,.52,.86),7.5:(.50,.15,.50,.85),
8:(.40,.15,.60,.85),8.5:(.41,.19,.59,.81),9:(.43,.20,.57,.80),
9.5:(.57,.27,.32,.36),10:(.62,.23,.33,.40),10.5:(.58,.23,.36,.40),11:(.59,.25,.34,.40),11.5:(.58,.26,.34,.40),12:(.57,.26,.36,.38)}
C={2.5:(.72,.30,.26,.20),3:(.53,.38,.30,.19),3.5:(.63,.40,.26,.22),4:(.64,.42,.28,.29),4.5:(.60,.38,.40,.40)}
O={5:(.23,.19,.20,.22),5.5:(.23,.21,.20,.24),6:(.28,.23,.20,.25),6.5:(.33,.24,.18,.26),7:(.27,.26,.20,.27),7.5:(.14,.26,.22,.28),
8:(.06,.23,.22,.29),8.5:(.16,.23,.23,.28),9:(.20,.27,.22,.27)}
save({"mediaId":4487,"level":"A","keyWord":"kind","defaultVoice":"male",
"taps":[
{"phrase":"to push the snow away","target":"the man","voice":"male","keys":keys(t,M)},
{"phrase":"to stand at the goal","target":"the child","voice":"male","keys":keys(t,C)},
{"phrase":"to wave from the door","target":"the old woman","voice":"female","keys":keys(t,O)}],
"stillS":8.0,
"nouns":[{"word":"a hat","x":.72,"y":.29,"voice":"male"},{"word":"a woman","x":.17,"y":.36,"voice":"female"},
{"word":"snow","x":.14,"y":.62,"voice":"male"},{"word":"a jacket","x":.80,"y":.72,"voice":"male"}],
"question":"Where is the man pushing the snow?",
"answer":["He","is","pushing","the","snow","off","the","path."],
"answerVoice":"male",
"notes":"Three shots: hockey on a frozen pond (0-4.5 s, the child in the orange jacket at the goal from 2.5 s), snow shovelling in front of a house with an old woman waving in the doorway (5-9 s), pancakes with four children (9.5-12 s; the children there are not targets). The man also raises his hand to wave back at 7.5 s, hence 'from the door' in the old woman's phrase. The child's gender is not clear, so the target is 'the child' with the default voice. At 6.0-7.0 s the woman stands right beside his hat: the boxes meet at a vertical line and his gloves on the shovel (lower left of him) fall just outside his box. The key word 'kind' is an adjective and not visible as such; it is not in the texts."})
