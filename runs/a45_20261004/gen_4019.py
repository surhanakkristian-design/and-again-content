import json
times=[i*0.5 for i in range(31)]
def keys(d):
    return [dict(t=t, **({"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if d.get(t) else {"off":True})) for t in times]
M={0.0:(.0,.07,.98,.93),0.5:(.0,.07,1.0,.93),1.0:(.0,.06,1.0,.94),1.5:(.0,.04,1.0,.96),2.0:(.02,.0,.98,1.0),2.5:(.06,.0,.94,1.0),
3.0:(.73,.0,.27,1.0),3.5:(.82,.0,.18,1.0)}
P={4.0:(.10,.20,.78,.44),4.5:(.06,.18,.82,.57),5.0:(.06,.18,.82,.56),5.5:(.08,.19,.81,.54),6.0:(.08,.20,.79,.55),6.5:(.10,.19,.80,.47),
12.5:(.0,.15,1.0,.60),13.0:(.0,.16,1.0,.78),13.5:(.0,.16,1.0,.67),14.0:(.0,.16,1.0,.84),14.5:(.0,.16,1.0,.82),15.0:(.0,.17,1.0,.83)}
G={7.0:(.03,.24,.97,.63),7.5:(.0,.22,1.0,.73),8.0:(.0,.19,1.0,.55),8.5:(.0,.20,1.0,.66),9.0:(.0,.23,1.0,.64)}
c={"mediaId":4019,"level":"B","keyWord":"a ring","defaultVoice":"male",
"taps":[
 {"phrase":"to reveal a hidden dog","target":"the man","voice":"male","keys":keys(M)},
 {"phrase":"to wear a pink ring","target":"the golden puppy","voice":"male","keys":keys(P)},
 {"phrase":"to wear a red ring","target":"the grey dog","voice":"male","keys":keys(G)}],
"stillS":4.5,
"nouns":[{"word":"a puppy","x":0.50,"y":0.27,"voice":"male"},
 {"word":"a ring","x":0.50,"y":0.46,"voice":"male"},
 {"word":"a paw","x":0.37,"y":0.67,"voice":"male"},
 {"word":"water","x":0.72,"y":0.85,"voice":"male"}],
"question":"What is the puppy floating in?",
"answer":["The","puppy","is","floating","in","a","pink","ring."],
"answerVoice":"male",
"notes":"The frames differ from the packet description: the man lifts a towel off a brown dachshund in a PURPLE ring (3.0-3.5 s), then four separate shots: golden puppy / pink ring (4.0-6.5 and 12.5-15.0 s), grey dog / red ring (7.0-9.0 s), black French bulldog / blue ring (9.5-12.0 s). All four dogs float and rest their chin, so the two dog phrases are told apart by ring colour only (state phrases). The dachshund and the black dog are not targets and have no box; at 3.0-3.5 s the man's box is only his body on the right (the towel/arm above the dachshund is left out). 'to reveal a hidden dog' = pulling the towel away at 2.5-3.0 s."}
json.dump(c,open("content/4019.json","w"),indent=1)
