import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(lst): return [dict(t=t,x=b[0],y=b[1],w=b[2],h=b[3]) if b else {"t":t,"off":True} for t,b in zip(T,lst)]
woman=K([(.19,.27,.53,.73),(.19,.25,.56,.75),(.15,.23,.59,.77),(.13,.21,.64,.79),(.12,.18,.65,.82),(.10,.15,.69,.85),(.08,.19,.72,.81),(.08,.20,.73,.80)])
girl=K([(0,.41,.18,.56),(0,.41,.18,.56),(0,.41,.14,.56),(0,.40,.13,.55),(0,.40,.12,.52),(0,.40,.10,.50),None,None])
lion=K([(.35,.05,.33,.22),(.35,.04,.34,.21),(.34,.03,.34,.20),(.34,.03,.36,.18),(.33,0,.37,.18),(.33,0,.39,.15),(.32,0,.38,.19),(.31,0,.41,.20)])
c={"mediaId":6815,"level":"B","keyWord":"acid","defaultVoice":"female",
"taps":[
 {"phrase":"to squeeze half a lemon","target":"the woman in the lab coat","voice":"female","keys":woman},
 {"phrase":"to film with her phone","target":"the woman with the phone","voice":"female","keys":girl},
 {"phrase":"to tower over the crowd","target":"the lion","voice":"female","keys":lion}],
"stillS":2.7,
"nouns":[{"word":"a lion","x":0.50,"y":0.10,"voice":"female"},{"word":"safety goggles","x":0.50,"y":0.37,"voice":"female"},
 {"word":"a test strip","x":0.38,"y":0.53,"voice":"female"},{"word":"a bowl","x":0.88,"y":0.77,"voice":"female"}],
"question":"What is the woman in goggles doing?",
"answer":["She","is","squeezing","half","a","lemon."],
"answerVoice":"female",
"notes":"Woman with the phone sits at the left edge and drifts out: narrow box at 2.2-2.7, off at 3.2-3.7 (only a sliver of phone). Lion box is cut above the lab-coat woman's box (her raised hand); at 3.2-3.7 her box starts at her head so the raised glove is partly outside both boxes. Lion is a sculpture made of fruit; key word 'acid' not visible as a noun."}
json.dump(c,open('content/6815.json','w'),indent=1)
