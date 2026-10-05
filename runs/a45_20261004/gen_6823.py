from gen_6821_6823_6825_6826_lib import write
woman = [(0.03,0.43,0.20,0.36),(0.03,0.43,0.20,0.36),(0.03,0.44,0.20,0.35),(0.03,0.44,0.21,0.35),(0.02,0.44,0.27,0.36),(0.02,0.44,0.27,0.36),(0.02,0.45,0.27,0.36),(0.02,0.45,0.27,0.36)]
water = [(0.23,0.61,0.40,0.13),(0.23,0.61,0.38,0.13),(0.23,0.62,0.44,0.13),(0.26,0.63,0.58,0.13),None,None,None,None]
boat  = [(0.31,0.08,0.38,0.53),(0.31,0.08,0.38,0.53),(0.31,0.08,0.38,0.53),(0.31,0.08,0.38,0.55),(0.31,0.08,0.38,0.58),(0.31,0.08,0.38,0.58),(0.31,0.09,0.38,0.58),(0.31,0.09,0.38,0.58)]
write(6823,"B","aftermath","female",[
 ("to stare up in shock","the woman","female",woman),
 ("to gush onto the pavement","the water","female",water),
 ("to block the narrow street","the boat","female",boat)],
 3.2,[("a fishing boat",0.42,0.53,"female"),("a dog",0.75,0.62,"female"),("a crate",0.54,0.77,"female"),("seaweed",0.30,0.92,"female")],
 "What is the woman staring at?","She is staring at a stranded boat.","female",
 "The gush of water from the doorway is visible 0.2-1.7 s only, then it has stopped (off from 2.2 s). Water and boat boxes are split at y ~0.61 where the stream runs past the bow. Dog = the black dog by the car. Key word 'aftermath' is abstract, not placed. Seagulls left out (two of them, gone after 1.7 s); the two men and the dog are tiny in the background.")
