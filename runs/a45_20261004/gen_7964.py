from gen_7963_7964_7965_7967_lib import build
dog = [(0.46,0.31,0.90,0.71),(0.53,0.30,0.90,0.71),(0.48,0.29,0.90,0.72),(0.37,0.25,0.92,0.72),
       (0.38,0.29,0.97,0.72),(0.35,0.29,0.94,0.72),(0.36,0.24,0.99,0.74),(0.35,0.24,0.97,0.74)]
cro = [(0.22,0.43,0.45,0.57),(0.28,0.53,0.52,0.69),(0.14,0.66,0.47,1.0),None,None,None,None,None]
build(7964, "B", "rest", "female",
  [("to tilt a wooden paddle", "the dog", "female", dog),
   ("to tumble off the paddle", "the croissants", "female", cro),
   ("to grin at the camera", "the dog", "female", dog)],
  3.2,
  [("a wicker basket", 0.75, 0.25, "female"), ("a paddle", 0.25, 0.43, "female"),
   ("an apron", 0.72, 0.62, "female"), ("a baking tray", 0.35, 0.84, "female")],
  "What is the dog holding?", "The dog is holding a wooden paddle.", "female",
  "The croissants are only visible 0.2-1.2 s (on the peel, then falling; at 1.2 one over a tray and two falling at the bottom edge), off afterwards. 'paddle' used for the baker's peel. Grin only from ~2.7 s. Key word 'rest' (noun) is not a placeable noun.")
