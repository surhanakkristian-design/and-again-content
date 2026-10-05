from lib_5658_5659_5662_5663 import write
B=[(0,.32,.50,1),(0,.32,.52,1),(0,.33,.42,1),(0,.34,.42,1),(0,.33,.50,1),(0,.32,.42,1),(0,.31,.37,1),(0,.30,.36,1)]
G=[(.50,.02,.76,.76),(.53,.02,.81,.76),(.44,.02,.81,.76),(.44,.02,.79,.77),(.51,.02,.77,.77),(.43,.02,.80,.77),(.43,.02,.80,.77),(.40,.02,.75,.78)]
H=[(.77,.35,1,1),(.82,.35,1,1),(.82,.34,1,1),(.80,.34,1,1),(.78,.35,1,1),(.81,.34,1,1),(.81,.33,1,1),(.76,.33,1,1)]
write(5663,"A","blow","male",[
 ("to punch the bag","the man in grey","male",B),
 ("to hold the bag still","the man in cream","male",H),
 ("to hang on chains","the punching bag","male",G)],
 3.2,[("a wall",.20,.12,"male"),("a window",.90,.20,"male"),("a punching bag",.62,.50,"male"),("a bottle",.66,.92,"male")],
 "What is the man in grey doing?",["He","is","punching","the","bag."],"male",
 "Three targets: boxer (left), punching bag (middle, with chains), man holding the bag (right). At 0.2, 0.7 and 2.2 the boxer's fist is in the bag, so his box stops at x~0.50 and the fist belongs to the bag box; the holder's hands on the bag are split off at x~0.76-0.82. Punches land at 0.2-0.7 and 2.2; in between he is in a fighting stance.")
