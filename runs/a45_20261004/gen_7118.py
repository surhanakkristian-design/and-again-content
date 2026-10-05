import json
W=[(0.2,.12,.19,.54,.67),(0.7,.12,.18,.55,.69),(1.2,.10,.16,.58,.73),(1.7,.10,.17,.66,.73),(2.2,.31,.25,.43,.65),(2.7,.30,.33,.39,.57),(3.2,.27,.49,.49,.42),(3.7,.27,.49,.50,.42)]
C=[(0.2,.68,.38,.19,.33),(0.7,.69,.39,.19,.33),(1.2,.70,.38,.19,.35),(1.7,.77,.37,.16,.34),(2.2,.75,.36,.16,.36),(2.7,.71,.35,.20,.37),(3.2,.77,.33,.19,.39),(3.7,.78,.32,.19,.40)]
k=lambda L:[dict(t=t,x=x,y=y,w=w,h=h) for t,x,y,w,h in L]
d={"mediaId":7118,"level":"B","keyWord":"first lady","defaultVoice":"female",
"taps":[{"phrase":"to lift her cello overhead","target":"the cellist","voice":"female","keys":k(W)},
{"phrase":"to bow deeply over her cello","target":"the cellist","voice":"female","keys":k(W)},
{"phrase":"to applaud from the podium","target":"the conductor","voice":"male","keys":k(C)}],
"stillS":2.2,
"nouns":[{"word":"a cello","x":0.62,"y":0.58,"voice":"female"},{"word":"a conductor","x":0.82,"y":0.45,"voice":"male"},
{"word":"a cello case","x":0.76,"y":0.80,"voice":"female"},{"word":"a bow","x":0.30,"y":0.90,"voice":"female"}],
"question":"What is the conductor doing?","answer":["He","is","applauding","from","the","podium."],"answerVoice":"male",
"notes":"Key word 'first lady' is not a visible noun (no pill). Cellist boxes exclude the cello's far tip where it crosses the conductor (t=1.7). 'a bow' = the cello bow lying on the floor."}
json.dump(d,open("content/7118.json","w"),indent=1)
