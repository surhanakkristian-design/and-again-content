from lib_7055_7056_7057_7058 import build
doc = [(0.27,0.41,0.64,0.80),(0.28,0.42,0.62,0.82),(0.28,0.41,0.68,0.84),(0.30,0.42,0.67,0.84),
       (0.33,0.42,0.70,0.84),(0.30,0.41,0.70,0.82),(0.31,0.42,0.70,0.80),(0.40,0.41,0.70,0.80)]
nur = [(0.11,0.44,0.27,0.72),(0.10,0.43,0.28,0.72),(0.07,0.44,0.27,0.73),(0.03,0.44,0.27,0.75),
       (0.0,0.45,0.20,0.73),(0.0,0.44,0.18,0.72),(0.0,0.44,0.18,0.72),(0.0,0.44,0.18,0.72)]
crw = [(0.70,0.42,0.88,0.63),(0.70,0.41,0.88,0.62),(0.70,0.42,0.88,0.63),(0.70,0.41,0.88,0.62),
       (0.71,0.40,0.89,0.63),(0.71,0.39,0.92,0.63),(0.71,0.38,0.92,0.62),(0.71,0.36,0.95,0.62)]
build(7057, "B", "doc", "female",
  [("to carry a medical bag", "the doctor", "female", doc),
   ("to hurry after the doctor", "the nurse on the left", "female", nur),
   ("to crouch in the doorway", "the man in the helicopter", "male", crw)],
  3.7,
  [("a helicopter", 0.80, 0.27, "female"), ("a doc", 0.55, 0.52, "female"),
   ("a stretcher", 0.24, 0.62, "female"), ("a medical bag", 0.72, 0.67, "female")],
  "What is the doctor carrying?", "She is carrying a red medical bag.", "female",
  "Nurse and doctor are close at 0.7 s (split at x 0.28, nurse's folder and doctor's bag tip cut). From 2.7 s the man in the helicopter door reaches towards the doctor: split at x ~0.70-0.75, so the doctor's bag is cut a little at 3.2-3.7. Nurse holds a dark folder or laptop (unclear), so the phrase avoids naming it. A second person in blue scrubs and a man in a dark uniform push the stretcher in the back from 1.7 s, hence the nurse on the left.")
