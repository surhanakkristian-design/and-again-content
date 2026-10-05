import json
T=[i*0.5 for i in range(21)]
W={2.0:(0,0,.22,.36),2.5:(0,0,.28,.80),3.0:(0,0,.33,.76),3.5:(0,.05,.34,.66),4.0:(0,.07,.35,.61),4.5:(0,.07,.35,.61),5.0:(0,.12,.36,.54),5.5:(0,.12,.36,.54),
   6.0:(0,.14,.35,.50),6.5:(0,.14,.35,.50),7.0:(0,.14,.35,.50),7.5:(0,.14,.35,.50),8.0:(0,.14,.35,.50),8.5:(0,.22,.30,.40),9.0:(0,.36,.27,.28),9.5:(0,.36,.24,.28),10.0:(0,.36,.24,.27)}
M={2.5:(.78,0,.22,.76),3.0:(.73,.02,.27,.72),3.5:(.70,.07,.30,.63),4.0:(.67,.09,.33,.58),4.5:(.67,.09,.33,.58),5.0:(.65,.14,.35,.52),5.5:(.65,.14,.35,.52),
   6.0:(.64,.14,.36,.50),6.5:(.64,.14,.36,.50),7.0:(.64,.14,.36,.50),7.5:(.66,.14,.34,.50),8.0:(.64,.14,.36,.50),8.5:(.67,.25,.33,.45),9.0:(.66,.36,.34,.28),9.5:(.71,.36,.29,.28),10.0:(.71,.35,.29,.29)}
G={2.0:(.42,.15,.34,.20),2.5:(.30,.17,.46,.24),3.0:(.34,.20,.38,.16),3.5:(.35,.22,.34,.15),4.0:(.36,.22,.30,.15),4.5:(.37,.24,.28,.14),5.0:(.37,.25,.27,.14),5.5:(.37,.25,.27,.14),
   6.0:(.37,.26,.26,.14),6.5:(.37,.26,.26,.14),7.0:(.37,.26,.26,.14),7.5:(.37,.26,.26,.14),8.0:(.37,.26,.26,.14),8.5:(.36,.28,.30,.26),9.0:(.29,.30,.35,.23),9.5:(.26,.30,.44,.27),10.0:(.26,.30,.44,.30)}
for _t in [3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0]:
    g=G[_t]; G[_t]=(g[0],round(g[1]+0.03,2),g[2],round(g[3]+0.01,2))
def keys(D):
    return [({"t":t,"x":D[t][0],"y":D[t][1],"w":D[t][2],"h":D[t][3]} if t in D else {"t":t,"off":True}) for t in T]
c={"mediaId":240,"level":"B","keyWord":"draw","defaultVoice":"female",
"taps":[
 {"phrase":"to wear a turquoise T-shirt","target":"the woman in turquoise","voice":"female","keys":keys(W)},
 {"phrase":"to have a thick beard","target":"the big man","voice":"male","keys":keys(M)},
 {"phrase":"to drape a tea towel","target":"the grandmother","voice":"female","keys":keys(G)}],
"stillS":10.0,
"nouns":[{"word":"a tea towel","x":0.47,"y":0.56,"voice":"female"},{"word":"a table","x":0.50,"y":0.70,"voice":"female"},{"word":"an elderly woman","x":0.49,"y":0.44,"voice":"female"}],
"question":"How does the arm-wrestling match end?",
"answer":["The","match","ends","in","a","draw."],
"answerVoice":"female",
"notes":"0.0-1.5 s is a close-up of the locked, crossing forearms only (no face, shirt or beard visible), so all targets are off there; at 2.0 only the woman's face and the grandmother are in the picture. The two wrestlers do the same actions, so their phrases are states (shirt colour, beard). The grandmother stands behind the fists: her box stops above the fists while they wrestle. A teenage boy and a young woman stand in the background, partly inside the wrestlers' boxes at 8.5-10.0. Whether it is the grandmother's hand that holds the towel up at 2.0-4.0 is not certain; she clearly drapes it at 9.0-10.0."}
json.dump(c,open('content/240.json','w'),indent=1,ensure_ascii=False)
