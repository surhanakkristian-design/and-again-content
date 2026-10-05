import json
T=[i*0.5 for i in range(25)]
def keys(d):
    out=[]
    for t in T:
        v=d.get(t)
        out.append({"t":t,"off":True} if v is None else {"t":t,"x":v[0],"y":v[1],"w":v[2],"h":v[3]})
    return out
boy={0.5:(.30,.24,.40,.47),1.0:(.05,.07,.83,.79),1.5:(.16,.29,.68,.71),2.0:(.27,.23,.73,.57),2.5:(.34,.29,.58,.46),
3.0:(.26,.34,.41,.51),3.5:(.26,.23,.40,.47),4.0:(.29,.31,.31,.40),4.5:(.28,.15,.56,.58),5.0:(.24,.19,.40,.55),
5.5:(.36,.24,.36,.52),6.0:(.24,.27,.72,.42),6.5:(.27,.30,.64,.36),7.0:(.24,.31,.55,.38),7.5:(.36,.36,.30,.58),
8.0:(.36,.37,.38,.44),8.5:(.40,.37,.36,.43),9.0:(.33,.38,.48,.57),9.5:(.33,.36,.63,.61),10.0:(.33,.36,.56,.60),
10.5:(.35,.36,.40,.64),11.0:(.32,.36,.68,.64),11.5:(.30,.35,.70,.65),12.0:(.31,.34,.69,.66)}
sun={5.0:(.64,.22,.28,.20),5.5:(.08,.28,.26,.16),7.5:(.10,.38,.24,.14),8.0:(.10,.38,.24,.14),8.5:(.10,.38,.24,.14),
9.0:(.08,.39,.24,.12),9.5:(.08,.39,.24,.10),10.0:(.06,.38,.26,.12),10.5:(.08,.42,.24,.14),11.0:(.08,.43,.22,.14),
11.5:(.07,.43,.22,.09),12.0:(.06,.44,.24,.10)}
c={"mediaId":4757,"level":"A","keyWord":"freedom","defaultVoice":"male",
"taps":[
 {"phrase":"to jump over a gate","target":"the boy","voice":"male","keys":keys(boy)},
 {"phrase":"to open his arms wide","target":"the boy","voice":"male","keys":keys(boy)},
 {"phrase":"to shine in the sky","target":"the sun","voice":"male","keys":keys(sun)}],
"stillS":6.5,
"nouns":[{"word":"the sky","x":.50,"y":.12,"voice":"male"},{"word":"a field","x":.22,"y":.46,"voice":"male"},
 {"word":"a bike","x":.50,"y":.62,"voice":"male"},{"word":"a road","x":.72,"y":.83,"voice":"male"}],
"question":"What is the boy doing?",
"answer":["He","is","riding","a","bike","down","the","road."],
"answerVoice":"male",
"notes":"Key word 'freedom' is abstract, not used as a noun. A second bike-like object lies in the grass in the last shot (generation artifact), so the bike is not a tap target. The sun box is shrunk and the boy box cut on the left from 9.0 s on because his left hand reaches over the sun; sun marked only where the disc/glow is clear (5.0, 5.5, 7.5-12.0)."}
json.dump(c,open("content/4757.json","w"),indent=1)
