from gen_7939_7940_7941_7942_lib import build
T = {
 'the delivery man': [(0.11,0.08,0.74,0.92),(0.11,0.05,0.75,0.95),(0.11,0.02,0.77,0.98),(0.10,0.02,0.81,0.98),
                      (0.00,0.18,0.34,0.56),(0.00,0.18,0.37,0.56),(0.00,0.18,0.35,0.54),(0.00,0.18,0.36,0.53)],
 'the woman in yellow': [(0.86,0.56,0.14,0.44),(0.87,0.56,0.13,0.44),(0.89,0.56,0.11,0.44),(0.92,0.62,0.08,0.38),
                      (0.35,0.39,0.25,0.32),(0.38,0.37,0.22,0.34),(0.36,0.36,0.24,0.36),(0.37,0.36,0.23,0.36)],
 'the dog': [None,None,None,None,(0.00,0.75,0.44,0.17),(0.00,0.75,0.42,0.18),(0.00,0.73,0.49,0.21),(0.00,0.73,0.54,0.21)],
}
build(7940, 'B', 'plenty', 'male', T,
 [('to balance a tall stack', 'the delivery man', 'male'), ('to clutch her forehead', 'the woman in yellow', 'female'), ('to wolf down a pizza', 'the dog', 'male')],
 2.2,
 [('a helmet', 0.10, 0.37, 'male'), ('a houseplant', 0.77, 0.47, 'male'), ('a coffee table', 0.62, 0.80, 'male'), ('a golden retriever', 0.16, 0.82, 'male')],
 'What is the dog doing?', 'It is wolfing down a whole pizza.', 'male',
 'Delivery man box includes the pizza stack he holds; in the wide shot the stack top (x>0.35) is cut to stay clear of the woman in yellow. Woman in yellow only partly visible at the right edge 0.2-1.7 s (hand on head only from 2.2 s). Friends on the sofa eat slices, the dog eats a whole pizza from a box on the floor (3.2-3.7 s). defaultVoice male = delivery man as main person.')
