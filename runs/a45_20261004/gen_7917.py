from gen_7917_7919_7920_7921_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
sheet=[(.20,.29,.20,.16),(.17,.23,.26,.16),(.20,.29,.23,.14),(.20,.29,.22,.14),(.14,.21,.29,.16),(.13,.27,.30,.14),(.15,.18,.27,.17),(.10,.25,.29,.14)]
dust=[(.00,.36,.19,.26),(.00,.26,.16,.36),(.24,.44,.20,.19),(.01,.44,.42,.22),(.00,.55,.34,.15),(.00,.15,.12,.20),(.00,.27,.14,.16),(.00,.10,.09,.25)]
pud=[(.00,.72,.70,.26)]*8
build(7917,"B","nowhere","male",T,[
 ("to flap in the strong wind","the loose metal sheet","male",sheet),
 ("to swirl across the salt flat","the dust","male",dust),
 ("to reflect the stormy sky","the puddle","male",pud)],
 3.7,[("a bus shelter",.62,.52,"male"),("a puddle",.30,.86,"male"),("mountains",.86,.42,"male"),("clouds",.50,.12,"male")],
 "Where is the bus shelter?","The bus shelter stands in the middle of nowhere.","male",
 "No people. Dust is faint at 2.7-3.7 (thin plume at the left edge), boxes small there. Puddle reflection is dim and brownish; puddle box fixed bottom-left.")
