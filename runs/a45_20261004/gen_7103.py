from gen_7103_7104_7105_7106_lib import write
man = [[.57,.27,.17,.15],[.59,.27,.18,.15],[.57,.29,.19,.12],[.57,.27,.21,.15],[.60,.26,.20,.16],[.60,.25,.17,.12],[.58,.25,.22,.17],[.58,.25,.23,.18]]
dog = [[.18,.43,.35,.50],[.20,.42,.33,.52],[.14,.39,.38,.58],[.05,.38,.49,.59],[.01,.40,.51,.58],[.00,.40,.50,.58],[.13,.42,.43,.58],[.08,.48,.44,.52]]
pink = [[.53,.43,.28,.47],[.53,.43,.29,.46],[.52,.42,.34,.54],[.54,.43,.34,.55],[.53,.44,.41,.54],[.56,.45,.43,.53],[.57,.48,.43,.50],[.60,.48,.40,.52]]
write(7103, "A", "favorite", "female",
  [("to hold a cake", "the older man", "male", man),
   ("to stand on its back legs", "the big dog", "female", dog),
   ("to wear a pink shirt", "the woman in pink", "female", pink)],
  0.2,
  [("a lamp", .12, .25, "female"), ("a cake", .66, .40, "female"), ("a table", .15, .56, "female"), ("a dog", .35, .72, "female")],
  "What is the big dog doing?", "It is standing on its back legs.", "female",
  "Phrase 3 is a state: hugging is shared with the young man, laughing with everyone. 'a dog' pill is on the big dog; the small dog is not labelled.")
