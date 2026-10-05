from gen_6993_6994_6995_6996_lib import build
T = [0.2, 0.7, 1.2, 1.7, 2.2, 2.7, 3.2, 3.7]
house = [(0.28,0.13,0.46,0.34),(0.28,0.13,0.46,0.34),(0.28,0.12,0.46,0.35),(0.27,0.12,0.47,0.74),
         (0.27,0.12,0.47,0.58),(0.27,0.12,0.47,0.54),(0.27,0.12,0.47,0.66),(0.27,0.12,0.47,0.74)]
wave = [(0.30,0.48,0.68,0.35),(0.38,0.48,0.60,0.36),(0.24,0.48,0.46,0.38),None,
        (0.66,0.70,0.34,0.19),(0.48,0.67,0.32,0.24),(0.40,0.79,0.30,0.14),None]
build(6996, "B", "covering", "female", T,
  [("to tower over the icy pier", "the lighthouse", "female", house),
   ("to crash against the lighthouse", "the wave", "female", wave),
   ("to burst into white spray", "the wave", "female", wave)],
  3.7,
  [("a lighthouse", 0.50, 0.52, "female"), ("a hut", 0.83, 0.66, "female"),
   ("icicles", 0.14, 0.82, "female"), ("a pier", 0.50, 0.93, "female")],
  "What is the wave doing?", "It is crashing against the lighthouse.", "female",
  "No people; two of three phrases on the wave. The wave sits in front of the lighthouse, so the boxes are split horizontally: lighthouse = lantern, gallery and upper tower while the wave covers the base (0.2-1.2, 2.2-3.2); full tower at 1.7 and 3.7 when the wave is off. 2.2-3.2 is a second, smaller splash at the base. Key word 'covering' (the coat of ice) is not used as a noun pill. Gulls left out (several, ambiguous).")
