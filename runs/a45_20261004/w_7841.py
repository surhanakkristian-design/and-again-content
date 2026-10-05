from w_7841_7842_7843_7846_lib import write
W = [(.38,.19,.62,.38),(.42,.21,.58,.36),(.42,.24,.58,.33),(.43,.24,.57,.33),(.40,.25,.60,.32),(.40,.26,.60,.31),(.39,.25,.61,.32),(.37,.21,.63,.36)]
M = [(0,.58,1,.42)]*8
write(7841, "B", "forwards", "female",
 [("to stretch her arms forwards", "the woman", "female", W),
  ("to grin at the camera", "the woman", "female", W),
  ("to grip the safety bar", "the man in green", "male", M)],
 2.7,
 [("the sky", .50, .08, "female"), ("a Ferris wheel", .40, .26, "female"), ("a baseball cap", .80, .34, "female"), ("a safety bar", .32, .67, "female")],
 "What is the woman doing?", "She is stretching her arms forwards.", "female",
 "Man behind her shown only by arms/green T-shirt (hairy arms, read as male). Woman box cut at y .57 so it does not overlap the man's hands/arms; her shorts/legs below are inside the man's box. 'to grin at the camera' fits mainly the last frames (3.7) when she turns to the lens.")
