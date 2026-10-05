import json
T=[i*0.5 for i in range(19)]
def keys(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
boy={0.0:(.29,.18,.71,.82),0.5:(.30,.18,.70,.82),1.0:(.30,.20,.70,.80),1.5:(.29,.21,.71,.79),2.0:(.31,.22,.69,.78),
2.5:(0,.36,1.0,.64),3.0:(.12,.35,.88,.65),3.5:(.38,.21,.62,.79),4.0:(.31,.21,.69,.79),4.5:(.28,.22,.72,.78),
5.0:(.29,.21,.71,.79),5.5:(0,.20,1.0,.80),6.0:(.31,.18,.69,.82),6.5:(.32,.20,.68,.80),7.0:(.30,.21,.70,.79),
7.5:(.28,.21,.72,.79),8.0:(.24,.20,.76,.80),8.5:(.23,.19,.77,.81),9.0:(.22,.20,.78,.80)}
cp={0.0:(.03,.36,.24,.14),0.5:(.05,.37,.23,.14),1.0:(.07,.37,.22,.14),1.5:(.07,.37,.20,.14),2.0:(.09,.36,.20,.14),
3.5:(.19,.37,.18,.14),4.0:(.10,.36,.20,.14),4.5:(.06,.38,.20,.14),5.0:(.08,.37,.20,.14),6.0:(.12,.35,.18,.14),
6.5:(.11,.36,.19,.14),7.0:(.08,.37,.20,.14),7.5:(.07,.38,.19,.14),8.0:(.05,.37,.18,.14),8.5:(.04,.37,.18,.14),9.0:(.03,.37,.18,.14)}
d={"mediaId":5302,"level":"B","keyWord":"blossom","defaultVoice":"male",
"taps":[{"phrase":"to throw his head back","target":"the young man","voice":"male","keys":keys(boy)},
{"phrase":"to pinch his nose","target":"the young man","voice":"male","keys":keys(boy)},
{"phrase":"to stroll along the path","target":"the couple in the background","voice":"male","keys":keys(cp)}],
"stillS":7.0,
"nouns":[{"word":"blossom","x":0.50,"y":0.08,"voice":"male"},{"word":"a park bench","x":0.17,"y":0.62,"voice":"male"},
{"word":"a paper cup","x":0.24,"y":0.82,"voice":"male"},{"word":"a hooded jacket","x":0.72,"y":0.66,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","sneezing","beneath","a","blossoming","cherry","tree."],"answerVoice":"male",
"notes":"Only one main person; third target is the small couple walking (with a dog) on the path in the background, hidden at 2.5, 3.0, 5.5. Couple overlaps the boy's left side, so the boy's box is cut on the left (x .24-.38) where his arm/jacket would reach the couple. 'cherry' tree taken from the pale pink blossom and the description."}
json.dump(d,open("content/5302.json","w"),indent=1)
