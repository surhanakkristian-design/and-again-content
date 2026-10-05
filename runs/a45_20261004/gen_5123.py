import json
from gen_5122_5123_5124_5125_lib import build
times = json.load(open('frames/5123/packet.json'))['times']
man = {3.0:(0,.03,.34,.95), 3.5:(0,.2,.88,.8), 4.0:(0,.11,.74,.84), 4.5:(.07,0,.93,1), 5.0:(.24,.25,.56,.68), 5.5:(.35,.23,.3,.52),
 6.0:(.33,.16,.38,.36), 6.5:(.36,.15,.39,.32), 7.0:(.31,.14,.38,.35), 7.5:(.3,.12,.4,.36), 8.0:(.31,.11,.38,.38), 8.5:(.31,.12,.38,.4),
 9.0:(.3,.12,.4,.42), 9.5:(.29,.11,.4,.45), 10.0:(.28,.1,.42,.47), 10.5:(.28,.09,.42,.49), 11.0:(.27,.1,.43,.52), 11.5:(.26,.1,.44,.53), 12.0:(.26,.1,.44,.54)}
cup = {0.0:(.36,.37,.34,.24), 0.5:(.34,.37,.34,.24), 1.0:(.34,.37,.34,.24), 1.5:(.35,.36,.34,.24), 2.0:(.35,.34,.33,.24), 2.5:(.3,.33,.18,.14), 3.0:(.34,.34,.18,.14)}
build(5123, "B", "flood", "male", [
  ("to overflow with coffee", "the cup", "male", cup),
  ("to rush into the bathroom", "the man", "male", man),
  ("to clutch his head", "the man", "male", man)],
  8.5, [("a shower curtain", .13, .42, "male"), ("a hoodie", .5, .27, "male"), ("foam", .65, .54, "male"), ("a bathtub", .2, .7, "male")],
  "What is the man doing?", ["He", "is", "clutching", "his", "head", "with", "both", "hands."], "male",
  "Targets: the overflowing coffee cup (0-2 s close-up; at 2.5-3.0 s the same cup is a tiny speck under the machine in the background, given a minimum-size box; at 3.0 s it sits right by the man's hand, so the boxes are split at x 0.34) and the man (3.0 s on). 'to rush into the bathroom' = 5.0-6.5 s through the hallway door into the bathroom; 'to clutch his head' = 7.5-10.0 s hands in his hair. The sink and bathtub also overflow, so 'overflow' is tied to coffee, which only the cup does. Key word 'flood' is a verb, not placed.",
  times)
