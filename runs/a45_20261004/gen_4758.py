import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
man={0.0:(0,.24,.96,.76),1.0:(0,.26,.76,.74),1.5:(0,.24,.76,.76),2.0:(0,.08,.72,.72),2.5:(0,0,.82,.53),
3.0:(0,0,.66,.54),3.5:(0,0,.64,.55),4.0:(0,.60,.27,.24),4.5:(0,.44,.42,.28),5.0:(0,.46,.65,.30),5.5:(0,.56,.50,.44),
6.0:(0,.48,.80,.52),6.5:(0,.42,.76,.50),7.0:(0,.43,.88,.57),7.5:(0,.44,.64,.56),8.0:(0,.39,.92,.50),8.5:(0,.32,.72,.46),
9.0:(0,.29,.97,.71),9.5:(0,.02,.88,.98),10.0:(0,0,.27,1.0),10.5:(0,.13,.18,.87),11.0:(0,.21,.35,.79),11.5:(0,.20,.41,.80),
12.0:(0,.18,.40,.82)}
tray={2.0:(.08,.86,.34,.14),2.5:(.09,.57,.43,.27),3.0:(.10,.56,.34,.24),3.5:(.15,.58,.30,.21)}
c={"mediaId":4758,"level":"A","keyWord":"full","defaultVoice":"male",
"taps":[
 {"phrase":"to open the fridge door","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to put food on shelves","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to lie in an empty drawer","target":"the ice tray","voice":"male","keys":keys(tray)}],
"stillS":12.0,
"nouns":[{"word":"a cupboard","x":.28,"y":.19,"voice":"male"},{"word":"a man","x":.14,"y":.34,"voice":"male"},
 {"word":"a pizza","x":.46,"y":.50,"voice":"male"},{"word":"a fridge","x":.72,"y":.76,"voice":"male"}],
"question":"What is the man looking at?",
"answer":["He","is","looking","at","a","full","fridge."],
"answerVoice":"male",
"notes":"From 4.0 to 9.0 s only the man's hands and arms are in the picture; the man box covers them (with the food he is holding). 0.5 s is a blurred pan, man off. Second target is the ice tray in the empty freezer drawer (2.0-3.5 s). Noun 'a fridge' is placed on the fridge body at the right, 'a pizza' on the pizza in the door."}
json.dump(c,open("content/4758.json","w"),indent=1)
