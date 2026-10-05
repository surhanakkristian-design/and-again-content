from lib_7147_7148_7149_7150 import build
# boxes as (x1,y1,x2,y2) per time 0.2..3.7
man = [(.46,.30,.85,.89),(.46,.30,.85,.88),(.48,.29,.87,.88),(.50,.28,.88,.86),
       (.50,.15,.87,.80),(.50,.16,.89,.77),(.51,.31,.92,.77),(.44,.36,.88,.79)]
woman = [(.17,.40,.46,.82),(.19,.39,.46,.81),(.20,.36,.48,.81),(.21,.34,.50,.82),
         (.23,.31,.50,.78),(.20,.29,.50,.78),(.18,.09,.51,.78),(.15,.03,.44,.81)]
build(7147,'B','frying pan','male',[
 ('to crouch by the campfire','the man','male',man),
 ('to catch a flying pan','the man','male',man),
 ('to stroll across the sand','the woman','female',woman)],
 1.2,[('a frying pan',.52,.24,'male'),('a pancake',.46,.06,'male'),('a mixing bowl',.15,.70,'male'),('a campfire',.80,.82,'male')],
 'What is the man catching?','He is catching a frying pan in mid-air.','male',
 'Two frying pans (his flies, she carries one); the frying pan pill sits on the airborne pan at 1.2. Woman stands still at 3.2-3.7 (lifts her pan), strolling is 0.2-2.7. Man/woman boxes split around x .46-.51 where her hand and his knee are close; his knee is clipped slightly.')
