from gen_7085_7086_7087_7089_lib import write
woman = [(.30,.28,.41,.70),(.34,.24,.37,.75),(.30,.28,.43,.70),(.29,.32,.46,.67),(.36,.33,.37,.66),(.35,.33,.40,.66),(.37,.32,.37,.67),(.38,.33,.39,.66)]
crowd = [(0,.35,.29,.25),(0,.36,.33,.23),(0,.36,.29,.24),(0,.36,.28,.26),(0,.35,.35,.25),(0,.35,.34,.25),(0,.35,.36,.25),(0,.35,.37,.26)]
pan = [(.72,.43,.27,.15),(.72,.43,.27,.15),(.74,.44,.25,.15),(.76,.44,.23,.15),(.74,.43,.25,.15),(.76,.44,.23,.15),(.75,.46,.24,.15),(.78,.46,.22,.15)]
write(7085, "B", "entrepreneur", "female",
 [("to raise the roller shutter", "the woman", "female", woman),
  ("to queue in the rain", "the people outside", "female", crowd),
  ("to give off steam", "the frying pan", "female", pan)],
 0.7,
 [("a roller shutter", .22, .12, "female"), ("an entrepreneur", .58, .62, "female"), ("a stepladder", .14, .80, "female"), ("a bar stool", .80, .74, "female")],
 "What is the woman doing?", "She is raising the roller shutter.", "female",
 "Woman raises the shutter only 0.2-1.2 s, then turns and waves; phrase still fits only her. 'the people outside' = the queue on the wet pavement, box split from the woman's raised arm. Steam rises from the pan on the stove (steam could also come from the pot behind). 'an entrepreneur' pill on the woman's apron (key word, implied by her opening the cafe).")
