import json
T=[i*0.5 for i in range(25)]
N=None
man=[(0,.36,.74,.64),(0,.22,.77,.78),(0,.13,.78,.85),(.1,.14,.88,.84),(.14,.09,.62,.59),(.13,.29,.86,.27)]+[N]*19
suit=[N]*6+[(.18,.17,.68,.83),(.19,.18,.78,.82),(.18,.21,.56,.79),(.22,.24,.53,.76),(.16,.23,.72,.77),(.07,.44,.68,.27),(0,.45,1,.32)]+[N]*12
old=[N]*13+[(.55,.3,.24,.42),(.55,.3,.22,.39),(.54,.27,.23,.41),(.51,.25,.24,.41),(.51,.23,.27,.4),(.51,.2,.34,.41),(.51,.17,.42,.44),
(.52,.15,.43,.48),(.53,.23,.28,.42),(.5,.29,.31,.31),(.5,.34,.33,.23),(.52,.34,.37,.31)]
def keys(b): return [dict(t=t,off=True) if v is None else dict(t=t,x=v[0],y=v[1],w=v[2],h=v[3]) for t,v in zip(T,b)]
c={"mediaId":5338,"level":"A","keyWord":"stay","defaultVoice":"female",
"taps":[{"phrase":"to climb onto a bunk bed","target":"the young man","voice":"male","keys":keys(man)},
{"phrase":"to take off her shoes","target":"the woman in the suit","voice":"female","keys":keys(suit)},
{"phrase":"to wear a long dress","target":"the old woman","voice":"female","keys":keys(old)}],
"stillS":12.0,
"nouns":[{"word":"the sky","x":0.5,"y":0.12,"voice":"female"},{"word":"the sea","x":0.6,"y":0.28,"voice":"female"},
{"word":"a phone","x":0.85,"y":0.43,"voice":"female"},{"word":"a bed","x":0.8,"y":0.67,"voice":"female"}],
"question":"What is the young man doing?",
"answer":["He","is","climbing","onto","a","bunk","bed."],"answerVoice":"male",
"notes":"Three scenes, one target per scene. The old woman has no action of her own (she does everything together with the old man), so her phrase is a state. Her box is split from the old man's at their joined hands. Question is about the first scene (young man)."}
json.dump(c,open('content/5338.json','w'),indent=1)
