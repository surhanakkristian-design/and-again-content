import json
T=[i*0.5 for i in range(21)]
man=[(0,.28,.88,.72),(0,.28,.92,.72),(0,.23,.88,.77),(0,.12,.92,.88),(0,.22,.85,.78),(.05,.27,.8,.73),(.03,.3,.82,.7),(.07,.31,.8,.69),
(.08,.34,.78,.66),(.08,.36,.78,.64),(.08,.4,.76,.6),(.08,.45,.72,.55),(.08,.5,.7,.5),(.08,.55,.68,.45),(.08,.59,.6,.41),(.08,.62,.6,.38),
(.08,.66,.55,.34),(.13,.7,.48,.3),(.08,.73,.45,.27),(.06,.74,.47,.26),(.04,.75,.45,.25)]
lights=[(.25,0,.75,.12),(.25,0,.75,.12),(.3,0,.7,.14),(.3,0,.7,.11),(.3,0,.7,.17),(.3,0,.7,.19),(.3,.02,.7,.16),(.3,.02,.7,.16),
(.3,.03,.7,.2),(.3,.06,.7,.18),(.3,.08,.7,.17),(.3,.08,.7,.18),(.3,.13,.7,.16),(.3,.15,.7,.16),(.28,.19,.72,.15),(.25,.21,.75,.15),
(.2,.24,.8,.17),(.18,.26,.82,.17),(.12,.31,.88,.17),(.12,.32,.88,.17),(.08,.33,.92,.18)]
def keys(b): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,b)]
c={"mediaId":5336,"level":"B","keyWord":"loyalty","defaultVoice":"male",
"taps":[{"phrase":"to take off his cap","target":"the bearded man","voice":"male","keys":keys(man)},
{"phrase":"to clutch his flat cap","target":"the bearded man","voice":"male","keys":keys(man)},
{"phrase":"to light up the stadium","target":"the floodlights","voice":"male","keys":keys(lights)}],
"stillS":6.5,
"nouns":[{"word":"floodlights","x":0.62,"y":0.24,"voice":"male"},{"word":"a flag","x":0.54,"y":0.57,"voice":"male"},
{"word":"a beard","x":0.37,"y":0.68,"voice":"male"},{"word":"a flat cap","x":0.34,"y":0.84,"voice":"male"}],
"question":"What is the bearded man doing?",
"answer":["He","is","clutching","his","cap","to","his","chest."],"answerVoice":"male",
"notes":"Only the bearded man has a cap; others only lay a hand on the heart, so the cap phrases fit him alone. Floodlights box follows the main bright row of lights. Flag noun is a small white flag behind the crowd."}
json.dump(c,open('content/5336.json','w'),indent=1)
