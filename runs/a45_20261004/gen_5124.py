import json
from gen_5122_5123_5124_5125_lib import build
times = json.load(open('frames/5124/packet.json'))['times']
L = {1.0:(0,.35,.22,.65), 1.5:(0,.3,.38,.7), 2.0:(0,.35,.33,.65), 2.5:(0,.3,.48,.7), 3.0:(0,.33,.58,.67), 3.5:(0,.31,.5,.69),
 4.0:(0,.28,.38,.72), 4.5:(0,.28,.48,.72), 5.0:(0,.33,.4,.67), 5.5:(0,.3,.45,.7), 6.0:(0,.28,.33,.72), 6.5:(0,.3,.3,.7),
 7.0:(0,.26,.33,.74), 7.5:(0,.28,.37,.72), 8.0:(0,.35,.38,.65)}
Y = {5.0:(.8,.36,.2,.32), 5.5:(.64,.34,.36,.33), 6.0:(.56,.3,.38,.37), 6.5:(.5,.33,.36,.37), 7.0:(.34,.34,.4,.36)}
S = {0.0:(.8,.3,.2,.22), 0.5:(.6,.27,.36,.14), 1.0:(.55,.3,.45,.14), 1.5:(.6,.29,.4,.14), 2.0:(.36,.28,.64,.16), 2.5:(.5,.3,.5,.2),
 3.0:(.6,.4,.4,.16), 3.5:(.52,.28,.48,.18), 4.0:(.4,.3,.6,.2), 4.5:(.5,.3,.5,.2), 5.0:(.41,.35,.38,.22), 5.5:(.46,.3,.18,.17),
 6.0:(.34,.3,.2,.18), 6.5:(.31,.3,.18,.18), 7.0:(.74,.36,.26,.16), 7.5:(.38,.36,.45,.16), 8.0:(.4,.37,.6,.14)}
build(5124, "B", "marathon", "female", [
  ("to stare straight ahead", "the runner on the left", "female", L),
  ("to clap behind the barriers", "the spectators", "female", S),
  ("to wear a yellow vest", "the runner in yellow", "male", Y)],
  4.5, [("a balcony", .58, .22, "female"), ("spectators", .37, .37, "female"), ("cobblestones", .65, .82, "female")],
  "What are the spectators doing?", ["They", "are", "clapping", "behind", "the", "barriers."], "female",
  "Crowded POV race clip: every runner runs, so the phrases rest on what only one target shows. 'the runner on the left' = the woman in the blue vest right beside the camera (1.0-8.0 s, seen in profile; all other runners are seen from behind). The spectators box covers only a part of the crowd band where it would otherwise overlap the runner boxes (5.5-6.5 s small slices; the left runner's fist is cut off at 6.0-6.5 s). 'the runner in yellow' is boxed 5.0-7.0 s; tiny yellow tops far up the pack at 0.0-4.0 s may be the same man but are too small to identify, so they are OFF - verifier please check. The yellow runner's back foot at 7.0 s is outside his box (split at x 0.34). Key word 'marathon' is not a placeable thing, so not a noun. Only 3 nouns: no fourth clearly separate thing at 4.5 s.",
  times)
