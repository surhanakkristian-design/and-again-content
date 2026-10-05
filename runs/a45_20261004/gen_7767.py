import json
vid=7767
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
def keys(rows): return [{"t":t,"x":r[0],"y":r[1],"w":r[2],"h":r[3]} if r else {"t":t,"off":True} for t,r in zip(T,rows)]
lh=[(0,.21,.30,.34),(0,.22,.30,.34),(0,.26,.27,.35),(0,.26,.27,.35),(0,.28,.37,.50),(0,.33,.32,.43),(0,.31,.28,.40),(0,.30,.27,.37)]
rh=[(.73,.23,.27,.42),(.74,.25,.26,.40),(.73,.25,.27,.40),(.74,.26,.26,.40),(.82,.25,.18,.16),(.82,.28,.18,.25),(.81,.28,.19,.42),(.74,.30,.26,.37)]
bt=[(.30,.79,.42,.21),(.30,.80,.42,.20),(.30,.81,.40,.19),(.31,.82,.40,.18),(.29,.82,.42,.18),(.33,.85,.42,.15),(.32,.86,.40,.14),(.32,.86,.42,.14)]
c={"mediaId":vid,"level":"A","keyWord":"bridge","defaultVoice":"male",
"taps":[{"phrase":"to wear a ring","target":"the left hand","voice":"male","keys":keys(lh)},
{"phrase":"to wear a bracelet","target":"the right hand","voice":"male","keys":keys(rh)},
{"phrase":"to hang above the bridge","target":"the boots","voice":"male","keys":keys(bt)}],
"stillS":1.7,
"nouns":[{"word":"the sky","x":.40,"y":.07,"voice":"male"},{"word":"water","x":.45,"y":.45,"voice":"male"},
{"word":"a bridge","x":.66,"y":.62,"voice":"male"},{"word":"fog","x":.22,"y":.68,"voice":"male"}],
"question":"What are the cars driving on?",
"answer":["The","cars","are","driving","on","a","red","bridge."],
"answerVoice":"male",
"notes":"POV paraglider clip: the pilot is only seen as two hands and two boots, so states are used for the hands (ring on the left hand, beaded bracelet on the right wrist) because both hands do the same action (holding the handles). The bracelet is hard to see at 2.2-2.7 s when the right hand is at the edge. Cars on the bridge deck are tiny; the question relies on them being visible from 1.2 s on. Key word 'bridge' is a verb in the packet; the noun 'a bridge' is used in slots and answer. defaultVoice male (hands look male; evenId false)."}
json.dump(c,open(f'content/{vid}.json','w'),indent=1)
