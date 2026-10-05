from gen_6855_6856_6858_6859_lib import K, write
T=[0.2,0.7,1.2,1.7,2.2]
woman=K(T,[(.14,.25,.72,1),(.12,.24,.76,1),(.11,.22,.80,1),(0,.19,.94,1),(.12,.14,.99,1)])
man=K(T,[(0,.32,.14,.62),(0,.32,.12,.62),(0,.32,.11,.60),None,(0,.30,.12,.50)])
write(6856,{"mediaId":6856,"level":"A","keyWord":"band","defaultVoice":"female",
"taps":[{"phrase":"to tie a red ribbon","target":"the woman","voice":"female","keys":woman},
{"phrase":"to carry a lot of bread","target":"the woman","voice":"female","keys":woman},
{"phrase":"to have a beard","target":"the man on the left","voice":"male","keys":man}],
"stillS":0.2,
"nouns":[{"word":"a lantern","x":0.52,"y":0.18,"voice":"female"},{"word":"bread","x":0.42,"y":0.47,"voice":"female"},
{"word":"a table","x":0.82,"y":0.71,"voice":"female"},{"word":"a dog","x":0.80,"y":0.93,"voice":"female"}],
"question":"What is the woman doing?","answer":["She","is","tying","a","red","ribbon."],"answerVoice":"female",
"notes":"Man on the left is only half in frame at the left edge (box narrower than 0.18 because the woman's arm is right next to him); off at 1.7 s. Third phrase is a state: other guests (dog, thrower) appear only for one frame. A second lantern is half visible at the top-right edge at 0.2 s."})
