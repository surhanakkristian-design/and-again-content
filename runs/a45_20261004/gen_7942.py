from gen_7939_7940_7941_7942_lib import build
T = {
 'the man': [(0.09,0.15,0.43,0.80),(0.08,0.16,0.43,0.81),(0.07,0.16,0.46,0.81),(0.07,0.16,0.46,0.81),
             (0.06,0.14,0.44,0.84),(0.08,0.14,0.43,0.84),(0.09,0.14,0.42,0.84),(0.08,0.14,0.43,0.84)],
 'the woman': [(0.53,0.28,0.40,0.57),(0.52,0.25,0.41,0.65),(0.54,0.36,0.33,0.50),(0.54,0.38,0.33,0.34),
               (0.51,0.37,0.34,0.39),(0.52,0.37,0.34,0.41),(0.52,0.37,0.35,0.39),(0.52,0.37,0.33,0.41)],
}
build(7942, 'B', 'point of view', 'male', T,
 [('to hold a pet snake', 'the man', 'male'), ('to scream in horror', 'the woman', 'female'), ('to perch on the armrest', 'the woman', 'female')],
 2.2,
 [('a snake', 0.56, 0.36, 'male'), ('a hanging plant', 0.72, 0.17, 'male'), ('a cushion', 0.45, 0.92, 'male'), ('a rug', 0.82, 0.84, 'male')],
 'What is the man holding?', 'He is holding a pet snake.', 'male',
 'The snake lies on the man, so it is not a separate tap target; man and woman split along x ~0.51-0.53 (the snake head and his hand reach into her box). The woman only stands at 0.2-0.7 s and perches on the sofa arm from 1.2 s.')
