import json
def keys(T,b):
    return [({"t":t,"off":True} if k is None else {"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]}) for t,k in zip(T,b)]
def R(x1,y1,x2,y2): return (round(x1,2),round(y1,2),round(x2-x1,2),round(y2-y1,2))
T=[i*0.5 for i in range(21)]
man=[R(0,.05,.47,1),R(0,.05,.5,1),R(0,.06,.53,1),R(0,.08,.53,1),R(0,.06,.5,1),R(0,.06,.48,1),R(0,.09,.5,1),R(0,.1,.48,1),
R(0,.1,.5,1),R(0,.14,.36,1),R(0,.15,.5,1),R(0,.14,.5,1),R(0,.17,.57,1),R(0,.15,.52,1),R(0,.12,.45,1),R(0,.1,.47,1),
R(0,.08,.47,1),R(0,.07,.47,1),R(0,.07,.46,1),R(0,.07,.45,1),R(0,.07,.47,1)]
cat=[R(.47,.42,1,.92),R(.5,.42,1,.92),R(.53,.45,1,.93),R(.53,.45,1,.93),R(.5,.44,1,.93),R(.48,.44,1,.93),R(.5,.46,.87,.95),R(.48,.49,.78,.97),
R(.5,.43,1,.97),R(.36,.27,.8,.97),R(.5,.28,.92,.5),R(.5,.34,.8,.68),R(.57,.36,.8,.68),R(.52,.35,.83,.75),R(.48,.33,.85,.78),R(.5,.32,.87,.8),
R(.52,.31,.86,.81),R(.52,.31,.86,.83),R(.52,.33,.86,.93),R(.52,.33,.87,.95),R(.53,.33,.87,.88)]
man=[R(0,.05,.47,1),R(0,.05,.5,1),R(0,.06,.53,1),R(0,.08,.53,1),R(0,.06,.5,1),R(0,.06,.48,1),R(0,.09,.5,1),R(0,.1,.48,1),
R(0,.1,.5,1),R(0,.14,.36,1),R(0,.15,.5,1),R(0,.14,.5,1),R(0,.17,.57,1),R(0,.15,.52,1),R(0,.12,.45,1),R(0,.1,.47,1),
R(0,.08,.47,1),R(0,.07,.47,1),R(0,.07,.46,1),R(0,.07,.45,1),R(0,.07,.47,1)]
wom=[None]*6+[R(.87,.2,1,.98),R(.78,.18,1,.98),R(.5,0,1,.97),R(.36,.05,1,1),R(.5,.2,1,1),R(.5,.2,1,1),R(.57,.2,1,1),R(.52,.2,1,1),
R(.45,.2,1,1),R(.47,.18,1,1),R(.47,.15,1,1),R(.47,.15,1,1),R(.46,.18,1,1),R(.45,.2,1,1),R(.47,.18,1,1)]
d={"mediaId":4299,"level":"B","keyWord":"react","defaultVoice":"male",
"taps":[{"phrase":"to sneeze into a tissue","target":"the man","voice":"male","keys":keys(T,man)},
{"phrase":"to cradle the fluffy cat","target":"the woman","voice":"female","keys":keys(T,wom)},
{"phrase":"to wipe his watery eyes","target":"the man","voice":"male","keys":keys(T,man)}],
"stillS":6.5,
"nouns":[{"word":"a tissue","x":.33,"y":.42,"voice":"male"},{"word":"fur","x":.62,"y":.55,"voice":"male"},
{"word":"a jumper","x":.2,"y":.66,"voice":"male"},{"word":"a denim jacket","x":.78,"y":.68,"voice":"male"}],
"question":"How is the man reacting?","answer":["He","is","sneezing","into","a","tissue."],"answerVoice":"male",
"notes":"Key word 'react' is in the question. Only two targets: the cat is no tap target because it overlaps the man (on his lap, 0-3.5 s) and then the woman (in her arms) too heavily for separate boxes. From 4.0 s the woman's box is the woman together with the cat she is holding (a tap on the cat in her arms counts for 'to cradle the fluffy cat'); 3.0-3.5 s it is the strip of her at the right edge; 0-2.5 s only a sliver of her arm is visible: off. At 4.0-4.5 s (handover) the cat still partly lies in the man's box. 'to wipe his watery eyes': 0.5-1.5 s he wipes his red, streaming eyes with his sleeve. 'to sneeze': shown as a tissue pressed to his nose with a screwed-up face. Noun 'fur' is on the cat (no noun 'a cat')."}
json.dump(d,open("content/4299.json","w"),indent=1)
