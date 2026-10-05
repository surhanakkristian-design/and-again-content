import json
O={"off":True}
def B(x,y,w,h): return {"x":x,"y":y,"w":w,"h":h}
times=[i*0.5 for i in range(19)]
woman=[B(0,.36,.46,.32),B(0,.33,.35,.67),O,O,O,O,B(0,.28,.48,.46),B(0,.36,.48,.38),B(0,.34,.54,.39),B(0,.32,.66,.38),O,B(0,.35,.33,.65),B(.03,.40,.45,.60),B(.03,.32,.45,.68),B(0,.40,.46,.60),B(.06,.40,.41,.60),B(.19,.40,.29,.34),B(.27,.44,.21,.21),B(.30,.45,.19,.20)]
man=[B(.52,.18,.48,.82),B(.56,.15,.44,.85),O,O,O,O,B(.50,.17,.50,.57),B(.50,.18,.50,.56),B(.56,.26,.42,.74),B(.67,.34,.31,.44),B(.70,.53,.28,.27),B(.60,.28,.38,.70),B(.50,.24,.50,.76),B(.50,.22,.50,.78),B(.48,.24,.52,.76),B(.49,.31,.44,.69),B(.49,.37,.27,.37),B(.49,.41,.21,.24),B(.49,.44,.19,.21)]
comp=[B(.10,.69,.24,.15),B(.35,.60,.20,.21),B(.08,.08,.80,.90),B(.05,0,.88,1.0),B(.05,0,.88,.90),B(.05,0,.88,.90),B(.36,.75,.22,.17),B(.38,.75,.22,.17),B(.34,.74,.20,.14),B(.36,.71,.20,.15),B(.27,.37,.40,.53),B(.34,.55,.20,.16),B(.25,.24,.20,.15),O,O,O,O,O,O]
def K(l): return [dict(t=t,**k) for t,k in zip(times,l)]
d={"mediaId":502,"level":"A","keyWord":"north","defaultVoice":"female",
"taps":[
 {"phrase":"to hold a compass","target":"the woman","voice":"female","keys":K(woman)},
 {"phrase":"to wear a blue hat","target":"the man","voice":"male","keys":K(man)},
 {"phrase":"to lie in her hand","target":"the compass","voice":"female","keys":K(comp)}],
"stillS":0.0,
"nouns":[{"word":"the sky","x":.50,"y":.10,"voice":"female"},{"word":"a man","x":.82,"y":.50,"voice":"male"},{"word":"the sun","x":.50,"y":.44,"voice":"female"},{"word":"a woman","x":.22,"y":.58,"voice":"female"}],
"question":"What does the compass show?",
"answer":["The","compass","shows","the","way","north."],
"answerVoice":"female",
"notes":"'compass' is above A2 but is the central object of the clip (key word north is not a visible noun). Woman is OFF in the close-ups (1.0-2.5, 5.0) where only her mitten is visible around the compass. Woman/man boxes are cut above the compass at 0.0, 3.0-4.5 so they do not overlap the compass box. State phrase for the man (both hikers walk). Answer relies on the needle resting on N at 2.0-2.5."}
json.dump(d,open("content/502.json","w"),indent=1)
