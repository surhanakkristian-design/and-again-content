from gen_7064_7065_7066_7068_lib import write
waiter=[(.43,.27,.86,.84),(.45,.27,.84,.86),(.53,.26,.86,.92),(.60,.26,.85,.92),(.55,.25,.86,.87),(.41,.27,.85,.87),(.33,.28,.73,.93),(.36,.28,.74,.92)]
goats=[(0,.46,.42,.74),(.02,.47,.44,.73),(.02,.46,.52,.76),(.02,.49,.59,.84),(.02,.47,.54,.75),(.02,.48,.40,.73),(.02,.48,.31,.71),(.01,.51,.20,.70)]
waitress=[(.87,.27,1.0,.58),(.86,.27,1.0,.56),(.87,.29,1.0,.53),(.86,.30,1.0,.56),(.87,.28,1.0,.49),(.86,.29,1.0,.52),(.86,.30,1.0,.57),(.82,.30,1.0,.58)]
write(7068,"B","drive out","male",[
 ("to drive the goats out","the waiter","male",waiter),
 ("to escape through the doorway","the goats","male",goats),
 ("to carry a silver tray","the waitress","female",waitress)],
 3.7,[("the sea",.12,.40,"male"),("a goat",.12,.58,"male"),("a red tablecloth",.54,.56,"male"),("bread rolls",.36,.90,"male")],
 "What is the waiter doing?","He is driving the goats out of the room.","male",
 "Waiter box excludes the far ends of the swinging red cloth where it reaches toward the goats / the waitress (split along the line between targets). 'the goats' is a group target; only one goat is left by the door at 3.2-3.7 (small box). Waitress (white T-shirt, far right) holds a silver tray up early and lower later. Answer avoids 'driving out the goats' word-order ambiguity by ending 'out of the room'.")
