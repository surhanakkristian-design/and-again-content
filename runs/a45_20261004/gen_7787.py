import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,x=x,y=y,w=w,h=h) for t,(x,y,w,h) in zip(T,b)]
cap=K([(.28,.30,.60,.51),(.26,.36,.60,.45),(.25,.37,.55,.42),(.30,.40,.48,.39),(.32,.36,.39,.45),(.30,.19,.39,.61),(.31,.20,.35,.59),(.32,.22,.35,.56)])
man=K([(0,.02,.22,.64),(0,.07,.23,.56),(0,.13,.24,.53),(0,.18,.26,.48),(0,.21,.27,.45),(0,.23,.29,.43),(0,.25,.28,.42),(0,.26,.29,.41)])
yel=K([(.82,0,.18,.30),(.80,.03,.20,.33),(.76,.10,.24,.26),(.73,.15,.27,.25),(.72,.18,.28,.48),(.70,.20,.30,.47),(.69,.22,.31,.45),(.69,.24,.31,.43)])
d={"mediaId":7787,"level":"B","keyWord":"compare","defaultVoice":"female",
"taps":[
 {"phrase":"to crouch behind the plank","target":"the woman in the cap","voice":"female","keys":cap},
 {"phrase":"to clench his fists","target":"the man in dungarees","voice":"male","keys":man},
 {"phrase":"to gasp in amazement","target":"the woman in the jumper","voice":"female","keys":yel}],
"stillS":3.7,
"nouns":[{"word":"a tent","x":0.15,"y":0.16,"voice":"female"},
 {"word":"a flat cap","x":0.50,"y":0.25,"voice":"female"},
 {"word":"a plank","x":0.30,"y":0.65,"voice":"female"},
 {"word":"straw","x":0.50,"y":0.90,"voice":"female"}],
"question":"What is the man in dungarees doing?",
"answer":["He","is","clenching","his","fists."],
"answerVoice":"male",
"notes":"Two pumpkins look alike, so no pumpkin noun. Cap woman crouches 0.2-2.2, then stands. Yellow-jumper woman gasps with hands at her mouth throughout. Boxes split where the cap woman meets the jumper woman (0.7-1.7)."}
json.dump(d,open('content/7787.json','w'),indent=1)
