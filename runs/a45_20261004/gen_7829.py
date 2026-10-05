import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
wom=[(.00,.19,.51,.96),(.02,.18,.47,.97),(.00,.17,.51,.97),(.02,.16,.51,.98),(.00,.15,.52,1.0),(.00,.14,.53,1.0),(.00,.13,.53,1.0),(.00,.12,.54,1.0)]
rib=[(.51,.41,.66,.58),(.50,.41,.66,.58),(.52,.41,.68,.58),(.51,.41,.66,.59),(.53,.42,.68,.60),(.54,.42,.69,.60),(.54,.47,.70,.65),(.55,.47,.70,.66)]
def k(b): return [dict(t=t,x=round(a[0],2),y=round(a[1],2),w=round(a[2]-a[0],2),h=round(a[3]-a[1],2)) for t,a in zip(T,b)]
W=k(wom)
d={"mediaId":7829,"level":"B","keyWord":"firmly","defaultVoice":"female",
"taps":[{"phrase":"to dig her heels in","target":"the woman in coral","voice":"female","keys":W},
{"phrase":"to hold her end alone","target":"the woman in coral","voice":"female","keys":W},
{"phrase":"to dangle from the rope","target":"the red ribbon","voice":"female","keys":k(rib)}],
"stillS":0.2,
"nouns":[{"word":"palm trees","x":0.78,"y":0.07,"voice":"female"},{"word":"a ribbon","x":0.57,"y":0.50,"voice":"female"},
{"word":"a rope","x":0.13,"y":0.55,"voice":"female"},{"word":"sand","x":0.70,"y":0.82,"voice":"female"}],
"question":"What is the woman in coral doing?",
"answer":["She","is","digging","her","heels","into","the","sand."],"answerVoice":"female",
"notes":"Only one strong human target that the overlap rule allows: the men pull together and overlap each other, the head-holding spectator is hidden behind the front woman from t=1.7. So two phrases on the woman in coral and one state phrase on the red marker ribbon (no action fits it). 'to dig her heels in' is used literally (feet dug into the sand, visible t=0.2-1.7; feet cropped later). Avoided 'firmly' in the answer because it could stand in two places."}
json.dump(d,open('content/7829.json','w'),indent=1)
