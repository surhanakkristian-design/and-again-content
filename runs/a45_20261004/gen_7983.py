from gen_7982_7983_7984_7985_lib import write
M = [(0.17,0.29,0.43,0.33),(0.20,0.31,0.32,0.30),(0.13,0.29,0.40,0.34),(0.13,0.28,0.48,0.35),
     (0.20,0.27,0.30,0.37),(0.12,0.25,0.50,0.40),(0.09,0.24,0.56,0.40),(0.13,0.23,0.53,0.41)]
D = [(0.61,0.48,0.39,0.51),(0.53,0.46,0.47,0.54),(0.53,0.46,0.47,0.54),(0.62,0.45,0.38,0.55),
     (0.51,0.43,0.49,0.57),(0.62,0.43,0.38,0.57),(0.65,0.42,0.35,0.58),(0.66,0.42,0.34,0.58)]
write(7983, "B", "sick leave", "male",
  [("to blow his nose", "the man", "male", M),
   ("to sit up in bed", "the man", "male", M),
   ("to deliver a tray", "the dog", "male", D)],
  3.7,
  [("a houseplant", 0.55, 0.17, "male"), ("a tray", 0.50, 0.52, "male"),
   ("a golden retriever", 0.82, 0.68, "male"), ("clogs", 0.32, 0.92, "male")],
  "What is the dog doing?", "The dog is delivering a tray of soup.", "male",
  "Only two targets (man, dog). Tray is held by both at 1.7-3.7; boxes split at the tray, so the dog's front paws fall partly in the man's box at 0.7-2.7. 'to blow his nose' visible 0.2-1.2 only (tissue). Key word 'sick leave' not a visible noun.")
