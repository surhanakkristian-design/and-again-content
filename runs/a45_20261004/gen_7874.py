from gen_7874_7875_7876_7877_lib import build
T=[0.2,0.7,1.2,1.7,2.2,2.7,3.2,3.7]
R=[.58,.58,.58,.58,.62,.62,.645,.645]
denim=[(.06,.29,r,.88) for r in R]
BL=[.585,.60,.61,.62,.63,.64,.66,.66]; SP=[.725,.76,.77,.78,.82,.83,.86,.85]; BR=[.94,.98,.98,.99,1,1,1,1]
yellow=[(l,.45,s-.005,.75) for l,s in zip(BL,SP)]
blue=[(s+.005,.46,r,.81) for s,r in zip(SP,BR)]
build(7874,"B","illusion","female",[
 ("to press against the mural","the woman in denim","female",denim),
 ("to giggle behind her hand","the woman in yellow","female",yellow),
 ("to wear a blue blouse","the woman in blue","female",blue)],
 3.2,[("a mural",.15,.28,"female"),("shutters",.60,.40,"female"),("cherry blossom",.85,.20,"female"),("cobblestones",.55,.92,"female")],
 "What is the woman in denim doing?","She is pressing her hand against the mural.","female",
 "giggle behind her hand only from 2.7 s on (before she laughs and points); woman in blue is a state phrase; camera pans right so the table group drifts right",T)
