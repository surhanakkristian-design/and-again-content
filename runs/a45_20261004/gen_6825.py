from gen_6821_6823_6825_6826_lib import write
young = [(0.06,0.26,0.94,0.36),(0.06,0.26,0.92,0.36),(0.03,0.25,0.80,0.55),(0.0,0.25,0.70,0.53),(0.03,0.22,0.95,0.40),(0.06,0.24,0.74,0.49),(0.0,0.26,0.53,0.56),(0.0,0.26,0.57,0.56)]
older = [(0.22,0.78,0.36,0.22),(0.22,0.78,0.38,0.22),(0.22,0.80,0.36,0.20),(0.22,0.80,0.40,0.20),(0.22,0.79,0.21,0.21),(0.22,0.80,0.21,0.20),(0.28,0.83,0.20,0.17),(0.28,0.83,0.20,0.17)]
cat   = [None,None,None,None,(0.43,0.85,0.18,0.14),(0.43,0.86,0.18,0.14),(0.48,0.86,0.18,0.14),(0.49,0.86,0.18,0.14)]
write(6825,"B","air out","female",[
 ("to flap a white duvet","the young woman","female",young),
 ("to arrange the pillows","the older woman","female",older),
 ("to rest on a pillow","the cat","female",cat)],
 2.7,[("a church tower",0.92,0.22,"female"),("geraniums",0.50,0.47,"female"),("a duvet",0.52,0.63,"female"),("a rug",0.12,0.75,"female")],
 "What is the young woman doing?","She is shaking a duvet over the balcony.","female",
 "The young woman's box includes the duvet she is holding; cut above the older woman where the duvet hangs down (1.2, 3.2, 3.7 s). The cat appears only from 2.2 s on the pillows next to the older woman. Answer avoids 'airing out' because 'airing the duvet out' would give a second word order. Key word 'air out' is a phrasal verb, not placed.")
