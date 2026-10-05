from gen_7747_7749_7750_7752_lib import write
W = [(0.0,0.38,0.54,0.77),(0.0,0.43,0.48,0.80),(0.0,0.44,0.43,0.78),(0.0,0.45,0.43,0.79),
     (0.0,0.37,0.44,0.80),(0.0,0.29,0.50,0.76),(0.0,0.04,0.56,0.78),(0.0,0.0,0.63,0.78)]
S = [(0.55,0.38,0.73,0.60),(0.55,0.39,0.73,0.60),(0.56,0.37,0.74,0.58),(0.56,0.37,0.74,0.58),
     (0.59,0.34,0.77,0.55),(0.61,0.31,0.80,0.51),(0.59,0.22,0.82,0.46),(0.64,0.16,0.86,0.40)]
write(7750, "A", "as soon as possible", "female", [
  ("to throw an old tyre", "the woman", "female", W),
  ("to hold up a sign", "the man with the sign", "male", S),
  ("to put on a wheel", "the woman", "female", W)],
  2.2, [("the sky", 0.50, 0.08, "female"), ("a woman", 0.17, 0.50, "female"), ("a wheel", 0.38, 0.62, "female"), ("a car", 0.76, 0.52, "female")],
  "What is the woman in front doing?", "She is putting a new wheel on the car.", "female",
  "Sign man is small and in the background (box widened to the minimum, it also covers the crew member next to him at 0.2-1.7 s); he only raises the sign high at 3.2-3.7 s, before that he holds it at chest height. 'to throw an old tyre' shows at 0.2-0.7 s only. Crouching crew member at the right works the jack, not a wheel. Second woman in the background, so the question says 'in front'.")
