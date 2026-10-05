import json
W=[(0.0,.62,.27,.28,.34),(0.5,.60,.27,.28,.36),(1.0,.60,.25,.28,.38),(1.5,.63,.24,.32,.39),(2.0,.61,.23,.29,.41),(2.5,.60,.24,.28,.39),
(3.0,.37,.29,.44,.37),(3.5,.36,.28,.42,.37),(4.0,.08,.24,.76,.74),(4.5,.27,.19,.65,.79),(5.0,.29,.22,.60,.77),(5.5,.27,.26,.50,.73),
(6.0,.26,.29,.50,.70),(6.5,.21,.27,.45,.71),(7.0,.46,.29,.34,.36),(7.5,.41,.28,.47,.37),(8.0,.46,.34,.30,.32),(8.5,.30,.35,.47,.32),
(9.0,.29,.35,.50,.31),(9.5,.27,.35,.42,.31),(10.0,.22,.40,.62,.21)]
keys=[dict(t=t,x=x,y=y,w=w,h=h) for t,x,y,w,h in W]
d={"mediaId":5264,"level":"B","keyWord":"shift","defaultVoice":"female",
"taps":[{"phrase":p,"target":"the woman","voice":"female","keys":keys} for p in ["to shift the heavy sofa","to hang a large canvas","to stretch out on the sofa"]],
"stillS":9.0,
"nouns":[{"word":"a window","x":.30,"y":.30,"voice":"female"},{"word":"a sofa","x":.22,"y":.57,"voice":"female"},
{"word":"a coffee table","x":.70,"y":.62,"voice":"female"},{"word":"a rug","x":.50,"y":.75,"voice":"female"}],
"question":"What is the woman moving first?",
"answer":["She","is","shifting","the","sofa","across","the","floor."],
"answerVoice":"female",
"notes":"Only one person; all three taps on the woman. Last shot from the doorway (7.0-10.0) she is small. 'to hang a large canvas' = 4.5-6.0."}
json.dump(d,open('content/5264.json','w'),indent=1)
