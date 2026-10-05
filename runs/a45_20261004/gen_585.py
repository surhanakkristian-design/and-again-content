import json
T=[i*0.5 for i in range(19)]
def keys(rows):
    return [{"t":t,"off":True} if r is None else {"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} for t,r in zip(T,rows)]
s=(.38,.45,.18,.14)
W=[(.08,.22,.84,.78),(.08,.23,.92,.77),(.10,.27,.88,.73),(.10,.29,.80,.71),(.13,.32,.68,.56),(.21,.35,.54,.45),(.26,.48,.44,.36),(.34,.42,.30,.30),(.41,.43,.20,.17),(.44,.45,.18,.14),s,s,s,s,s,s,s,s,s]
F=[None]*6+[(.78,.25,.22,.22),(.65,.03,.35,.46),(.20,.06,.78,.36),(.12,.10,.86,.33),(.10,.25,.88,.20),(.12,.17,.80,.27),(.14,.19,.74,.26),(.15,.20,.72,.25),(.15,.25,.70,.20),(.15,.25,.70,.20),(.15,.22,.70,.23),(.15,.22,.70,.23),(.15,.25,.70,.20)]
d={"mediaId":585,"level":"A","keyWord":"public","defaultVoice":"female",
"taps":[
 {"phrase":"to play music in public","target":"the young woman","voice":"female","keys":keys(W)},
 {"phrase":"to sit on a black box","target":"the young woman","voice":"female","keys":keys(W)},
 {"phrase":"to shoot water up","target":"the fountain","voice":"female","keys":keys(F)}],
"stillS":2.0,
"nouns":[{"word":"a street lamp","x":.25,"y":.12,"voice":"female"},{"word":"men","x":.50,"y":.36,"voice":"male"},{"word":"an accordion","x":.55,"y":.60,"voice":"female"},{"word":"a case","x":.60,"y":.90,"voice":"female"}],
"question":"What is the young woman doing?",
"answer":["She","is","playing","the","accordion","in","public."],
"answerVoice":"female",
"notes":"Camera pulls back: from 5.0 s the accordion player is tiny in the middle of the crowd (minimum box 0.18 x 0.14 around her, other listeners fall inside it). The supporting people (workers, old man) change between shots, so no phrase uses them; third target is the fountain (visible from 3.0 s). 'an accordion' is above A level but is the one central object. 'a case' = the open instrument case on the ground."}
json.dump(d,open("content/585.json","w"),indent=1)
