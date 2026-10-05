from gen_4968 import write
O = {0.0:(.5,.62,.77,1), 0.5:(.48,.68,.78,1), 1.0:(.47,.69,.8,1), 1.5:(.5,.71,.82,1), 2.0:(.56,.69,.86,1), 2.5:(.58,.78,.9,1),
     3.0:(.6,.76,.96,1), 3.5:(.72,.82,1,1), 4.0:(.78,.84,1,1), 8.0:(.8,.3,1,.48)}
W = {7.0:(0,.66,.65,1), 7.5:(.05,.37,.8,1), 8.0:(0,.38,.8,1), 8.5:(.05,.45,.72,1), 9.0:(.08,.7,.7,1)}
F = {4.0:(.15,.57,.62,.79), 4.5:(.05,.35,.8,.78), 5.0:(0,.25,1,.78), 5.5:(0,.17,1,.8), 6.0:(0,.1,1,.75), 6.5:(0,.05,1,.68),
     7.0:(0,0,1,.52), 7.5:(0,0,.95,.36), 8.0:(0,0,1,.3), 8.5:(0,0,1,.4), 9.0:(0,0,1,.62), 9.5:(0,.12,1,.72), 10.0:(0,.2,1,.8)}
write(4972, dict(level='B', keyWord='patriotic', dv='female',
    taps=[("to hoist the national flag", "the officer", "male", O),
          ("to wear face paint", "the young woman", "female", W),
          ("to explode behind the dome", "the fireworks", "female", F)],
    stillS=6.0, nouns=[("fireworks", .25, .4, "female"), ("a flagpole", .77, .54, "female"), ("a dome", .53, .69, "female"), ("a crowd", .5, .93, "female")],
    q="What is on the woman's cheeks?", a="She has patriotic face paint on her cheeks.", av="female",
    notes="Officer 0.0-4.0 (only a glove at 4.5-6.0 -> off) and again partly behind the pole at 8.0 (top right). Woman with painted cheeks only 7.0-9.0 (a second screaming woman at the right edge 8.5-9.0 has no visible face paint, so 'scream' was avoided). Fireworks 4.0-10.0. 'a flag' avoided as a noun (many small flags in the crowd); flagpole pill sits on the pole among the fireworks. Key word 'patriotic' is an adjective: used in the answer. Answer is a state (has), not present continuous, since the question asks what is on her cheeks."))
