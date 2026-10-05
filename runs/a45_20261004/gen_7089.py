from gen_7085_7086_7087_7089_lib import write
woman = [(.13,.35,.44,.46),(.15,.36,.43,.45),(.14,.38,.38,.43),(.27,.39,.25,.42),(.22,.40,.27,.42),(.21,.42,.26,.40),(.19,.44,.26,.39),(.18,.47,.25,.36)]
eleph = [(.57,.29,.31,.24),(.58,.29,.31,.25),(.52,.28,.38,.30),(.52,.26,.40,.32),(.49,.25,.47,.36),(.47,.24,.50,.38),(.45,.26,.53,.38),(.43,.27,.55,.39)]
man = [None,None,None,(.08,.40,.19,.28),(.05,.41,.17,.29),(.04,.41,.17,.30),(.01,.44,.18,.30),(.01,.46,.17,.28)]
write(7089, "B", "expand", "female",
 [("to push against a giant sponge", "the woman", "female", woman),
  ("to knock off a wooden crate", "the elephant sponge", "female", eleph),
  ("to film with his phone", "the man in the denim jacket", "male", man)],
 2.2,
 [("an awning", .80, .22, "female"), ("a wooden crate", .84, .50, "female"), ("a barrel", .70, .70, "female"), ("cobblestones", .30, .90, "female")],
 "What is the elephant sponge doing?", "The elephant sponge is expanding.", "female",
 "Key word in the answer. Woman's hands touch the sponge: boxes split at her hands. The man in the denim jacket appears from 1.7 s (at 0.2-1.2 a man in a white T-shirt walks there, maybe the same man without jacket - continuity glitch), so OFF before 1.7; he films only from about 2.2 s. From 1.7 the woman box starts right of the man, so her back foot is cut. The crate tilts / is pushed aside rather than fully falling off - verifier please check 'to knock off a wooden crate'. Yellow sponges also expand, so the answer subject is the elephant sponge.")
