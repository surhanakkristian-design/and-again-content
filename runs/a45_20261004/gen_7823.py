from lib_7820_7821_7823_7824 import *
bd=[(.645,.44,.84,.58),(.74,.37,.92,.51),(.62,.29,.80,.43),(.57,.24,.83,.37),(.68,.24,.86,.38),(.76,.21,.96,.35),(.79,.23,.99,.37),(.79,.23,.97,.37)]
sf=[(.42,.45,.64,.70)]+[(.42,.45,.68,.70)]*7
save({"mediaId":7823,"level":"B","keyWord":"face","defaultVoice":"male",
 "taps":[tap("to flutter beside a sunflower","the bird","male",bd),
         tap("to fly off towards the sun","the bird","male",bd),
         tap("to face the rising sun","the tall sunflower","male",sf)],
 "stillS":0.2,
 "nouns":[nn("a tree",.33,.35,"male"),nn("the sun",.89,.32,"male"),nn("a goldfinch",.73,.50,"male"),nn("a sunflower",.53,.59,"male")],
 "question":"What is the bird doing?",
 "answer":["It","is","flying","off","towards","the","sun."],
 "answerVoice":"male",
 "notes":"Only two targets: the goldfinch (two phrases: flutters beside the tall sunflower at 0.2 s, then flies off towards the sun 0.7-3.7 s) and the tall sunflower in the middle, the only big head seen in profile turned to the right towards the low sun (the others face the camera; the description says all face the camera, the frames show this one sideways). The sun itself is not a target because the bird flies right over it. Bird box cut at x 0.645 at 0.2 s where it touches the sunflower's petals. 'a sunflower' pill sits on the lower half of the tall sunflower head."})
