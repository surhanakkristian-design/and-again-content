import json
times=[i*0.5 for i in range(21)]
def keys(d): return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in times]
wom={0.0:(.05,.42,.45,.52),0.5:(.10,.45,.36,.44),1.0:(.07,.47,.40,.38),1.5:(.09,.48,.37,.36),2.0:(.09,.49,.35,.35),2.5:(.09,.50,.35,.34),3.0:(.09,.49,.35,.36),3.5:(.10,.50,.35,.34),
4.0:(.12,.59,.33,.23),4.5:(.12,.62,.34,.21),5.0:(.15,.67,.36,.15),5.5:(.24,.62,.27,.18),6.0:(.27,.35,.23,.30),6.5:(.27,.32,.22,.26),7.0:(.27,.30,.21,.25),7.5:(.28,.30,.20,.20),
8.0:(.27,.24,.22,.24),8.5:(.29,.20,.20,.29),9.0:(.29,.22,.20,.39),9.5:(.28,.27,.22,.35),10.0:(.30,.27,.20,.24)}
man={0.0:(.52,.34,.44,.48),0.5:(.49,.40,.37,.42),1.0:(.49,.45,.32,.36),1.5:(.48,.45,.30,.35),2.0:(.45,.47,.30,.33),2.5:(.45,.47,.30,.33),3.0:(.45,.47,.30,.35),3.5:(.48,.54,.40,.26),
4.0:(.48,.63,.44,.22),4.5:(.48,.59,.36,.23),5.0:(.52,.62,.29,.18),5.5:(.52,.59,.27,.19),6.0:(.51,.35,.27,.35),6.5:(.50,.32,.29,.29),7.0:(.48,.30,.29,.28),7.5:(.48,.29,.27,.24),
8.0:(.49,.25,.20,.25),8.5:(.50,.20,.20,.29),9.0:(.50,.22,.20,.39),9.5:(.50,.22,.20,.40),10.0:(.50,.25,.18,.26)}
rock={0.0:(0,0,.80,.34),0.5:(0,0,.86,.40),1.0:(0,0,.88,.45),1.5:(0,0,.86,.45),2.0:(0,.02,.82,.45),2.5:(0,.05,.82,.42),3.0:(0,.06,.82,.41),3.5:(0,.06,.82,.44),
4.0:(0,.05,.82,.54),4.5:(0,.03,.84,.56),5.0:(0,0,.85,.62),5.5:(0,0,.84,.59),6.0:(.08,.70,.92,.19),6.5:(.06,.61,.94,.28),7.0:(.05,.58,.93,.40),7.5:(.05,.53,.93,.47),
8.0:(.05,.50,.93,.48),8.5:(.08,.50,.92,.50),9.0:(.06,.62,.94,.38),9.5:(.06,.62,.94,.38),10.0:(.06,.52,.94,.48)}
c={"mediaId":616,"level":"A","keyWord":"rock","defaultVoice":"female",
"taps":[{"phrase":"to have red hair","target":"the woman","voice":"female","keys":keys(wom)},
{"phrase":"to wear a grey sweater","target":"the man","voice":"male","keys":keys(man)},
{"phrase":"to be big and round","target":"the rock","voice":"female","keys":keys(rock)}],
"stillS":10.0,
"nouns":[{"word":"a rock","x":.50,"y":.75,"voice":"female"},{"word":"the sky","x":.50,"y":.10,"voice":"female"},{"word":"a bird","x":.88,"y":.37,"voice":"female"},{"word":"a river","x":.86,"y":.58,"voice":"female"}],
"question":"What are they standing on?","answer":["They","are","standing","on","a","big","rock."],"answerVoice":"female",
"notes":"Man and woman do exactly the same all the time (push, slide down, climb, cheer), so their phrases are states (red hair / grey sweater). The rock is behind or under the people in every frame: its box is the part of the rock free of people (above them while they push, below them while they climb and stand), so it never holds the whole rock. Cut at 6.0 s. 'a bird' at 10.0 is small at the right edge (pill at x .88, bird at about .95). The people are not nouns (too close together for two pills). defaultVoice female: a couple, evenId true."}
json.dump(c,open('content/616.json','w'),indent=1,ensure_ascii=False)
