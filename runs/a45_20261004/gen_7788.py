import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,b)]
wom=K([(.28,.16,.49,.35),(.28,.16,.49,.34),(.28,.15,.50,.35),(.28,.14,.51,.35),(.27,.12,.53,.35),(.27,.11,.55,.35),(.27,.10,.54,.37),(.27,.10,.57,.37)])
sto=K([(.30,.52,.34,.17),(.31,.51,.37,.19),(.25,.50,.45,.19),(.22,.49,.51,.20),(.20,.47,.60,.21),(.18,.46,.63,.22),(.16,.47,.66,.22),(.15,.47,.67,.23)])
d={"mediaId":7788,"level":"B","keyWord":"contain","defaultVoice":"female",
"taps":[
 {"phrase":"to crack into two halves","target":"the stone","voice":"female","keys":sto},
 {"phrase":"to lean on the workbench","target":"the woman","voice":"female","keys":wom},
 {"phrase":"to point at the crystals","target":"the woman","voice":"female","keys":wom}],
"stillS":1.2,
"nouns":[{"word":"a desk lamp","x":0.12,"y":0.27,"voice":"female"},
 {"word":"a cactus","x":0.88,"y":0.41,"voice":"female"},
 {"word":"crystals","x":0.40,"y":0.60,"voice":"female"},
 {"word":"a sack","x":0.86,"y":0.58,"voice":"female"}],
"question":"What is the woman pointing at?",
"answer":["She","is","pointing","at","the","purple","crystals."],
"answerVoice":"female",
"notes":"Stone box split from the woman's box at the stone's top edge; it also covers the viewer's hands holding it. Woman points only at 3.2-3.7. 'crystals' pill on the left half; both halves are full of crystals (one group)."}
json.dump(d,open('content/7788.json','w'),indent=1)
