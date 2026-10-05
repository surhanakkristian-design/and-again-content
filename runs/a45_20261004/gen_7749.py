from gen_7747_7749_7750_7752_lib import write
S = [0.47, 0.50, 0.51, 0.51, 0.52, 0.55, 0.54, 0.51]   # split line man | woman
MT = [0.10, 0.12, 0.11, 0.10, 0.20, 0.30, 0.20, 0.26]  # man's left edge (arm)
WR = [0.85, 0.89, 0.90, 0.93, 0.93, 0.94, 0.90, 0.89]
WT = [0.33, 0.33, 0.34, 0.40, 0.39, 0.37, 0.34, 0.34]
M = [(MT[i], 0.21, S[i], 0.63) for i in range(8)]
W = [(S[i], WT[i], WR[i], 0.91) for i in range(8)]
write(7749, "B", "artistic", "female", [
  ("to fling paint at the canvas", "the woman with the tin", "female", W),
  ("to stand on a stepladder", "the man", "male", M),
  ("to throw her head back", "the woman with the tin", "female", W)],
  3.2, [("a canvas", 0.15, 0.55, "female"), ("a stepladder", 0.45, 0.71, "female"), ("a paint tin", 0.70, 0.58, "female"), ("a lamp", 0.58, 0.24, "female")],
  "What is the woman in front doing?", "She is flinging paint at the canvas.", "female",
  "Man (on the stepladder) and the woman with the tin overlap in x around 0.47-0.55; boxes split vertically at the gap (cuts the woman's left boot / the man's hand by a few %). Flinging happens at 0.2-0.7 s, head thrown back at 1.7-2.2 s. Two women in the background, so the target is 'the woman with the tin'.")
