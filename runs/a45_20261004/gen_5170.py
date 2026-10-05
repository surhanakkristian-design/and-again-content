import json
T=[i*0.5 for i in range(19)]
def K(d):
    return [{"t":t,"off":True} if d.get(t) is None else dict(t=t,x=d[t][0],y=d[t][1],w=d[t][2],h=d[t][3]) for t in T]
M={0.0:(0,.17,.95,.83),0.5:(0,.10,1,.90),1.0:(0,.10,.80,.90),1.5:(0,.10,.80,.90),2.0:(0,.12,.80,.88),2.5:(0,.20,.58,.80),
 3.0:(0,.08,.70,.92),3.5:(.50,.28,.50,.70),4.0:(.52,.27,.48,.72),4.5:(.48,.27,.52,.72),5.0:(0,0,.78,.95),5.5:(0,0,.92,1),
 6.0:(0,.10,.35,.88),6.5:(0,.12,.60,.88),7.0:(0,.20,.75,.80),7.5:(0,.20,.70,.80),8.0:(0,.19,.75,.81),8.5:(.05,.21,.90,.79),9.0:(.03,.24,.90,.76)}
W={3.5:(0,.38,.18,.36),4.0:(.25,.40,.25,.30)}
c={"mediaId":5170,"level":"B","keyWord":"package","defaultVoice":"male",
"taps":[{"phrase":"to deliver a package","target":"the postman","voice":"male","keys":K(M)},
{"phrase":"to rummage in his bag","target":"the postman","voice":"male","keys":K(M)},
{"phrase":"to water the front garden","target":"the old woman","voice":"female","keys":K(W)}],
"stillS":7.0,
"nouns":[{"word":"a cap","x":0.33,"y":0.25,"voice":"male"},{"word":"a package","x":0.69,"y":0.48,"voice":"male"},
{"word":"a brick wall","x":0.72,"y":0.78,"voice":"male"},{"word":"a bicycle","x":0.28,"y":0.90,"voice":"male"}],
"question":"What is the postman doing?","answer":["He","is","delivering","a","package."],"answerVoice":"male",
"notes":"The old woman watering is only visible at 3.5-4.0 s (hidden behind the postman at 4.5 s, off). The resident who takes the parcel shows only a hand/arm, so not used as a target. Postman boxes include his bag but not the bicycle."}
json.dump(c,open('content/5170.json','w'),indent=1)
