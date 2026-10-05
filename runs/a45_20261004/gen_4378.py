import json
T=[i*0.5 for i in range(25)]
N=None
B=[(.15,.16,.63,.84),(.17,.21,.62,.79),(.12,.24,.63,.76),(.12,.26,.73,.74),(.14,.29,.67,.71),(.14,.31,.67,.69),(.14,.32,.67,.68)]+[N]*18
Wm=[N]*9+[(.15,.20,.56,.68),(.20,.19,.50,.81),(.19,.21,.44,.79),(.10,.22,.50,.78),(.09,.21,.46,.79),(.09,.21,.53,.79)]+[N]*10
M=[N]*15+[(.42,.33,.18,.67),(.35,.32,.31,.68),(.24,.32,.51,.68),(.12,.32,.73,.68),(.07,.31,.91,.69),(.02,.31,.95,.69),(.05,.30,.93,.70),(.05,.31,.91,.69),(0,.31,.95,.69),(0,.30,.90,.70)]
def keys(B):
    return [{"t":t,"off":True} if b is None else {"t":t,"x":b[0],"y":b[1],"w":b[2],"h":b[3]} for t,b in zip(T,B)]
c={"mediaId":4378,"level":"A","keyWord":"shower","defaultVoice":"female",
"taps":[{"phrase":"to brush his teeth","target":"the boy","voice":"male","keys":keys(B)},
{"phrase":"to touch a yellow duck","target":"the woman","voice":"female","keys":keys(Wm)},
{"phrase":"to open two big doors","target":"the man","voice":"male","keys":keys(M)}],
"stillS":6.5,
"nouns":[{"word":"a shower","x":.14,"y":.21,"voice":"female"},{"word":"a towel","x":.62,"y":.42,"voice":"female"},{"word":"ducks","x":.70,"y":.63,"voice":"female"},{"word":"a bath","x":.72,"y":.86,"voice":"female"}],
"question":"What is the boy doing?","answer":["He","is","brushing","his","teeth."],"answerVoice":"male",
"notes":"Three shots, one person each (boy 0-3.0, woman 4.5-7.0, man 7.5-12.0); 3.5 s is only a door, at 4.0 s only the woman's hand shows behind the door (set off). defaultVoice female by evenId (mixed group). The shower on the still (6.5 s) is the small one behind the glass on the left; the key word is clearer in shots 1 and 3 but those have fewer nouns."}
json.dump(c,open('content/4378.json','w'),indent=1)
