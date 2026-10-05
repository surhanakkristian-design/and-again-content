from gen_6925_6926_6927_6928_lib import build
W = [(.27,.27,.78,1),(.25,.27,.86,1),(.22,.25,.79,1),(.19,.24,.77,1),(.01,.23,.76,1),(.10,.22,.79,1),(.02,.18,.71,1),(0,.13,.62,1)]
build(6927, "B", "cash machine", "female",
 [("to withdraw some cash", "the woman", "female", W),
  ("to turn towards the queue", "the woman", "female", W),
  ("to wear a sequinned coat", "the woman", "female", W)],
 2.2,
 [("a bobble hat", .42, .33, "female"), ("a sequinned coat", .22, .62, "female"), ("a cash machine", .84, .72, "female"), ("snow", .10, .90, "female")],
 "What is the woman doing?", "She is withdrawing money from a cash machine.", "female",
 "Only one clear target: the people queuing behind her are blurred and all do the same thing, so all three phrases go to the woman. Turn towards the queue: 3.2-3.7 s. 'A card' held up at 3.7 is unclear (looks like banknotes in a dark glove), not used.")
