import json
def b(t,x,y,w,h): return {"t":t,"x":x,"y":y,"w":w,"h":h}
def off(t): return {"t":t,"off":True}
T=[i*0.5 for i in range(29)]
W={0.0:(.17,.43,.66,.57),0.5:(.19,.41,.66,.59),1.0:(.15,.43,.68,.57),1.5:(.17,.41,.66,.59),2.0:(.12,.40,.70,.60),2.5:(.14,.40,.68,.60),3.0:(.10,.40,.73,.60),
 3.5:(.10,.24,.90,.76),4.0:(.10,.26,.90,.74),4.5:(.10,.28,.90,.72),5.0:(.10,.33,.90,.67),5.5:(.10,.38,.90,.62),6.0:(.10,.41,.90,.59),6.5:(.10,.45,.90,.55),7.0:(.12,.50,.88,.50),7.5:(.17,.53,.83,.47)}
P={8.0:(.10,0,.88,1),8.5:(.08,0,.92,1),9.0:(.08,0,.90,1),9.5:(.08,0,.92,1),10.0:(.10,0,.85,1),10.5:(.10,.03,.87,.97),11.0:(.14,.08,.78,.92),11.5:(.15,.14,.78,.86),
 12.0:(.16,.17,.73,.83),12.5:(.16,.22,.76,.78),13.0:(.16,.28,.70,.72),13.5:(.16,.33,.72,.67),14.0:(.18,.35,.68,.65)}
for t in T:
    if 3.5<=t<=7.5: P[t]=(.07,0,.64,W[t][1])
k=lambda M:[b(t,*M[t]) if t in M else off(t) for t in T]
c={"mediaId":11,"level":"A","keyWord":"library","defaultVoice":"female",
"taps":[{"phrase":"to carry a big bag","target":"the woman","voice":"female","keys":k(W)},
 {"phrase":"to walk between the shelves","target":"the woman","voice":"female","keys":k(W)},
 {"phrase":"to be tall and round","target":"the book tower","voice":"female","keys":k(P)}],
"stillS":4.0,
"nouns":[{"word":"books","x":0.35,"y":0.15,"voice":"female"},{"word":"hair","x":0.70,"y":0.42,"voice":"female"},
 {"word":"a coat","x":0.70,"y":0.72,"voice":"female"},{"word":"a bag","x":0.38,"y":0.90,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","looking","up","at","the","books."],
"answerVoice":"female",
"notes":"Only one person. Third phrase is a state on the round tower of books (no thing in the clip does an action); target name 'the book tower'. From 3.5 to 7.5 the woman stands in front of the tower: the tower box is the part above her head. From 8.0 she is out of the picture. Key word 'library' is the whole place, so it is not a noun slot; 'books' sits on the tower."}
json.dump(c,open('content/11.json','w'),indent=1)
