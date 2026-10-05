from gen_7758_7759_7760_7762_lib import write
gw = [(0.16,0.28,0.33,0.43),(0.26,0.28,0.25,0.48),(0.28,0.26,0.22,0.55),(0.24,0.26,0.26,0.60),
      (0.25,0.24,0.26,0.65),(0.24,0.23,0.27,0.66),(0.23,0.24,0.27,0.64),(0.23,0.24,0.27,0.64)]
bw = [(0.50,0.35,0.20,0.25),(0.52,0.36,0.20,0.22),(0.51,0.35,0.20,0.25),(0.51,0.35,0.20,0.23),
      (0.51,0.34,0.20,0.26),(0.51,0.34,0.21,0.26),(0.51,0.33,0.19,0.28),(0.51,0.32,0.19,0.29)]
cat = [None,None,None,(0.55,0.59,0.18,0.14),(0.62,0.61,0.18,0.15),(0.63,0.61,0.19,0.17),(0.60,0.63,0.20,0.20),(0.52,0.65,0.22,0.20)]
write(7760, "B", "beautifully", "female",
 [("to take a mirror selfie", "the woman in green", "female", gw),
  ("to take off her heels", "the woman in black", "female", bw),
  ("to tread on the train", "the cat", "female", cat)],
 2.7,
 [("a luggage trolley", 0.20, 0.45, "female"), ("a satin gown", 0.38, 0.60, "female"),
  ("a white cat", 0.74, 0.71, "female"), ("a marble floor", 0.35, 0.92, "female")],
 "What is the woman in green doing?", "She is taking a mirror selfie.", "female",
 "woman in black: holds one shoe and reaches for the raised foot - read as taking off her heels, check; green gown train runs under the woman in black/cat so her box covers only her body; cat enters at 1.7")
