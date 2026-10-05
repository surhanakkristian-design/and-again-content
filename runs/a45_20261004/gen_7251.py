from gen_7249_7250_7251_7252_lib import build
T = [0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
man = [(0.25,0.28,0.5,0.46),(0.24,0.28,0.54,0.46),(0.24,0.27,0.55,0.48),(0.22,0.25,0.6,0.5),
       (0.21,0.21,0.66,0.53),(0.2,0.19,0.69,0.55),(0.21,0.2,0.52,0.52),(0.23,0.2,0.5,0.5)]
dark = [(0.0,0.36,0.24,0.38),(0.0,0.36,0.23,0.38),(0.0,0.35,0.23,0.4),(0.0,0.33,0.21,0.42),
        (0.0,0.3,0.2,0.42),(0.0,0.28,0.19,0.42),(0.0,0.26,0.2,0.48),(0.0,0.24,0.22,0.5)]
red = [(0.79,0.39,0.21,0.33),(0.79,0.4,0.21,0.32),(0.8,0.4,0.2,0.36),(0.83,0.37,0.17,0.4),None,None,None,None]
build(7251,"B","intellectual","male",
 [("to sketch a diagram","the man with glasses","male",man),
  ("to fold her arms","the woman with black hair","female",dark),
  ("to take notes","the woman with red hair","female",red)],
 0.2,
 [("bookshelves",0.12,0.17,"male"),("an intellectual",0.43,0.43,"male"),("a stack of books",0.6,0.6,"male"),("sugar cubes",0.26,0.77,"male")],
 "What is the man with glasses doing?","He is sketching a diagram.","male",
 "Red-haired woman only at 0.2-1.7 (squeezed at the right edge at 1.7; at 2.2-2.7 only her writing hand shows at the edge -> off). The laughing man behind is not a target (the man with glasses laughs too from 2.2). 'an intellectual' pill sits on the man with glasses (key word).",T)
