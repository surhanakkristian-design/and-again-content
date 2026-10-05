from gen_7939_7940_7941_7942_lib import build
T = {
 'the woman': [(0.17,0.29,0.71,0.30),(0.39,0.45,0.39,0.16),(0.37,0.37,0.31,0.25),(0.35,0.28,0.26,0.26),(0.30,0.35,0.30,0.25),(0.33,0.45,0.34,0.17),(0.19,0.37,0.66,0.25),(0.19,0.32,0.77,0.26)],
 'the dog':   [(0.00,0.65,0.45,0.22),(0.08,0.57,0.30,0.32),(0.22,0.64,0.23,0.21),(0.23,0.65,0.20,0.22),(0.18,0.65,0.22,0.19),(0.06,0.64,0.26,0.19),(0.00,0.67,0.33,0.19),(0.00,0.67,0.37,0.21)],
 'the man':   [(0.48,0.60,0.44,0.31),(0.52,0.62,0.40,0.29),(0.53,0.63,0.44,0.28),(0.55,0.61,0.43,0.31),(0.56,0.61,0.42,0.30),(0.54,0.63,0.43,0.28),(0.52,0.63,0.45,0.28),(0.52,0.60,0.44,0.32)],
}
build(7939, 'A', 'pleasure', 'female', T,
 [('to swing under a tree', 'the woman', 'female'), ('to eat chocolate cake', 'the man', 'male'), ('to play in the grass', 'the dog', 'female')],
 1.7,
 [('the sky', 0.75, 0.22, 'female'), ('a tree', 0.22, 0.12, 'female'), ('a dog', 0.33, 0.76, 'female'), ('a blanket', 0.42, 0.89, 'female')],
 'What is the man eating?', 'He is eating chocolate cake.', 'male',
 'Woman and man overlap at 0.7/1.2/2.7 s: woman box cut above the man (her dress hem/feet partly outside). Dog "to play in the grass" = it jumps/runs around beside the blanket.')
