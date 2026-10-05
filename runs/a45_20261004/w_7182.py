from w_7176_7177_7178_7182_lib import write
man  = [(.19,.22,.76,.74),(.19,.22,.76,.74),(.18,.22,.63,.74),(.18,.27,.51,.74),(.19,.29,.51,.75),(.22,.29,.51,.76),(.23,.28,.53,.75),(.25,.28,.55,.75)]
cook = [(.77,.40,1.0,.82),(.77,.37,1.0,.82),(.77,.48,1.0,.82),(.82,.52,1.0,.78),(.82,.54,1.0,.76),None,None,None]
wom  = [(0,.29,.18,.62),(0,.29,.18,.62),(0,.33,.17,.62),(0,.33,.17,.62),(0,.30,.18,.62),(0,.30,.21,.62),(0,.30,.22,.62),(0,.30,.22,.62)]
write(7182, "A", "go out for dinner", "male",
 [("to carry the hot food", "the man at the front", "male", man),
  ("to sit in a boat", "the cook", "male", cook),
  ("to hold her hands together", "the woman on the left", "female", wom)],
 3.7,
 [("the sky", .70, .07, "male"), ("houses", .22, .17, "male"), ("a table", .24, .63, "male"), ("water", .72, .86, "male")],
 "What is the young man carrying?", "He is carrying dinner to the table.", "male",
 "defaultVoice male (main person is the young man). Cook only visible 0.2-2.2 (then only a white sliver at the right edge -> off). At 0.2-0.7 the man's arm reaches the dome right above the cook's hand; boxes split at x .76/.77. Woman on the left is cut by the frame edge; she holds her hands together under her chin in every frame. 'carry' fits only the man; the cook holds a second plate up at 1.2 but does not carry it.")
