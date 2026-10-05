import json
T=[round(i*0.5,1) for i in range(19)]
def keys(d):
    return [dict(t=t,**dict(zip('xywh',d[t]))) if t in d else {'t':t,'off':True} for t in T]
shorts={0.0:(.30,.35,.37,.40),0.5:(.22,.34,.43,.50),1.0:(.09,.37,.50,.60),1.5:(0,.35,.42,.50),2.0:(.28,.31,.44,.52),
 2.5:(.17,.37,.38,.52),3.0:(0,.40,.50,.59),3.5:(0,.32,.58,.67),4.0:(0,.35,.55,.60),4.5:(.06,.32,.30,.52),5.0:(0,.40,.25,.53),
 5.5:(0,.37,.18,.47),6.0:(0,.35,.18,.40),6.5:(0,.36,.20,.38),7.0:(0,.44,.30,.42),7.5:(.02,.37,.73,.63),8.0:(.10,.38,.52,.62),
 8.5:(.05,.40,.62,.60),9.0:(0,.42,.55,.58)}
cap={4.5:(.82,.37,.18,.58),5.0:(.82,.48,.18,.42),5.5:(.76,.36,.24,.58),6.0:(.68,.37,.28,.50),6.5:(.63,.34,.32,.43),7.0:(.52,.40,.28,.55),7.5:(.76,.45,.23,.52),
 8.0:(.70,.44,.30,.41),8.5:(.68,.43,.30,.42),9.0:(.62,.52,.28,.47)}
truck={5.0:(.53,.12,.47,.30),5.5:(.36,.08,.64,.27),6.0:(.30,.03,.68,.33),6.5:(.27,.03,.70,.30),7.0:(.20,.02,.78,.37),
 7.5:(.30,.14,.70,.22),8.0:(.26,.17,.74,.20),8.5:(.22,.19,.78,.20),9.0:(.20,.20,.75,.21)}
c={"mediaId":4875,"level":"A","keyWord":"truck","defaultVoice":"female",
"taps":[
 {"phrase":"to wipe her face","target":"the woman in shorts","voice":"female","keys":keys(shorts)},
 {"phrase":"to wear a blue cap","target":"the woman in the cap","voice":"female","keys":keys(cap)},
 {"phrase":"to be full of boxes","target":"the truck","voice":"female","keys":keys(truck)}],
"stillS":8.0,
"nouns":[{"word":"the sky","x":0.50,"y":0.06,"voice":"female"},
 {"word":"a truck","x":0.45,"y":0.22,"voice":"female"},
 {"word":"boxes","x":0.70,"y":0.50,"voice":"female"},
 {"word":"shorts","x":0.40,"y":0.90,"voice":"female"}],
"question":"What is the woman in shorts doing?",
"answer":["She","is","carrying","boxes","to","the","truck."],
"answerVoice":"female",
"notes":"Wipe-face happens at 8.0-8.5 s (arm across mouth). Truck box keyed only from 5.0 s (earlier only the ramp / an edge is visible) and only the upper cargo part so it never overlaps the two women standing in front. Cap woman keyed from 5.5 s (cap visible). State phrases for cap and truck because both women carry/push boxes and the sofa."}
json.dump(c,open('content/4875.json','w'),indent=1)
