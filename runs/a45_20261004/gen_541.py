import json
T=[i*0.5 for i in range(21)]
def keys(d):
    out=[]
    for t in T:
        b=d.get(t)
        out.append({"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":round(b[2]-b[0],2),"h":round(b[3]-b[1],2)})
    return out
W={0.0:(0,.44,.60,.97),0.5:(0,.39,.62,.97),1.0:(0,.37,.92,1),1.5:(0,.48,1,1),2.0:(0,.37,1,1),2.5:(.82,.47,1,.68),
   3.0:(0,.49,1,1),3.5:(0,.64,1,1),4.0:(0,.50,1,1),4.5:(.55,.35,1,1),5.0:(.35,.30,.95,1),5.5:(.77,.46,1,1),
   6.0:(0,0,.52,1),6.5:(0,.48,.82,1),7.0:(0,.05,.58,1),7.5:(0,.44,.85,1),8.0:(0,.42,.90,1),8.5:(0,.42,.95,1),
   9.0:(0,.46,.92,1),9.5:(0,.50,.67,1),10.0:(0,.03,.46,1)}
M={0.0:(.66,.08,1,.60),0.5:(.71,0,1,.55),1.0:(.42,.22,1,.37),1.5:(.40,.14,1,.34),2.0:(.28,0,1,.27),2.5:(.26,0,1,.30),
   3.0:(.70,0,1,.49),3.5:(.61,0,1,.63),4.0:(.68,0,1,.48),4.5:(.18,0,1,.30),5.0:(.18,0,1,.27),5.5:(.20,0,1,.33),
   6.0:(.70,0,1,.52),6.5:(.70,0,1,.48),7.0:(.76,.05,1,.60),7.5:(.35,.17,1,.42),8.0:(.31,0,1,.33),8.5:(.33,0,1,.34),
   9.0:(.71,0,1,.44),9.5:(.75,0,1,.66),10.0:(.64,.10,1,.65)}
C={0.0:(.46,.16,.66,.38),0.5:(.53,.10,.71,.33),1.0:(.59,0,.78,.22),1.5:(.64,0,.84,.14),3.0:(.52,0,.70,.26),3.5:(.43,.16,.61,.42),
   4.0:(.50,0,.68,.18),6.0:(.52,.04,.70,.27),6.5:(.52,.07,.70,.30),7.0:(.58,.07,.76,.30),7.5:(.60,0,.80,.17),9.0:(.53,0,.71,.21),
   9.5:(.46,.11,.70,.33),10.0:(.46,.22,.64,.41)}
c={"mediaId":541,"level":"A","keyWord":"pencil","defaultVoice":"female",
 "taps":[{"phrase":"to draw with a pencil","target":"the woman","voice":"female","keys":keys(W)},
         {"phrase":"to clap his hands","target":"the man","voice":"male","keys":keys(M)},
         {"phrase":"to sit in the window","target":"the cat","voice":"female","keys":keys(C)}],
 "stillS":9.0,
 "nouns":[{"word":"a pencil","x":.22,"y":.76,"voice":"female"},{"word":"a cat","x":.62,"y":.10,"voice":"female"},
          {"word":"fruit","x":.14,"y":.31,"voice":"female"},{"word":"a notebook","x":.50,"y":.61,"voice":"female"}],
 "question":"What is the woman doing?",
 "answer":["She","is","drawing","with","a","pencil."],"answerVoice":"female",
 "notes":"Many cuts. The woman is mostly only hands and arms over the notebook; her box follows the drawing hand and arms. Her face (left edge) is inside her box only at 6.0, 7.0 and 10.0 s; at 1.5, 3.0, 3.5, 4.0, 6.5, 7.5 s it is outside, because one rectangle with face and drawing hand would cover the man or the cat. At 6.0 and 10.0 s her box is cut at the cat's left edge, so the tip of her right hand is outside. The man's box is cut where the cat sits beside him (3.0, 4.0, 6.0-7.0, 9.0 s: his face and chest, not his arm on the table). The man claps only at 9.5-10 s. Cat at 1.5 s is only its lower body at the top edge. 'fruit': a bowl of orange fruit (apricots or oranges), named generally on purpose."}
json.dump(c,open('content/541.json','w'),indent=1)
