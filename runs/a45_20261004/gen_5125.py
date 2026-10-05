import json
from gen_5122_5123_5124_5125_lib import build
times = json.load(open('frames/5125/packet.json'))['times']
M = {2.0:(.07,.25,.71,.75), 2.5:(.07,.25,.66,.75), 3.0:(.33,.28,.35,.43), 3.5:(.37,.3,.34,.38), 4.0:(.33,.31,.35,.31), 4.5:(.35,.29,.37,.33),
 5.0:(0,.58,.95,.18), 5.5:(0,.52,.8,.25), 6.0:(0,.54,.85,.18), 6.5:(0,.62,.8,.36), 7.0:(0,.63,.78,.35), 7.5:(0,.6,.68,.38),
 8.0:(0,.5,.68,.46), 8.5:(0,.5,.68,.46), 9.0:(0,.5,.66,.46)}
W = {2.0:(.79,.52,.21,.48), 2.5:(.74,.45,.26,.55), 3.0:(.68,.33,.26,.4), 3.5:(.71,.33,.25,.4), 4.0:(.68,.33,.24,.37), 4.5:(.72,.32,.26,.38),
 5.0:(.8,.38,.2,.2), 5.5:(.82,.3,.18,.4), 6.0:(.75,.24,.25,.3), 6.5:(.38,.32,.4,.3), 7.0:(.32,.14,.48,.49), 7.5:(.46,.12,.36,.48),
 8.0:(.47,.13,.33,.37), 8.5:(.48,.12,.33,.38), 9.0:(.47,.13,.33,.37)}
A = {0.0:(0,.6,1,.4), 0.5:(0,.6,1,.4), 1.0:(0,.6,1,.4), 1.5:(0,.6,1,.4), 6.5:(0,.17,1,.15), 7.0:(0,.3,.3,.25), 7.5:(0,.33,.45,.2),
 8.0:(0,.05,.46,.44), 8.5:(0,.05,.47,.44), 9.0:(0,.05,.46,.44)}
build(5125, "A", "stage", "male", [
  ("to fall off his chair", "the man with the moustache", "male", M),
  ("to lift a helmet high", "the woman", "female", W),
  ("to clap their hands", "the audience", "male", A)],
  8.5, [("a helmet", .62, .18, "male"), ("people", .25, .4, "male"), ("a man", .4, .62, "male"), ("a mattress", .8, .78, "male")],
  "What is the woman holding?", ["She", "is", "holding", "a", "helmet", "above", "her", "head."], "female",
  "0.0-1.5 s wide shot from the seats: the throne is still empty and the actors are tiny, so the man and the woman are OFF there; the audience box = the seated rows in front. The woman with the long hair at the right edge 2.0-6.0 s is taken to be the same actress who later lifts the helmet (same costume and hair) - verifier please check. Many splits: at 5.0-6.0 s and 7.0-9.0 s the man and the woman overlap in the picture, the boxes are split (woman above, man below). The audience is OFF 2.0-6.0 s (dark balconies, no clear faces) and only partly boxed 6.5-9.0 s where it does not meet the other boxes. 'chair' = the golden throne (A-level word). Key word 'stage' is a verb here, not placed.",
  times)
