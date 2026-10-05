import json
M=[(0.0,.02,.42,.70,.58),(0.5,.02,.42,.70,.58),(1.0,.02,.30,.56,.70),(1.5,0,.42,.68,.58),(2.0,0,.37,.46,.63),
(2.5,0,.29,.82,.71),(3.0,0,.24,.90,.76),(3.5,0,.35,.42,.65),(4.0,.09,.38,.35,.62),(4.5,.15,.54,.38,.46),
(5.0,.16,.61,.36,.39),(5.5,.19,.69,.33,.31),(6.0,.18,.52,.45,.46),(6.5,.29,.37,.43,.59),(7.0,.34,.24,.32,.53),
(7.5,.35,.26,.34,.49),(8.0,.35,.26,.32,.49),(8.5,.35,.26,.32,.49),(9.0,.35,.29,.32,.47),(9.5,.16,.19,.73,.59),(10.0,.12,.10,.72,.72)]
F={4.0:(.44,.07,.27,.64),4.5:(.40,.09,.28,.45),5.0:(.40,.07,.28,.36),5.5:(.46,.04,.27,.23),6.0:(.33,0,.35,.25),
6.5:(.33,0,.20,.14),7.0:(.45,0,.20,.14),7.5:(.46,0,.20,.14),8.0:(.40,0,.20,.14),8.5:(.36,0,.20,.14),9.0:(.39,0,.20,.14),
9.5:(.46,0,.20,.15),10.0:(.33,0,.30,.10)}
man=[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,x,y,w,h in M]
flag=[]
for t,*_ in M:
    if t in F:
        x,y,w,h=F[t]; flag.append({"t":t,"x":x,"y":y,"w":w,"h":h})
    else: flag.append({"t":t,"off":True})
mn="the man in the blue suit"
d={"mediaId":4703,"level":"B","keyWord":"raise","defaultVoice":"male",
"taps":[
 {"phrase":"to raise a green flag","target":mn,"voice":"male","keys":man},
 {"phrase":"to flutter in the wind","target":"the flag","voice":"male","keys":flag},
 {"phrase":"to cut a ribbon with scissors","target":mn,"voice":"male","keys":man}],
"stillS":8.0,
"nouns":[{"word":"a flagpole","x":0.52,"y":0.12,"voice":"male"},{"word":"a ladder","x":0.16,"y":0.34,"voice":"male"},
 {"word":"a ribbon","x":0.78,"y":0.53,"voice":"male"},{"word":"steps","x":0.50,"y":0.86,"voice":"male"}],
"question":"What is the man in blue raising?",
"answer":["He","is","raising","a","green","flag."],"answerVoice":"male",
"notes":"Two targets only: the crowd and the two drummers stand behind / on both sides of the man and cannot get a box of their own. The flag is off until 3.5 s (first shots at the door); from 6.5 s only its lower edge shows at the top of the picture (small box kept). At 4.0-4.5 s the man's hands are on the flag / halyard: split between them. At 10.0 s the flag box is only 0.10 high so it stays above his raised hand. 'the man in blue' in the question because many men are in the crowd. The ladder (noun) is small."}
json.dump(d,open("content/4703.json","w"),indent=1)
