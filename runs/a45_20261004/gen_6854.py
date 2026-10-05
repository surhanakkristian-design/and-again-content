from gen_6851_6852_6853_6854_lib import write
wom = [(0.24,0.19,0.43,0.81),(0.25,0.18,0.44,0.82),(0.24,0.18,0.49,0.82),(0.24,0.17,0.5,0.83),(0.21,0.16,0.54,0.84),(0.2,0.15,0.57,0.85),(0.18,0.15,0.6,0.85),(0.2,0.12,0.58,0.88)]
boat = [(0.68,0.3,0.28,0.23),(0.7,0.3,0.28,0.23),(0.74,0.3,0.25,0.24),(0.74,0.3,0.26,0.23),(0.75,0.3,0.25,0.23),(0.77,0.3,0.23,0.23),(0.78,0.3,0.22,0.24),(0.79,0.3,0.21,0.25)]
bh = [(0,0,0.42,0.19),(0,0,0.4,0.18),(0,0,0.43,0.18),(0,0,0.44,0.17),(0,0,0.45,0.16),(0,0,0.45,0.15),(0,0,0.46,0.15),(0,0,0.2,0.2)]
write(6854, "B", "band", "female",
 [("to admire the red band", "the woman in the middle", "female", wom),
  ("to rest on the jetty", "the rowing boat", "female", boat),
  ("to overlook the river", "the boathouse", "female", bh)],
 2.2,
 [("a boathouse", 0.2, 0.07, "female"), ("a rowing boat", 0.85, 0.4, "female"), ("a band", 0.5, 0.57, "female"), ("a coiled rope", 0.22, 0.9, "female")],
 "What is the smiling woman doing?", "She is admiring the red band.", "female",
 "The two teammates who tie the band are only arms/hands at the frame edges (0.2-1.2) and both tie, so no phrase for them. 'to admire the red band' is true from 1.7 (she looks down and smiles); at 0.2-1.2 the band is being tied. Boat box sits right of the woman's box (her stretched hand is cut at 1.2-3.7). Boathouse box is only the top band of the frame above the heads; at 3.7 only its left part (her head rises to y 0.12).")
