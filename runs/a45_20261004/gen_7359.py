import json
T=[0.2,0.7,1.2,1.7]
def K(rows): return [dict(t=t,**dict(zip('xywh',r))) if r else {"t":t,"off":True} for t,r in zip(T,rows)]
woman=K([(.10,.26,.70,.58),(.11,.27,.69,.62),(.03,.25,.77,.63),(.00,.23,.81,.73)])
cond=K([(.81,.21,.19,.52),(.81,.19,.19,.52),(.81,.17,.19,.55),(.82,.26,.18,.16)])
c={"mediaId":7359,"level":"B","keyWord":"miss","defaultVoice":"female",
"taps":[{"phrase":"to chase a moving train","target":"the woman","voice":"female","keys":woman},
{"phrase":"to clutch her skis","target":"the woman","voice":"female","keys":woman},
{"phrase":"to lean out of the doorway","target":"the conductor","voice":"male","keys":cond}],
"stillS":0.2,
"nouns":[{"word":"a lamp post","x":.13,"y":.24,"voice":"female"},{"word":"a wooden hut","x":.16,"y":.36,"voice":"female"},
{"word":"a conductor","x":.88,"y":.30,"voice":"male"},{"word":"a ski pole","x":.20,"y":.64,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","chasing","a","moving","train."],"answerVoice":"female",
"notes":"Only two clear targets: the porter by the hut and the friends at the window overlap the woman's skis/pole region, so they are not used. Woman and conductor boxes are split at x 0.80/0.81: her outstretched glove and his outstretched hand are partly cut. At 1.7 s only the conductor's hand is in frame (box on the hand). Key word 'miss' is a verb and not placed; she is still running, so 'to miss the train' is not used as it is not yet shown."}
json.dump(c,open('content/7359.json','w'),indent=1)
