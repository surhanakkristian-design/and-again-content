from gen_4968 import write
O = {0.0:(.64,.35,1,1), 0.5:(.7,.38,1,1), 1.0:(.68,.46,1,1), 1.5:(.65,.58,1,1), 2.0:(.64,.68,1,1), 2.5:(.65,.78,1,1),
     3.0:(.76,.85,1,1), 3.5:(.56,.86,.76,1)}
F = {5.0:(.13,.01,.87,.46), 5.5:(0,0,1,.52), 6.0:(0,0,1,.53), 7.5:(.03,0,.97,.7), 8.0:(0,0,1,.68), 8.5:(0,0,1,.68), 9.0:(0,0,1,.68), 9.5:(0,0,1,.68)}
C = {0.0:(0,.6,.64,1), 0.5:(0,.62,.7,1), 1.0:(0,.7,.68,1), 1.5:(0,.8,.65,1), 6.5:(0,0,1,1), 7.0:(0,0,1,1),
     7.5:(0,.71,1,1), 8.0:(0,.69,1,1), 8.5:(0,.69,1,1), 9.0:(0,.69,1,1), 9.5:(0,.69,1,1),
     10.0:(0,0,1,1), 10.5:(0,0,1,1), 11.0:(0,0,1,1), 11.5:(0,0,1,1), 12.0:(0,0,1,1)}
write(4971, dict(level='B', keyWord='fireworks', dv='male',
    taps=[("to hoist the flag", "the officer", "male", O),
          ("to burst over the dome", "the fireworks", "male", F),
          ("to wave small flags", "the crowd", "male", C)],
    stillS=8.0, nouns=[("fireworks", .5, .1, "male"), ("a flagpole", .5, .46, "male"), ("a dome", .48, .6, "male"), ("a crowd", .5, .88, "male")],
    q="What is the officer doing?", a="He is hoisting the flag up the pole.", av="male",
    notes="Many cuts. Officer only 0.0-3.5 (tiny at 3.0-3.5; the two tiny uniformed figures at the base at 7.5-9.5 are left off, ambiguous). Fireworks only 5.0-6.0 and 7.5-9.5 (sparklers in the crowd are not counted). Crowd = the flag-waving crowd: full frame in the close-ups of the women (6.5-7.0, 10.0-12.0), where the boxes are the whole picture. 'a flag' avoided as a noun because many small flags are visible; flagpole pill sits on the pole below the big flag. defaultVoice male: no single main person (officer + crowd), evenId false."))
