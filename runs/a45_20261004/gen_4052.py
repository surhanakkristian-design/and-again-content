import json
T=[i*0.5 for i in range(31)]
def mk(d):
    return [({"t":t,"x":d[t][0],"y":d[t][1],"w":d[t][2],"h":d[t][3]} if t in d else {"t":t,"off":True}) for t in T]
phone={t:(.37,.67,.26,.33) for t in T}
w=[(0,.27,.68,.39),(.05,.27,.53,.39),(.10,.28,.46,.38),(.19,.27,.38,.39),(.19,.27,.38,.39),(.20,.27,.36,.39),(.21,.27,.36,.39),(.20,.27,.36,.39),
(.22,.27,.36,.39),(.07,.24,.51,.42),(.06,.27,.51,.39),(.14,.27,.42,.39),(.15,.27,.42,.39),(.20,.27,.37,.39),(.20,.27,.37,.39),(.20,.27,.36,.39),
(.21,.27,.36,.39),(.07,.27,.52,.39),(.09,.27,.45,.39),(.16,.27,.38,.39),(.17,.27,.37,.39),(.17,.27,.36,.39),(.16,.27,.37,.39),(.17,.27,.36,.39),
(.16,.27,.37,.39),(.17,.27,.36,.39),(.16,.27,.37,.39),(.18,.28,.36,.38),(.29,.27,.27,.39),(.33,.28,.25,.38),(.32,.30,.29,.36)]
woman=dict(zip(T,w))
dog={11.0:(.63,.84,.37,.16),11.5:(.15,.72,.22,.28),12.0:(.17,.67,.20,.29),12.5:(.09,.67,.25,.27),13.0:(.12,.66,.22,.28),13.5:(.11,.67,.23,.27),
14.0:(.09,.68,.28,.27),14.5:(.15,.69,.22,.27),15.0:(.63,.74,.18,.16)}
d={"mediaId":4052,"level":"A","keyWord":"record","defaultVoice":"female",
"taps":[{"phrase":"to record the couple","target":"the phone","voice":"female","keys":mk(phone)},
{"phrase":"to walk to the phone","target":"the woman","voice":"female","keys":mk(woman)},
{"phrase":"to run across the sand","target":"the dog","voice":"female","keys":mk(dog)}],
"stillS":12.0,
"nouns":[{"word":"a phone","x":.52,"y":.72,"voice":"female"},{"word":"a dog","x":.26,"y":.82,"voice":"female"},{"word":"trees","x":.60,"y":.10,"voice":"female"},{"word":"sand","x":.80,"y":.90,"voice":"female"}],
"question":"What is the phone doing?","answer":["It","is","recording","the","couple."],"answerVoice":"female",
"notes":"The phone in the foreground overlaps the woman's legs and later the dog, so the woman's box is her head and upper body down to the top edge of the phone box (her legs below y 0.66 are outside it). The man is not a target; the woman's box overlaps him where they stand close or hug. Dog: at 15.0 s it is mostly hidden behind the phone, the box holds its head to the right of the phone. 'to record the couple' chosen so that it fits only the phone ('to record a video' would also fit the people)."}
json.dump(d,open("content/4052.json","w"),indent=1)
