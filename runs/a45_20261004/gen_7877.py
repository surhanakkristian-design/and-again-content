from gen_7874_7875_7876_7877_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
# green man left/right, navy left
G=[(.61,.34,.775,.59),(.71,.34,.81,.58),(.66,.33,.815,.60),(.665,.33,.84,.60),(.625,.33,.825,.60),(.625,.32,.815,.61),(.625,.32,.795,.62),(.635,.31,.79,.62)]
NV=[(.785,.33,.99,.71),(.82,.33,1,.70),(.825,.33,1,.74),(.85,.33,1,.76),(.835,.32,1,.76),(.82,.31,1,.80),(.80,.30,1,.74),(.795,.30,1,.76)]
tent=[(.18,.14,.69,.335),(.13,.23,.70,.45),(.38,.44,.655,.64),(.30,.42,.66,.66),(.27,.41,.62,.67),(.19,.41,.62,.68),(.09,.40,.62,.74),(.01,.40,.63,.75)]
build(7877,"B","in no time","female",[
 ("to pop open in mid-air","the tent","female",tent),
 ("to punch the air","the man in green","male",G),
 ("to hold tangled tent poles","the man in navy","male",NV)],
 3.7,[("a canoe",.57,.45,"female"),("a tent",.17,.52,"female"),("a dog",.50,.61,"female"),("tent poles",.82,.87,"female")],
 "What is the man in green doing?","He is punching the air.","male",
 "tent pops open in the air only 0.2-0.7 s, then stands on the grass; man in green punches the air 0.2-2.2 s; navy man holds the poles until ~2.2 s then drops them; tent box cut at the right where it meets the man in green",T)
