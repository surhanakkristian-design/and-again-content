import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(rows): return [({"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]}) for t,r in zip(T,rows)]
wom=K([(.05,.42,.34,.49),(.02,.42,.35,.50),(.04,.42,.34,.50),(.03,.42,.35,.50),(.02,.42,.36,.50),(.02,.42,.35,.50),(.00,.42,.34,.54),(.00,.42,.28,.54)])
cat=K([(.40,.53,.18,.14),(.39,.52,.18,.14),(.39,.52,.18,.14),(.39,.52,.18,.15),(.39,.52,.18,.15),(.39,.53,.18,.14),(.35,.55,.20,.14),(.33,.55,.21,.14)])
man=K([(.60,.41,.33,.50),(.60,.40,.37,.51),(.60,.41,.36,.51),(.61,.40,.36,.52),(.64,.40,.33,.52),(.65,.40,.31,.52),(.60,.40,.38,.55),(.56,.39,.42,.57)])
c={"mediaId":7914,"level":"B","keyWord":"next door","defaultVoice":"female",
"taps":[{"phrase":"to soak her neighbour","target":"the red-haired woman","voice":"female","keys":wom},
{"phrase":"to operate a leaf blower","target":"the man","voice":"male","keys":man},
{"phrase":"to perch on the fence","target":"the cat","voice":"female","keys":cat}],
"stillS":2.2,
"nouns":[{"word":"a chimney","x":0.48,"y":0.07,"voice":"female"},{"word":"a leaf blower","x":0.80,"y":0.70,"voice":"female"},
{"word":"a picket fence","x":0.45,"y":0.80,"voice":"female"},{"word":"wellies","x":0.27,"y":0.89,"voice":"female"}],
"question":"What is the red-haired woman doing?","answer":["She","is","soaking","the","man","next","door."],"answerVoice":"female",
"notes":"two women (the second waves from an upstairs window, also in blue) -> target named 'the red-haired woman'; leaf blower only blows leaves at her from 3.2 s, so the phrase uses 'operate'; 'wellies' is British English"}
json.dump(c,open('content/7914.json','w'),indent=1)
