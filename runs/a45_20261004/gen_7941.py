from gen_7939_7940_7941_7942_lib import build
T = {
 'the woman in red': [(0.49,0.16,0.31,0.60),(0.50,0.17,0.30,0.60),(0.50,0.16,0.30,0.62),(0.50,0.16,0.30,0.63),
                      (0.37,0.22,0.37,0.60),(0.23,0.38,0.37,0.60),(0.15,0.39,0.32,0.59),(0.08,0.39,0.34,0.59)],
 'the man': [(0.36,0.47,0.12,0.37),(0.37,0.47,0.12,0.38),(0.37,0.49,0.12,0.36),(0.37,0.49,0.12,0.36),
             None,(0.61,0.49,0.16,0.40),(0.48,0.44,0.28,0.48),(0.43,0.44,0.26,0.48)],
 'the woman in yellow': [(0.10,0.40,0.23,0.41),(0.00,0.43,0.36,0.48),(0.00,0.62,0.36,0.36),(0.00,0.80,0.18,0.18),None,None,None,None],
}
build(7941, 'B', 'plot', 'female', T,
 [('to balance a metal bucket', 'the woman in red', 'female'), ('to hold the chair steady', 'the man', 'male'), ('to hurry down the hallway', 'the woman in yellow', 'female')],
 3.7,
 [('a bucket', 0.76, 0.21, 'female'), ('a pendant lamp', 0.25, 0.25, 'female'), ('a wooden chair', 0.58, 0.83, 'female'), ('a doorknob', 0.86, 0.69, 'female')],
 'What is the woman in red balancing?', 'She is balancing a bucket on the door.', 'female',
 'The man is mostly hidden behind the woman in red: 0.2-1.7 s only his visible strip left of her legs is boxed (his hand on the chair back is inside her box), 2.2 s marked off (almost fully hidden behind her jump), 2.7 s only his arm/shoulder right of her. Woman in yellow leaves frame at the bottom left (1.2-1.7 s legs only), off from 2.2 s. Answer refers to 0.2-1.7 s; from 2.2 s the bucket already sits on the door.')
