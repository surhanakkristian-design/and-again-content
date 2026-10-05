from gen_6971_6972_6973_6975_lib import write
W = [(0.03,0.36,0.50,0.55),(0.0,0.38,0.56,0.52),(0.0,0.42,0.54,0.50),(0.04,0.41,0.52,0.52),
     (0.02,0.43,0.53,0.54),(0.02,0.46,0.48,0.54),(0.0,0.48,0.44,0.52),(0.02,0.50,0.42,0.50)]
N = [(0.62,0.10,0.38,0.55),(0.62,0.08,0.38,0.56),(0.68,0.05,0.32,0.58),(0.68,0.02,0.32,0.56),
     (0.62,0.0,0.38,0.48),(0.56,0.0,0.42,0.45),(0.50,0.0,0.38,0.47),(0.51,0.0,0.40,0.49)]
write(6971, "B", "come up", "female",
  [("to lean against a rope winch", "the woman", "female", W),
   ("to gaze up in amazement", "the woman", "female", W),
   ("to dangle from a crane", "the net", "female", N)],
  2.2,
  [("a net", 0.80, 0.28, "female"), ("a wheelhouse", 0.36, 0.46, "female"),
   ("fish", 0.66, 0.84, "female"), ("the sea", 0.82, 0.53, "female")],
  "What is the woman leaning against?", "She is leaning against a rope winch.", "female",
  "Net early (0.2-1.7) is still pouring fish over the side; box covers net + pouring column on the right. Crew men also cheer, so cheering phrases avoided; only the woman looks up.")
