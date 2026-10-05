from mk_7214_7215_7216_7219 import write
M=[(.11,.29,.58,.45),(.17,.28,.55,.50),(.19,.23,.55,.55),(.08,.19,.45,.60),(.11,.19,.41,.62),(.08,.18,.40,.63),(.09,.18,.36,.65),(.08,.18,.36,.66)]
W=[(.70,.36,.30,.26),(.72,.36,.28,.25),(.74,.36,.26,.25),(.69,.35,.31,.27),(.61,.35,.39,.23),(.57,.35,.35,.22),(.55,.35,.31,.21),(.47,.35,.33,.22)]
write(7216,"B","help","male",[
 ("to push a stuck car","the man","male",M),
 ("to wave a white mitten","the woman","female",W),
 ("to lean out of the window","the woman","female",W)],
 2.2,[("a streetlamp",.22,.06,"male"),("a camel coat",.30,.45,"male"),("a wing mirror",.88,.54,"male"),("a paper bag",.18,.82,"male")],
 "What is the smiling man doing?","He is pushing a stuck car.","male",
 "He pushes only at 0.2-1.2, then straightens up laughing; answer is present continuous for the clip's main action. Background people with umbrellas are tiny and not targets.")
