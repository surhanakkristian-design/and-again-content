import json
def K(t,b): return {"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]}
def keys(times,d): return [K(t,d.get(t)) for t in times]
def T(n,end): return [round(i*0.5,1) for i in range(int(end/0.5)+1)]
out={}
# ---- 89
t=T(0,6.0)
black={0.0:(.37,.11,.30,.22),0.5:(.36,.07,.30,.25),1.0:(.41,.08,.29,.26),1.5:(.40,.15,.30,.20),2.0:(.40,.15,.29,.19),
2.5:(.40,.16,.27,.19),3.0:(.40,.16,.26,.21),3.5:(.41,.17,.26,.21),4.0:(.41,.16,.25,.19),4.5:(.42,.17,.25,.19),5.0:(.41,.18,.25,.19),5.5:(.42,.18,.25,.19),6.0:(0,0,1,1)}
rope={0.0:(.30,0,.24,.10),0.5:(.32,0,.24,.065),1.0:(.22,0,.19,.14),1.5:(.35,0,.22,.145),2.0:(.31,0,.22,.14),2.5:(.34,0,.22,.15),
3.0:(.30,0,.22,.14),3.5:(.34,0,.22,.15),4.0:(.30,0,.22,.15),4.5:(.34,0,.22,.15),5.0:(.30,0,.22,.15),5.5:(.34,0,.22,.16)}
tab={x:(.30,.53,.26,.22) for x in t if x<6.0}
out[89]={"mediaId":89,"level":"A","keyWord":"cat","defaultVoice":"male",
"taps":[{"phrase":"to jump off the tower","target":"the black cat","voice":"male","keys":keys(t,black)},
{"phrase":"to sit under the black cat","target":"the brown cat","voice":"male","keys":keys(t,tab)},
{"phrase":"to hang from the ceiling","target":"the rope","voice":"male","keys":keys(t,rope)}],
"stillS":2.0,
"nouns":[{"word":"a cat","x":.52,"y":.25,"voice":"male"},{"word":"a rope","x":.42,"y":.08,"voice":"male"},
{"word":"a door","x":.78,"y":.55,"voice":"male"},{"word":"a mirror","x":.13,"y":.45,"voice":"male"}],
"question":"What is the black cat doing?","answer":["It","is","jumping","off","the","tower."],"answerVoice":"male",
"notes":"The black cat sits on top for 5.5 s and jumps only at the very end (t=6.0 it fills the frame). Two cats: the 'a cat' pill sits on the black one; the brown cat is not a noun. At t=0.5 the black cat's paws touch the rope knot, boxes split at y=0.065 (rope box thin there)."}
# ---- 90
t=T(0,9.0)
p={0.0:(.30,.15,.46,.58),0.5:(.27,.11,.55,.63),1.0:(.27,.12,.54,.70),1.5:(.28,.16,.52,.70),2.0:(.26,.17,.47,.60),2.5:(.24,.12,.63,.64),
3.0:(.24,.12,.62,.71),3.5:(.32,.18,.51,.69),4.0:(.34,.18,.46,.58),4.5:(.18,.13,.64,.62),5.0:(.22,.18,.53,.69),5.5:(.24,.19,.51,.73),
6.0:(.20,.11,.66,.68),6.5:(.27,.18,.62,.62),7.0:(.33,.18,.50,.71),7.5:(.25,.14,.60,.72),8.0:(.21,.17,.60,.63),8.5:(.14,.16,.55,.65),9.0:(.13,.14,.59,.71)}
pk=keys(t,p)
out[90]={"mediaId":90,"level":"A","keyWord":"puppy","defaultVoice":"female",
"taps":[{"phrase":"to stand on two legs","target":"the puppy","voice":"female","keys":pk},
{"phrase":"to dance in the water","target":"the puppy","voice":"female","keys":pk},
{"phrase":"to show its pink tongue","target":"the puppy","voice":"female","keys":pk}],
"stillS":4.0,
"nouns":[{"word":"a puppy","x":.55,"y":.45,"voice":"female"},{"word":"water","x":.22,"y":.78,"voice":"female"},
{"word":"bottles","x":.58,"y":.10,"voice":"female"}],
"question":"What is the puppy doing?","answer":["It","is","dancing","in","the","water."],"answerVoice":"female",
"notes":"Only one possible target (the puppy) for all three phrases. 'a bath' left out as a noun because it could not be told apart from 'water'."}
# ---- 91
t=T(0,10.0)
F=(0,0,1,1)
w={0.0:(.24,.09,.62,.91),0.5:F,1.0:F,1.5:(0,.41,1,.26),2.0:(0,.47,.78,.25),2.5:(0,.03,.27,.70),
4.5:(.77,0,.23,1),5.0:(.58,0,.42,1),5.5:(.77,0,.23,1),6.0:(.57,0,.43,1),6.5:(.77,0,.23,1),
7.0:(.62,.08,.38,.92),7.5:(.64,.08,.36,.92),8.0:(.59,.18,.41,.82),8.5:(.60,.18,.40,.82),9.0:(.60,.20,.40,.80),9.5:(.60,.20,.40,.80),10.0:(.59,.17,.41,.83)}
b={2.5:(.72,0,.28,1),3.0:(.06,.05,.92,.95),3.5:(0,.07,1,.93),4.0:(0,.04,1,.96),
4.5:(0,0,.77,1),5.0:(0,0,.58,1),5.5:(0,0,.77,1),6.0:(0,0,.57,1),6.5:(0,0,.77,1),
7.0:(0,0,.41,1),7.5:(0,0,.40,1),8.0:(0,.15,.41,.85),8.5:(0,.15,.42,.85),9.0:(0,.18,.42,.82),9.5:(0,.18,.42,.82),10.0:(0,.16,.40,.84)}
c={7.0:(.41,.38,.20,.20),7.5:(.41,.39,.22,.24),8.0:(.41,.43,.18,.14),8.5:(.42,.44,.18,.15),9.0:(.42,.43,.18,.20),9.5:(.42,.43,.18,.20),10.0:(.40,.42,.19,.20)}
out[91]={"mediaId":91,"level":"B","keyWord":"blame","defaultVoice":"female",
"taps":[{"phrase":"to blame the boy","target":"the woman","voice":"female","keys":keys(t,w)},
{"phrase":"to cross his arms","target":"the boy","voice":"male","keys":keys(t,b)},
{"phrase":"to lurk under the table","target":"the cat","voice":"female","keys":keys(t,c)}],
"stillS":10.0,
"nouns":[{"word":"an apron","x":.82,"y":.72,"voice":"female"},{"word":"paw prints","x":.50,"y":.85,"voice":"female"},
{"word":"a hoodie","x":.18,"y":.70,"voice":"female"},{"word":"headphones","x":.17,"y":.52,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","blaming","the","boy","for","the","mess."],"answerVoice":"female",
"notes":"Many cuts and close-ups. t=1.5/2.0 show only the woman's pointing arm (boxed as the woman). In the two-shots 4.5-6.5 woman and boy overlap (her finger on his sleeve): split by a vertical line, so part of his sleeve lies in her box. At 8.0/8.5 both point at the cat and their fingertips are cut out of their boxes to keep the cat's box free. The boy crosses his arms only at 9.5-10.0. 'to blame' is read from her angry pointing at him; the cat is under the table at 7.0-7.5 and in front of it afterwards. 'headphones' and 'a hoodie' are both on the boy, 0.18 apart in y."}
# ---- 96
t=T(0,8.0)
y={0.0:(0,.27,.50,.73),0.5:(.08,.37,.56,.63),1.0:(0,.52,.69,.48),7.5:(.05,0,.95,1),8.0:(0,.30,.97,.70)}
fa={3.5:(.42,.19,.29,.65)}
m={4.0:(.18,.37,.38,.46),4.5:(0,.40,.42,.60),5.0:(.08,.33,.32,.33),5.5:(.26,.37,.33,.32),6.0:(.24,.37,.35,.50),6.5:(0,.37,.44,.63),7.0:(0,.55,.28,.45)}
out[96]={"mediaId":96,"level":"B","keyWord":"board","defaultVoice":"female",
"taps":[{"phrase":"to scan a boarding pass","target":"the woman in yellow","voice":"female","keys":keys(t,y)},
{"phrase":"to welcome passengers aboard","target":"the flight attendant","voice":"female","keys":keys(t,fa)},
{"phrase":"to flick through a magazine","target":"the man in the suit","voice":"male","keys":keys(t,m)}],
"stillS":6.5,
"nouns":[{"word":"a magazine","x":.20,"y":.75,"voice":"female"},{"word":"curtains","x":.56,"y":.28,"voice":"female"},
{"word":"the aisle","x":.62,"y":.90,"voice":"female"}],
"question":"What is the woman in yellow doing?","answer":["She","is","boarding","the","plane."],"answerVoice":"female",
"notes":"POV clip: the woman in yellow is only an arm at 0-1.0 and a face at 7.5-8.0; the flight attendant is on screen only at 3.5 (one frame time). The man in the suit is passed twice (4.0-4.5, then again 5.0-6.5, 7.0 only his dark shoulder at the left edge). A tiny figure far down the aisle (x~0.6, y~0.3) from 4.0 to 7.0 may be another attendant, not boxed. The answer covers the whole clip (gate, jet bridge, cabin), no single frame shows 'boarding'."}
for i,d in out.items(): json.dump(d,open(f"content/{i}.json","w"),indent=1,ensure_ascii=False)
