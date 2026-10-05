import json
def b(t,x,y,w,h): return {"t":t,"x":x,"y":y,"w":w,"h":h}
def off(t): return {"t":t,"off":True}
man=[b(0.0,0,.10,1,.64),b(0.5,0,.10,1,.64),b(1.0,0,.10,1,.64),
 b(1.5,0,.08,.95,.92),b(2.0,0,0,.90,1.0),
 b(2.5,0,0,1,.75),b(3.0,0,0,1,.79),b(3.5,0,0,1,.79),b(4.0,0,0,1,.77),
 b(4.5,0,0,.62,.62),b(5.0,0,0,.86,.50),b(5.5,0,0,.86,.50),
 b(6.0,0,.55,.51,.32),b(6.5,0,.48,.51,.34),
 b(7.0,0,.64,.90,.36),b(7.5,0,.68,.50,.32),b(8.0,0,.14,.33,.34),off(8.5),
 b(9.0,0,0,.76,.47),b(9.5,0,0,.74,.62),
 b(10.0,0,.08,1,.61),b(10.5,0,.08,1,.62),b(11.0,0,.08,1,.66),b(11.5,0,.08,1,.66),b(12.0,0,.07,1,.67)]
mac=[b(0.0,.80,.75,.20,.25),b(0.5,.80,.75,.20,.25),b(1.0,.80,.75,.20,.25),
 off(1.5),off(2.0),
 b(2.5,.40,.76,.60,.24),b(3.0,.45,.80,.55,.20),b(3.5,.45,.80,.55,.20),b(4.0,.40,.78,.60,.22),
 b(4.5,0,.63,1,.37),b(5.0,0,.51,1,.49),b(5.5,0,.51,1,.49),
 b(6.0,.52,.28,.48,.72),b(6.5,.52,.28,.48,.72),
 b(7.0,0,.18,1,.45),b(7.5,0,.18,1,.49),b(8.0,.34,.03,.66,.97),b(8.5,0,.05,1,.95),
 b(9.0,.12,.48,.88,.52),b(9.5,0,.63,1,.37),
 b(10.0,.70,.70,.30,.30),b(10.5,.78,.71,.22,.29),b(11.0,.80,.75,.20,.25),b(11.5,.80,.75,.20,.25),b(12.0,.80,.75,.20,.25)]
d={"mediaId":4640,"level":"B","keyWord":"detergent","defaultVoice":"male",
"taps":[
 {"phrase":"to measure out the detergent","target":"the man","voice":"male","keys":man},
 {"phrase":"to frown at a stain","target":"the man","voice":"male","keys":man},
 {"phrase":"to spin the laundry","target":"the washing machine","voice":"male","keys":mac}],
"stillS":5.0,
"nouns":[{"word":"a bottle","x":.86,"y":.20,"voice":"male"},
 {"word":"a measuring cup","x":.44,"y":.37,"voice":"male"},
 {"word":"detergent","x":.50,"y":.64,"voice":"male"},
 {"word":"a drawer","x":.22,"y":.80,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","pouring","detergent","into","the","drawer."],
"answerVoice":"male",
"notes":"Clip with many cuts and close-ups. Target 'the man': his whole body in the first (0-1.0 s) and last (10-12 s) shots, only his hands/arms in the close-ups (1.5-9.5 s; the bottle he holds lies inside his box, it is not a target); no hand at 8.5 s -> off. At 6.0-6.5 s two hands are far apart, the box is on the lower hand that pushes the drawer. Target 'the washing machine': boxed wherever a part is visible; in the body shots only a narrow edge of a machine shows bottom right behind the T-shirt (small box, may be judged too hidden); in the close-ups the hands lie over the machine, so the boxes are split along straight lines and some machine surface is unboxed. 'to spin the laundry' relies on the 8.5 s shot of the closed door with washing in the drum - turning is hard to prove on a still. He frowns at the stain at 0.5-1.0 s. 'a measuring cup' = the small translucent dosing cup he tips out at 5.0 s."}
json.dump(d,open("content/4640.json","w"),indent=1,ensure_ascii=False)
