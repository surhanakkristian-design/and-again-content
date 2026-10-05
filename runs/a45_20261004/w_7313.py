from w_7310_7311_7312_7313_lib import build
older = [(0,.16,.56,.84),(0,.16,.45,.84),(0,.15,.26,.85),(0,.15,.25,.85),(0,.16,.22,.84),(0,.16,.37,.84),(0,.19,.33,.81),(0,.19,.22,.81)]
young = [(.56,.17,.42,.74),(.47,.15,.46,.73),(.50,.16,.47,.67),(.43,.17,.53,.66),(.43,.19,.44,.58),(.48,.20,.33,.53),(.34,.22,.38,.50),(.22,.22,.34,.46)]
build(7313, "B", "maiden", "female",
  [("to place a daisy crown", "the older woman", "female", older),
   ("to lean on the wooden table", "the young woman", "female", young),
   ("to stroll away from the table", "the young woman", "female", young)],
  1.2,
  [("a flower crown", .73, .25, "female"), ("a maiden", .76, .47, "female"), ("a violin case", .33, .52, "female"), ("wildflowers", .35, .76, "female")],
  "What is the young woman wearing?", "She is wearing a crown of wildflowers.", "female",
  "Older woman places the crown only at 0.2-0.7 (her hands reach the crown, box split at x .56 / .47 there); later she sorts flowers at the left edge. The seated girls on the right also hold flower crowns, so no phrase for them; they lie inside the young woman's box at 0.2-2.2 (not a target). 'a maiden' placed on the young woman in navy (key word).")
