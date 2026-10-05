from gen_7365_7367_7368_7370_lib import write
W = [[.19,.20,.62,.92],[.19,.21,.62,.92],[.19,.22,.62,.92],[.19,.21,.62,.92],[.19,.21,.62,.92],[.19,.21,.62,.92],[.19,.21,.63,.92],[.15,.19,.63,.92]]
M = [[0,.26,.19,.70]]*7 + [[0,.26,.15,.70]]
P = [[.62,.27,.80,.43]]*6 + [[.63,.27,.81,.43]]*2
write(7365, "B", "model", "female",
  [("to scrape clay off the car", "the woman", "female", W),
   ("to shape a lump of clay", "the man on the left", "male", M),
   ("to snap photos in the background", "the photographer", "male", P)],
  0.2,
  [("a clay model", .28, .74, "female"), ("a turntable", .40, .84, "female"), ("shavings", .70, .93, "female"), ("ceiling lights", .50, .17, "female")],
  "What is the woman doing?", "She is scraping clay off the car.", "female",
  "woman's box ends at x .62/.63 to stay clear of the photographer (her right hand and the tool reach ~.66); man's box narrowed at 3.7 where the woman steps left")
