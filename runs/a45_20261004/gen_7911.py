import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
man=K([(.07,.35,.38,.37),(.08,.35,.37,.37),(.08,.34,.37,.38),(.07,.33,.38,.39),(.05,.33,.41,.40),(.08,.32,.42,.40),(.06,.32,.45,.40),(.07,.32,.44,.40)])
red=K([(.46,.40,.25,.31),(.45,.40,.28,.31),(.46,.40,.28,.32),(.46,.40,.31,.32),(.47,.39,.32,.32),(.51,.39,.30,.32),(.52,.39,.29,.33),(.52,.39,.29,.33)])
rgt=K([(.72,.38,.18,.30),(.74,.39,.18,.28),(.75,.37,.22,.30),(.78,.37,.22,.30),(.80,.36,.20,.30),(.82,.35,.18,.30),(.82,.35,.18,.30),(.82,.35,.18,.30)])
c={"mediaId":7911,"level":"A","keyWord":"musical","defaultVoice":"female",
"taps":[{"phrase":"to tap bottles with a spoon","target":"the woman in red","voice":"female","keys":red},
{"phrase":"to hit the pots with spoons","target":"the man in white","voice":"male","keys":man},
{"phrase":"to clap her hands","target":"the woman on the right","voice":"female","keys":rgt}],
"stillS":0.2,
"nouns":[{"word":"cups","x":0.12,"y":0.30,"voice":"female"},{"word":"a window","x":0.67,"y":0.20,"voice":"female"},
{"word":"a pot","x":0.32,"y":0.77,"voice":"female"},{"word":"bottles","x":0.73,"y":0.73,"voice":"female"}],
"question":"What is the woman in red doing?","answer":["She","is","tapping","bottles","with","a","spoon."],"answerVoice":"female",
"notes":"defaultVoice female: the woman in the rust (red) jumper is the main person; the man at the door crosses his arms and only covers his face at 3.7 s, so not used; the woman blowing into a bottle not used to keep the bottle phrase unique"}
json.dump(c,open('content/7911.json','w'),indent=1)
