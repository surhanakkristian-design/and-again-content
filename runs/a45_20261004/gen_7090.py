import sys; sys.path.insert(0,'.')
from gen_7090_7091_7092_7093_lib import write
W=[(0.10,0.35,0.73,0.50),(0.09,0.34,0.75,0.52),(0.08,0.34,0.75,0.54),(0.06,0.34,0.80,0.54),
   (0.03,0.32,0.77,0.58),(0.02,0.31,0.81,0.61),(0.01,0.29,0.80,0.62),(0.01,0.30,0.90,0.63)]
write(7090,"B","experience","female",
 [("to spread her arms wide","the woman","female",W),
  ("to stand barefoot on a rock","the woman","female",W),
  ("to shield her eyes","the woman","female",W)],
 0.2,
 [("a waterfall",0.55,0.15,"female"),("a swimsuit",0.53,0.54,"female"),("moss",0.80,0.70,"female"),("a rock",0.45,0.90,"female")],
 "What is the woman doing?","She is spreading her arms wide.","female",
 "single person clip, all three phrases on the woman; shield-her-eyes (hand over eyes) only around 2.7 s")
