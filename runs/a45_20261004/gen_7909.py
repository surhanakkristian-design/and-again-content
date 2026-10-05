from gen_7905_7906_7908_7909_lib import write
din = [(.30,.39,.19,.22),(.27,.39,.22,.23),(.28,.39,.20,.22),(.28,.39,.19,.22),(.28,.39,.20,.22),(.27,.41,.20,.21),(.27,.47,.22,.16),(.27,.47,.22,.16)]
wai = [(.10,.48,.19,.16),(.08,.48,.19,.16),(.09,.48,.19,.16),(.08,.48,.19,.17),(.08,.48,.19,.16),(.07,.48,.19,.16),(.07,.48,.19,.16),(.07,.48,.19,.16)]
write(7909, "B", "mistake", "male",
 [("to waddle across the floor", "the man in the costume", "male", din),
  ("to crouch down awkwardly", "the man in the costume", "male", din),
  ("to carry a drinks tray", "the waiter", "male", wai)],
 0.2,
 [("a glass roof", .55, .08, "male"), ("a dinosaur costume", .40, .51, "male"),
  ("a string quartet", .82, .47, "male"), ("a silver dress", .79, .76, "male")],
 "What is the man in green doing?", "He is waddling across the floor.", "male",
 "Small far-away targets: dinosaur and waiter boxes are padded to the minimum size. Crouch happens at 3.2-3.7 s. Key word 'mistake' not used (would be interpretation). 'a string quartet' is a group label on the four musicians.")
