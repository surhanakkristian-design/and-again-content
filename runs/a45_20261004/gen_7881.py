from gen_7878_7879_7881_7882_lib import write
T = [(.42,.50,.40,.22),(.47,.50,.45,.19),(.43,.49,.46,.19),(.47,.49,.44,.19),(.45,.49,.45,.18),(.43,.47,.47,.18),(.46,.49,.40,.17),(.45,.47,.40,.17)]
C = [(.06,.64,.34,.14),(.07,.66,.34,.14),(.00,.68,.28,.14),(.00,.72,.20,.14),None,None,None,None]
write(7881, "B", "instinct", "male",
 [("to crawl towards the sea", "the turtle", "male", T),
  ("to flick up sand", "the turtle", "male", T),
  ("to scuttle across the sand", "the crab", "male", C)],
 0.2,
 [("palm trees", .30, .15, "male"), ("eggshells", .15, .45, "male"), ("a baby turtle", .64, .58, "male"), ("a crab", .22, .71, "male")],
 "What is the baby turtle doing?", "It is crawling towards the sea.", "male",
 "Only two living targets (turtle, crab), so the turtle carries two phrases. The crab is blurry and leaves the frame at the bottom left after 1.7 (off from 2.2). 'to flick up sand': small sprays of sand are visible behind its flippers at 0.7-2.7; check it reads clearly. Eggshells are small (left, next to the coconut husk at the nest).")
