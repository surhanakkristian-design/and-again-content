from gen_7777_7778_7779_7780_lib import write
W = [(0,.12,.32,.88)]*3 + [(0,.10,.27,.90)] + [(0,.08,.27,.92)]*4
M = [(.34,.27,.56,.73),(.34,.27,.56,.73),(.34,.26,.56,.74),(.28,.23,.62,.77),(.28,.22,.62,.78),(.29,.21,.61,.79),(.29,.22,.61,.78),(.29,.21,.61,.79)]
L = [(.33,0,.25,.23)]*3 + [(.28,0,.30,.22),(.28,0,.30,.21),(.28,0,.30,.20),(.28,0,.30,.21),(.28,0,.30,.20)]
write(7777, "A", "choice", "female",
  [("to point at the doughnuts", "the woman", "female", W),
   ("to pick up a doughnut", "the man", "male", M),
   ("to hang from the ceiling", "the lamp", "female", L)],
  0.7, [("a lamp", .40, .12, "female"), ("a man", .78, .34, "male"), ("a woman", .14, .50, "female"), ("doughnuts", .60, .80, "female")],
  "What is the man holding?", "He is holding a pink doughnut.", "male",
  "Woman's pointing arm reaches into the man's box (split at x .28-.34, woman box = her body). At 3.7 her thumbs-up hand sits inside the man's box. Lamp box cut at x .33 for 0.2-1.2 to stay clear of the woman's head. Key word 'choice' not a visible noun.")
