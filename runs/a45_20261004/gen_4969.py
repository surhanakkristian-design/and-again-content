from gen_4968 import write
W = {0.0:(0,.31,.52,1), 0.5:(0,.3,.5,1), 1.0:(0,.3,.46,1), 1.5:(0,.3,.48,1), 2.0:(0,.3,.4,1), 2.5:(0,.28,.45,1), 3.0:(0,.29,.53,1),
     3.5:(0,.3,.44,1), 4.0:(0,.31,.46,1), 4.5:(0,.32,.47,1), 5.0:(0,.33,.48,1), 5.5:(0,.33,.46,1), 6.0:(0,.34,.49,1), 6.5:(0,.34,.51,1),
     7.0:(0,.33,.46,1), 7.5:(0,.32,.48,1), 8.0:(0,.32,.45,1), 8.5:(0,.32,.38,1), 9.0:(0,.32,.42,1), 9.5:(0,.32,.38,1), 10.0:(0,.32,.42,1),
     10.5:(0,.33,.52,1), 11.0:(0,.32,.58,1), 11.5:(0,.33,.58,1), 12.0:(0,.31,.57,1)}
M = {0.0:(.52,.29,1,.66), 0.5:(.5,.28,1,.66), 1.0:(.46,.28,1,.66), 1.5:(.48,.28,1,.65), 2.0:(.4,.29,1,.63), 2.5:(.45,.28,1,.63),
     3.0:(.53,.41,1,.66), 3.5:(.44,.33,1,.64), 4.0:(.46,.22,1,.64), 4.5:(.47,.26,1,.62), 5.0:(.48,.26,1,.64), 5.5:(.46,.28,1,.63),
     6.0:(.49,.26,1,.64), 6.5:(.51,.31,1,.63), 7.0:(.46,.34,1,.63), 7.5:(.48,.32,1,.64), 8.0:(.45,.32,1,.63), 8.5:(.38,.32,1,.68),
     9.0:(.42,.33,1,.68), 9.5:(.38,.33,1,.68), 10.0:(.42,.3,1,.66), 10.5:(.52,.3,1,.65), 11.0:(.58,.4,1,.67), 11.5:(.58,.43,1,.68),
     12.0:(.57,.43,1,.67)}
write(4969, dict(level='A', keyWord='cafe', dv='female',
    taps=[("to read a book", "the old woman", "female", W),
          ("to drink coffee", "the old woman", "female", W),
          ("to show her his phone", "the young man", "male", M)],
    stillS=12.0, nouns=[("a tree", .62, .33, "female"), ("a book", .48, .7, "female"), ("a newspaper", .86, .75, "female"), ("a bag", .3, .9, "female")],
    q="What is the old woman doing?", a="She is reading a book at a cafe.", av="female",
    notes="Only two clear targets (the waiter is tiny in the background), so the woman carries two phrases; she sips her coffee at 4.5-6.5 and holds the cup the rest of the time. Boxes split vertically between her and the man; her hands on the book/cup at the table are partly cut where his box starts. Man shows the phone 8.5-10.0. 'cafe' is the whole setting, so it is not a noun pill; it is in the answer. defaultVoice female: the woman is taken as the main person."))
