from gen_7977_7978_7979_7980_lib import *
woman = keys([(.26,.28,.74,.72),(.30,.27,.70,.73),(.33,.27,.67,.73),(.28,.27,.72,.73),(.22,.27,.78,.73),(.24,.26,.76,.74),(.22,.27,.78,.73),(.24,.27,.76,.73)])
man = keys([(0,.02,.26,.98),(0,.02,.30,.98),(0,.05,.30,.55),(0,.36,.20,.16),None,None,(0,.05,.21,.95),(0,.06,.23,.94)])
write(7977, {"mediaId": 7977, "level": "A", "keyWord": "seeing", "defaultVoice": "female",
 "taps": [
  {"phrase": "to point out of the window", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to sit in a chair", "target": "the woman", "voice": "female", "keys": woman},
  {"phrase": "to stand by the chair", "target": "the man", "voice": "male", "keys": man}],
 "stillS": 0.7,
 "nouns": [{"word": "a bird", "x": .86, "y": .34, "voice": "female"}, {"word": "a lamp", "x": .20, "y": .27, "voice": "female"},
           {"word": "a chair", "x": .28, "y": .66, "voice": "female"}, {"word": "a window", "x": .88, "y": .14, "voice": "female"}],
 "question": "What is the woman doing?",
 "answer": ["She", "is", "pointing", "out", "of", "the", "window."],
 "answerVoice": "female",
 "notes": "Key word 'seeing' (noun) is not a visible thing, so not a noun slot. The man is only a hand at the left edge at 1.2/1.7 and off at 2.2/2.7 (fingertips only); his arm with the lens reaches into the woman's area at 0.2/0.7, the split cuts his arm. The bird is only visible until ~1.7, so it is a noun at 0.7 but not a tap target."})
