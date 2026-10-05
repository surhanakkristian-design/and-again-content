import json
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def K(b): return [dict(t=t,off=True) if bb is None else dict(t=t,x=bb[0],y=bb[1],w=round(bb[2]-bb[0],2),h=round(bb[3]-bb[1],2)) for t,bb in zip(T,b)]
pair=K([(.25,.27,.68,.87),(.32,.29,.78,.91),(.33,.30,.73,.98),(.30,.31,.71,.98),(.26,.27,.70,1.0),(.20,.29,.78,1.0),(.20,.27,.74,1.0),(.17,.28,.79,1.0)])
cond=K([(.73,.42,.90,.72),(.80,.41,.96,.73),(.74,.42,.88,.74),(.72,.42,.88,.79),(.72,.42,.93,.74),(.79,.42,.99,.76),None,(.80,.42,.99,.79)])
c={"mediaId":7818,"level":"B","keyWord":"emotional","defaultVoice":"female",
"taps":[{"phrase":"to leap into her arms","target":"the dark-haired woman","voice":"female","keys":pair},
{"phrase":"to kick up her legs","target":"the dark-haired woman","voice":"female","keys":pair},
{"phrase":"to glance at his watch","target":"the conductor","voice":"male","keys":cond}],
"stillS":2.2,
"nouns":[{"word":"a glass roof","x":0.55,"y":0.10,"voice":"female"},{"word":"tulips","x":0.13,"y":0.62,"voice":"female"},
{"word":"a train","x":0.86,"y":0.42,"voice":"female"},{"word":"a conductor","x":0.82,"y":0.60,"voice":"male"}],
"question":"What are the two women doing?","answer":["They","are","crying","in","each","other's","arms."],"answerVoice":"female",
"notes":"The two women are entangled the whole clip, so only the dark-haired woman is a target and her box covers the whole hugging pair (the woman in the lilac coat is not a target). Leg kick clearest at 0.2-0.7 s. Conductor checks his wrist/watch at 2.7 and 3.7 s; he is hidden behind the young man at 3.2 s (off). They are laughing at first and crying from ~2.7 s."}
json.dump(c,open('content/7818.json','w'),indent=1)
