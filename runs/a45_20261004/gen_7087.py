from gen_7085_7086_7087_7089_lib import write
woman = [(.42,.28,.47,.50),(.46,.28,.44,.50),(.44,.29,.29,.53),(.45,.29,.36,.53),(.43,.28,.35,.54),(.45,.28,.31,.57),(.41,.26,.40,.60),(.43,.26,.36,.61)]
dog = [(.24,.37,.18,.16),(.28,.38,.18,.15),(.26,.40,.18,.15),(.27,.40,.18,.15),(.25,.40,.18,.15),(.27,.40,.18,.15),(.23,.41,.18,.15),(.25,.41,.18,.15)]
cat = [(.32,.09,.18,.14),(.31,.10,.18,.14),(.30,.10,.18,.14),(.29,.10,.18,.14),(.26,.08,.18,.14),(.25,.09,.18,.14),(.23,.09,.18,.14),(.23,.09,.18,.14)]
write(7087, "B", "escort", "female",
 [("to carry a bundle of letters", "the woman", "female", woman),
  ("to trot behind the geese", "the dog", "female", dog),
  ("to perch on the stone wall", "the cat", "female", cat)],
 2.2,
 [("a quad bike", .85, .19, "female"), ("a cat", .36, .15, "female"), ("a collie", .37, .47, "female"), ("a goose", .56, .82, "female")],
 "What are the geese doing?", "The geese are escorting the woman.", "female",
 "Key word 'escort' used in the answer (geese walk closely around her). Woman box is cut on the left where the dog walks right behind her (split along the line), geese overlap her legs. Cat is small on the wall top-left, min-size box. Two laughing farm workers not used (same action for both). 'a goose' pill on the front goose; other geese elsewhere, no other bird noun.")
