from gen_7026_7027_7028_7029_lib import write
W = [(.24,.31,.38,.53),(.22,.32,.45,.51),(.22,.30,.29,.64),(.13,.26,.36,.64),(.12,.23,.35,.58),(.09,.21,.35,.59),(.08,.19,.36,.61),(.07,.18,.36,.62)]
C = [(.68,.82,.24,.15),(.70,.82,.20,.15),(.70,.86,.20,.14),(.68,.81,.20,.19),(.71,.80,.26,.15),(.70,.80,.29,.15),(.70,.86,.20,.14),(.68,.85,.20,.15)]
write(7027, "B", "defender", "female",
 [("to swing a paper parasol", "the waitress", "female", W),
  ("to stand on a wicker chair", "the waitress", "female", W),
  ("to take shelter under the table", "the cat", "female", C)],
 2.7,
 [("a waitress", .26, .36, "female"), ("a parasol", .62, .45, "female"), ("a glass dome", .66, .61, "female"), ("a cat", .84, .84, "female")],
 "What is the waitress doing?", "She is defending the table with a parasol.", "female",
 "Key word 'defender' labelled as 'a waitress' (role noun not a visible thing). Avoided monkeys (several) and the tourist (a second photographer behind). Parasol is swung only at 0.2-1.2, then held out.")
