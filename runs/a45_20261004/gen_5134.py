import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
mother={0.0:(0,.1,.40,.9),0.5:(0,.12,.42,.88),1.0:(0,.13,.42,.87),1.5:(0,.13,.42,.87),2.0:(0,.15,.48,.85),
 2.5:(0,.08,.26,.55),3.0:(0,.08,.20,.52),3.5:(0,.08,.18,.5),4.0:(0,.07,.20,.5),4.5:(0,.05,.58,.42),5.0:(0,.1,.42,.5),
 5.5:(0,.12,.40,.4),6.0:(0,.14,.18,.3),7.5:(.12,.33,.25,.38),8.0:(.18,.37,.22,.26),8.5:(.27,.39,.18,.22),9.0:(.29,.42,.18,.18)}
father={0.0:(.78,.1,.22,.9),0.5:(.82,.1,.18,.9),1.0:(.82,.13,.18,.87),1.5:(.82,.12,.18,.88),
 2.5:(.62,.04,.38,.58),3.0:(.62,.03,.38,.6),3.5:(.74,.03,.26,.57),4.0:(.78,.02,.22,.55),4.5:(.72,.30,.28,.2),
 5.0:(.68,.13,.32,.55),5.5:(.62,.15,.38,.47),6.0:(.46,.13,.54,.48),6.5:(.32,.18,.68,.42)}
baby={0.0:(.40,.22,.38,.78),0.5:(.42,.22,.40,.78),1.0:(.42,.24,.40,.76),1.5:(.42,.25,.40,.75),2.0:(.48,.27,.47,.73),
 2.5:(.26,.24,.21,.36),3.0:(.20,.25,.25,.37),3.5:(.18,.25,.27,.37),4.0:(.20,.25,.33,.36)}
c={"mediaId":5134,"level":"A","keyWord":"parent","defaultVoice":"female",
"taps":[
 {"phrase":"to feed the baby","target":"the mother","voice":"female","keys":K(mother)},
 {"phrase":"to read a book","target":"the father","voice":"male","keys":K(father)},
 {"phrase":"to eat from a spoon","target":"the baby","voice":"male","keys":K(baby)}],
"stillS":3.0,
"nouns":[{"word":"a man","x":0.82,"y":0.15,"voice":"male"},{"word":"a woman","x":0.15,"y":0.28,"voice":"female"},
 {"word":"a tower","x":0.52,"y":0.42,"voice":"female"},{"word":"blocks","x":0.84,"y":0.66,"voice":"female"}],
"question":"What is the mother doing?",
"answer":["She","is","feeding","the","baby."],"answerVoice":"female",
"notes":"Four scenes. The baby boy in the high chair (0-2.0 s) is taken to be the boy in grey on the left in the block scene (2.5-4.0 s); he is marked off in the bed and playground scenes because the children there cannot be matched for sure. The dark-haired woman in a cream jumper pushing a swing (7.5-9.0 s) is taken to be the mother (same jumper); the father cannot be found in the playground shots, so he is off there. Father off at 2.0 s (only his hand) and the mother off at 6.5/7.0 s. Key word parent is not used as a noun slot (no single place)."}
json.dump(c,open('content/5134.json','w'),indent=1)
