import json
K=[(0.0,.06,.11,.74,.89),(0.5,.10,.14,.90,.86),(1.0,.10,.16,.86,.84),(1.5,.14,.19,.80,.81),(2.0,.23,.22,.65,.78),
(2.5,.22,.25,.51,.75),(3.0,.30,.29,.44,.67),(3.5,.31,.31,.38,.58),(4.0,.35,.32,.32,.43),(4.5,.37,.34,.25,.36),
(5.0,.37,.36,.26,.33),(5.5,.37,.38,.22,.28),(6.0,.39,.39,.20,.27),(6.5,.39,.40,.18,.25),(7.0,.39,.41,.18,.23),
(7.5,.39,.42,.18,.22),(8.0,.39,.42,.18,.21),(8.5,.38,.43,.18,.20),(9.0,.38,.43,.18,.20)]
keys=[dict(t=t,x=x,y=y,w=w,h=h) for t,x,y,w,h in K]
d={"mediaId":4888,"level":"B","keyWord":"barefoot","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman in white","voice":"female","keys":keys} for p in ["to wear a white sundress","to lead the crowd","to stare into the lens"]],
"stillS":3.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.12,"voice":"female"},{"word":"a sundress","x":0.52,"y":0.58,"voice":"female"},
{"word":"waves","x":0.80,"y":0.68,"voice":"female"},{"word":"sand","x":0.15,"y":0.82,"voice":"female"}],
"question":"What is the woman in white doing?",
"answer":["She","is","leading","the","crowd","along","the","shore."],"answerVoice":"female",
"notes":"Only one clearly identifiable person (everyone else is an anonymous, changing crowd who also walk barefoot in the surf), so all three phrases share the woman in white. Weak spots: a woman in a light floral sundress is at the far left edge at 0.0-1.0 s (but hers is patterned, not plain white); people walking toward the camera also roughly face the lens, she is the one staring straight into it. Key word 'barefoot' is an adjective and not used as a noun; the answer avoids it because 'barefoot' could stand in two places."}
json.dump(d,open("content/4888.json","w"),indent=1)
