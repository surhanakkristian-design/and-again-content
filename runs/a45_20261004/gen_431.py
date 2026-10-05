import json
T=[i*0.5 for i in range(21)]
man={0.0:(0,.38,.84,.29),0.5:(0,.38,.84,.29),1.0:(0,.30,.92,.34),1.5:(0,.27,.92,.37),2.0:(0,.21,.92,.39),
2.5:(0,.26,.82,.30),3.0:(0,.28,.95,.31),3.5:(0,.27,.95,.31),4.0:(.30,.28,.68,.32),4.5:(0,.27,.85,.33),5.0:(0,.27,.85,.33),
5.5:(0,.27,.85,.33),6.0:(.20,.27,.80,.33),6.5:(.24,.27,.76,.33),7.0:(0,.22,.90,.47),7.5:(0,.27,1.0,.49),8.0:(0,.26,1.0,.42),
8.5:(0,.20,1.0,.54),9.0:(0,.23,1.0,.77),9.5:(0,.23,1.0,.77),10.0:(0,.22,1.0,.78)}
broom={0.0:(.30,.18,.22,.20),0.5:(.30,.18,.22,.20),1.0:(.22,.08,.24,.22),1.5:(.20,.06,.26,.21),2.0:(.28,0,.20,.21),
2.5:(.30,.56,.42,.14),3.0:(.28,.59,.38,.14),3.5:(.30,.58,.38,.14),4.0:(0,.36,.30,.26),6.0:(0,.36,.20,.20),6.5:(0,.36,.24,.20)}
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
c={"mediaId":431,"level":"A","keyWord":"lazy","defaultVoice":"male",
"taps":[
 {"phrase":"to lie on the sofa","target":"the man","voice":"male","keys":keys(man)},
 {"phrase":"to stand by the wall","target":"the broom","voice":"male","keys":keys(broom)},
 {"phrase":"to take the remote","target":"the man","voice":"male","keys":keys(man)}],
"stillS":0.0,
"nouns":[{"word":"a window","x":.76,"y":.12,"voice":"male"},{"word":"a broom","x":.40,"y":.24,"voice":"male"},
 {"word":"a man","x":.42,"y":.46,"voice":"male"},{"word":"a table","x":.52,"y":.71,"voice":"male"}],
"question":"What is the man doing?",
"answer":["He","is","lying","on","the","sofa."],
"answerVoice":"male",
"notes":"From 2.5 s the man holds the broom across his body: the broom box there covers only the broom head (2.5-3.5 s) or the left strip (4.0, 6.0, 6.5 s) and the man's box is cut along that line; 4.5-5.5 s only a sliver of the handle is in frame, set off. 'to stand by the wall' is true 0-2 s only. Two remotes appear after 2.5 s (generation glitch). Key word 'lazy' is an adjective, not used in the texts."}
json.dump(c,open("content/431.json","w"),indent=1)
