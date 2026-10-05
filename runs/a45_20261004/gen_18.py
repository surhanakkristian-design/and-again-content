import json
T=[i*0.5 for i in range(19)]
G={0.0:(.05,.05,.77,.63),0.5:(.05,.05,.77,.63),1.0:(.05,.08,.77,.58),1.5:(.05,.07,.77,.50),2.0:(.10,0,.72,.26),2.5:(.10,.04,.72,.28),
3.0:None,3.5:None,4.0:None,4.5:None,5.0:None,5.5:(.10,.12,.72,.30),6.0:(.08,.15,.74,.35),6.5:(.08,.15,.74,.35),7.0:(.08,.15,.74,.35),
7.5:(.10,.07,.72,.43),8.0:(.05,.07,.90,.39),8.5:(.05,.07,.90,.39),9.0:(0,.07,.78,.43)}
S={0.0:(.33,.68,.34,.22),0.5:(.33,.68,.34,.22),1.0:(.33,.66,.34,.24),1.5:(.32,.57,.36,.37),2.0:(.30,.26,.40,.50),2.5:(.30,.32,.40,.50),
3.0:(.10,0,.85,1),3.5:(.10,0,.85,1),4.0:(.10,0,.85,1),4.5:(.15,.02,.70,.72),5.0:(.15,.10,.70,.75),5.5:(.25,.42,.50,.52),
6.0:(.25,.50,.50,.44),6.5:(.25,.50,.50,.44),7.0:(.25,.50,.50,.44),7.5:(.28,.50,.48,.40),8.0:(.28,.50,.34,.40),8.5:(.28,.50,.34,.40),9.0:(.28,.50,.48,.40)}
C={0.0:(.82,.48,.18,.36),0.5:(.82,.48,.18,.36),1.0:(.82,.48,.18,.36),1.5:(.82,.55,.18,.31),2.0:(.82,.53,.18,.36),2.5:(.82,.72,.18,.26),
3.0:None,3.5:None,4.0:None,4.5:None,5.0:None,5.5:(.82,.52,.18,.36),6.0:(.82,.52,.18,.36),6.5:(.82,.52,.18,.36),7.0:(.82,.52,.18,.36),
7.5:(.82,.50,.18,.46),8.0:(.62,.47,.38,.33),8.5:(.62,.47,.38,.33),9.0:(.78,.46,.22,.47)}
def keys(d): return [({"t":t,"off":True} if d[t] is None else {"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]}) for t in T]
c={"mediaId":18,"level":"B","keyWord":"root","defaultVoice":"female",
"taps":[{"phrase":"to kneel in the soil","target":"the girl","voice":"female","keys":keys(G)},
{"phrase":"to have long pale roots","target":"the seedling","voice":"female","keys":keys(S)},
{"phrase":"to have a long spout","target":"the watering can","voice":"female","keys":keys(C)}],
"stillS":6.0,
"nouns":[{"word":"roots","x":.50,"y":.89,"voice":"female"},{"word":"leaves","x":.48,"y":.70,"voice":"female"},
{"word":"a watering can","x":.90,"y":.62,"voice":"female"},{"word":"a stone wall","x":.78,"y":.14,"voice":"female"}],
"question":"What is the girl doing?","answer":["She","is","lifting","a","seedling","with","long","roots."],"answerVoice":"female",
"notes":"Girl and seedling overlap in the picture: the girl's box is her head/upper body above the plant, the seedling's box is the plant with her gloved hands around it; her knees are in neither box. 3.0-5.0 s are close-ups of the plant with only her hands/arms: girl set off. The seedling and watering-can phrases are states (no action fits only them); the can is only a sliver at the right edge until 7.5 s and its spout shows from 8.0 s. Key word used as the plural 'roots'."}
json.dump(c,open('content/18.json','w'),indent=1)
