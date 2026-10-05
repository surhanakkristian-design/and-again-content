from lib_7147_7148_7149_7150 import build
man = [(.21,.22,.71,.79),(.21,.21,.72,.79),(.21,.21,.73,.80),(.21,.20,.74,.80),
       (.21,.19,.75,.80),(.21,.18,.75,.80),(.22,.16,.75,.81),(.21,.14,.75,.81)]
woman = [(.03,.17,.21,.35),(.03,.17,.21,.36),(.03,.17,.21,.37),(.03,.17,.21,.37),
         (.03,.17,.21,.35),(.03,.17,.21,.36),(.03,.16,.22,.37),(.04,.16,.21,.41)]
lan = [(.78,.45,.99,.70),(.78,.45,1.0,.70),(.78,.45,.99,.71),(.79,.45,1.0,.71),
       (.82,.44,1.0,.71),(.82,.44,1.0,.72),(.82,.44,1.0,.72),(.82,.44,1.0,.73)]
build(7150,'B','gasoline','male',[
 ('to refuel a generator','the man','male',man),
 ('to watch from a window','the woman','female',woman),
 ('to glow on the generator','the lantern','male',lan)],
 1.2,[('a jerry can',.25,.51,'male'),('gasoline',.58,.60,'male'),('a lantern',.89,.50,'male'),('a generator',.72,.85,'male')],
 'What is the man pouring?','He is pouring gasoline into a funnel.','male',
 'The woman is small in the upper-left window, right above the man\'s jerry can/left arm: man box starts at x .21 so the left part of the can and his back are outside his box (woman box x .03-.21). He stops pouring at 3.2-3.7 and smiles; refuel phrase is true for 0.2-2.7. The gasoline pill sits on the thin stream between can spout and funnel. His headlamp also glows but is not on the generator.')
