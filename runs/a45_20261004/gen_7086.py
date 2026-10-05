from gen_7085_7086_7087_7089_lib import write
woman = [(.45,.09,.41,.88),(.47,.09,.40,.88),(.47,.10,.42,.87),(.48,.10,.42,.87),(.46,.08,.44,.89),(.46,.08,.44,.89),(.24,.10,.67,.60),(.22,.10,.67,.68)]
curd = [(.21,.45,.24,.17),(.21,.43,.26,.17),(.20,.45,.27,.16),(.21,.45,.27,.16),(.17,.44,.29,.16),(.17,.45,.29,.15),(.14,.70,.29,.17),(.14,.78,.31,.15)]
write(7086, "B", "enzyme", "female",
 [("to lift a block of curd", "the woman", "female", woman),
  ("to drip with whey", "the block of curd", "female", curd),
  ("to hold a measuring spoon", "the woman", "female", woman)],
 0.2,
 [("cheese moulds", .16, .33, "female"), ("a block of curd", .33, .53, "female"), ("a copper vat", .22, .68, "female"), ("a cheesecloth", .68, .92, "female")],
 "What is the woman holding?", "She is holding a block of curd.", "female",
 "Woman's box is split from the curd box (her left hand holds the curd), so her left hand sits in the curd box at 0.2-2.7. From 3.2 the curd is lowered into the vat (woman box cut above it). Key word 'enzyme' is not visible, no noun for it. Blurry people in the background are not used.")
