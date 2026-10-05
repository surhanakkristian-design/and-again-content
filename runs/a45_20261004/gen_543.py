import json
T=[i*0.5 for i in range(21)]
B=[(.12,0,.88,.75),(.1,0,.9,.72),(.12,0,.88,.72),(.15,0,.85,.6),(.05,0,.95,.47),(.08,0,.92,.5),(0,0,1,.58),(0,0,1,.63),(0,0,1,.63),(0,0,1,.72),(0,.06,1,.8),(0,.1,1,.82),(0,.07,1,.72),(0,.2,.9,.58),(0,.17,.9,.68),(0,.13,1,.84),(0,.14,1,.8),(0,.12,1,.8),(0,.03,1,.95),(0,.07,1,.9),(0,.05,1,.9)]
keys=[{"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
d={"mediaId":543,"level":"A","keyWord":"pepper","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in ["to put pepper on pasta","to sneeze into his arm","to show a bowl of pasta"]],
"stillS":8.0,
"nouns":[{"word":"a window","x":.82,"y":.25,"voice":"male"},{"word":"a man","x":.45,"y":.47,"voice":"male"},{"word":"pasta","x":.5,"y":.88,"voice":"male"}],
"question":"What is the man doing?","answer":["He","is","putting","pepper","on","his","pasta."],"answerVoice":"male",
"notes":"One target (the man). 0-2.5 s only his hands, arm and the pepper mill are in the picture, the box holds them. He sneezes into his arm at 6.5 s, shows the bowl 8.5-10 s. A cat sits small at the right edge 6.5-9.5 s, not used. Key word 'pepper' is not placed as a noun: it is only small black dots on the pasta (same place as 'pasta') or inside the mill. Only 3 nouns; 'a man' sits on his shirt."}
json.dump(d,open("content/543.json","w"),indent=1,ensure_ascii=False)
