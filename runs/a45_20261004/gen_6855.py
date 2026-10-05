from gen_6855_6856_6858_6859_lib import K, write
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
young=K(T,[(.12,.14,.67,1),(.12,.14,.67,1),(.10,.14,.67,1),(.09,.14,.65,1),(.06,.13,.65,1),(.07,.13,.65,1),(.08,.13,.64,1),(0,.12,.64,1)])
cap=K(T,[(.67,.19,.89,.50),(.67,.19,.89,.50),(.67,.20,.89,.50),(.65,.20,.86,.50),(.65,.20,.85,.50),(.65,.20,.85,.48),(.64,.21,.84,.50),(.64,.21,.84,.50)])
write(6855,{"mediaId":6855,"level":"A","keyWord":"band","defaultVoice":"male",
"taps":[{"phrase":"to tie the flowers together","target":"the young man","voice":"male","keys":young},
{"phrase":"to lift the flowers up","target":"the young man","voice":"male","keys":young},
{"phrase":"to wear a cap","target":"the man in the cap","voice":"male","keys":cap}],
"stillS":2.2,
"nouns":[{"word":"a cart","x":0.77,"y":0.46,"voice":"male"},{"word":"a knife","x":0.13,"y":0.80,"voice":"male"},
{"word":"string","x":0.61,"y":0.80,"voice":"male"},{"word":"a table","x":0.32,"y":0.92,"voice":"male"}],
"question":"What is the young man doing?","answer":["He","is","tying","the","flowers","together."],"answerVoice":"male",
"notes":"Young man's flowers reach into the background man in the cap (x .62-.78) at 0.2-1.2 s; boxes split at x .67 / .65, so the left edge of the cap man is inside the young man's box. Older man at right edge is not a target."})
