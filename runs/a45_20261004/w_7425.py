from w_7421_7422_7425_7427_lib import build
S=[[.47,.24,.25,.22],[.47,.24,.25,.22],[.48,.28,.25,.19],[.49,.28,.25,.19],[.48,.20,.25,.25],[.48,.18,.26,.26],[.48,.18,.26,.26],[.48,.17,.27,.26]]
B=[[.32,.46,.44,.31],[.31,.46,.44,.31],[.30,.47,.47,.31],[.30,.47,.48,.31],[.28,.45,.52,.34],[.27,.44,.54,.35],[.27,.44,.55,.36],[.26,.43,.58,.38]]
P=[[.00,.77,.60,.22],[.00,.77,.62,.22],[.00,.78,.75,.22],[.00,.78,.80,.22],[.00,.79,.85,.21],[.00,.79,.95,.21],[.00,.80,1.00,.20],[.00,.81,1.00,.19]]
build(7425,'B','petroleum','male',
 [("to gush from the valve","the stream of oil","male",S),
  ("to overflow with crude oil","the metal bucket","male",B),
  ("to spread across the ground","the black puddle","male",P)],
 1.2,
 [("a pump jack",.38,.25,"male"),("a hose",.15,.53,"male"),("a bucket",.50,.66,"male"),("petroleum",.20,.88,"male")],
 "What is happening to the metal bucket?","It is overflowing with crude oil.","male",
 "No people: defaultVoice male (evenId false). Stream, bucket and puddle touch each other: boxes split at the bucket rim (stream above) and the bucket base (puddle below), so the upper-left part of the puddle beside the bucket is outside the puddle box. 'petroleum' pill sits on the rainbow puddle.")
