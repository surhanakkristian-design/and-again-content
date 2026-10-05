import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
guide=K([(.01,.43,.54,.46)]*8)
ele=K([(.24,.12,.57,.31),(.22,.12,.59,.31),(.22,.11,.63,.32),(.20,.10,.70,.33),(.17,.10,.71,.33),(.10,.08,.81,.35),(.11,.09,.80,.34),(.06,.07,.93,.36)])
drv=K([(.60,.68,.33,.21),(.60,.68,.34,.21),(.60,.68,.33,.21),(.60,.68,.36,.21),(.60,.69,.35,.21),(.60,.69,.36,.21),(.60,.69,.36,.21),(.60,.69,.38,.21)])
c={"mediaId":6968,"level":"B","keyWord":"come on","defaultVoice":"male",
"taps":[{"phrase":"to approach the safari vehicle","target":"the big elephant","voice":"male","keys":ele},
{"phrase":"to raise his palm","target":"the guide","voice":"male","keys":guide},
{"phrase":"to sit behind the wheel","target":"the driver","voice":"male","keys":drv}],
"stillS":3.2,
"nouns":[{"word":"an acacia tree","x":0.22,"y":0.06,"voice":"male"},{"word":"an elephant","x":0.50,"y":0.20,"voice":"male"},
{"word":"a dry branch","x":0.84,"y":0.51,"voice":"male"},{"word":"a safari vehicle","x":0.65,"y":0.70,"voice":"male"}],
"question":"What is the big elephant doing?","answer":["It","is","approaching","the","safari","vehicle."],"answerVoice":"male",
"notes":"defaultVoice male: the guide is the main person (evenId true would give female only without a main person). The big elephant's trunk and legs go down behind the guide's head/hand, so the elephant box ends at the guide's head line (y 0.43) and covers head, ears and tusks; the trunk tip near his hand belongs to neither box. Other elephants of the herd are smaller and further back; the 'an elephant' pill sits on the big one's forehead. Driver box overlaps the blonde tourist's head at the bottom right (not a target)."}
json.dump(c,open('content/6968.json','w'),indent=1)
