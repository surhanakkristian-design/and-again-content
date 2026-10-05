from gen_7275_7276_7277_7278_lib import *
def b(x0,y0,x1,y1): return (x0,y0,round(x1-x0,2),round(y1-y0,2))
lamp=[b(.28,.01,.50,.15),b(.29,.02,.48,.16),b(.28,.03,.49,.17),b(.28,.04,.48,.18),b(.27,.05,.47,.19),b(.27,.06,.47,.20),b(.26,.07,.46,.21),b(.26,.07,.46,.21)]
tower=[b(.36,.15,.54,.68),b(.37,.16,.55,.69),b(.37,.17,.55,.71),b(.36,.18,.54,.71),b(.36,.19,.54,.73),b(.36,.20,.54,.75),b(.30,.21,.48,.76),b(.35,.21,.53,.77)]
man=[b(.54,.13,.86,.87),b(.55,.13,.86,.87),b(.55,.26,.97,.88),b(.54,.28,1,.89),b(.54,.29,.99,.91),b(.54,.29,1,.92),b(.48,.30,.92,.93),b(.53,.31,.92,.93)]
write(7277,"B","kill time","male",
 [("to spread his arms wide","the young man","male",man),
  ("to balance on a suitcase","the tower of cups","male",tower),
  ("to light up the platform","the street lamp","male",lamp)],
 2.2,
 [("a street lamp",0.37,0.13,"male"),("a clock",0.21,0.24,"male"),("a suitcase",0.50,0.82,"male"),("paper boats",0.70,0.95,"male")],
 "What is the young man doing?","He is spreading his arms wide.","male",
 "Tower box widened to the 0.18 minimum; the man's raised hand (0.2-0.7) and left hand on the tower (1.2-2.7) fall inside the tower box. Arms spread 1.2-2.7, fists clenched 3.2-3.7 (answer fits the middle of the clip).")
