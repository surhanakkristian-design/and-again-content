from gen_7982_7983_7984_7985_lib import write
W = [(0.15,0.24,0.29,0.33),(0.18,0.25,0.30,0.37),(0.33,0.48,0.20,0.20),None,
     None,(0.35,0.53,0.20,0.15),(0.32,0.42,0.20,0.21),(0.28,0.45,0.25,0.20)]
L = [(0.78,0.37,0.22,0.14),(0.72,0.33,0.22,0.17),(0.60,0.13,0.21,0.15),(0.58,0.13,0.23,0.16),
     (0.54,0.10,0.24,0.16),(0.53,0.09,0.24,0.17),(0.51,0.09,0.26,0.16),(0.51,0.09,0.25,0.16)]
T = [(0.66,0.51,0.18,0.16),None,(0.42,0.26,0.18,0.17),(0.34,0.23,0.19,0.18),
     (0.27,0.22,0.18,0.18),(0.16,0.20,0.18,0.18),(0.12,0.22,0.18,0.17),None]
write(7984, "B", "simultaneously", "female",
  [("to wear a blue bikini", "the woman in blue", "female", W),
   ("to point across the pool", "the lifeguard", "male", L),
   ("to towel his hair dry", "the man with a towel", "male", T)],
  3.2,
  [("a lifeguard", 0.64, 0.16, "male"), ("a diving board", 0.17, 0.38, "female"),
   ("a bikini", 0.42, 0.57, "female"), ("a swimming pool", 0.55, 0.82, "female")],
  "What are the woman and man doing?", "They are leaping into the swimming pool.", "female",
  "The jumping couple do everything together, so no action fits only one of them: the woman gets a state phrase (blue bikini; the other woman on the deck wears lilac). Woman off at 1.7-2.2 (hidden in the splash). Towel man is small: hidden behind the jumper at 0.7, overlaps the lilac-bikini woman at 3.2, hidden behind her at 3.7. Lifeguard points from 1.2 on, at 0.2-0.7 he blows his whistle. Answer: 'leaping into the pool' - the clip shows the jump only in the first ~1 s, then they surface laughing.")
