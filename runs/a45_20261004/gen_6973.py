from gen_6971_6972_6973_6975_lib import write
M = [(0.57,0.22,0.33,0.60),(0.60,0.21,0.32,0.63),(0.60,0.21,0.32,0.66),(0.58,0.20,0.35,0.69),
     (0.53,0.20,0.40,0.78),(0.54,0.19,0.46,0.81),(0.50,0.17,0.49,0.83),(0.46,0.17,0.48,0.83)]
C = [(0.27,0.37,0.27,0.21),(0.25,0.37,0.30,0.21),(0.28,0.37,0.26,0.23),(0.24,0.37,0.31,0.25),
     (0.20,0.53,0.32,0.20),(0.27,0.63,0.26,0.25),(0.17,0.69,0.33,0.25),(0.17,0.76,0.29,0.24)]
write(6973, "B", "comedian", "male",
  [("to keep a straight face", "the man on stage", "male", M),
   ("to stand next to a microphone", "the man on stage", "male", M),
   ("to topple over backwards", "the chair", "male", C)],
  1.7,
  [("a spotlight", 0.80, 0.13, "male"), ("a microphone", 0.55, 0.35, "male"),
   ("a chair", 0.40, 0.48, "male"), ("a comedian", 0.80, 0.56, "male")],
  "What is the man on stage doing?", "The comedian is keeping a straight face.", "male",
  "The chair tips over in mid-air (0.2-2.2, blurred at 2.2) and lies upside down on the floor from 2.7; at 3.2-3.7 it sits behind the comedian's legs, so the chair box is cut at the split line (right part of the chair outside its box at 3.7). Audience laughs, so no laughing phrase. 'a comedian' pill sits on the man (no 'a man' noun).")
