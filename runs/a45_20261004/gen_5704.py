from gen_5702_5703_5704_5705_lib import write
W = [(0.2,0.28,0.36,0.48,0.48),(0.7,0.30,0.33,0.49,0.53),(1.2,0.29,0.32,0.49,0.58),(1.7,0.29,0.32,0.50,0.60),
     (2.2,0.28,0.33,0.50,0.62),(2.7,0.29,0.32,0.49,0.64),(3.2,0.30,0.34,0.48,0.64),(3.7,0.28,0.35,0.50,0.63)]
R = [(0.2,0.77,0.55,0.18,0.22),(0.7,0.79,0.57,0.18,0.22),(1.2,0.78,0.60,0.19,0.22),(1.7,0.79,0.63,0.19,0.21),
     (2.2,0.78,0.64,0.19,0.22),(2.7,0.78,0.65,0.20,0.22),(3.2,0.78,0.67,0.20,0.22),(3.7,0.78,0.67,0.20,0.22)]
write(5704, "B", "capable", "female",
  [("to hold up a steel beam", "the superhero", "female", W),
   ("to grab the crane cable", "the worker on the right", "male", R),
   ("to rise from a crouch", "the superhero", "female", W)],
  2.7,
  [("a steel beam", 0.40, 0.15, "female"), ("a crane hook", 0.78, 0.40, "female"), ("a cape", 0.74, 0.60, "female"), ("skyscrapers", 0.20, 0.60, "female")],
  "What is the superhero doing?", "She is lifting a huge steel beam.", "female",
  "Cape flies over the right worker at 0.7/1.7/2.2+; superhero box cut at x~0.78 so the boxes do not overlap. Right worker reaches up to the crane cable; check he really holds it.")
