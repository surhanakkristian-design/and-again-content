import json
from gen_5122_5123_5124_5125_lib import build
times = json.load(open('frames/5122/packet.json'))['times']
climber = {0.0: (.27,.25,.45,.6), 0.5: (.28,.19,.42,.63), 1.0: (.33,.2,.52,.76), 1.5: (.17,.2,.64,.8), 2.0: (.04,.25,.76,.75)}
lifter = {2.5: (.15,.3,.7,.62), 3.0: (.12,.25,.76,.72)}
runner = {3.5: (.28,.38,.33,.37), 4.0: (.23,.29,.48,.51)}
build(5122, "A", "achieve", "female", [
  ("to climb a wall", "the climber", "female", climber),
  ("to lift heavy weights", "the man with the bar", "male", lifter),
  ("to cross the finish line", "the runner", "female", runner)],
  4.0, [("the sky", .25, .24, "female"), ("trees", .75, .32, "female"), ("a runner", .45, .47, "female"), ("a track", .3, .76, "female")],
  "What is the man lifting?", ["He", "is", "lifting", "heavy", "weights."], "male",
  "Montage of separate shots; each target is visible only in its own shot and OFF elsewhere. The climber is boxed again at 1.5-2.0 s where the same woman cheers on the ground (same top and leggings). The puzzle man and the final selfie group are not used. 'the man with the bar' = the barbell lifter 2.5-3.0 s; the bar is included in his box. Key word 'achieve' is a verb, not placed.",
  times)
