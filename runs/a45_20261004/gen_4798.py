import json
W=[(0.0,.19,.42,.62,.58),(0.5,.27,.36,.60,.64),(1.0,.33,.37,.50,.63),(1.5,.28,.32,.50,.68),(2.0,.24,.35,.54,.65),
(2.5,.31,.36,.50,.64),(3.0,.28,.38,.54,.62),(3.5,.34,.37,.52,.63),(4.0,.18,.39,.53,.52),(4.5,.23,.44,.48,.44),
(5.0,.21,.43,.43,.37),(5.5,.25,.43,.39,.44),(6.0,.24,.43,.40,.46),(6.5,.25,.43,.41,.43),(7.0,.20,.41,.45,.59),
(7.5,.31,.42,.37,.51),(8.0,.14,.39,.50,.60),(8.5,.30,.22,.62,.78),(9.0,.32,.20,.54,.78),(9.5,.32,.18,.52,.80),
(10.0,.31,.22,.48,.70),(10.5,.28,.19,.50,.72),(11.0,.24,.17,.50,.78),(11.5,.25,.20,.46,.78),(12.0,.18,.20,.46,.80)]
keys=[{"t":t,"x":x,"y":y,"w":w,"h":round(min(h,1-y),2)} for t,x,y,w,h in W]
c={"mediaId":4798,"level":"A","keyWord":"temple","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to walk up to the temple","to run down the street","to hold a straw hat"]],
"stillS":2.5,
"nouns":[{"word":"the sky","x":.50,"y":.08,"voice":"female"},{"word":"a temple","x":.50,"y":.28,"voice":"female"},
{"word":"a dress","x":.55,"y":.62,"voice":"female"},{"word":"stones","x":.25,"y":.70,"voice":"female"}],
"question":"Where is the woman walking?","answer":["She","is","walking","to","the","temple."],"answerVoice":"female",
"notes":"Only one clear target (the woman), so all three phrases use her. She wears a hat and also holds a second straw hat (AI quirk); 'to hold a straw hat' is true from 2.0 to 8.0 s. Temple walk 0-1.5 s, street run 4-8 s, dance 8.5-12 s with friends (not used: others dance too)."}
json.dump(c,open('content/4798.json','w'),indent=1)
