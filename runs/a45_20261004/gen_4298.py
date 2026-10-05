import json
def keys(T,b):
    return [({"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]}) for t,k in zip(T,b)]
def R(x1,y1,x2,y2): return (round(x1,2),round(y1,2),round(x2-x1,2),round(y2-y1,2))
T=[i*0.5 for i in range(21)]
boys=[R(0,0,.88,.57),R(0,0,1,.67),R(0,0,.92,.95),R(.1,0,1,.97),R(0,0,1,.9),R(0,0,1,.92),
R(.08,0,.85,1),R(0,.02,.84,.97),R(0,0,.82,.98),R(0,0,.87,1),R(.05,.02,.83,1),R(.05,.03,.86,1),R(.03,0,.87,1),R(.02,.02,.86,1),
R(0,.03,.85,1),R(0,.05,.87,1),R(0,.08,.83,.98),R(0,.1,.84,.95),R(0,.15,.82,.9),R(.02,.2,.84,.88),R(.03,.2,.8,.8)]
tea=[None]*6+[R(.85,0,1,.95),R(.84,0,1,.97),R(.82,0,1,1),R(.87,.08,1,1),R(.83,.17,1,1),R(.86,.2,1,1),R(.87,.2,1,.9),R(.86,.22,1,.92),
R(.85,.23,1,.98),R(.87,.25,1,.95),R(.83,.3,1,1),R(.84,.3,1,.98),R(.82,.2,1,1),R(.84,.22,1,1),R(.8,.2,1,.9)]
d={"mediaId":4298,"level":"A","keyWord":"straight","defaultVoice":"male",
"taps":[{"phrase":"to make a straight line","target":"the boys","voice":"male","keys":keys(T,boys)},
{"phrase":"to give a thumbs up","target":"the woman","voice":"female","keys":keys(T,tea)},
{"phrase":"to walk to the line","target":"the boys","voice":"male","keys":keys(T,boys)}],
"stillS":10.0,
"nouns":[{"word":"windows","x":.35,"y":.08,"voice":"male"},{"word":"boys","x":.3,"y":.33,"voice":"male"},
{"word":"a woman","x":.88,"y":.47,"voice":"female"},{"word":"the floor","x":.3,"y":.85,"voice":"male"}],
"question":"What are the boys doing?","answer":["They","are","standing","in","a","straight","line."],"answerVoice":"male",
"notes":"Key word 'straight' (adverb) appears as the adjective in 'a straight line' (phrase 1 and answer). Target 'the boys' = the whole row, one box, used for two phrases (walk to the line: 0-3.5 s, the straight line: from about 3.0 s). The woman (teacher in red) enters at 3.0 s at the right edge and overlaps the front boy; boxes are split on a vertical line, so her thumbs-up arm (8.0-9.5 s) reaches into the boys' box and the front boy is partly in her box at 8.5-10.0 s. At 2.5 s only her shoe is visible: off. defaultVoice male (boys are the main people)."}
json.dump(d,open("content/4298.json","w"),indent=1)
