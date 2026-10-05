import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
cop=K([(.07,.34,.45,.44),(.06,.34,.42,.45),(.04,.35,.45,.44),(.04,.35,.46,.44),(.02,.34,.50,.45),(.03,.34,.49,.46),(.01,.34,.53,.46),(.02,.34,.51,.47)])
ducks=K([(.52,.62,.40,.14),(.48,.62,.40,.14),(.49,.62,.33,.14),(.50,.61,.26,.15),(.52,.59,.18,.15),(.52,.58,.18,.14),(.55,.59,.22,.14),(.62,.58,.22,.15)])
bike=K([(.66,.32,.18,.18),(.66,.32,.18,.18),(.66,.34,.18,.18),(.67,.34,.18,.18),(.66,.32,.18,.18),(.66,.32,.18,.18),(.67,.32,.18,.18),(.68,.32,.18,.18)])
c={"mediaId":6989,"level":"A","keyWord":"cop","defaultVoice":"female",
"taps":[
 {"phrase":"to stop the traffic","target":"the cop","voice":"female","keys":cop},
 {"phrase":"to walk in a line","target":"the ducks","voice":"female","keys":ducks},
 {"phrase":"to ride a bike","target":"the man on the bike","voice":"male","keys":bike}],
"stillS":0.7,
"nouns":[{"word":"a bus","x":0.12,"y":0.22,"voice":"female"},
 {"word":"a police car","x":0.55,"y":0.41,"voice":"female"},
 {"word":"a cop","x":0.35,"y":0.50,"voice":"female"},
 {"word":"ducks","x":0.66,"y":0.71,"voice":"female"}],
"question":"What is the cop doing?",
"answer":["She","is","stopping","the","traffic."],
"answerVoice":"female",
"notes":"Cop box and duck box split at about x 0.50 where her right glove is close to the mother duck (glove tip or duck tail slightly cut). Ducks = mother duck + ducklings as one target. Cyclist is small in the background, boxes at the minimum size."}
json.dump(c,open('content/6989.json','w'),indent=1)
