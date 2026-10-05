import json
K=[(0.0,.05,.15,.88,.55),(0.5,.02,.13,.90,.58),(1.0,.03,.15,.84,.62),(1.5,.04,.15,.83,.63),(2.0,.14,.11,.62,.70),(2.5,.13,.12,.62,.70),
(3.0,.11,.13,.62,.70),(3.5,.10,.13,.62,.70),(4.0,.09,.14,.62,.68),(4.5,.08,.15,.62,.68),(5.0,.05,.28,.69,.56),(5.5,.23,.13,.66,.62),
(6.0,.38,.25,.40,.42),(6.5,.40,.33,.34,.31),(7.0,.45,.37,.28,.27),(7.5,.46,.39,.23,.23),(8.0,.46,.41,.18,.18),(8.5,.45,.42,.18,.15),(9.0,.45,.42,.18,.14)]
keys=[{"t":t,"x":x,"y":y,"w":w,"h":h} for t,x,y,w,h in K]+[{"t":9.5,"off":True},{"t":10.0,"off":True}]
d={"mediaId":219,"level":"A","keyWord":"deer","defaultVoice":"male",
"taps":[{"phrase":p,"target":"the deer","voice":"male","keys":keys} for p in ["to look at the camera","to open its mouth","to run away"]],
"stillS":2.5,
"nouns":[{"word":"a deer","x":.50,"y":.50,"voice":"male"},{"word":"trees","x":.72,"y":.07,"voice":"male"},{"word":"plants","x":.50,"y":.86,"voice":"male"}],
"question":"What is the deer doing?","answer":["The","deer","is","running","away."],"answerVoice":"male",
"notes":"Only one target (the deer) for all three phrases; a small bird flies top right for the first second only, not used. The deer fades into fog: boxes off at 9.5 and 10.0, barely visible at 9.0. The question fits the second half of the clip (it walks and stands before it runs away). 'plants' used for the ferns (level A)."}
json.dump(d,open("content/219.json","w"),indent=1)
