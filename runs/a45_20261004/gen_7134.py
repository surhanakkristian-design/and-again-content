from gen_7131_7132_7134_7136_lib import write
white=[(.13,.25,.77,.64),(.22,.25,.64,.63),(.20,.24,.60,.64),(.55,.19,.45,.78),None,None,None,None]
blue=[None,None,None,(.27,.41,.16,.25),(.16,.38,.18,.29),(.05,.37,.20,.33),(0,.35,.14,.39),(0,.33,.14,.45)]
blue=[b if b is None else (b[0],b[1],max(b[2],.18),max(b[3],.14)) for b in blue]
write(7134,"A","footballer","male",[
 ("to catch the ball","the player in white","male",white),
 ("to run with the ball","the player in white","male",white),
 ("to wear a blue jacket","the man in blue","male",blue)],
 0.2,[("a light",.45,.06,"male"),("a ball",.81,.32,"male"),("a footballer",.42,.46,"male"),("grass",.66,.86,"male")],
 "What is the player in white doing?","He is catching the ball with both hands.","male",
 "Two phrases share the player in white (catch, then runs on with the ball tucked); he leaves the frame after 2.2 (at 2.2 a raised arm with the ball shows top right, but it is unclear whose arm it is, so it is set off). The opponent in gold is not a target: he is mostly hidden behind/overlapping the white player. Clapping not used: several people on the sideline clap. 'a footballer' is the keyword; the sport is American football.")
