import json
B=[(0.0,.05,0,.87,.76),(0.5,.08,0,.84,.76),(1.0,.08,0,.84,.76),(1.5,.06,0,.86,.78),(2.0,.08,0,.86,.80),
(2.5,0,0,1.0,.80),(3.0,0,0,1.0,.85),(3.5,0,0,.98,.80),(4.0,.15,0,.80,.86),(4.5,.07,0,.80,.76),
(5.0,.10,0,.78,.76),(5.5,.03,0,.85,.80),(6.0,.05,0,.85,.76),(6.5,.04,0,.90,.76),(7.0,.05,0,.86,.80),
(7.5,.05,0,.90,.76),(8.0,.03,0,.92,.76),(8.5,0,0,1.0,.86),(9.0,0,0,.96,.78),(9.5,.02,0,.94,.76),(10.0,.02,0,.94,.76)]
keys=[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,x,y,w,h in B]
d={"mediaId":4641,"level":"A","keyWord":"diet","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the man","voice":"male","keys":keys} for p in
 ["to point with his finger","to put food in boxes","to make a tall tower"]],
"stillS":0.0,
"nouns":[{"word":"doughnuts","x":.26,"y":.81,"voice":"male"},
 {"word":"strawberries","x":.70,"y":.75,"voice":"male"},
 {"word":"a window","x":.88,"y":.24,"voice":"male"},
 {"word":"a T-shirt","x":.27,"y":.41,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","putting","food","in","boxes."],
"answerVoice":"male",
"notes":"Only one living target (the man); the things on the counter only allow states, so all three phrases use him with the same keys. He points 0.5-2.0 s, fills the boxes 3.5-5.5 s, stacks them into a tower 6.0-10.0 s (jump cuts in between). Key word 'diet' is not a visible noun, so it is not placed and not used in the answer. 'a T-shirt' pill sits on his white sleeve (the apron covers the rest); 'doughnuts' and 'strawberries' are 0.44 apart in x and 0.06 in y."}
json.dump(d,open("content/4641.json","w"),indent=1,ensure_ascii=False)
