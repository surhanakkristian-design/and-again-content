import json
T=[i*0.5 for i in range(21)]
N=None
wom=[N]*18+[(0,.29,.26,.33),(0,.36,.31,.30),(0,.36,.29,.30)]
bird=[N]*17+[(.47,.23,.18,.14),(.47,.31,.18,.14),(.47,.34,.18,.14),(.47,.35,.18,.14)]
hand=[N]*7+[(.5,.18,.5,.82),(.5,.14,.5,.80),(.55,.12,.45,.75)]+[N]*4+[(.06,.26,.94,.56),(.13,.34,.87,.45),(.23,.26,.77,.36),(.42,.37,.58,.29),(.62,.56,.38,.28),(.65,.62,.35,.27),(.64,.64,.36,.27)]
def keys(b):
    return [({"t":t,"x":k[0],"y":k[1],"w":k[2],"h":k[3]} if k else {"t":t,"off":True}) for t,k in zip(T,b)]
d={"mediaId":485,"level":"B","keyWord":"moss","defaultVoice":"female",
"taps":[
 {"phrase":"to lean against the boulder","target":"the woman","voice":"female","keys":keys(wom)},
 {"phrase":"to squeeze out the water","target":"the hand in the orange sleeve","voice":"female","keys":keys(hand)},
 {"phrase":"to perch in a hollow","target":"the bird","voice":"female","keys":keys(bird)}],
"stillS":9.5,
"nouns":[{"word":"moss","x":.60,"y":.55,"voice":"female"},{"word":"a braid","x":.16,"y":.44,"voice":"female"},{"word":"a fist","x":.80,"y":.76,"voice":"female"},{"word":"branches","x":.35,"y":.13,"voice":"female"}],
"question":"What is the woman doing?",
"answer":["She","is","resting","her","cheek","on","the","moss."],"answerVoice":"female",
"notes":"Many cuts; no person is seen whole. The woman appears only 9.0-10.0 s (at 8.5 s just a sliver at the left edge: off). The bird is SMALL (about 0.05 wide) and sits in the hollow of the mossy rock from 8.5 s (blurred there) - check it is visible enough. The hand in the orange sleeve: the squeezing hand 7.0-10.0 s; at 3.5-4.5 s both orange-sleeved hands on the right half (the green-sleeved hands are on the left, split at about x 0.5). The squeezing happens only from 7.0 s. 'a fist' = the hand closed around the moss; 'branches' = the bare branches at the top."}
json.dump(d,open("content/485.json","w"),indent=1,ensure_ascii=False)
