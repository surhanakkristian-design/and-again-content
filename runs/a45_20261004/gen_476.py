import json
R=lambda t,x0,y0,x1,y1:{"t":t,"x":round(x0,2),"y":round(y0,2),"w":round(x1-x0,2),"h":round(y1-y0,2)}
O=lambda t:{"t":t,"off":True}
T=[i/2 for i in range(31)]
S=[R(0.0,0,.02,.68,1),R(0.5,0,.02,.66,1),R(1.0,0,.02,.72,1),R(1.5,0,.03,.46,1),R(2.0,0,0,.52,1),R(2.5,0,0,.56,1),
R(3.0,0,.09,.24,.36),R(3.5,0,.08,.26,.36),R(4.0,0,.08,.27,.40),R(4.5,.42,.40,1,1),R(5.0,.38,.49,1,1),R(5.5,.45,.47,1,1),
R(6.0,.33,0,1,1),R(6.5,.36,0,1,1),R(7.0,.42,0,1,1),R(7.5,.45,0,1,1)]+[O(t) for t in T[16:]]
M=[O(t) for t in T[:6]]+[R(3.0,.25,0,1,.95),R(3.5,.27,0,1,.95),R(4.0,.28,0,1,.90),R(4.5,.08,0,.86,.40),R(5.0,.12,0,.82,.49),R(5.5,.05,0,.62,.47),
R(6.0,0,.30,.33,.74),R(6.5,0,.26,.36,.90),R(7.0,0,.33,.42,.76),R(7.5,0,.31,.45,.80)]+[R(t,0,.08,1,.86) for t in T[16:]]
d={"mediaId":476,"level":"B","keyWord":"microscope","defaultVoice":"male",
"taps":[{"phrase":"to adjust the focus knob","target":"the student","voice":"male","keys":S},
{"phrase":"to peer into the eyepiece","target":"the student","voice":"male","keys":S},
{"phrase":"to magnify a leaf","target":"the microscope","voice":"male","keys":M}],
"stillS":4.0,
"nouns":[{"word":"a microscope","x":.66,"y":.70,"voice":"male"},{"word":"a pencil","x":.78,"y":.83,"voice":"male"},
{"word":"lenses","x":.45,"y":.23,"voice":"male"}],
"question":"What is the student doing?","answer":["He","is","peering","into","a","microscope."],"answerVoice":"male",
"notes":"Close-up clip with cuts: the student is only his hands at 0-5.5 s and his face at 6-7.5 s; from 8 s the picture is the view through the eyepiece (counted as the microscope, student off). At 1.5-2.5 s the microscope is only a blur in the background, half behind the hand: off. Where hand and microscope overlap (4.5-7.5 s) the boxes are split along a straight line, so parts of the microscope base and of the face fall outside their box. He turns the blue focus knob at 4.5-5.5 s. Only 3 nouns: nothing else is clear at the still."}
json.dump(d,open("content/476.json","w"),indent=1,ensure_ascii=False)
